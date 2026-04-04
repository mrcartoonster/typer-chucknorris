import httpx
from rich import print


def norris_quote():
    """
    Quick function https://api.chucknorris.io/jokes/random
    of Chuck Norris funny quotes.
    """

    url = "https://api.chucknorris.io/jokes/random"

    resp = httpx.get(url)

    norris = dict(resp.json())

    print(f"[blue bold]{norris['value']}[/ blue bold]")
