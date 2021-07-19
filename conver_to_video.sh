#!/bin/bash

ffmpeg -start_number 1 -i $1/%d.jpg -framerate 1/64 -c:v libx264 -r 30 -pix_fmt yuv420p output.mp4 

