import logging
import tempfile
from pathlib import Path

from pytube import Stream, YouTube
from rich.progress import Progress

from playlistbreaker.data_models import FileType
from playlistbreaker.util import title_to_filename

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


def download(link: str, format: FileType = FileType.M4A):
    with Progress() as progress:
        task_id = progress.add_task(description="Downloading Audio:")

        yt = YouTube(
            link,
            on_progress_callback=lambda stream, chunk, rem_bytes: _update_progress(
                progress, task_id, stream, chunk, rem_bytes
            ),
        )
        stream = yt.streams.get_audio_only(subtype=format.stream_subtype)
        logger.info(f"found stream {stream}")

        fpath = Path.cwd() / f"{title_to_filename(yt.title)}.{format.value}"
        stream.download(output_path=fpath.parent, filename=fpath.name)
        return fpath
