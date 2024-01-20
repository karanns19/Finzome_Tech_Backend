
import pandas as pd
import numpy as np
from typing import List


def calculate_volatility(data: pd.DataFrame) -> float:
    data.columns = data.columns.str.strip()
    data['Daily Returns'] = data['Close'].pct_change()
    daily_volatility = np.std(data['Daily Returns'])
    annualized_volatility = daily_volatility * np.sqrt(len(data))
    return daily_volatility, annualized_volatility

if __name__ == "__main__":
    data = pd.read_csv('NIFTY50.csv')
    daily_volatility, annualized_volatility = calculate_volatility(data)
    print("Daily Volatility:", daily_volatility)
    print("Annualized Volatility:", annualized_volatility)
