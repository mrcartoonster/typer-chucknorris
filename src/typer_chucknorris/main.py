import typer
from rich import print
import httpx



app = typer.Typer()


@app.command()
def chuck():
    url = 'https://api.chucknorris.io/jokes/random'

    resp = httpx.get(url)

    norris = dict(resp.json())

    print(f"[blue bold]{norris['value']}[/ blue bold]")


if __name__ == "__main__":
    app()
