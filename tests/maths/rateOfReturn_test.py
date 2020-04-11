import pytest
import numpy as np
import pandas as pd
from tests.context import simple_rate_of_return, avg_daily_rate_of_return, avg_annual_rate_of_return

def test_simple_rate_of_return():
    df = pd.DataFrame([1,2,3,4,5,6,7,8,9,10], columns=["Close"])
    expected = simple_rate_of_return(df)
    assert type(expected) is pd.Series
    assert np.isnan(expected[0])
    assert round(expected[1], 2) == 1.00
    assert round(expected[2], 2) == 0.50
    assert round(expected[3], 2) == 0.33
    assert round(expected[4], 2) == 0.25

def test_avg_daily_rate_of_return():
    df = pd.DataFrame([1,2,3,4,5,6,7,8,9,10], columns=["Close"])
    avg = avg_daily_rate_of_return(df)
    assert type(avg) is np.float64

def test_avg_annual_rate_of_return():
    df = pd.DataFrame([1,2,3,4,5,6,7,8,9,10], columns=["Close"])
    avg = avg_annual_rate_of_return(df)
    assert type(avg) is np.float64
