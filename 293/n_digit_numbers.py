from typing import List, TypeVar

T = TypeVar("T", int, float)


from typing import List, TypeVar

T = TypeVar("T", int, float)


def n_digit_numbers(numbers: List[T], n: int) -> List[int]:

    if n < 1:
        raise ValueError("n < 1 is not accepted!")
    mult = 10 ** (n - 1)
    result = []
    for num in numbers:
        is_negative = num < 0 or 0
        modif_num = int(str(int(num * mult))[: n + is_negative])
        result.append(modif_num)
    return result
