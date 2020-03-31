import pandas as pd
from datetime import datetime
from tests.context import DBMarketStore


class mock_pymarketstore_Client(object):
    def __init__(self, endpoint='http://localhost:5993/rpc'):
        self.endpoint = endpoint

    def write(self, recarray, tbk, isvariablelength=False):
        return {'responses': None}

    def query(self, params):
        return pd.DataFrame()

    def list_symbols(self):
        return ["EURUSD", "USDJPY"]


class TestDBMarketStore:
    def test_init_DBMarketstore(self, mocker):
        mocker.patch('pymarketstore.Client', mock_pymarketstore_Client)
        db = DBMarketStore("empty")
        assert db.endpoint == "empty"

    def test_write_candlestick(self, mocker):
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        mocker.patch('pymarketstore.Client', mock_pymarketstore_Client)
        db = DBMarketStore("empty")
        res = db.write_candlestick('EURUSD', '1m', timestamp, 1, 2, 3, 4, 5)
        assert res is True

    def test_read_candlestick(self, mocker):
        mocker.patch('pymarketstore.Client', mock_pymarketstore_Client)
        db = DBMarketStore("empty")
        res = db.read_candlestick('EURUSD', '1m', limit=10)
        assert isinstance(res, pd.DataFrame)

    def test_list_symbols(self, mocker):
        mocker.patch('pymarketstore.Client', mock_pymarketstore_Client)
        db = DBMarketStore("empty")
        res = db.list_symbols()
        assert isinstance(res, list)
