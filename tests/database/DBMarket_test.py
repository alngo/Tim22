from datetime import datetime
import pytest
from tests.context import DBMarket


class TestDBMarket:
    db = DBMarket("empty", 0000)

    def test_write_candlestick(self):
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        with pytest.raises(NotImplementedError) as err:
            self.db.write_candlestick('EURUSD', timestamp, 1, 2, 3, 4, 5)
        assert "Method is required!" in str(err.value)

    def test_read_candlestick(self):
        with pytest.raises(NotImplementedError) as err:
            self.db.read_candlestick('EURUSD', '1m', limit=10)
        assert "Method is required!" in str(err.value)

    def test_list_symbols(self):
        with pytest.raises(NotImplementedError) as err:
            self.db.list_symbols()
        assert "Method is required!" in str(err.value)
