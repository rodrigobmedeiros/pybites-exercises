from typing import List  # not needed when we upgrade to 3.9


def print_names_to_columns(names: List[str], cols: int = 2) -> None:

    counter = 0
    for name in names:
        name_with_pipe = "| " + name.ljust(10)
        if counter < cols - 1:
            print(name_with_pipe, end="")
            counter += 1
        else:
            print(name_with_pipe)
            counter = 0
