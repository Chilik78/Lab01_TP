# -*- coding: utf-8 -*-
import pytest
import json
from src.Types import DataType
from src.ReaderJSON import ReaderJSON
from src.ThirdQuartile import ThirdQuartile
from src.CalcRating import CalcRating


class TestTextDataReader:

    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
        json_data = {
            "Иванов Иван Иванович": {
                "математика": 67,
                "литература": 100,
                "программирование": 91
            },
            "Петров Петр Петрович": {
                "математика": 78,
                "химия": 87,
                "социология": 61
            },
            "Смирнов Сергей Игоревич": {
                "экономика": 61,
                "биология": 68,
                "программирование": 60,
                "обществознание": 90,
                "социология": 63
            },
            "Кузнецов Дмитрий Максимович": {
                "литература": 70,
                "физика": 90,
                "философия": 94
            }
        }
        data = [84.66666666666667, ["Кузнецов Дмитрий Максимович"]]
        return json_data, data

    @pytest.fixture()
    def filepath_and_data(
        self, file_and_data_content: tuple[str, DataType], tmpdir
    ) -> tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("my_data.json")
        p.write_text(json.dumps(file_and_data_content[0]), encoding='utf-8')
        return str(p), file_and_data_content[1]

    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
        file_content = ReaderJSON().read(filepath_and_data[0])
        rating = CalcRating(file_content).calc()
        third_quartile = ThirdQuartile(rating)
        third_quartile_val = third_quartile.calc()
        students_in_third_quartile = third_quartile.find()
        assert third_quartile_val == filepath_and_data[1][0]
        assert students_in_third_quartile == filepath_and_data[1][1]
