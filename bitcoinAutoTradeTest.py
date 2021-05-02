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

        # 오전 9:00 시 < 현재 < 오후 8:59:50
        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-BTC", 0.5)
            current_price = get_current_price("KRW-BTC")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000: #최소금액
                    upbit.buy_market_order("KRW-DOGE", krw*0.9995) #수수료 계산 0.9995
        # DOGE 
        elif start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-DOGE", 0.5)
            current_price = get_current_price("KRW-DOGE")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-DOGE", krw*0.9995) #수수료 계산 0.9995
        # ETC(이더리움)
        elif start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-ETC", 0.5)
            current_price = get_current_price("KRW-ETC")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-ETC", krw*0.9995) #수수료 계산 0.9995
        # XRP(리플)
        elif start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-XRP", 0.5)
            current_price = get_current_price("KRW-XRP")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-XRP", krw*0.9995) #수수료 계산 0.9995
        # MED(메디블록)
        elif start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-MED", 0.5)
            current_price = get_current_price("KRW-MED")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-MED", krw*0.9995) #수수료 계산 0.9995
        # VET(비체인)
        elif start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-VET", 0.5)
            current_price = get_current_price("KRW-VET")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-VET", krw*0.9995) #수수료 계산 0.9995
        # EOS(이오스)
        elif start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-EOS", 0.5)
            current_price = get_current_price("KRW-EOS")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-EOS", krw*0.9995) #수수료 계산 0.9995
        # NEO(네오)
        elif start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-NEO", 0.5)
            current_price = get_current_price("KRW-NEO")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-NEO", krw*0.9995) #수수료 계산 0.9995
        # PXL(픽셀)
        elif start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-PXL", 0.5)
            current_price = get_current_price("KRW-PXL")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-PXL", krw*0.9995) #수수료 계산 0.9995
        # ARDR(아더)
        elif start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-ARDR", 0.5)
            current_price = get_current_price("KRW-ARDR")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-ARDR", krw*0.9995) #수수료 계산 0.9995
        # EDR(엔도르)
        elif start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-BTC", 0.5)
            current_price = get_current_price("KRW-BTC")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-BTC", krw*0.9995) #수수료 계산 0.9995
        # BTG(비트코인골드)
        elif start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-BTG", 0.5)
            current_price = get_current_price("KRW-BTG")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000: 
                    upbit.buy_market_order("KRW-BTG", krw*0.9995) #수수료 계산 0.9995
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

            if btc > 0.00008:
                upbit.sell_market_order("KRW-BTC", btc*0.9995) #수수료고려 95.95%
            elif doge > 0.00008:
                upbit.sell_market_order("KRW-doge", btc*0.9995)
            elif etc > 0.00008:
                upbit.sell_market_order("KRW-etc", btc*0.9995)
            elif xrp > 0.00008:
                upbit.sell_market_order("KRW-xrp", btc*0.9995)
            elif med > 0.00008:
                upbit.sell_market_order("KRW-med", btc*0.9995)
            elif vet > 0.00008:
                upbit.sell_market_order("KRW-vet", btc*0.9995)
            elif eos > 0.00008:
                upbit.sell_market_order("KRW-eos", btc*0.9995)
            elif neo > 0.00008:
                upbit.sell_market_order("KRW-neo", btc*0.9995)
            elif pxl > 0.00008:
                upbit.sell_market_order("KRW-pxl", btc*0.9995) 
            elif ardr > 0.00008:
                upbit.sell_market_order("KRW-ardr", btc*0.9995)
            elif edr > 0.00008:
                upbit.sell_market_order("KRW-edr", btc*0.9995)
            elif btg > 0.00008:
                upbit.sell_market_order("KRW-btg", btc*0.9995)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)