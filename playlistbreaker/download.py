import logging
import tempfile

from pytube import Stream, YouTube
from rich.progress import Progress

from playlistbreaker.enums import FileType

logger = logging.getLogger(__name__)


def _update_progress(
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


def download(link: str, format: FileType = FileType.MP4):
    with Progress() as progress:
        task_id = progress.add_task(description="Downloading Audio:")

        yt = YouTube(
            link,
            on_progress_callback=lambda stream, chunk, rem_bytes: _update_progress(
                progress, task_id, stream, chunk, rem_bytes
            ),
        )
        stream = yt.streams.get_audio_only(subtype=format.value)
        logger.info(f"found stream {stream}")

        loc = tempfile.mkdtemp()
        stream.download(output_path=loc, filename=f"{yt.title}.{format.value}")
    return loc
