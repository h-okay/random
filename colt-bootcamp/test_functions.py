from functions import (
    find_factors,
    includes,
    remove_every_other,
    repeat,
    sum_pairs,
    titleize,
    truncate,
    two_list_dictionary,
    vowel_count,
)


def test_remove_every_other():
    assert remove_every_other([1, 2, 3, 4, 5]) == [1, 3, 5]
    assert remove_every_other([5, 1, 2, 4, 1]) == [5, 2, 1]
    assert remove_every_other([1]) == [1]


def test_sum_pairs():
    assert sum_pairs([4, 2, 10, 5, 1], 6) == [4, 2]
    assert not sum_pairs([11, 20, 4, 2, 1, 5], 100)


def test_vowel_count():
    assert vowel_count("awesome") == {"a": 1, "e": 2, "o": 1}
    assert vowel_count("Elie") == {"e": 2, "i": 1}
    assert vowel_count("Colt") == {"o": 1}


def test_titleize():
    assert titleize("this is awesome") == "This Is Awesome"
    assert titleize("oNLy cAPITALIZe fIRSt") == "ONLy CAPITALIZe FIRSt"


def test_find_factors():
    assert find_factors(10) == [1, 2, 5, 10]
    assert find_factors(11) == [1, 11]
    assert find_factors(111) == [1, 3, 37, 111]
    assert find_factors(321421) == [1, 293, 1097, 321421]
    assert find_factors(412146) == [
        1,
        2,
        3,
        6,
        7,
        9,
        14,
        18,
        21,
        42,
        63,
        126,
        3271,
        6542,
        9813,
        19626,
        22897,
        29439,
        45794,
        58878,
        68691,
        137382,
        206073,
        412146,
    ]


def test_includes():
    assert includes([1, 2, 3], 1) is True
    assert includes([1, 2, 3], 1, 2) is False
    assert includes({"a": 1, "b": 2}, 1) is True
    assert includes({"a": 1, "b": 2}, "a") is False
    assert includes("abcd", "b") is True
    assert includes("abcd", "e") is False


def test_repeat():
    assert repeat("*", 3) == "***"
    assert repeat("abc", 2) == "abcabc"
    assert repeat("abc", 0) == ""


def test_truncate():
    assert truncate("Super cool", 2) == "Truncation must be at least 3 characters."
    assert truncate("Super cool", 1) == "Truncation must be at least 3 characters."
    assert truncate("Super cool", 0) == "Truncation must be at least 3 characters."
    assert truncate("Hello World", 6) == "Hel..."
    assert truncate("Problem solving is the best!", 10) == "Problem..."
    assert truncate("Another test", 12) == "Another t..."
    assert truncate("Woah", 4) == "W..."
    assert truncate("Woah", 3) == "..."
    assert truncate("Yo", 100) == "Yo"
    assert truncate("Holy guacamole!", 152) == "Holy guacamole!"


def test_two_list_dictionary():
    assert two_list_dictionary(["a", "b", "c", "d"], [1, 2, 3]) == {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": None,
    }
    assert two_list_dictionary(["a", "b", "c"], [1, 2, 3, 4]) == {
        "a": 1,
        "b": 2,
        "c": 3,
    }
    assert two_list_dictionary(["x", "y", "z"], [1, 2]) == {"x": 1, "y": 2, "z": None}
