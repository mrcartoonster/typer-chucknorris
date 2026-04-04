import sys

import typer

sys.path.append(
    "/Users/evanbaird/Projects/Projects/typer_chucknorris/src/typer_chucknorris",
)
from chucknorris import norris

app = typer.Typer(rich_markup_mode="rich", no_args_is_help=True)
app.add_typer(norris.app)


if __name__ == "__main__":
    app()
