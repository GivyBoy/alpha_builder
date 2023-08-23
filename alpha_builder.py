"""
Script to show how a builder design pattern works
"""

from abc import ABC, abstractmethod
from typing import Callable
import pandas as pd
import yfinance as yf


class IAlpha(ABC):
    """
    The builder interface that specifies the methods for creating an alpha
    """

    @abstractmethod
    def get_data(self) -> pd.DataFrame:
        """
        returns the data
        """
        raise NotImplementedError

    @abstractmethod
    def run(self) -> pd.DataFrame:
        """
        runs the strategy
        """
        raise NotImplementedError


class FormulaicAlphaBuilder(IAlpha):
    """
    Follows the Builder interface
    """
    def __init__(self, alpha_func: Callable[[pd.DataFrame], pd.DataFrame],
                 start_date: str, vol_target: float) -> None:
        super(IAlpha).__init__()
        self._alpha_func = alpha_func
        self.start_date = start_date
        self.vol_target = vol_target
        self.data = self.get_data()

    def run(self) -> pd.DataFrame:
        print("Getting this 4 sharpe alpha...")
        return self._alpha_func(self.data)

    def get_data(self) -> pd.DataFrame:
        return yf.download("^GSPC")["Adj Close"]
