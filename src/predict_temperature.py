from datetime import datetime

import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing


def predictTemperature(startDate, endDate, temperature, n):
    date_fmt = "%Y-%m-%d"
    start_date = datetime.strptime(startDate, date_fmt).date()
    end_date = datetime.strptime(endDate, date_fmt).date()
    periods = ((end_date - start_date).days + 1) * 24
    dt_index = pd.date_range(start_date, periods=periods, freq="H")

    temp_series = pd.Series(temperature, index=dt_index)
    mod = ExponentialSmoothing(
        temp_series, trend="add", damped=True, seasonal="add", seasonal_periods=24
    )
    results = mod.fit()

    return results.forecast(n * 24)


start_date = "2013-01-01"
end_date = "2013-01-02"
n = 1
temperature = [
    34.38,
    34.36,
    34.74,
    35.26,
    35.23,
    35.29,
    35.64,
    36.02,
    36.1,
    36.98,
    37.01,
    36.75,
    36.01,
    35.66,
    34.72,
    33.9,
    32.62,
    31.51,
    30.73,
    29.5,
    26.94,
    25.47,
    23.84,
    22.55,
    34.38,
    34.36,
    34.74,
    35.26,
    35.23,
    35.29,
    35.64,
    36.02,
    36.5,
    36.9,
    37.01,
    36.75,
    36.01,
    35.66,
    34.72,
    33.9,
    32.62,
    31.51,
    30.73,
    29.5,
    26.94,
    25.47,
    23.84,
    22.55,
]

print(predictTemperature(start_date, end_date, temperature, n))
