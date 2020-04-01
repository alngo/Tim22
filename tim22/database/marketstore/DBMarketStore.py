import numpy as np
import pymarketstore as pymkts
from ..DBMarket import DBMarket


class DBMarketStore(DBMarket):
    def __init__(self, host, port, endpoint="http://localhost:5993/rpc"):
        super(DBMarketStore, self).__init__(host, port)
        self.cli = pymkts.Client(f"{endpoint}")

    def write_candlestick(self, symbol, period,
                          epoch, open, high, low, close, volume):
        try:
            data = np.array([(
                epoch,
                open,
                high,
                low,
                close,
                volume
            )],
                dtype=[
                ('Epoch', 'i8'),
                ('open', 'f4'),
                ('high', 'f4'),
                ('low', 'f4'),
                ('close', 'f4'),
                ('volume', 'i8')
            ])
            self.cli.write(data, f"{symbol}/{period}/OHLCV")
            return True
        except Exception as err:
            print(f"Error: {err}")
            return False

    def read_candlestick(self, symbol, period, start=None, end=None, limit=10):
        params = pymkts.Params(symbol, period, 'OHLCV', start, end, limit)
        reply = self.cli.query(params)
        return reply.first().df()

    def list_symbols(self):
        return self.cli.list_symbols()
