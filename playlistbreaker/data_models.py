from dataclasses import dataclass
from enum import Enum


@dataclass
class Track:
    title: str
    start: int


class FileType(str, Enum):
    M4A = "m4a"
    WEBM = "webm"

    @property
    def stream_subtype(self):
        match self:
            case self.M4A:
                return "mp4"
            case self.WEBM:
                return "webm"

class TracklistFormat(str, Enum):
    HHMMSS_SPACE_TITLE = "hhmmss_space_title"
    HHMMSS_MINUS_TITLE = "hhmmss_minus_title"

    @property
    def regex(self):
        match self:
            case self.HHMMSS_SPACE_TITLE:
                return r"(?P<hrs>\d?\d)?:?(?P<mins>\d?\d):(?P<secs>\d\d) (?P<title>.+)"
            case self.HHMMSS_MINUS_TITLE:
                return r"(?P<hrs>\d?\d)?:?(?P<mins>\d?\d):(?P<secs>\d\d) - (?P<title>.+)"