def simple_rate_of_return(df):
    """
    Compute simple rate of return for a given OHLCV
    return a series
    """
    return (df["Close"] / df["Close"].shift(1)) - 1

def avg_daily_rate_of_return(df):
    """
    Compute average daily rate of return
    return a float
    """
    serie = simple_rate_of_return(df)
    return round(serie.mean() * 100, 2)

def avg_annual_rate_of_return(df):
    """
    Compute average annual rate of return
    return a float
    """
    serie = simple_rate_of_return(df)
    return round((serie.mean() * 250) * 100, 2)
