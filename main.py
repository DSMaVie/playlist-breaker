import logging
from pathlib import Path

import typer
from rich.logging import RichHandler

from playlistbreaker.download import download

logging.basicConfig(level=logging.DEBUG, handlers=[RichHandler()])


def main(link: str, location: Path):  # TODO: enum filetype
    """Downloads the audio at the track and spits it according to its track_list in the description."""
    download(link, location)


if __name__ == "__main__":
    typer.run(main)
