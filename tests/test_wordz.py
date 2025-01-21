import wordz


def test_compte_mots():
    word_count = wordz.compte_mots(
        [
            "Je vous accorde qu'elle n'est pas étourdissante; mais je vous assure qu'elle est agréable quand on cause seul avec elle."
        ]
    )
    assert word_count["elle"] == 3
    assert word_count["accorde"] == 1
    assert word_count["est"] == 2
