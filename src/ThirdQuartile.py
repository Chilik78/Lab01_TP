# -*- coding: utf-8 -*-
from src.Types import RatingType


class ThirdQuartile:

    def __init__(self, rating: RatingType) -> None:
        self.rating: RatingType = rating

    def calc(self) -> RatingType:

        raiting_values = []

        for key, val in self.rating.items():
            raiting_values.append(val)

        raiting_values = list(sorted(raiting_values))

        count_values = len(raiting_values)
        position_second_quartile = 0.5 * count_values
        position_third_quartile = 0.75 * count_values

        position_second_quartile = int(position_second_quartile)
        position_third_quartile = int(position_third_quartile) - 1
        self.third_quartile_values = raiting_values[position_second_quartile:position_third_quartile+1]

        return self.third_quartile_values

    def find(self):
        result = []

        for key, val in self.rating.items():
            if val in self.third_quartile_values:
                result.append(key)

        return result
