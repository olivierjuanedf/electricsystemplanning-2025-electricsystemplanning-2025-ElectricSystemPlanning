from dataclasses import dataclass
from datetime import datetime
from typing import List, Union

import numpy as np

from common.constants.temporal import Timescale
from utils.dates import get_n_days_in_period, get_n_weeks_in_period, get_n_months_in_period, get_n_days_in_month


@dataclass
class Timeseries:
    timescale: str
    value: Union[float, np.ndarray]

    def check(self, allowed_timescales: List[str], period_start: datetime, period_end: datetime):
        # that timescale be in the list of allowed ones
        if self.timescale not in allowed_timescales:
            raise Exception(f'Timeseries with non-allowed timescale {self.timescale}; '
                            f'it must be in {allowed_timescales}')

        # if array value, check its size
        if isinstance(self.value, np.ndarray):
            timescale_to_func = {
                Timescale.day: get_n_days_in_period,
                Timescale.week: get_n_weeks_in_period,
                Timescale.month: get_n_months_in_period,
            }
            n_ts_in_period = timescale_to_func.get(self.timescale)(start=period_start, end=period_end)
            len_value = len(self.value)
            if not len_value == n_ts_in_period:
                raise Exception(f'Timesrie value has length {len_value}, but must be {n_ts_in_period} to be coherent '
                                f'with start {period_start: %Y/%m/%d}, end {period_end: %Y/%m/%d} and timescale '
                                f'{self.timescale}')

    def weigh_values(self, period_start: datetime, period_end: datetime):
        """
        Apply weight to first and last element in value, to account for possibly uncomplete timescale
        """
        if self.timescale == Timescale.day:
            start_hour = period_start.hour
            if start_hour > 0:
                first_weight = (24 - start_hour) / 24
            else:
                first_weight = 1
            end_hour = period_end.hour
            if len(self.value) > 1 and end_hour < 23:
                last_weight = (end_hour + 1) / 24
            else:
                last_weight = 1
        elif self.timescale == Timescale.week:
            start_isoweekday = period_start.isoweekday()  # assumption that hour is always 0
            if not start_isoweekday == 1:  # not a Monday
                first_weight = (8 - start_isoweekday) / 7
            else:
                first_weight = 1
            end_isoweekday = period_end.isoweekday()
            if len(self.value) > 1 and end_isoweekday < 7:
                last_weight = end_isoweekday / 7
            else:
                last_weight = 1
        elif self.timescale == Timescale.month:
            start_day = period_start.day
            if not start_day == 1:
                n_days_in_month_start = get_n_days_in_month(year=period_start.year, month=period_start.month)
                first_weight = (n_days_in_month_start - start_day + 1) / n_days_in_month_start
            else:
                first_weight = 1
            end_day = period_end.day
            n_days_in_month_end = get_n_days_in_month(year=period_end.year, month=period_end.month)
            if not end_day == n_days_in_month_end:
                last_weight = end_day / n_days_in_month_end
            else:
                last_weight = 1
        # apply obtained weights for first and last time-slots
        self.value[0] *= first_weight
        self.value[-1] *= last_weight
