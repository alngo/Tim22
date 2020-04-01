import os
import pandas as pd
import pymarketstore as pymkts
from datetime import datetime
from tests.context import DBMarketStore


class TestFakeDBMarketStore:
    def test_init_DBMarketstore(self, mocker):
        mocker.patch('pymarketstore.Client', mock_pymarketstore_Client)
        db = DBMarketStore("empty", 5555)
        assert db.cli.endpoint == "http://localhost:5993/rpc"
        assert db.host == "empty"
        assert db.port == 5555

    def test_ok_write_candlestick(self, mocker):
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        mocker.patch('pymarketstore.Client', mock_pymarketstore_Client)
        db = DBMarketStore("empty", 5555)
        res = db.write_candlestick('EURUSD', '1Min', timestamp, 1, 2, 3, 4, 5)
        assert res is True

    def test_err_write_candlestick(self, mocker):
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        mocker.patch('pymarketstore.Client.write', mock_pymarketstore_writerr)
        db = DBMarketStore("empty", 5555)
        res = db.write_candlestick('EURUSD', '1Min', timestamp, 1, 2, 3, 4, 5)
        assert res is False

    def test_ret_write_candlestick(self, mocker):
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        mocker.patch('pymarketstore.Client.write', mock_pymarketstore_wreterr)
        db = DBMarketStore("empty", 5555)
        res = db.write_candlestick('EURUSD', '1Min', timestamp, 1, 2, 3, 4, 5)
        assert res is False

    def test_read_candlestick(self, mocker):
        mocker.patch('pymarketstore.Client', mock_pymarketstore_Client)
        db = DBMarketStore("empty", 5555)
        res = db.read_candlestick('EURUSD', '1Min', limit=10)
        assert isinstance(res, pd.DataFrame)

    def test_list_symbols(self, mocker):
        mocker.patch('pymarketstore.Client', mock_pymarketstore_Client)
        db = DBMarketStore("empty", 5555)
        res = db.list_symbols()
        assert isinstance(res, list)


class TestEndDBMarketStore:
    def test_init_DBMarketstore(self):
        db = DBMarketStore("dbmarket", 5993,
                           endpoint=os.getenv('DB_ENDPOINT'))
        assert db.cli.endpoint == os.getenv('DB_ENDPOINT')
        assert db.host == "dbmarket"
        assert db.port == 5993

    def test_ok_write_candlestick(self):
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        db = DBMarketStore("dbmarket", 5993,
                           endpoint=os.getenv('DB_ENDPOINT'))
        res = db.write_candlestick('EURUSD', '1Min', timestamp, 1, 2, 3, 4, 5)
        assert res is True

    def test_read_candlestick(self):
        db = DBMarketStore("dbmarket", 5993,
                           endpoint=os.getenv('DB_ENDPOINT'))
        res = db.read_candlestick('EURUSD', '1Min', limit=10)
        assert isinstance(res, pd.DataFrame)
        assert res.iloc[0]["Open"] == 1.0
        assert res.iloc[0]["High"] == 2.0
        assert res.iloc[0]["Low"] == 3.0
        assert res.iloc[0]["Close"] == 4.0
        assert res.iloc[0]["Volume"] == 5

    def test_list_symbols(self):
        db = DBMarketStore("dbmarket", 5993,
                           endpoint=os.getenv('DB_ENDPOINT'))
        res = db.list_symbols()
        assert isinstance(res, list)
        assert res[0] == "EURUSD"


# MOCK pymarketstore class

class mock_pymarketstore_Client(object):
    def __init__(self, endpoint='http://localhost:5993/rpc'):
        self.endpoint = endpoint

    def write(self, recarray, tbk, isvariablelength=False):
        return {'responses': None}

    def query(self, params):
        query = mock_pymarketstore_QueryReply()
        return query

    def list_symbols(self):
        return ["EURUSD", "USDJPY"]


def mock_pymarketstore_writerr(self, recarray, tbk, isvariablelength=False):
    raise Exception("Test exception")


def mock_pymarketstore_wreterr(self, recarray, tbk, isvariablelength=False):
    return {"responses": [{"error": "some error"}]}


class mock_pymarketstore_DataSet():
    @staticmethod
    def df():
        return pd.DataFrame()


class mock_pymarketstore_QueryReply():
    @staticmethod
    def first():
        dataset = mock_pymarketstore_DataSet()
        return dataset
