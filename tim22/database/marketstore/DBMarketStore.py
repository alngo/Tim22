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
                ('Open', 'f4'),
                ('High', 'f4'),
                ('Low', 'f4'),
                ('Close', 'f4'),
                ('Volume', 'i8')
            ])
            resp = self.cli.write(data, f"{symbol}/{period}/OHLCV")
            if resp["responses"] is not None:
                raise Exception(resp["responses"][0]['error'])
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
