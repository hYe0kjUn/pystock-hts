**CpUtil**

    getConnected -> (boolean)
        - DASHIN HTS 서버 상태에 대해 반환
    
---

    getStockCount -> (number)
        - 전체 종목 갯수를 반환

---

    getStockCodeList -> (list)
        - 전체 종목 코드 리스트 반환

---

    getStockCodeToName(stock_code: string) -> string
        - 주식 코드에 대한 이름 반환

---

    getStockCodeAndNameAll -> (object {"stock_code": "stock_name", ... } )
        - 전체 종목에 대한 코드 (key) 이름 (value) 반환



**CpSysDib**

    getStockChartPriceToDate(date_count: number, stock_code: string) -> date_list: list, stock_high_price: list, stock_low_price: list, stock_last_price: list
        - 일수 (date_count) 만큼의 과거 일자, 고가, 저가, 종가 반환

---

    getStockPer(stock_code: string) -> number
        - 주식 코드에 대한 PER 반환

**CpTrade**

    buyStock(stock_code: string) -> boolean
        - 시장가로 stock_code 에 해당하는 종목을 매수

    sellStock(stock_code: string) -> boolean
        - 시장가로 stock_code 에 해당하는 종목을 매도