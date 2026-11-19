"""Reproduce stage 2 capacity scenarios. No files or external systems are changed."""
import json
import math

KIB = 1024
GIB = 1024 ** 3
ENDPOINTS = {0: 10, 1: 58, 3: 106, 5: 130}
DAILY_FORECAST = 400
DAILY_REQUIRED = 2000
CORE_BYTES = 8 * KIB
LOG_BYTES = 20 * 512
MESSAGE_BYTES = 6 * KIB
WAL_BYTES = 2 * (CORE_BYTES + LOG_BYTES + MESSAGE_BYTES)


def restaurants(year):
    for end in sorted(ENDPOINTS):
        if year == end:
            return ENDPOINTS[end]
        if year < end:
            start = max(t for t in ENDPOINTS if t < end)
            return ENDPOINTS[start] + (year - start) * (
                ENDPOINTS[end] - ENDPOINTS[start]
            ) / (end - start)
    raise ValueError(year)


def accumulated_orders(year, daily):
    # Uniform openings within each year; 365 days, no seasonal growth.
    return sum((restaurants(t - 1) + restaurants(t)) / 2 * 365 * daily
               for t in range(1, year + 1))


def storage(year, daily):
    count = accumulated_orders(year, daily)
    end_daily = restaurants(year) * daily
    # Retention windows at end-of-horizon rate are conservative for a growing network.
    core = count * CORE_BYTES
    logs = end_daily * 90 * LOG_BYTES
    messages = end_daily * 7 * MESSAGE_BYTES
    wal_local = end_daily * 2 * WAL_BYTES
    live = core + logs + messages
    node = (live + wal_local) * 1.3
    # Thirty daily full copies at current size, plus 30 days of archived WAL.
    backups = (30 * live + end_daily * 30 * WAL_BYTES) * 1.3
    return dict(orders=int(count), core_gib=round(core / GIB, 2),
                node_gib=round(node / GIB, 2),
                two_nodes_gib=round(2 * node / GIB, 2),
                backups_gib=round(backups / GIB, 2))


def calculate(active_manager_screens=1):
    network = []
    for year, n in ENDPOINTS.items():
        # Per restaurant: 4 kiosks, one board and active staff screens poll twice per second.
        # 20 further API calls and 30 DB transactions per order, 10 events/order.
        peak = n * 200 / 3600
        polls = n * (4 + 1 + active_manager_screens) * 2
        network.append(dict(year=year, restaurants=n, kiosks=n * 4,
                            forecast_day=n * DAILY_FORECAST,
                            required_day=n * DAILY_REQUIRED,
                            orders_sec=round(peak, 3),
                            api_sec=round(polls + 20 * peak, 2),
                            db_tx_sec=round(polls + 30 * peak, 2),
                            burst_orders_sec=n * 4 / 10,
                            burst_api_sec=round(polls + 20 * n * 4 / 10, 2),
                            burst_db_tx_sec=round(polls + 30 * n * 4 / 10, 2),
                            events_sec=round(10 * peak, 2)))
    return dict(network=network, storage={str(y): {
        "forecast": storage(y, DAILY_FORECAST),
        "required": storage(y, DAILY_REQUIRED)} for y in (1, 3, 5)},
        kiosk_mean_limit_sec=4 * 3600 / 200,
        kiosk_limit_at_3min=4 * 3600 / 180,
        cells_at_10min=math.ceil(200 * 10 / 60),
        downtime_minutes={str(days): days * 12 * 60 * 0.001
                          for days in (28, 30, 31)})


if __name__ == "__main__":
    result = calculate()
    # Independent checks of units, interpolation and fivefold scenario relation.
    assert [restaurants(y) for y in range(6)] == [10, 58, 82, 106, 118, 130]
    assert accumulated_orders(1, 400) == 34 * 365 * 400
    assert accumulated_orders(5, 400) == 434 * 365 * 400
    assert result["network"][-1]["kiosks"] == 520
    assert result["network"][-1]["api_sec"] == 1704.44
    assert result["network"][-1]["burst_db_tx_sec"] == 3120
    assert calculate(active_manager_screens=0)["network"][-1]["api_sec"] == 1444.44
    for year in (1, 3, 5):
        assert accumulated_orders(year, 2000) == 5 * accumulated_orders(year, 400)
    print(json.dumps(result, ensure_ascii=False, indent=2))
