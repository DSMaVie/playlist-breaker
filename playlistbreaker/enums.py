from enum import StrEnum, auto


class FileType(StrEnum):
    MP4 = auto()
    WEBM = auto()


class TracklistFormat(StrEnum):
    HHMMSS_TITLE = auto()

    def regex(self):
        match self:
            case self.HHMMSS_TITLE:
                return r"(?P<hrs>\d\d)?:?(?P<mins>\d\d):(?P<secs>\d\d) (?P<title>.+)"
