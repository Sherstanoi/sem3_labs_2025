from unittest import result

from RK2 import *
import pytest

stroki = [
    Stroki(1, "бла-бла", 7, 1),
    Stroki(2, "барбер", 6, 2),
    Stroki(3, "ода", 3, 3),
    Stroki(4, "гильгамеш", 9, 3)
]

tables = [
    Table(1, "текст"),
    Table(2, "мало текста"),
    Table(3, "много текста")
]

table_stroki = [
    TableStroka(1, 1, 1),
    TableStroka(2, 2, 2),
    TableStroka(3, 3, 3),
    TableStroka(4, 4, 3),
    TableStroka(5, 3, 2),
]

def testRequestOne():
    result = RequestOne(stroki, tables)

    expected = [{'StringId': 1,'StringContent': "бла-бла", 'TableName': "текст", 'TableId': 1},
                {'StringId': 2,'StringContent': "барбер", 'TableName': "мало текста", 'TableId': 2}]

    assert result == expected, f"Ожидали {expected}, получили {result}"

def testRequestTwo():
    result = RequestTwo(stroki, tables)
    expected = [
        ("много текста", 3),
        ("мало текста", 6),
        ("текст", 7)
    ]

    assert result == expected, f"Ожидали {expected}, получили {result}"

def testRequestThree():
    result = RequestThree(stroki, tables, table_stroki)

    expected = [
        {'StringId': 1, 'StringContent': 'бла-бла',    'TableName': 'текст',       'TableId': 1},
        {'StringId': 2, 'StringContent': 'барбер',     'TableName': 'мало текста', 'TableId': 2},
        {'StringId': 3, 'StringContent': 'ода',        'TableName': 'много текста','TableId': 3},
        {'StringId': 3, 'StringContent': 'ода',        'TableName': 'мало текста', 'TableId': 2},
        {'StringId': 4, 'StringContent': 'гильгамеш',  'TableName': 'много текста','TableId': 3},
    ]

    assert result == expected, f"Ожидали {expected}, получили {result}"