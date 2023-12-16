import os
from pathlib import Path
import sys
from urllib.request import urlretrieve
from zipfile import ZipFile

import typer

TMP = Path(os.getenv("TMP", "/tmp"))
S3 = "https://bites-data.s3.us-east-2.amazonaws.com"


def _setup():
    data_zipfile = '357-data.zip'
    urlretrieve(f'{S3}/{data_zipfile}', TMP / data_zipfile)
    ZipFile(TMP / data_zipfile).extractall(TMP)
    sys.path.append(TMP)


_setup()

from algorithms import app as algo_app  # noqa E402
from comparisons import app as compare_app  # noqa E402


app = typer.Typer()


if __name__ == "__main__":
    app()