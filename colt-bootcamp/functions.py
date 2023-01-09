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


def range_in_list(lst, start=0, end=None):
    end = end if end else len(lst)
    return sum(lst[start : end + 1])


def same_frequency(num1, num2):
    num1 = [str(num1).count(val) for val in str(num1)]
    num2 = [str(num2).count(val) for val in str(num2)]

    if num1 == num2:
        return True
    return False


def nth(lst, ind):
    return lst[ind]


def find_the_duplicate(arr):
    arr.sort()
    for ind, val in enumerate(arr):
        if val in arr[ind + 1 :]:
            return val
    return None


def sum_up_diagonals(arr):
    pointer1, pointer2 = 0, len(arr) - 1
    ind = 0
    total = 0
    for _ in range(len(arr)):
        total += arr[ind][ind] + arr[pointer1][pointer2]
        ind += 1
        pointer1 += 1
        pointer2 -= 1
    return total


def min_max_key_in_dictionary(dct):
    return [min(list(dct.keys())), max(list(dct.keys()))]


def find_greater_numbers(arr):
    count = 0
    i = 0
    j = 1
    while i < len(arr):
        while j < len(arr):
            if arr[j] > arr[i]:
                count += 1
            j += 1
        j = i + 1
        i += 1
    return count


def multiple_letter_count(string):
    return {letter: string.count(letter) for letter in string}
