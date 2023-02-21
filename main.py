import logging
from pathlib import Path

import typer
from rich.logging import RichHandler

from playlistbreaker.download import download
from playlistbreaker.enums import FileType, TracklistFormat
from playlistbreaker.parser import parse_description

logging.basicConfig(level=logging.DEBUG, handlers=[RichHandler()])


def main(
    link: str, tracklist_format: TracklistFormat, filetype: FileType = FileType.MP4
):
    """Downloads the audio at the track and spits it according to its track_list in the description."""
    file_loc = download(link, filetype)
    tracks = parse_description(link, tracklist_format)


if __name__ == "__main__":
    typer.run(main)
