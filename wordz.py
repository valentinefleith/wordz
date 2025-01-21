import sys
from collections import Counter
from typing import Iterable

def compte_mots(texte: Iterable[str]) -> Counter[str]:
    res = Counter()
    for line in texte:
        res.update(line.split())
    return res


def main():
    inpt = sys.argv[1]
    with open(inpt) as in_stream:
        count = compte_mots(in_stream)

    for w, count in count.most_common(16):
        print(f"{w}: {count}")



if __name__ == "__main__":
    main()
