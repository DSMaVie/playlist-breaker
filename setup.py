from importlib.metadata import entry_points

from setuptools import find_packages, setup

setup(
    name="PlaylistBreaker",
    version="0.2.0",
    description="Python Package to break up long YT audios into chunks according to given tracklist.",
    author="Max Vieweg",
    author_email="max.vieweg@outlook.com",
    url="https://github.com/DSMaVie/playlist-breaker",
    packages=find_packages(),
    entry_points={
        "console_scripts" : ["break-up-playlist=playlistbreaker.main:app"]
    }
)
