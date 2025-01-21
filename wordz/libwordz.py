from collections import Counter
from typing import Iterable
import regex


TOKEN_PATTERN = regex.compile(r"(?u)\b\w\w+\b")


def compte_mots(texte: Iterable[str]) -> Counter[str]:
    res = Counter()
    for line in texte:
        res.update(TOKEN_PATTERN.findall(line))
    return res
