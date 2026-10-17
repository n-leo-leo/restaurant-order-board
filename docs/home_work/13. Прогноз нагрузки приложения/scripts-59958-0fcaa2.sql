analyze;


---- индексы
explain (costs, verbose, format json, analyze) 
select * from tickets 
where passenger_name = 'EVGENIY MAKAROV'

---  Gather (cost=1000..19258.48 rows=74 width=104)                                     (actual=6.653..1 865.923 rows=278 loops=1)	
---  Bitmap Heap Scan on bookings.tickets as tickets (cost=5..285.74 rows=74 width=104) (actual=0.333..    7.686 rows=278 loops=1)

create index on tickets(passenger_name);
analyze tickets;

----индекс по выражению
explain (costs, verbose, format json, analyze)
select * from tickets where initcap(passenger_name) = 'Evgeniy Makarov'
--initcap('EVGENIY MAKAROV');

---  Gather (cost=1000..20529.19 rows=4145 width=104)                                   (actual=9.972..5 560.569 rows=278 loops=1)	
---  Bitmap Heap Scan on bookings.tickets as tickets (cost=5..285.93 rows=74 width=104) (actual=0.284..    0.872 rows=278 loops=1)


create index initcap_fio on tickets (initcap(passenger_name));
analyze tickets;

---------частичные индексы
explain (costs, verbose, format json, analyze)
select count(1) from flights where status = 'Cancelled';


create index status_all on flights(status); 
analyze flights;
select pg_size_pretty(pg_table_size('status_all'));   -- 464

create index status_canc on flights(status) where status = 'Cancelled';
analyze flights;
select pg_size_pretty(pg_table_size('status_canc')); -- 16


-----------

----- полнотекстный поиск
select ticket_no, passenger_name, to_tsvector(passenger_name) from tickets limit 50; 


select ticket_no, passenger_name, to_tsvector(passenger_name)@@to_tsquery('petr' ) from tickets limit 500; 

select ticket_no, passenger_name, to_tsvector(passenger_name)@@to_tsquery('olga | Elena' ) from tickets limit 50; 

alter table tickets add column fio_lexeme tsvector;
update tickets
set fio_lexeme = to_tsvector(passenger_name)
where ticket_no < '0005432005201';

 select ticket_no, passenger_name, fio_lexeme from tickets where ticket_no < '0005432005201';
 
explain analyze select ticket_no, passenger_name from tickets where fio_lexeme @@ to_tsquery('olga | Elena' ); 

-- Gather  (cost=1000.00..106591.00 rows=8282 width=30)               (actual time=15891.455..16 000.227 rows=59 loops=1)
-- Bitmap Heap Scan on tickets  (cost=13.39..145.19 rows=32 width=30) (actual time=0.194..         0.255 rows=59 loops=1)
drop index if exists search_index_title;
CREATE INDEX search_index_title ON tickets USING GIN (fio_lexeme);
analyze tickets;


------------ Индексы GiST
DROP TABLE IF EXISTS graph;

CREATE TABLE graph (
  name char(1),
  point point
);


INSERT INTO graph
  (name, point)
  VALUES
  ('A', point '(1, 1)'),
  ('B', point '(2, 4)'),
  ('C', point '(3, 9)'),
  ('X', point '(-1, 1)'),
  ('Y', point '(-2, 4)'),
  ('Z', point '(-3, 9)');

SELECT * FROM graph;

SELECT * FROM graph 
  WHERE point <@ box '(0,0),(100,100)';


EXPLAIN ANALYZE
SELECT * FROM graph 
  WHERE point <@ box '(0,0),(100,100)';
--- Seq Scan on graph  (cost=0.00..29.62 rows=2 width=24)                        (actual time=0.029..0.031 rows=3 loops=1)
--- Index Scan using graph_point_idx on graph  (cost=0.13..8.15 rows=1 width=24) (actual time=0.160..0.162 rows=3 loops=1)

CREATE INDEX ON graph USING gist(point);

SET enable_seqscan = off;

EXPLAIN ANALYZE
SELECT * FROM graph 
  WHERE point <@ box '(0,0),(100,100)';


SET enable_seqscan = on;


---- Количество уникальных значений**
-- Результат `−1` означает, что все значения в столбце уникальны:
SELECT
    s.n_distinct
    FROM pg_stats s
    WHERE s.tablename = 'tickets'
--    AND s.attname = 'ticket_no';
--	AND s.attname = 'passenger_name';

----- оптимизация запроса
create table test (id, title) as 
select 
  generate_series(1,10000000) as id,
  md5(random()::text) as title;

create index on test(id);

analyze test;

EXPLAIN (costs, verbose, format json, analyze)
SELECT * FROM test order by id limit 10 offset 5000000; 

EXPLAIN (costs, verbose, format json, analyze)
SELECT id FROM test order by id limit 10 offset 1000000;

EXPLAIN (costs, verbose, format json, analyze)
SELECT * FROM test 
where id >= (SELECT id FROM test order by id limit 1 offset 1000000) 
order by id limit 10;

-----------
1.
DELETE FROM sourcing_dates  
            WHERE id IN (
                SELECT id FROM (
                    SELECT id, row_number() OVER (PARTITION BY cal, date ORDER BY is_exclude DESC) row_num
                    FROM sourcing_dates
                    ) part
                WHERE part.row_num != 1
                );
который на 122 млн. записей работает час и потом падает из-за разрыва коннекта.

2.
delete from sourcing_dates a
 using 
  (select cal, date, min(ctid) as s_ctid from sourcing_dates group by cal, date) s
   where a.ctid <> s.ctid and (a.cal, a.date) = (s.cal, s.date);

3.
DELETE FROM sourcing_dates WHERE ctid NOT IN  
      (SELECT max(ctid) FROM sourcing_dates GROUP BY cal, date);
	  
