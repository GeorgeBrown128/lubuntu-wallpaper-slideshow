#!/usr/bin/python3

# Setup
# Wallpaper Path
wallpapers = "/home/user/Pictures/Wallpapers"

from time import sleep
import random
import subprocess
import os

while(True):
    paper = random.choice(os.listdir(wallpapers))
    print(paper)
    print(str("-w " + os.path.join(wallpapers, paper)))
    subprocess.call(["pcmanfm", "-w", os.path.join(wallpapers, paper)])
    sleep(10)
