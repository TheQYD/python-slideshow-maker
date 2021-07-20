#!/usr/bin/env python3

import ffmpeg

PATH = "test/"
strea = ffmpeg.input(PATH + "A.png")

audio = strea.audio.filter("aecho", 0.8, 0.9, 1000, 0.3)
video = strea.video.hflip()
out = ffmpeg.output(audio, video, 'A.mp4', pix_fmt='yuv420p')

print(out.__dict__)
