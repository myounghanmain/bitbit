import time
import pyupbit
import datetime

access = ""
secret = ""

def get_target_price(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    # 다음날 시가 = 'close' 임            # 변동폭
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price

def get_hightarget_price(ticker, k):
    """변동성 돌파 전략 중 고가 목표가 기준 """
    """수익률 50% 급등한 종목 """
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    hightarget_price = df.iloc[0]['close'] * 1.5
    return hightarget_price

def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time

def get_balance(ticker):
    """잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0

def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(tickers=ticker)[0]["orderbook_units"][0]["ask_price"]

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")

# 자동매매 시작
while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-BTC")  # 9:00
        end_time = start_time + datetime.timedelta(days=1) #9:00+1일

        # 오전 9:00 시 < 현재 < 오전 8:59:50
        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price_btc = get_target_price("KRW-BTC", 0.5)
            current_price_btc = get_current_price("KRW-BTC")
            
            target_price_doge = get_target_price("KRW-DOGE", 0.5):
            current_price_doge = get_current_price("KRW-DOGE")

            target_price_eth = get_target_price("KRW-ETH", 0.5)
            current_price_eth = get_current_price("KRW-ETH")

            target_price_xrp = get_target_price("KRW-XRP", 0.5)
            current_price_xrp = get_current_price("KRW-XRP")

            target_price_med = get_target_price("KRW-MED", 0.5)
            current_price_med = get_current_price("KRW-MED")

            target_price_vet = get_target_price("KRW-VET", 0.5)
            current_price_vet = get_current_price("KRW-VET")

            target_price_eos = get_target_price("KRW-EOS", 0.5)
            current_price_eos = get_current_price("KRW-EOS")

            target_price_neo = get_target_price("KRW-NEO", 0.5)
            current_price_neo = get_current_price("KRW-NEO")

            target_price_pxl = get_target_price("KRW-PXL", 0.5)
            current_price_pxl = get_current_price("KRW-PXL")

            target_price_ardr = get_target_price("KRW-ARDR", 0.5)
            current_price_ardr = get_current_price("KRW-ARDR")

            target_price_edr = get_target_price("KRW-EDR", 0.5)
            current_price_edr = get_current_price("KRW-EDR")

            target_price_btg = get_target_price("KRW-BTG", 0.5)
            current_price_btg = get_current_price("KRW-BTG")

            target_price_srm = get_target_price("KRW-SRM", 0.5)
            current_price_srm = get_current_price("KRW-SRM")

            target_price_btt = get_target_price("KRW-BTT", 0.5)
            current_price_btt = get_current_price("KRW-BTT")
        # BTC(비트코인)    
            if target_price_btc < current_price_btc:
                krw = get_balance("KRW")
                if krw > 5000: #최소금액
                    upbit.buy_market_order("KRW-BTC", krw*0.4998) #수수료 계산 0.9995
        # DOGE(도지코인) 
            elif target_price_doge < current_price_doge:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-DOGE", krw*0.4998) #수수료 계산 0.9995
        # ETH(이더리움)
            elif target_price_eth < current_price_eth:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-ETH", krw*0.4998) #수수료 계산 0.9995
        # XRP(리플)
            elif target_price_xrp < current_price_xrp:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-XRP", krw*0.4998) #수수료 계산 0.9995
        # MED(메디블록)
            elif target_price_med < current_price_med:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-MED", krw*0.4998) #수수료 계산 0.9995
        # VET(비체인)
            elif target_price_vet < current_price_vet:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-VET", krw*0.4998) #수수료 계산 0.9995
        # EOS(이오스)
            elif target_price_eos < current_price_eos:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-EOS", krw*0.4998) #수수료 계산 0.9995
        # NEO(네오)
            elif target_price_neo < current_price_neo:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-NEO", krw*0.4998) #수수료 계산 0.9995
        # PXL(픽셀)
            elif target_price_pxl < current_price_pxl:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-PXL", krw*0.4998) #수수료 계산 0.9995
        # ARDR(아더)
            elif target_price_ardr < current_price_ardr:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-ARDR", krw*0.4998) #수수료 계산 0.9995
        # EDR(엔도르)
            elif target_price_edr < current_price_edr:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-EDR", krw*0.4998) #수수료 계산 0.9995
        # BTG(비트코인골드)
            elif target_price_btg < current_price_btg:
                krw = get_balance("KRW")
                if krw > 5000: 
                    upbit.buy_market_order("KRW-BTG", krw*0.4998) #수수료 계산 0.9995
        # SRM(세럼)
            elif target_price_srm < current_price_srm:
                krw = get_balance("KRW")
                if krw > 5000: 
                    upbit.buy_market_order("KRW-SRM", krw*0.4998) #수수료 계산 0.9995
        # BTT(비트토렌트)
            elif target_price_btt < current_price_btt:
                krw = get_balance("KRW")
                if krw > 5000: 
                    upbit.buy_market_order("KRW-BTT", krw*0.4998) #수수료 계산 0.9995
        else:   #전량매도 코드
            btc = get_balance("BTC")
            doge = get_balance('DOGE')
            etc = get_balance("ETC")
            xrp = get_balance("XRP")
            med = get_balance("MED")  
            vet = get_balance("VET")
            eos = get_balance("EOS")
            neo = get_balance("NEO")
            pxl = get_balance("PXL")
            ardr= get_balance("ARDR")
            edr = get_balance("EDR")
            btg = get_balance("BTG")
            srm = get_balance("SRM")
            btt = get_balance("BTT")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-BTC", btc*0.9995) #수수료고려 95.95%
            elif doge > 0.00008:
                upbit.sell_market_order("KRW-DOGE", btc*0.9995)
            elif etc > 0.00008:
                upbit.sell_market_order("KRW-ETC", btc*0.9995)
            elif xrp > 0.00008:
                upbit.sell_market_order("KRW-XRP", btc*0.9995)
            elif med > 0.00008:
                upbit.sell_market_order("KRW-MED", btc*0.9995)
            elif vet > 0.00008:
                upbit.sell_market_order("KRW-VET", btc*0.9995)
            elif eos > 0.00008:
                upbit.sell_market_order("KRW-EOS", btc*0.9995)
            elif neo > 0.00008:
                upbit.sell_market_order("KRW-NEO", btc*0.9995)
            elif pxl > 0.00008:
                upbit.sell_market_order("KRW-PXL", btc*0.9995) 
            elif ardr > 0.00008:
                upbit.sell_market_order("KRW-ARDR", btc*0.9995)
            elif edr > 0.00008:
                upbit.sell_market_order("KRW-EDR", btc*0.9995)
            elif btg > 0.00008:
                upbit.sell_market_order("KRW-BTG", btc*0.9995)
            elif srm > 0.00008:
                upbit.sell_market_order("KRW-SRM", btc*0.9995)
            elif btt > 0.00008:
                upbit.sell_market_order("KRW-BTT", btc*0.9995)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)