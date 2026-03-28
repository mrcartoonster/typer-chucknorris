import secrets
from typing import Annotated
import typer
from rich import print
import httpx
import tomli
from pathlib import Path



app = typer.Typer()

#TODO Put version snippet below in another file

home = Path('../../pyproject.toml')

with open(home, mode='br') as v:
    version = tomli.load(v)

def version_callback(value: bool):
    """
    Call back function for project version number
    """
    if value:
        print(f"Awesome Chuck Norris CLI Version: {version['project']['version']}")
        raise typer.Exit()

#TODO Everything above in another file.

@app.command()
def chuck(
    random: Annotated[bool, typer.Argument(help='Get random quote')] = True,
    categories: Annotated[bool, typer.Option('--categories', '-c', help='Retrieve a list of available categories.')] = False,
    category_select: Annotated[str, typer.Option('--category-select', '-cs', help='Select category and retrieve a quote from the entered category')] = "",
    search: Annotated[str, typer.Option('--search', '-s', help='Free text search to find relavent joke')] = "",
    version: Annotated[bool | None, typer.Option("--version", "-v", callback=version_callback, is_eager=True)] = None,
):
    """
    Get a random bad a$$ Chuck Norris quote from the CLI!!!
    """

    if categories:

        resp = httpx.get(url='https://api.chucknorris.io/jokes/categories')

        print("\n[bold blue]The categories you can choose from are:[/]\n")

        for _ in resp.json():
            print(_)

        print()

    elif category_select:

        resp = httpx.get(url='https://api.chucknorris.io/jokes/random', params={'category': category_select})

        chuck  = dict(resp.json())

        norris = chuck['value']

        print(f"[green bold]{norris}[/ green bold]\n")

    elif search:

        resp = httpx.get(url='https://api.chucknorris.io/jokes/search', params={'query': search})

        chuck  = dict(resp.json())

        norris = chuck['result'][secrets.randbelow(chuck['total'])]['value']

        print(f"[blue bold]{norris}[/ blue bold]\n")

    else:

        resp = httpx.get(url='https://api.chucknorris.io/jokes/random')

        norris = dict(resp.json())

        print(f"[blue bold]{norris['value']}[/ blue bold]\n")


if __name__ == "__main__":
    app()
