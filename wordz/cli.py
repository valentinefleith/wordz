import click
from wordz.libwordz import compte_mots


@click.command()
@click.argument("inpt")
@click.argument("word", required=False)
@click.option(
    "-n", type=int, default=16)
def main(inpt: str, word: str | None, n: int):

    with open(inpt) as in_stream:
        count = compte_mots(in_stream)

    if word is not None:
        print(f"{word}: {count[word]}")
    else:
        for w, count in count.most_common(n):
            print(f"{w}: {count}")


if __name__ == "__main__":
    main()
