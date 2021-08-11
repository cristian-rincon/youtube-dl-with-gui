import PySimpleGUI as sg
from downloader import YoutubeDownloader


class YTDGUI(object):
    def __init__(self):
        self.layout = [
            [sg.Text("Enter the video that you want to download from youtube")],
            [sg.InputText()],
            [sg.Submit(), sg.Cancel()],
        ]
        self.theme = sg.theme("Default1")

    def main(self):
        window = sg.Window("Youtube Downloader", self.layout)

        event, values = window.read()
        window.close()

        text_input = values[0]
        yt_downloader = YoutubeDownloader(text_input)
        video_metadata = yt_downloader.download()
        if video_metadata.get("error"):
            sg.popup("Error: ", video_metadata.get("error"))
        sg.popup("File downloaded at: ", video_metadata.get("path"))



if __name__ == "__main__":
    YTDGUI().main()
