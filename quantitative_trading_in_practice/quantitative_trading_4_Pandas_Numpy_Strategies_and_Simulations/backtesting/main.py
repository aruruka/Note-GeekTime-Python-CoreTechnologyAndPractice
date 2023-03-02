import sys
sys.path.append('.')
from quantitative_trading_in_practice.quantitative_trading_4_Pandas_Numpy_Strategies_and_Simulations.backtesting.backtesting import Backtest
from quantitative_trading_in_practice.quantitative_trading_4_Pandas_Numpy_Strategies_and_Simulations.backtesting.exchange_api import ExchangeAPI
from quantitative_trading_in_practice.quantitative_trading_4_Pandas_Numpy_Strategies_and_Simulations.backtesting.strategy import SmaCross
from quantitative_trading_in_practice.quantitative_trading_4_Pandas_Numpy_Strategies_and_Simulations.utils import read_file


def main():
    BTCUSD = read_file('quantitative_trading_in_practice/BTCUSD_GEMINI.csv')
    ret = Backtest(BTCUSD, SmaCross, ExchangeAPI, 10000.0, 0.00).run()
    print(ret)

if __name__ == '__main__':
    main()