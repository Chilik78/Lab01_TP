# -*- coding: utf-8 -*-
import json
from src.DataReader import DataReader
from src.Types import DataType


class ReaderJSON(DataReader):
    """
    Класс для чтения данных о студентах и их оценках из JSON файла
    """

    def read(self, path: str) -> DataType:
        """
        Читает данные из JSON файла и возвращает в формате DataType

        Args:
            path (str): Путь к JSON файлу

        Returns:
            DataType: Словарь с данными о студентах и их оценках

        Raises:
            FileNotFoundError: Если файл не найден
            json.JSONDecodeError: Если файл содержит некорректный JSON
        """
        try:
            with open(path, 'r', encoding='utf-8') as file:
                data = json.load(file)

            result: DataType = {}

            for student, subjects in data.items():
                subjects_list = [
                    (subject, int(grade)) for subject, grade
                    in subjects.items()
                ]
                result[student] = subjects_list

            return result

        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {path} не найден")
        except json.JSONDecodeError as e:
            error_msg = f"Ошибка декодирования JSON в файле {path}: {e}"
            raise json.JSONDecodeError(error_msg)
        except ValueError as e:
            raise ValueError(f"Ошибка преобразования оценок в числа: {e}")
