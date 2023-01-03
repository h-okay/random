import itertools


def remove_every_other(num):
    answer = []
    for ind, value in enumerate(num):
        if ind == 0:
            answer.append(value)
        elif ind % 2 == 0:
            answer.append(value)
    return answer


def sum_pairs(lst, num):
    pairs = list(itertools.combinations(lst, 2))
    for tup in pairs:
        if sum(tup) == num:
            return list(tup)
        return []


def vowel_count(string):
    return {
        char: string.lower().count(char) for char in string.lower() if char in "aeiou"
    }


def titleize(string):
    return " ".join([val[0].upper() + val[1:] for val in string.split()])


def find_factors(num):
    return [i for i in range(1, num + 1) if num % i == 0]


def includes(give, search, search_from=0):

    if isinstance(give, list):
        for val in give[search_from:]:
            if val == search:
                return True

    if isinstance(give, dict):
        for val in give.values():
            if val == search:
                return True

    if isinstance(give, str):
        if search in give[search_from:]:
            return True

    return False


def repeat(num, times):
    return num * times


def truncate(num, most):
    if most < 3:
        return "Truncation must be at least 3 characters."
    if most > len(num) + 2:
        return num
    return num[: most - 3] + "..."


def two_list_dictionary(list1, list2):
    zipped = itertools.zip_longest(list1, list2)
    return {key: value for key, value in dict(zipped).items() if key is not None}
