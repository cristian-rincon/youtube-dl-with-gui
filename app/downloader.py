from typing import Dict
from pytube import YouTube
from settings import Config


class YoutubeDownloader:
    def __init__(self, url: str) -> None:
        self.url = url

    def download(self) -> Dict[str, str]:
        try:
            yt = YouTube(self.url)
            yt_name = yt.title
            output_path = Config.DOWNLOADS_PATH.value
            print(output_path)
            yt_stream = (
                yt.streams.filter(progressive=True, file_extension="mp4")
                .order_by("resolution")
                .desc()
                .first()
            )
            yt_stream.download(output_path=output_path)
            metadata = {
                "name": yt_name,
                "url": self.url,
                "path": output_path,
            }

        except Exception as e:
            metadata = {
                "error": e,
            }

        return metadata
