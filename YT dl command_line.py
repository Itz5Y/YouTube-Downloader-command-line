from pytube import YouTube
from pytube import Playlist
import os
from moviepy.editor import VideoFileClip


def download_video(url):
    yt = YouTube(url, on_progress_callback=progress)
    stream = yt.streams.get_highest_resolution()
    print("=========\nTitle:        " + yt.title + "\nResolution:   " + stream.resolution + "\n=========")
    stream.download('YT downloads')
    input('\nThe video is saved in ' + os.getcwd() + '\YT downloads')


def download_video(url):
    yt = YouTube(url, on_progress_callback=progress)
    try:
        stream = yt.streams.filter(res="720p").first()
    except:
        try:
            yt.streams.filter(res="360p").first()
        except:
            yt.streams.filter(res="240p").first()
    print("=========\nTitle:        " + yt.title + "\nResolution:   " + stream.resolution + "\n=========")
    stream.download('YT downloads')
    print('\nThe video is saved in ' + os.getcwd() + '\YT downloads')


def progress(stream, chunk, remains):  # 'chunk' must exist
    total = stream.filesize
    percent = (total - remains) / total * 100
    # print('Downloading… {:05.2f}%'.format(percent), end='\r')
    print('Download progress = [' + '▉' * int(percent / 5),
          ' ' * (20 - int(percent / 5)) + '] ' + '{:05.2f}%'.format(percent), end='\r')


def download_playlist(url):
    p = Playlist(url)
    print('Playlist url = ' + str(p))
    for urls in p.video_urls:
        print('\nDownloading ' + urls)
        download_video(urls)


def check_playlist(url):
    if 'playlist?list=' in str(url):
        download_playlist(url)
    else:
        download_video(url)


def download_audio(url):
    yt = YouTube(url, on_progress_callback=progress)
    try:
        stream = yt.streams.filter(mime_type='audio/mp4').first()
    except:
        yt.streams.filter(mime_type='audio/webm').first()

    print("=========\nTitle:        " + yt.title + "\nResolution:   " + stream.resolution + "\n=========")
    stream.download('YT downloads')
    print('\nThe video is saved in ' + os.getcwd() + '\YT downloads')


def convert_to_mp3(filename):
    filename = filename + '.mp4'
    audiofile = VideoFileClip(filename)
    audiofile.audio.write_audiofile(filename[:-4] + ".mp3")
    audiofile.close()


print(
    '''What do you want?
1) Download a YouTube video/playlist
2) Download the audio file of a YouTube video
3) Convert mp4 to mp3

I am not responsible for your downloads
Copyright (c) Itz5Y 2021
''')

choice = input('\n>Enter action\n')
while True:
    if choice == '1':
        url = input('>Enter URL\n')
        while True:
            try:
                check_playlist(url)
                break
            except:
                url = input('\n>Invalid, please enter URL again\n')
    elif choice == '2':
        url = input('>Enter URL\n')
        while True:
            try:
                download_audio(url)
                break
            except:
                url = input('\n>Invalid, please enter URL again\n')
    elif choice == '3':
        filename = input('\n>Enter the filename(without .mp4)\n')
        while True:
            try:
                convert_to_mp3(filename)
                break
            except:
                filename = input('\n>Invalid, please enter filename again\n')
    else:
        choice = input('\n>Please enter action again\n')
