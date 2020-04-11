def simple_rate_of_return(df):
    """
    Compute simple rate of return for a given OHLCV
    return a series
    """
    return (df["Close"] / df["Close"].shift(1)) - 1
