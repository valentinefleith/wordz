import click
from libwordz import compte_mots


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
