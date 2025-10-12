# -*- coding: utf-8 -*-
import argparse
import sys

from src.CalcRating import CalcRating
from src.TextDataReader import TextDataReader
from src.ReaderJSON import ReaderJSON
from src.ThirdQuartile import ThirdQuartile

def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True, help="Path to datafile")
    args = parser.parse_args(args)
    return args.path

def main():
    path = get_path_from_arguments(sys.argv[1:])
    reader = ReaderJSON()
    students = reader.read(path)
    print("Students: ", students)
    rating = CalcRating(students).calc()
    third_quartile = ThirdQuartile(rating)
    third_quartile_val = third_quartile.calc()
    print("Third quartile value: ", third_quartile_val)
    students_in_third_quartile = third_quartile.find()
    print("Students in third quartile: ", ", ".join(students_in_third_quartile))
    print("Rating: ", rating)

if __name__ == "__main__":
    main()
