# Трассировка требований, задач и проверок

Каждая строка матрицы связывает критерий приемки с задачами истории и запланированными проверками. В поле «Задачи» каждого тест-кейса указано, какие результаты он проверяет. Статус испытаний указан в разделах тестирования.

Основания и границы реализации задают [бизнес-требования](01_business/goals.md), [истории](02_requirements/user-stories.md) и [карта релизов](02_requirements/story-map.md).

## БТ → US → AC → задачи → тест-кейсы

| БТ | US / релиз | AC | Задачи | API / внешний интерфейс | Тест-кейсы |
|---|---|---|---|---|---|
| БТ-01 | US-01; MVP | [AC-01.1](06_decomposition/acceptance-criteria.md#ac-01-1) | [T-01A](06_decomposition/tasks.md#t-01a), [T-01B](06_decomposition/tasks.md#t-01b), [T-N01](06_decomposition/tasks.md#t-n01), [T-N04](06_decomposition/tasks.md#t-n04) | startSession, getMenu | [TC-M01](07_testing/test-cases-mvp.md#tc-m01), [TC-N08](07_testing/test-cases-mvp.md#tc-n08), [TC-N10](07_testing/test-cases-mvp.md#tc-n10) |
| БТ-04 | US-02; MVP | [AC-02.1](06_decomposition/acceptance-criteria.md#ac-02-1) | [T-02A](06_decomposition/tasks.md#t-02a), [T-02B](06_decomposition/tasks.md#t-02b), [T-N01](06_decomposition/tasks.md#t-n01) | getMenu, preparePurchase | [TC-M02](07_testing/test-cases-mvp.md#tc-m02), [TC-M03](07_testing/test-cases-mvp.md#tc-m03), [TC-M04](07_testing/test-cases-mvp.md#tc-m04), [TC-N07](07_testing/test-cases-mvp.md#tc-n07) |
| БТ-01, БТ-02 | US-03; MVP | [AC-03.1](06_decomposition/acceptance-criteria.md#ac-03-1) | [T-03A](06_decomposition/tasks.md#t-03a), [T-03B](06_decomposition/tasks.md#t-03b) | getMenuItem | [TC-M05](07_testing/test-cases-mvp.md#tc-m05), [TC-M42](07_testing/test-cases-mvp.md#tc-m42) |
| БТ-01 | US-04; MVP | [AC-04.1](06_decomposition/acceptance-criteria.md#ac-04-1) | [T-04A](06_decomposition/tasks.md#t-04a), [T-04B](06_decomposition/tasks.md#t-04b) | getCart, replaceCart | [TC-M06](07_testing/test-cases-mvp.md#tc-m06) |
| БТ-01 | US-05; MVP | [AC-05.1](06_decomposition/acceptance-criteria.md#ac-05-1) | [T-05A](06_decomposition/tasks.md#t-05a), [T-05B](06_decomposition/tasks.md#t-05b), [T-N04](06_decomposition/tasks.md#t-n04) | replaceCart | [TC-M07](07_testing/test-cases-mvp.md#tc-m07), [TC-N10](07_testing/test-cases-mvp.md#tc-n10) |
| БТ-01 | US-06; MVP | [AC-06.1](06_decomposition/acceptance-criteria.md#ac-06-1) | [T-06A](06_decomposition/tasks.md#t-06a), [T-06B](06_decomposition/tasks.md#t-06b), [T-N04](06_decomposition/tasks.md#t-n04) | replaceCart, startPayment | [TC-M08](07_testing/test-cases-mvp.md#tc-m08), [TC-N10](07_testing/test-cases-mvp.md#tc-n10) |
| БТ-14 | US-07; MVP | [AC-07.1](06_decomposition/acceptance-criteria.md#ac-07-1) | [T-07A](06_decomposition/tasks.md#t-07a), [T-07B](06_decomposition/tasks.md#t-07b) | getMenuItem, replaceCart | [TC-M09](07_testing/test-cases-mvp.md#tc-m09) |
| БТ-15 | US-08; MVP | [AC-08.1](06_decomposition/acceptance-criteria.md#ac-08-1) | [T-08A](06_decomposition/tasks.md#t-08a), [T-08B](06_decomposition/tasks.md#t-08b) | preparePurchase | [TC-M10](07_testing/test-cases-mvp.md#tc-m10) |
| БТ-03, БТ-05 | US-09; MVP | [AC-09.1](06_decomposition/acceptance-criteria.md#ac-09-1) | [T-09A](06_decomposition/tasks.md#t-09a), [T-09B](06_decomposition/tasks.md#t-09b), [T-N01](06_decomposition/tasks.md#t-n01), [T-N03](06_decomposition/tasks.md#t-n03), [T-N04](06_decomposition/tasks.md#t-n04), [T-N05](06_decomposition/tasks.md#t-n05), [T-N06](06_decomposition/tasks.md#t-n06) | preparePurchase, startPayment, getPayment, getSession, getPurchase, verifyPurchase, reprintTicket | [TC-M04](07_testing/test-cases-mvp.md#tc-m04), [TC-M11](07_testing/test-cases-mvp.md#tc-m11), [TC-M12](07_testing/test-cases-mvp.md#tc-m12), [TC-M14](07_testing/test-cases-mvp.md#tc-m14), [TC-N01](07_testing/test-cases-mvp.md#tc-n01), [TC-N02](07_testing/test-cases-mvp.md#tc-n02), [TC-N09](07_testing/test-cases-mvp.md#tc-n09), [TC-N10](07_testing/test-cases-mvp.md#tc-n10), [TC-N12](07_testing/test-cases-mvp.md#tc-n12), [TC-N14](07_testing/test-cases-mvp.md#tc-n14), [TC-N15](07_testing/test-cases-mvp.md#tc-n15), [TC-N16](07_testing/test-cases-mvp.md#tc-n16) |
| БТ-03, БТ-05, БТ-07 | US-09, US-10; MVP | [AC-09.2](06_decomposition/acceptance-criteria.md#ac-09-2) | [T-09A](06_decomposition/tasks.md#t-09a), [T-09B](06_decomposition/tasks.md#t-09b), [T-10A](06_decomposition/tasks.md#t-10a), [T-10B](06_decomposition/tasks.md#t-10b), [T-N02](06_decomposition/tasks.md#t-n02) | preparePurchase, startPayment, getPayment, getSession, getPurchase, verifyPurchase, reprintTicket | [TC-M13](07_testing/test-cases-mvp.md#tc-m13), [TC-M14](07_testing/test-cases-mvp.md#tc-m14), [TC-N04](07_testing/test-cases-mvp.md#tc-n04), [TC-N05](07_testing/test-cases-mvp.md#tc-n05), [TC-N06](07_testing/test-cases-mvp.md#tc-n06) |
| БТ-03, БТ-05, БТ-06, БТ-07, БТ-10 | US-09, US-12, US-14, US-15; MVP | [AC-09.3](06_decomposition/acceptance-criteria.md#ac-09-3) | [T-09A](06_decomposition/tasks.md#t-09a), [T-09B](06_decomposition/tasks.md#t-09b), [T-12A](06_decomposition/tasks.md#t-12a), [T-12B](06_decomposition/tasks.md#t-12b), [T-14A](06_decomposition/tasks.md#t-14a), [T-14B](06_decomposition/tasks.md#t-14b), [T-15A](06_decomposition/tasks.md#t-15a), [T-15B](06_decomposition/tasks.md#t-15b), [T-35A](06_decomposition/tasks.md#t-35a), [T-N05](06_decomposition/tasks.md#t-n05) | preparePurchase, startPayment, getPayment, getSession, getPurchase, verifyPurchase, reprintTicket, I-03 (талон и выдача), listProblems, acceptProblem, resolveProblem, getStaffSalesState, setSalesState, findPurchases, getStaffPurchase, recordImpossibility, registerExternalRefund, getRefund | [TC-M15](07_testing/test-cases-mvp.md#tc-m15), [TC-M16](07_testing/test-cases-mvp.md#tc-m16), [TC-N11](07_testing/test-cases-mvp.md#tc-n11), [TC-N13](07_testing/test-cases-mvp.md#tc-n13), [TC-N14](07_testing/test-cases-mvp.md#tc-n14) |
| БТ-03, БТ-07 | US-10; MVP | [AC-10.1](06_decomposition/acceptance-criteria.md#ac-10-1) | [T-10A](06_decomposition/tasks.md#t-10a), [T-10B](06_decomposition/tasks.md#t-10b), [T-N03](06_decomposition/tasks.md#t-n03) | getPayment, getSession, getPurchase | [TC-M12](07_testing/test-cases-mvp.md#tc-m12), [TC-M17](07_testing/test-cases-mvp.md#tc-m17), [TC-M37](07_testing/test-cases-mvp.md#tc-m37), [TC-N09](07_testing/test-cases-mvp.md#tc-n09) |
| БТ-06 | US-11; MVP | [AC-11.1](06_decomposition/acceptance-criteria.md#ac-11-1) | [T-11A](06_decomposition/tasks.md#t-11a), [T-11B](06_decomposition/tasks.md#t-11b), [T-N01](06_decomposition/tasks.md#t-n01), [T-N06](06_decomposition/tasks.md#t-n06) | getBoard, confirmBoardDisplay, getBoardDisplay | [TC-M19](07_testing/test-cases-mvp.md#tc-m19), [TC-M20](07_testing/test-cases-mvp.md#tc-m20), [TC-M26](07_testing/test-cases-mvp.md#tc-m26), [TC-M43](07_testing/test-cases-mvp.md#tc-m43), [TC-N07](07_testing/test-cases-mvp.md#tc-n07), [TC-N16](07_testing/test-cases-mvp.md#tc-n16) |
| БТ-06 | US-12; MVP | [AC-12.1](06_decomposition/acceptance-criteria.md#ac-12-1) | [T-12A](06_decomposition/tasks.md#t-12a), [T-12B](06_decomposition/tasks.md#t-12b), [T-N06](06_decomposition/tasks.md#t-n06) | I-03 (талон и выдача), reprintTicket | [TC-M21](07_testing/test-cases-mvp.md#tc-m21), [TC-M22](07_testing/test-cases-mvp.md#tc-m22), [TC-M23](07_testing/test-cases-mvp.md#tc-m23), [TC-N16](07_testing/test-cases-mvp.md#tc-n16), [TC-N20](07_testing/test-cases-mvp.md#tc-n20) |
| БТ-07 | US-13; MVP | [AC-13.1](06_decomposition/acceptance-criteria.md#ac-13-1) | [T-13A](06_decomposition/tasks.md#t-13a), [T-13B](06_decomposition/tasks.md#t-13b) | getPurchase, getBoard; помощь в зале | [TC-M24](07_testing/test-cases-mvp.md#tc-m24) |
| БТ-07 | US-14; MVP | [AC-14.1](06_decomposition/acceptance-criteria.md#ac-14-1) | [T-14A](06_decomposition/tasks.md#t-14a), [T-14B](06_decomposition/tasks.md#t-14b), [T-N05](06_decomposition/tasks.md#t-n05), [T-N07](06_decomposition/tasks.md#t-n07) | listProblems, confirmProblemDisplay, acceptProblem, resolveProblem, getStaffSalesState, setSalesState | [TC-M25](07_testing/test-cases-mvp.md#tc-m25), [TC-M26](07_testing/test-cases-mvp.md#tc-m26), [TC-N11](07_testing/test-cases-mvp.md#tc-n11), [TC-N19](07_testing/test-cases-mvp.md#tc-n19) |
| БТ-07, БТ-10 | US-15; MVP | [AC-15.1](06_decomposition/acceptance-criteria.md#ac-15-1) | [T-15A](06_decomposition/tasks.md#t-15a), [T-15B](06_decomposition/tasks.md#t-15b), [T-N05](06_decomposition/tasks.md#t-n05) | findPurchases, getStaffPurchase, recordImpossibility, registerExternalRefund, getRefund | [TC-M27](07_testing/test-cases-mvp.md#tc-m27), [TC-M28](07_testing/test-cases-mvp.md#tc-m28), [TC-M29](07_testing/test-cases-mvp.md#tc-m29), [TC-N11](07_testing/test-cases-mvp.md#tc-n11), [TC-N14](07_testing/test-cases-mvp.md#tc-n14) |
| БТ-06, БТ-07 | US-16; MVP | [AC-16.1](06_decomposition/acceptance-criteria.md#ac-16-1) | [T-16A](06_decomposition/tasks.md#t-16a), [T-16B](06_decomposition/tasks.md#t-16b), [T-N06](06_decomposition/tasks.md#t-n06) | I-03, I-05, recordBoardVisibility, resolveProblem, listCells, serviceCell, acceptProblem, recordImpossibility, registerExternalRefund | [TC-M30](07_testing/test-cases-mvp.md#tc-m30), [TC-N20](07_testing/test-cases-mvp.md#tc-n20), [TC-M43](07_testing/test-cases-mvp.md#tc-m43) |
| БТ-06, БТ-07 | US-12, US-16; MVP | [AC-16.2](06_decomposition/acceptance-criteria.md#ac-16-2) | [T-12A](06_decomposition/tasks.md#t-12a), [T-12B](06_decomposition/tasks.md#t-12b), [T-16A](06_decomposition/tasks.md#t-16a), [T-16B](06_decomposition/tasks.md#t-16b), [T-N06](06_decomposition/tasks.md#t-n06) | I-03 (талон и выдача), reprintTicket, listCells, serviceCell, acceptProblem | [TC-M31](07_testing/test-cases-mvp.md#tc-m31), [TC-N20](07_testing/test-cases-mvp.md#tc-n20) |
| БТ-06, БТ-07 | US-16; MVP | [AC-16.3](06_decomposition/acceptance-criteria.md#ac-16-3) | [T-16A](06_decomposition/tasks.md#t-16a), [T-16B](06_decomposition/tasks.md#t-16b), [T-N05](06_decomposition/tasks.md#t-n05), [T-N06](06_decomposition/tasks.md#t-n06) | listCells, serviceCell, acceptProblem | [TC-M23](07_testing/test-cases-mvp.md#tc-m23), [TC-M32](07_testing/test-cases-mvp.md#tc-m32), [TC-N11](07_testing/test-cases-mvp.md#tc-n11), [TC-N20](07_testing/test-cases-mvp.md#tc-n20) |
| БТ-06, БТ-07 | US-12, US-16; MVP | [AC-16.4](06_decomposition/acceptance-criteria.md#ac-16-4) | [T-12A](06_decomposition/tasks.md#t-12a), [T-12B](06_decomposition/tasks.md#t-12b), [T-16A](06_decomposition/tasks.md#t-16a), [T-16B](06_decomposition/tasks.md#t-16b), [T-N06](06_decomposition/tasks.md#t-n06) | I-03 (талон и выдача), reprintTicket, listCells, serviceCell, acceptProblem | [TC-M33](07_testing/test-cases-mvp.md#tc-m33), [TC-N20](07_testing/test-cases-mvp.md#tc-n20) |
| БТ-01, БТ-02 | US-17; MVP | [AC-17.1](06_decomposition/acceptance-criteria.md#ac-17-1) | [T-17A](06_decomposition/tasks.md#t-17a), [T-17B](06_decomposition/tasks.md#t-17b), [T-N05](06_decomposition/tasks.md#t-n05) | endSession, getSession, getSalesState, setSalesState | [TC-M36](07_testing/test-cases-mvp.md#tc-m36), [TC-M37](07_testing/test-cases-mvp.md#tc-m37), [TC-N13](07_testing/test-cases-mvp.md#tc-n13) |
| БТ-01, БТ-02, БТ-03, БТ-05, БТ-07 | US-01, US-09, US-10, US-14, US-17; MVP | [AC-17.2](06_decomposition/acceptance-criteria.md#ac-17-2) | [T-01A](06_decomposition/tasks.md#t-01a), [T-01B](06_decomposition/tasks.md#t-01b), [T-09A](06_decomposition/tasks.md#t-09a), [T-09B](06_decomposition/tasks.md#t-09b), [T-10A](06_decomposition/tasks.md#t-10a), [T-10B](06_decomposition/tasks.md#t-10b), [T-14A](06_decomposition/tasks.md#t-14a), [T-14B](06_decomposition/tasks.md#t-14b), [T-17A](06_decomposition/tasks.md#t-17a), [T-17B](06_decomposition/tasks.md#t-17b), [T-N03](06_decomposition/tasks.md#t-n03) | startSession, getMenu, preparePurchase, startPayment, getPayment, getPurchase, verifyPurchase, reprintTicket, listProblems, acceptProblem, resolveProblem, getStaffSalesState, setSalesState, endSession, getSession, getSalesState | [TC-M38](07_testing/test-cases-mvp.md#tc-m38), [TC-N08](07_testing/test-cases-mvp.md#tc-n08) |
| БТ-01, БТ-02, БТ-03, БТ-05, БТ-07 | US-01, US-09, US-14, US-17; MVP | [AC-17.3](06_decomposition/acceptance-criteria.md#ac-17-3) | [T-01A](06_decomposition/tasks.md#t-01a), [T-01B](06_decomposition/tasks.md#t-01b), [T-09A](06_decomposition/tasks.md#t-09a), [T-09B](06_decomposition/tasks.md#t-09b), [T-14A](06_decomposition/tasks.md#t-14a), [T-14B](06_decomposition/tasks.md#t-14b), [T-17A](06_decomposition/tasks.md#t-17a), [T-17B](06_decomposition/tasks.md#t-17b), [T-N02](06_decomposition/tasks.md#t-n02), [T-N03](06_decomposition/tasks.md#t-n03) | startSession, getMenu, preparePurchase, startPayment, getPayment, getPurchase, verifyPurchase, reprintTicket, listProblems, acceptProblem, resolveProblem, getStaffSalesState, setSalesState, endSession, getSession, getSalesState | [TC-M39](07_testing/test-cases-mvp.md#tc-m39), [TC-N03](07_testing/test-cases-mvp.md#tc-n03), [TC-N08](07_testing/test-cases-mvp.md#tc-n08) |
| БТ-08 | US-18; R1 | [AC-18.1](06_decomposition/acceptance-criteria.md#ac-18-1) | [T-18A](06_decomposition/tasks.md#t-18a), [T-18B](06_decomposition/tasks.md#t-18b), [T-N08](06_decomposition/tasks.md#t-n08) | requestLoyaltyCode, confirmLoyalty | [TC-R01](07_testing/test-cases-r1.md#tc-r01), [TC-R02](07_testing/test-cases-r1.md#tc-r02), [TC-R03](07_testing/test-cases-r1.md#tc-r03), [TC-R42](07_testing/test-cases-r1.md#tc-r42), [TC-R43](07_testing/test-cases-r1.md#tc-r43), [TC-R44](07_testing/test-cases-r1.md#tc-r44), [TC-R48](07_testing/test-cases-r1.md#tc-r48) |
| БТ-08 | US-19; R1 | [AC-19.1](06_decomposition/acceptance-criteria.md#ac-19-1) | [T-19A](06_decomposition/tasks.md#t-19a), [T-19B](06_decomposition/tasks.md#t-19b), [T-N08](06_decomposition/tasks.md#t-n08) | confirmLoyalty, getLoyalty | [TC-R04](07_testing/test-cases-r1.md#tc-r04), [TC-R05](07_testing/test-cases-r1.md#tc-r05), [TC-R42](07_testing/test-cases-r1.md#tc-r42), [TC-R43](07_testing/test-cases-r1.md#tc-r43), [TC-R44](07_testing/test-cases-r1.md#tc-r44), [TC-R48](07_testing/test-cases-r1.md#tc-r48) |
| БТ-08 | US-20; R1 | [AC-20.1](06_decomposition/acceptance-criteria.md#ac-20-1) | [T-20A](06_decomposition/tasks.md#t-20a), [T-20B](06_decomposition/tasks.md#t-20b), [T-N08](06_decomposition/tasks.md#t-n08) | getLoyalty, preparePurchase | [TC-R06](07_testing/test-cases-r1.md#tc-r06), [TC-R07](07_testing/test-cases-r1.md#tc-r07), [TC-R08](07_testing/test-cases-r1.md#tc-r08), [TC-R43](07_testing/test-cases-r1.md#tc-r43), [TC-R45](07_testing/test-cases-r1.md#tc-r45), [TC-R46](07_testing/test-cases-r1.md#tc-r46), [TC-R47](07_testing/test-cases-r1.md#tc-r47), [TC-R48](07_testing/test-cases-r1.md#tc-r48) |
| БТ-08 | US-21; R1 | [AC-21.1](06_decomposition/acceptance-criteria.md#ac-21-1) | [T-21A](06_decomposition/tasks.md#t-21a), [T-21B](06_decomposition/tasks.md#t-21b) | getPurchase; I-07 начисление по оплате | [TC-R09](07_testing/test-cases-r1.md#tc-r09), [TC-R10](07_testing/test-cases-r1.md#tc-r10), [TC-R47](07_testing/test-cases-r1.md#tc-r47) |
| БТ-09 | US-22; R1 | [AC-22.1](06_decomposition/acceptance-criteria.md#ac-22-1) | [T-22A](06_decomposition/tasks.md#t-22a), [T-22B](06_decomposition/tasks.md#t-22b) | getSession, startPayment, getPayment, cancelCashPayment | [TC-R11](07_testing/test-cases-r1.md#tc-r11), [TC-R12](07_testing/test-cases-r1.md#tc-r12), [TC-R13](07_testing/test-cases-r1.md#tc-r13), [TC-R49](07_testing/test-cases-r1.md#tc-r49), [TC-R50](07_testing/test-cases-r1.md#tc-r50) |
| БТ-07, БТ-10 | US-23; R1 | [AC-23.1](06_decomposition/acceptance-criteria.md#ac-23-1) | [T-23A](06_decomposition/tasks.md#t-23a), [T-23B](06_decomposition/tasks.md#t-23b) | findPurchases, getStaffPurchase | [TC-R14](07_testing/test-cases-r1.md#tc-r14), [TC-R15](07_testing/test-cases-r1.md#tc-r15) |
| БТ-10 | US-24; R1 | [AC-24.1](06_decomposition/acceptance-criteria.md#ac-24-1) | [T-24A](06_decomposition/tasks.md#t-24a), [T-24B](06_decomposition/tasks.md#t-24b) | cancelOrder, startRefund, getRefund | [TC-R16](07_testing/test-cases-r1.md#tc-r16), [TC-R17](07_testing/test-cases-r1.md#tc-r17), [TC-R18](07_testing/test-cases-r1.md#tc-r18), [TC-R19](07_testing/test-cases-r1.md#tc-r19), [TC-R51](07_testing/test-cases-r1.md#tc-r51), [TC-R52](07_testing/test-cases-r1.md#tc-r52) |
| БТ-10 | US-25; R1 | [AC-25.1](06_decomposition/acceptance-criteria.md#ac-25-1) | [T-25A](06_decomposition/tasks.md#t-25a), [T-25B](06_decomposition/tasks.md#t-25b) | cancelOrder, startRefund, registerExternalRefund, getRefund | [TC-R20](07_testing/test-cases-r1.md#tc-r20), [TC-R21](07_testing/test-cases-r1.md#tc-r21), [TC-R51](07_testing/test-cases-r1.md#tc-r51), [TC-R52](07_testing/test-cases-r1.md#tc-r52) |
| БТ-07 | US-26; R1 | [AC-26.1](06_decomposition/acceptance-criteria.md#ac-26-1) | [T-26A](06_decomposition/tasks.md#t-26a), [T-26B](06_decomposition/tasks.md#t-26b) | listNotifications | [TC-R22](07_testing/test-cases-r1.md#tc-r22), [TC-R23](07_testing/test-cases-r1.md#tc-r23) |
| БТ-11 | US-27; R1 | [AC-27.1](06_decomposition/acceptance-criteria.md#ac-27-1) | [T-27A](06_decomposition/tasks.md#t-27a), [T-27B](06_decomposition/tasks.md#t-27b), [T-N08](06_decomposition/tasks.md#t-n08) | getMenuDraft, saveMenuEntry | [TC-R24](07_testing/test-cases-r1.md#tc-r24), [TC-R25](07_testing/test-cases-r1.md#tc-r25), [TC-R53](07_testing/test-cases-r1.md#tc-r53) |
| БТ-11 | US-28; R1 | [AC-28.1](06_decomposition/acceptance-criteria.md#ac-28-1) | [T-28A](06_decomposition/tasks.md#t-28a), [T-28B](06_decomposition/tasks.md#t-28b) | getMenuDraft, saveMenuEntry | [TC-R26](07_testing/test-cases-r1.md#tc-r26), [TC-R27](07_testing/test-cases-r1.md#tc-r27) |
| БТ-11 | US-29; R1 | [AC-29.1](06_decomposition/acceptance-criteria.md#ac-29-1) | [T-29A](06_decomposition/tasks.md#t-29a), [T-29B](06_decomposition/tasks.md#t-29b) | savePromotion, saveMenuEntry | [TC-R28](07_testing/test-cases-r1.md#tc-r28), [TC-R29](07_testing/test-cases-r1.md#tc-r29) |
| БТ-11 | US-30; R1 | [AC-30.1](06_decomposition/acceptance-criteria.md#ac-30-1) | [T-30A](06_decomposition/tasks.md#t-30a), [T-30B](06_decomposition/tasks.md#t-30b), [T-N08](06_decomposition/tasks.md#t-n08) | getIngredients, getRecipe, saveRecipe | [TC-R30](07_testing/test-cases-r1.md#tc-r30), [TC-R31](07_testing/test-cases-r1.md#tc-r31), [TC-R53](07_testing/test-cases-r1.md#tc-r53) |
| БТ-16 | US-31; R1 | [AC-31.1](06_decomposition/acceptance-criteria.md#ac-31-1) | [T-31A](06_decomposition/tasks.md#t-31a), [T-31B](06_decomposition/tasks.md#t-31b) | preparePurchase, savePromotion, I-03 (комплектация по jobId) | [TC-R32](07_testing/test-cases-r1.md#tc-r32), [TC-R33](07_testing/test-cases-r1.md#tc-r33), [TC-R34](07_testing/test-cases-r1.md#tc-r34) |
| БТ-17 | US-32; R1 | [AC-32.1](06_decomposition/acceptance-criteria.md#ac-32-1) | [T-32A](06_decomposition/tasks.md#t-32a), [T-32B](06_decomposition/tasks.md#t-32b), [T-N08](06_decomposition/tasks.md#t-n08) | getProduction | [TC-R35](07_testing/test-cases-r1.md#tc-r35), [TC-R53](07_testing/test-cases-r1.md#tc-r53) |
| БТ-17 | US-33; R1 | [AC-33.1](06_decomposition/acceptance-criteria.md#ac-33-1) | [T-33A](06_decomposition/tasks.md#t-33a), [T-33B](06_decomposition/tasks.md#t-33b), [T-N08](06_decomposition/tasks.md#t-n08) | getProduction | [TC-R36](07_testing/test-cases-r1.md#tc-r36), [TC-R37](07_testing/test-cases-r1.md#tc-r37) |
| БТ-13 | US-34; R1 | [AC-34.1](06_decomposition/acceptance-criteria.md#ac-34-1) | [T-34A](06_decomposition/tasks.md#t-34a), [T-34B](06_decomposition/tasks.md#t-34b), [T-N08](06_decomposition/tasks.md#t-n08) | getSalesReport, createExport, getExport | [TC-R38](07_testing/test-cases-r1.md#tc-r38), [TC-R39](07_testing/test-cases-r1.md#tc-r39), [TC-R40](07_testing/test-cases-r1.md#tc-r40), [TC-R41](07_testing/test-cases-r1.md#tc-r41), [TC-R53](07_testing/test-cases-r1.md#tc-r53) |
| БТ-18 | US-35; MVP | [AC-35.1](06_decomposition/acceptance-criteria.md#ac-35-1) | [T-35A](06_decomposition/tasks.md#t-35a), [T-35B](06_decomposition/tasks.md#t-35b) | getPurchase, getStaffPurchase | [TC-M41](07_testing/test-cases-mvp.md#tc-m41) |
| БТ-03, БТ-04, БТ-05, БТ-07, БТ-10 | US-02, US-09, US-10, US-15; MVP | [AC-09.4](06_decomposition/acceptance-criteria.md#ac-09-4) | [T-02A](06_decomposition/tasks.md#t-02a), [T-02B](06_decomposition/tasks.md#t-02b), [T-09A](06_decomposition/tasks.md#t-09a), [T-09B](06_decomposition/tasks.md#t-09b), [T-10A](06_decomposition/tasks.md#t-10a), [T-10B](06_decomposition/tasks.md#t-10b), [T-15A](06_decomposition/tasks.md#t-15a), [T-15B](06_decomposition/tasks.md#t-15b), [T-N01](06_decomposition/tasks.md#t-n01) | getSession, getSalesState, getMenu, preparePurchase, getPurchase, startPayment, getPayment, getProblem, resolveProblem, findPurchases, getStaffPurchase, verifyPurchase, reprintTicket, recordImpossibility, registerExternalRefund, getRefund, setSalesState | [TC-M18](07_testing/test-cases-mvp.md#tc-m18), [TC-N02](07_testing/test-cases-mvp.md#tc-n02) |
| БТ-06, БТ-07 | US-12, US-16; MVP | [AC-16.5](06_decomposition/acceptance-criteria.md#ac-16-5) | [T-12A](06_decomposition/tasks.md#t-12a), [T-12B](06_decomposition/tasks.md#t-12b), [T-16A](06_decomposition/tasks.md#t-16a), [T-16B](06_decomposition/tasks.md#t-16b), [T-N06](06_decomposition/tasks.md#t-n06) | loginStaff, getBoard, confirmBoardDisplay, getBoardDisplay, listProblems, getProblem, acceptProblem, resolveProblem, reprintTicket, listCells, serviceCell | [TC-M34](07_testing/test-cases-mvp.md#tc-m34), [TC-N20](07_testing/test-cases-mvp.md#tc-n20) |
| БТ-06, БТ-07 | US-12, US-16; MVP | [AC-16.6](06_decomposition/acceptance-criteria.md#ac-16-6) | [T-12A](06_decomposition/tasks.md#t-12a), [T-12B](06_decomposition/tasks.md#t-12b), [T-16A](06_decomposition/tasks.md#t-16a), [T-16B](06_decomposition/tasks.md#t-16b), [T-N06](06_decomposition/tasks.md#t-n06) | loginStaff, getBoard, confirmBoardDisplay, getBoardDisplay, listProblems, getProblem, acceptProblem, resolveProblem, reprintTicket, listCells, serviceCell | [TC-M35](07_testing/test-cases-mvp.md#tc-m35), [TC-N20](07_testing/test-cases-mvp.md#tc-n20) |
| БТ-01, БТ-02, БТ-03, БТ-05, БТ-07 | US-09, US-10, US-14, US-17; MVP | [AC-17.4](06_decomposition/acceptance-criteria.md#ac-17-4) | [T-09A](06_decomposition/tasks.md#t-09a), [T-09B](06_decomposition/tasks.md#t-09b), [T-10A](06_decomposition/tasks.md#t-10a), [T-10B](06_decomposition/tasks.md#t-10b), [T-14A](06_decomposition/tasks.md#t-14a), [T-14B](06_decomposition/tasks.md#t-14b), [T-17A](06_decomposition/tasks.md#t-17a), [T-17B](06_decomposition/tasks.md#t-17b), [T-N05](06_decomposition/tasks.md#t-n05) | loginStaff, logoutStaff, startSession, getSession, endSession, getSalesState, preparePurchase, getPurchase, startPayment, getPayment, listProblems, getProblem, acceptProblem, resolveProblem, verifyPurchase, reprintTicket, getStaffSalesState, setSalesState | [TC-M40](07_testing/test-cases-mvp.md#tc-m40), [TC-N14](07_testing/test-cases-mvp.md#tc-n14) |

БТ-12 (поэтапный ввод) проверяется по [карте релизов](02_requirements/story-map.md) и [чек-листу CL-01/CL-02](07_testing/checklist.md#scope-checks). Это ограничение состава поставки; отдельная пользовательская операция не требуется.

## Требования без отдельной пользовательской истории

| Требование | Чем покрывается |
|---|---|
| БТ-02 — понятность интерфейса | US-03, US-13, US-17; НФТ-11; TC-N10 |
| БТ-05 — передача роботам | US-09; НФТ-02, НФТ-04; процесс приготовления |
| БТ-12 — поэтапность | Карта историй и разделение функций по релизам; отдельная функция приложения не требуется |

## Связи уточненных правил

| Правило | Процесс и проверка |
|---|---|
| A-07/A-08; НФТ-05/10 — сохранение покупки до оплаты | Оформление и оплата; US-09/10; AC-09.1/09.2 и AC-10.1; метрика М-08. I-01 подтверждает held до банка. Граница 5 мин и перезапуск — TC-M04, позднее подтверждение — TC-M18 |
| A-03/A-14 — помощь без талона | Оформление и помощь; US-09/12/14/15; AC-09.3 и AC-15.1; S-01 ищет по localDate и печатному номеру, S-02 получает исходный киоск. Принтер выбирает сервер. S-02 показывает киоск печати и фиксирует вручение копии (TC-M15/27). Права и аудит — НФТ-12–15 |
| A-02/A-04 — остаток заказа после срока хранения | Приготовление и выдача; US-12/16; AC-16.2/16.4; НФТ-20. Недоступная выдача и поздний факт выдачи до срока — AC-16.1, TC-M43 |
| A-10 — порог подарка после скидок, до бонусов | Управление меню и акции; БТ-16, US-31, AC-31.1. Задание и подтверждение комплектации — I-03, TC-R33 |
| A-15 — плановая остановка продаж | Оформление и оплата; US-01/09/10/14/17; AC-17.2/17.3; доступность — НФТ-04, изоляция сессий — НФТ-14, аудит — НФТ-15. События C-08 и отдельная команда resume — TC-M39 |

Плановая остановка — операционный порядок для существующих историй, без отдельного календаря и изменения состава релизов.

## Цели и требования

| Цель | Связь |
|---|---|
| Ц-1 — проверка пилота | Метрики М-01–04, М-06–11; приемка требований MVP |
| Ц-2 — снижение издержек | БТ-01, БТ-03, БТ-05, БТ-06; эффект оценивается на уровне ресторана, а не одного приложения |
| Ц-3 — сокращение персонала | БТ-05, БТ-17; зависит от роботизированного комплекса |
| Ц-4 — автоматическое обслуживание | БТ-01–07 и соответствующие истории MVP |
| Ц-5 — тиражирование | НФТ-03; нагрузка и архитектура |

Количественные и организационные ограничения из раздела бизнеса проверяются расчетами и оценкой пилота, а не искусственными историями гостя. Технические зависимости проверяются по реестру интеграций и плану испытаний.

## Связи модели и архитектуры

Имена сущностей соответствуют [диаграмме классов](03_model/class-diagram.md) и [словарю](03_model/entities.md). C-ID определены в [компонентах](04_architecture/components.md), I-ID — в [интеграциях](04_architecture/integrations.md). Состояния приведены в [модели переходов](03_model/order-states.md). Релиз каждой истории сохраняется по карте.

| US | Сущности | Компоненты | Интеграции |
|---|---|---|---|
| US-01–03 | Restaurant, TradingDay, MenuVersion, MenuEntry, Dish, RecipeVersion, Session | C-01/02/08 | I-01 |
| US-04–05 | Cart, CartLine, Order, OrderLine | C-01/02 | I-01 перед оплатой |
| US-06 | Order.fulfillmentType, KitchenJob | C-02/05 | I-03 |
| US-07–08 | MenuEntry, PromotionRule, OrderLine | C-01/02 | I-01 |
| US-09–10 | Order, Reservation, PaymentAttempt, KitchenJob, Ticket, PrintTask | C-02–06/08 | I-01–05 |
| US-11–12 | KitchenJob, CellRef, CellAssignment, Ticket | C-05/08 | I-03/05 |
| US-13–14 | Problem, Notification, Employee, Role | C-05/07/08 | I-03 |
| US-15 | Order, Problem, Refund, PaymentAttempt, FiscalOperation | C-04/06/07 | I-02/04 |
| US-16 | CellRef, CellAssignment, Problem, Notification | C-05/07/08 | I-03 |
| US-17 | Session, Cart, Reservation, PaymentAttempt, Restaurant | C-02/03/04/08 | I-01/02 |
| US-18–19 | LoyaltyProfileRef, Session | C-07/09 | I-07/08 |
| US-20–21 | BonusOperationRef, Order, PaymentAttempt | C-02/04/09 | I-07 |
| US-22 | PaymentAttempt, Ticket, PrintTask | C-04/06 | I-04/05/10 |
| US-23 | Order, Problem, PaymentAttempt, Refund | C-02/04/07 | I-02/04 |
| US-24–25 | Order, Refund, KitchenJob, CellAssignment, FiscalOperation | C-04–07 | I-02/03/04/10 по способу |
| US-26 | Problem, Notification, MenuEntry | C-01/07 | I-01/03 |
| US-27–29 | MenuVersion, MenuEntry, PromotionRule, ComboLine, TradingDay | C-01/07/08 | — |
| US-30 | RecipeVersion, RecipeLine, IngredientRef | C-01/07 | I-01 — справочник IngredientRef; I-03 — согласованная версия |
| US-31 | GiftAllocation, Reservation, Order | C-02/03/09 | I-01/03 |
| US-32–33 | RobotRef, IngredientRef, актуальность состояний | C-05/07 | I-03; в MVP внешний I-06 |
| US-34 | Order, PaymentAttempt, Refund, ExportBatch, ExportLine | C-04/10 | I-09 |
| US-35 | FiscalOperation, PrintTask, Problem | C-06/07 | I-04/05 |

Группы диапазонов охватывают все US-01–35; они не меняют ID и не объединяют истории. AC-09.4 связан с US-02/09/10/15, AC-16.5/16.6 — с US-12/16, AC-17.4 — с US-09/10/14/17. Их БТ следуют из существующих связей этих историй.

| НФТ | Данные и компоненты | Проверка |
|---|---|---|
| НФТ-01–03 | C-01–06/08, снимки, задания и проекции | Профиль нагрузки, 4 киоска, сеть 10–130, первая отправка ≤1 с для подтвержденного пригодного резерва, включая проверку; неизвестная пригодность — сверка, невозможность исполнения — полный возврат |
| НФТ-04–07 | C-08, PostgreSQL, копии и WAL | Бюджет A-16, резервирование, RPO/RTO и восстановление |
| НФТ-08–10 | C-01/03/04/05/08, версии и ID операций | Свежесть p95 ≤2 с, блокировка, внешние повторы и сверка |
| НФТ-11 | C-01/02, Session | не менее 5 из 10 участников завершают заказ за ≤3 мин; среднее отдельно для мощности |
| НФТ-12–16 | C-07/08/09, роли, сессии, аудит, профиль | Права по ресторану, очистка, отсутствие карточных данных, 90 дней/12 месяцев |
| НФТ-17 | Адаптеры C-03–06/09/10 | REST, совместимость оборудования, инфраструктура заказчика |
| НФТ-18 | C-05, RobotRef | Первый релиз, обновление не реже 30 с и признак устаревания |
| НФТ-19 | C-07, Notification | Принятие ≤1 мин после доставки; оба времени фиксируются |
| НФТ-20 | C-05/06, CellAssignment, Ticket, recordBoardVisibility, I-03/05 | Последовательность веса/дверцы, остатки, срок, неисправность; подтверждение первого показа и применения expiresAt — AC-11.1 |

A-16 связан с НФТ-04/М-07, AC-17.3 и расчетом доступности. Регулярные технические работы выполняются вне 10:00–22:00; остановки внутри дня по A-15 суммируются со сбоями в общем бюджете простоя. A-02/A-03/A-05/A-08/A-14 связаны с реестром проверок внешних возможностей. Расчетный профиль и испытания A-06 находятся в [нагрузке](04_architecture/load-db.md#verification). Подтверждение конкретных поставщиков не получено; связи не означают успешного испытания.

## Цепочки интерфейсов и API

[Описание экранов](05_api/ui.md) · [Прототипы](05_api/prototypes.md) · [Операции API](05_api/resources.md) · [OpenAPI](05_api/openapi.yaml) · [Схемы взаимодействия](04_architecture/integration-flows.md).

| US | Экран | Операция / внешний интерфейс |
|---|---|---|
| US-01 | K-01 | startSession, getMenu |
| US-02 | K-01/03 | getMenu, preparePurchase |
| US-03 | K-02 | getMenuItem |
| US-04 | K-01/03 | getCart, replaceCart |
| US-05 | K-03 | replaceCart |
| US-06 | K-03 | replaceCart, startPayment |
| US-07 | K-02 | getMenuItem, replaceCart |
| US-08 | K-03 | preparePurchase |
| US-09 | K-03–06, S-02 | preparePurchase, startPayment, getPayment, getSession, getPurchase, verifyPurchase, reprintTicket |
| US-10 | K-04/06 | getPayment, getSession, getPurchase |
| US-11 | B-01 | getBoard, confirmBoardDisplay, getBoardDisplay |
| US-12 | B-02, S-02 | I-03 (талон и выдача), reprintTicket |
| US-13 | K-06, B-01/02 | getPurchase, getBoard; помощь в зале |
| US-14 | S-01/02/04 | listProblems, confirmProblemDisplay, acceptProblem, resolveProblem, getStaffSalesState, setSalesState |
| US-15 | S-01/02 | findPurchases, getStaffPurchase, recordImpossibility, registerExternalRefund, getRefund |
| US-16 | S-03 | listCells, serviceCell, acceptProblem |
| US-17 | K-01/07, S-04 | endSession, getSession, getSalesState, setSalesState |
| US-18 | R-01/02 | requestLoyaltyCode, confirmLoyalty, preparePurchase |
| US-19 | R-01/02 | confirmLoyalty, getLoyalty |
| US-20 | R-02 | getLoyalty, preparePurchase |
| US-21 | R-02, K-05 | getPurchase; I-07 начисление по оплате |
| US-22 | R-02/03 | getSession, startPayment, getPayment, cancelCashPayment |
| US-23 | R-04 | findPurchases, getStaffPurchase |
| US-24 | R-04 | cancelOrder, startRefund, getRefund |
| US-25 | R-04 | cancelOrder, startRefund, registerExternalRefund, getRefund |
| US-26 | R-04 | listNotifications |
| US-27 | R-05 | getMenuDraft, saveMenuEntry |
| US-28 | R-05 | getMenuDraft, saveMenuEntry |
| US-29 | R-05 | savePromotion, saveMenuEntry |
| US-30 | R-06 | getMenuDraft, getIngredients, getRecipe, saveRecipe |
| US-31 | R-02/05 | preparePurchase, savePromotion, I-03 (комплектация) |
| US-32 | R-07 | getProduction |
| US-33 | R-07 | getProduction |
| US-34 | R-08 | getSalesReport, createExport, getExport |
| US-35 | K-05/06, S-02 | getPurchase, getStaffPurchase |

| Ветка и AC | Экран → операция | Данные/состояние → компонент/интеграция → результат и восстановление |
|---|---|---|
| Расчет и согласие, AC-05.1/08.1/09.1 | K-03 → replaceCart, preparePurchase, startPayment | Cart.version, Calculation, Reservation → C-01–04/I-01/02 → явное согласие, снимок до банка; конфликт требует перечитать |
| Неизвестный платеж, AC-09.2/09.4/10.1 | K-04 → getPayment, getSession, getPurchase | PaymentAttempt.unknown, исходный резерв → C-03/04/08/I-01/02 → сверка каждые 10 с, менеджер через 1 мин; поздний успех без новой покупки, непригодность — полный возврат |
| Документы и помощь, AC-09.3/15.1/35.1 | K-05/06, S-02 → getStaffPurchase, verifyPurchase, reprintTicket | FiscalOperation, PrintTask, Problem → C-06/07/I-04/05 → тот же талон, независимый чек, повтор исходной команды |
| Первое появление и доступ, AC-11.1/12.1 | B-01/02 → getBoard, confirmBoardDisplay, getBoardDisplay; I-03 | Версия проекции, CellAssignment.firstReadyAt/expiresAt → C-05/08/I-03 → 10 мин от первого показа; применение срока до доступа; сверка исходной версии |
| Частичное получение, срок и контроль, AC-16.1–16.6 | B-02/S-03 → I-03, listCells, serviceCell | CellAssignment, Ticket, исправность/последовательность → C-05/07/I-03 → issued только по полному циклу; остаток сохраняет срок, неявка требует талона и подтвержденного интервала доступа по AC-16.1; при подтвержденном неполучении и нарушенном или недоказуемом окне → отмена и полный возврат по TC-M43 |
| Отмена и деньги, AC-15.1/24.1/25.1 | S-02/R-04 → recordImpossibility, registerExternalRefund; R1 cancelOrder/startRefund | Order и Refund раздельно → C-04–07/I-02/03/04/10 → при просьбе гостя в R1 требуется stopped_before_start по I-03 (TC-R51); полный возврат по исходной операции |
| Остановка и гонка, AC-17.2–17.4 | K-07/S-04 → getSalesState, setSalesState | Restaurant.manualStop, PaymentAttempt → C-02/04/08 → порядок регистрации, запрет только новых оплат; старые сверяются, resume после проверок |
| Лояльность и подарок, AC-18.1–21.1/31.1 | R-01/02 → confirmLoyalty, getLoyalty, preparePurchase | LoyaltyProfileRef, BonusOperationRef, GiftAllocation → C-02/03/09/I-01/07/08 → лимит 30%, начисление 5%, строгий порог подарка, компенсация при возврате |
| Наличные, AC-22.1 | R-02/03 → getSession, startPayment, getPayment, cancelCashPayment | PaymentAttempt, возврат внесенного → C-04/I-10 → подтверждение суммы, сдача; неизвестный возврат блокирует терминал |
| Рабочие места, AC-23.1/26.1–30.1/32.1–34.1 | R-04–08 → операции соответствующих строк | Order/Notification, MenuVersion/RecipeVersion, RobotRef, ExportBatch → C-01/05/07/10/I-03/09 → будущий день, версии, свежесть 30 с, досылка поздней оплаты и повтор каждого пакета без удвоения (TC-R40) |

Там, где действие происходит на устройстве комплекса или во внешнем контуре, клиентский REST-эндпоинт не добавляется искусственно. Все 35 историй имеют экран либо автоматический результат в границах своего релиза. Все AC связаны с задачами и запланированными тестами в основной матрице.

Для AC-17.1 запрет endSession в created проверяется в TC-N13 (T-17A). Сверка удержания после сбоя проверяется в TC-M04 (T-02A, T-09A). Для AC-14.1 минимум displayedAt и поздний пересчет реакции проверяются в TC-N19 (T-14B, T-N07).

## НФТ → задачи → проверки

Условия стенда, измерения и ожидаемые результаты заданы в полных кейсах MVP. НФТ-16 и НФТ-18 имеют дополнительный объем R1. Протоколы реальных испытаний еще не получены.

| НФТ | Задачи | Проверки |
|---|---|---|
| НФТ-01 | [T-N01](06_decomposition/tasks.md#t-n01) | [TC-N01](07_testing/test-cases-mvp.md#tc-n01) |
| НФТ-02 | [T-N01](06_decomposition/tasks.md#t-n01) | [TC-N02](07_testing/test-cases-mvp.md#tc-n02), [TC-M18](07_testing/test-cases-mvp.md#tc-m18) |
| НФТ-03 | [T-N01](06_decomposition/tasks.md#t-n01) | [TC-N01](07_testing/test-cases-mvp.md#tc-n01) |
| НФТ-04 | [T-N02](06_decomposition/tasks.md#t-n02) | [TC-N03](07_testing/test-cases-mvp.md#tc-n03) |
| НФТ-05 | [T-N02](06_decomposition/tasks.md#t-n02) | [TC-N04](07_testing/test-cases-mvp.md#tc-n04), [TC-M13](07_testing/test-cases-mvp.md#tc-m13) |
| НФТ-06 | [T-N02](06_decomposition/tasks.md#t-n02) | [TC-N05](07_testing/test-cases-mvp.md#tc-n05) |
| НФТ-07 | [T-N02](06_decomposition/tasks.md#t-n02) | [TC-N06](07_testing/test-cases-mvp.md#tc-n06) |
| НФТ-08 | [T-N01](06_decomposition/tasks.md#t-n01) | [TC-N07](07_testing/test-cases-mvp.md#tc-n07) |
| НФТ-09 | [T-N03](06_decomposition/tasks.md#t-n03) | [TC-N08](07_testing/test-cases-mvp.md#tc-n08) |
| НФТ-10 | [T-N03](06_decomposition/tasks.md#t-n03) | [TC-N09](07_testing/test-cases-mvp.md#tc-n09), [TC-M17](07_testing/test-cases-mvp.md#tc-m17) |
| НФТ-11 | [T-N04](06_decomposition/tasks.md#t-n04) | [TC-N10](07_testing/test-cases-mvp.md#tc-n10) |
| НФТ-12 | [T-N05](06_decomposition/tasks.md#t-n05), [T-N08](06_decomposition/tasks.md#t-n08) | [TC-N11](07_testing/test-cases-mvp.md#tc-n11), [TC-R53](07_testing/test-cases-r1.md#tc-r53) |
| НФТ-13 | [T-N05](06_decomposition/tasks.md#t-n05) | [TC-N12](07_testing/test-cases-mvp.md#tc-n12) |
| НФТ-14 | [T-N05](06_decomposition/tasks.md#t-n05), [T-N08](06_decomposition/tasks.md#t-n08) | [TC-N13](07_testing/test-cases-mvp.md#tc-n13), [TC-R43](07_testing/test-cases-r1.md#tc-r43) |
| НФТ-15 | [T-28A](06_decomposition/tasks.md#t-28a), [T-N05](06_decomposition/tasks.md#t-n05), [T-N08](06_decomposition/tasks.md#t-n08) | [TC-N14](07_testing/test-cases-mvp.md#tc-n14), [TC-R26](07_testing/test-cases-r1.md#tc-r26), [TC-R43](07_testing/test-cases-r1.md#tc-r43) |
| НФТ-16 | [T-N05](06_decomposition/tasks.md#t-n05), [T-N08](06_decomposition/tasks.md#t-n08) | [TC-N15](07_testing/test-cases-mvp.md#tc-n15), [TC-R42](07_testing/test-cases-r1.md#tc-r42) |
| НФТ-17 | [T-N06](06_decomposition/tasks.md#t-n06) | [TC-N16](07_testing/test-cases-mvp.md#tc-n16) |
| НФТ-18 | [T-N08](06_decomposition/tasks.md#t-n08) | [TC-R35](07_testing/test-cases-r1.md#tc-r35), [TC-R36](07_testing/test-cases-r1.md#tc-r36), [TC-R37](07_testing/test-cases-r1.md#tc-r37) |
| НФТ-19 | [T-N07](06_decomposition/tasks.md#t-n07) | [TC-N19](07_testing/test-cases-mvp.md#tc-n19) |
| НФТ-20 | [T-N06](06_decomposition/tasks.md#t-n06) | [TC-N20](07_testing/test-cases-mvp.md#tc-n20) |
