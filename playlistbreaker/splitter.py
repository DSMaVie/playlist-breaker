
import logging
from pathlib import Path

import librosa
import soundfile as sf

from playlistbreaker.data_models import Track
from playlistbreaker.util import title_to_filename

logger = logging.getLogger(__name__)

def split_audio(src:Path, dst:Path, tracklist:list[Track]):

    tracklist_shifted = tracklist[1:-2] +[None]

    for current_track, next_track in zip(tracklist, tracklist_shifted):
        logger.info(f"creating file for track {current_track.title}")

        offset = current_track.start
        if next_track is not None:
            duration = next_track.start - current_track.start
        else:
            duration = None

        data, sr = librosa.load(src,sr=None, offset=offset, duration=duration)
        sf.write(dst / f"{title_to_filename(current_track.title)}.wav", data, samplerate=sr, subtype="PCM_24")