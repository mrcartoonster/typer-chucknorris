import sys
import secrets
from pathlib import Path
from typing import Annotated


import typer
from rich import print
import httpx
import tomli

sys.path.append('/Users/evanbaird/Projects/Projects/typer_chucknorris/src/typer_chucknorris')
from chucknorris.categories import chuck_completions


app = typer.Typer(rich_markup_mode='rich', no_args_is_help=True)

#TODO Put version snippet below in another file

home = Path('../../pyproject.toml')

with open(home, mode='br') as v:
    version = tomli.load(v)


def version_callback(value: bool):
    """
    Call back function for project version number
    """
    if value:
        # print(f"Awesome Chuck Norris CLI Version: [bold green]{version['project']['version']}[/]")
        print(f"Awesome Chuck Norris CLI Version: [bold green]{version['project']['version']}[/]")
        raise typer.Exit()

#TODO Everything above in another file.

@app.command(epilog="[bold]In tribute to [link=https://www.imdb.com/title/tt0090927/]Chuck Norris[/link][/] :fist:!")
def chuck(
    random: Annotated[bool, typer.Argument(help='Get random quote')] = True,
    categories: Annotated[bool, typer.Option('--categories', '-c', rich_help_panel='Options', help='Retrieve a list of available categories.')] = False,
    category_select: Annotated[
        str,
        typer.Option(
            '--category-select',
            '-cs',
            rich_help_panel='Options',
            help='Select category and retrieve a quote from the entered category',
            autocompletion=chuck_completions,
        )
    ] = "",
    search: Annotated[str, typer.Option('--search', '-s', rich_help_panel='Options', help='Free text search to find relavent joke')] = "",
    version: Annotated[bool | None, typer.Option("--version", "-v", rich_help_panel='Options', callback=version_callback, is_eager=True)] = None,
):
    """
    Get a random bad a$$ Chuck Norris quote from the CLI!!!
    """

    if categories:

        resp = httpx.get(url='https://api.chucknorris.io/jokes/categories')

        print("\nThe categories you can choose from are:\n")

        for _ in resp.json():
            print(_)

        print()

    elif category_select:

        resp = httpx.get(url='https://api.chucknorris.io/jokes/random', params={'category': category_select})

        chuck  = dict(resp.json())

        norris = chuck['value']

        print(f"[bold blue]{norris}[/]\n")

    elif search:

        resp = httpx.get(url='https://api.chucknorris.io/jokes/search', params={'query': search})

        chuck  = dict(resp.json())

        norris = chuck['result'][secrets.randbelow(chuck['total'])]['value']

        print(f"[bold green]{norris}[/]\n")

    else:

        resp = httpx.get(url='https://api.chucknorris.io/jokes/random')

        norris = dict(resp.json())

        print(f"[bold red]{norris['value']}[/]\n")


#TODO: We'll see if we can add this back...
#   @app.callback()
#   def callback():
#       """
#       [bold yellow]Chuck Norris Quote dispenser![/bold yellow]

#       Passing in the argument [code]chuck[/] to get a bad ass random Chuck Norris quote!

#       Passing the option [code]--categories[/] [bold]|[/] [code]-c[/] will list Category quote option to choose from.

#       Passing the option [code]--category-select[/] [bold]|[/] [code]-cs[/] and pass in the selected category you want the quote from.

#       Passing the option [code]--search[/] [bold]|[/] [code]-s[/] and passing a search time will output a bad ass quote relative to the search term.
#       """


if __name__ == "__main__":
    app()
