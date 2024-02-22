from typing import List, Union


def join_lists(lst_of_lst: List[List[str]], sep: str) -> Union[List[str], None]:
    if not lst_of_lst:
        return None
    complete_lst = []
    for lst in lst_of_lst:
        complete_lst.extend(lst)
        complete_lst.append(sep)
    del complete_lst[-1]
    return complete_lst
