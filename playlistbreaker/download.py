import logging
from pathlib import Path

from pytube import Stream, YouTube
from rich.progress import Progress

logger = logging.getLogger(__name__)


def update_progress(
    progress: Progress,
    task_id: str,
    stream: Stream,
    data_chunk: bytes,
    remaining_bytes: int,
):
    logger.debug(
        f"receiving data. remaining bytes are {remaining_bytes} of {stream.filesize}"
    )
    progress.update(
        task_id=task_id,
        advance=stream.filesize - remaining_bytes,
        total=stream.filesize,
    )


def download(link: str, loc: Path):
    loc = loc.resolve()

    with Progress() as progress:
        task_id = progress.add_task(description="Downloading Audio:")

        yt = YouTube(
            link,
            on_progress_callback=lambda stream, chunk, rem_bytes: update_progress(
                progress, task_id, stream, chunk, rem_bytes
            ),
        )
        stream = yt.streams.get_audio_only()
        logger.info(f"found stream {stream}")

        stream.download(output_path=str(loc.parent), filename=str(loc.name))
    
