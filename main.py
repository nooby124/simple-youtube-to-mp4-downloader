from pytube import YouTube
import time
from moviepy.editor import *
def download():
	link = input("gib link (type 'mp3' to convert mp4 to mp3 and type 'm2' to use method 2): ")
	if link == "m2":
		print("this is method 2 btw")
		video = input("give link for method 2: ")
		video2= YouTube(
			video,
			use_oauth=True,
			allow_oauth_cache=True)
		video2.streams.all()
		again()
		exit()
	if link == "mp3":
		print("converting a video to mp3")
		vidpath = input("video path: ")
		vidpath.replace('\\', '/')
		vidpath.replace('"', '')
		audpath = input("audio path: ")
		def MP4ToMP3(mp4, mp3):
			FILETOCONVERT = AudioFileClip(mp4)
			FILETOCONVERT.write_audiofile(mp3)
			FILETOCONVERT.close()
		VIDEO_FILE_PATH = vidpath
		AUDIO_FILE_PATH = audpath

		MP4ToMP3(VIDEO_FILE_PATH, AUDIO_FILE_PATH)
		again()	
		exit()
	yt = YouTube(link)
	vid = yt.streams.get_highest_resolution()
	vid.download()
	print("done")
	again()
def again():
	agaain = input("do you want to download again (y/n)?: ")
	if agaain == "y":
		download()
	if agaain == "n":
		print("ok")
		exit()
	else:
		print("you can only type y (yes) or n (no)!")
		again()
download()
