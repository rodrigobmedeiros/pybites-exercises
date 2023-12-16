import typer


def sum_numbers(a: int, b: int):
    return a + b


def main(
    a: int = typer.Argument(..., help="The value of the first summand"),
    b: int = typer.Argument(..., help="The value of the second summand"),
):
    """CLI that allows you to add two numbers"""

    print(sum_numbers(a, b))


if __name__ == "__main__":
    typer.run(main)