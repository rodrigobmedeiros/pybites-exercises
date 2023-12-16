import typer


def sum_numbers(a: int, b: int):
    return a + b


app = typer.Typer()
state = {}  # TODO: edit this


@app.command()
def sum(
    a: int = typer.Argument(..., help="The value of the first summand"),
    b: int = typer.Argument(..., help="The value of the second summand"),
):
    """Command that allows you to add two numbers."""
    sum_ab = sum_numbers(a, b)

    # TODO: add an if-else to write verbose output as a function of the callback setting
    print(f"The sum is {sum_ab}")


@app.command()
def compare(
    c: int = typer.Argument(..., help="First number to compare against."),
    d: int = typer.Argument(
        ..., help="Second number that is compared against first number."
    ),
):
    """Command that checks whether a number d is greater than a number c."""

    STRING_TRUE = "greater"
    STRING_FALSE = "not greater"

    d_greater_c = d > c

    c_evaluation = STRING_TRUE if d_greater_c else STRING_FALSE

    # TODO: add an if-else to write verbose output as a function of the callback setting
    print(f"{d=} is {c_evaluation} than {c=}")


# TODO: decorate this
def main(
    verbose,  # TODO: edit this
):
    """
    Have sum fun with numbers.
    """
    # TODO: inform user and set state according to user input about verbosity


if __name__ == "__main__":
    app()