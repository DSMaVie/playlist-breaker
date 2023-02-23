import logging
import os
from pathlib import Path

import typer
from rich.logging import RichHandler

from playlistbreaker.data_models import FileType, TracklistFormat
from playlistbreaker.download import download
from playlistbreaker.parser import parse_description
from playlistbreaker.splitter import split_audio

logging.basicConfig(level=logging.WARN, handlers=[RichHandler()])

app = typer.Typer()

@app.command()
def main(
    url: str, destination:Path, tracklist_format: TracklistFormat, filetype: FileType = FileType.M4A
):
    """Downloads the audio at the track and spits it according to its track_list in the description."""
    file_loc = download(url, filetype)
    tracks = parse_description(url, tracklist_format)
    split_audio(Path(file_loc), dst=destination, tracklist=tracks)
    os.remove(file_loc)


# if __name__ == "__main__":
#     typer.run(main)
