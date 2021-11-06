import json
from HW_2_part_1_task import Advert


def example_location_address():
    lesson_str = """{
            "title": "python",
            "price": 0,
            "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"]
                }
            }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    print(lesson_ad.location.address)


def example_price_is_not_negative():
    lesson_str = '{"title": "python", "price": -1}'
    lesson = json.loads(lesson_str)
    Advert(lesson)


def example_wo_price():
    lesson_str = '{"title": "python"}'
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    print(lesson_ad.price)


if __name__ == "__main__":
    example_location_address()
    example_price_is_not_negative()
    example_wo_price()

