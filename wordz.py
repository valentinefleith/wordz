from collections import Counter
from typing import Iterable
import regex
import click

TOKEN_PATTERN = regex.compile(r"(?u)\b\w\w+\b")


def compte_mots(texte: Iterable[str]) -> Counter[str]:
    res = Counter()
    for line in texte:
        res.update(TOKEN_PATTERN.findall(line))
    return res


@click.command()
@click.argument("inpt")
@click.argument("word", required=False)
def main(inpt: str, word: str | None):

    with open(inpt) as in_stream:
        count = compte_mots(in_stream)

    if word is not None:
        print(f"{word}: {count[word]}")
    else:
        for w, count in count.most_common(16):
            print(f"{w}: {count}")


if __name__ == "__main__":
    main()
