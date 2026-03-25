from typing import Annotated
import typer
from rich import print
import httpx



app = typer.Typer()


@app.command()
def chuck(
    random: Annotated[bool, typer.Argument(help='Get random quote')] = True,
    categories: Annotated[bool, typer.Option(help='Retrieve a list of available categories.')] = False,
    category_select: Annotated[str, typer.Option(help='Select category and retrieve a quote from the entered category')] = "",
):
    """
    Get a random bad a$$ Chuck Norris quote from the CLI!!!
    """

    if categories:
        url = 'https://api.chucknorris.io/jokes/categories'

        resp = httpx.get(url)

        print("\n[bold blue]The categories you can choose from are:[/]\n")

        for _ in resp.json():
            print(_)

        print()

    elif category_select:
        url = 'https://api.chucknorris.io/jokes/random/'

        resp = httpx.get(url, params={'category': category_select})

        norris = dict(resp.json())

        print(f"[green bold]{norris['value']}[/ green bold]")

    elif random:
        url = 'https://api.chucknorris.io/jokes/random'

        resp = httpx.get(url)

        norris = dict(resp.json())

        print(f"[blue bold]{norris['value']}[/ blue bold]")


if __name__ == "__main__":
    app()
