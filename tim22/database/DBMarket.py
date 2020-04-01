from abc import abstractmethod


class DBMarket(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port

    @abstractmethod
    def write_candlestick(self, symbol, epoch, open, high, low, close, volume):
        """
        Method use to write data
        Return a boolean
        """
        raise NotImplementedError('Method is required!')

    @abstractmethod
    def read_candlestick(self, symbol, period, start=None, end=None, limit=10):
        """
        Method use to read data
        Return a OHLCV dataframe
        """
        raise NotImplementedError('Method is required!')

    def list_symbols(self):
        """
        Method use to list symbols in database
        The list of all symbols stored are returned.
        """
        raise NotImplementedError('Method is required!')
