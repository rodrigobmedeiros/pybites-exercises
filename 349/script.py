import os
from pathlib import Path
from typing import List
import unicodedata
from urllib.request import urlretrieve


def _get_spanish_dictionary_words() -> List[str]:
    filename = "spanish.txt"
    # source of file
    # https://raw.githubusercontent.com/bitcoin/bips
    # /master/bip-0039/spanish.txt
    url = f"https://bites-data.s3.us-east-2.amazonaws.com/{filename}"
    tmp_folder = os.getenv("TMP", "/tmp")
    local_filepath = Path(tmp_folder) / filename
    if not Path(local_filepath).exists():
        urlretrieve(url, local_filepath)
    return local_filepath.read_text().splitlines()


SPANISH_WORDS = _get_spanish_dictionary_words()


def get_accentuated_sentence(
    text: str, words: List[str] = SPANISH_WORDS
) -> str:
    pass