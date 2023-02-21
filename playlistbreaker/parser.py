import logging
import re

from pytube import YouTube

from playlistbreaker.enums import TracklistFormat

logger = logging.getLogger(__name__)

def parse_description(link: str, tracklist_format: TracklistFormat):
    desc = YouTube(link).description
    tracks = []

    for line in (line_wise_desc:=desc.split("\n")):
        match = re.match(tracklist_format.regex(), line)
        if match:
            track_info = match.groupdict()
            track_info = {k: v for k, v in track_info.items() if v is not None}

            logger.info(f"found {track_info} in tracklist in description.")
            tracks.append(
                {
                    "seconds": int(track_info.get("secs", 0))
                    + 60 * int(track_info.get("mins", 0))
                    + 60 * 60 * int(track_info.get("hrs", 0)),
                    "title": track_info["title"],
                }
            )
    if not len(line_wise_desc):
        logger.warning(f"Did not found any tracks with the format {tracklist_format.value} in the description.")
    return tracks


if __name__ == "__main__":
    print(
        parse_description(
            "https://www.youtube.com/watch?v=ROcups0YaHE", TracklistFormat.hhmmss_title
        )
    )
