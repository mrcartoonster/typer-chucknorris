chuck_list = [
    ("animal", "Chuck Norris and animals"),
    ("career", "Chuck Norris and careers"),
    ("celebrity", "Chuck Norris and other lesser celebrities"),
    ("dev", "Chuck Norris and computer stuff"),
    ("explicit", "Chuck Norris and explicit sh*t"),
    ("fashion", "Chuck Norris and girl crap"),
    ("food", "Chuck Norris and chow"),
    ("history", "Chuck Norris making history"),
    ("money", "Chuck Norris and money money"),
    ("movie", "Chuck Norris movies and films"),
    ("music", "Chuck Norris and tunes"),
    ("political", "Chuck Norris and politics"),
    ("religion", "Chuck Norris and being worshipped"),
    ("science", "Chuck Norris and science"),
    ("sport", "Chuck Norris and Male sports"),
    ("travel", "Chuck Norris traveling to your mom"),
]


def chuck_completions(incomplete: str):
    for name, help_text in chuck_list:
        if name.startswith(incomplete):
            yield (name, help_text)
