#!python

import subprocess
from math import ceil
import sys
import os

if not os.path.exists("/tmp/eww.stdin"):
    os.mkfifo("/tmp/eww.stdin")

def set_volume(amount:str):
    subprocess.check_call([
        "amixer",
        "-Mq",
        "set",
        "Master,0",
        amount,
        "unmute"
    ])

def get_volume():
    if not "on" in subprocess.check_output([
        "amixer",
        "get",
        "Master"
    ]).decode().strip().split("\n")[-1].split(" ")[-1]:
        return 0
    return int(subprocess.check_output([
        "amixer",
        "get",
        "Master"
    ]).decode().strip().split("\n")[-1].split(" ")[-2][1:-2])

def toggle():
    subprocess.check_call([
        "amixer",
        "-Mq",
        "set",
        "Master",
        "toggle"
    ])

def icon():
    path = "assets/"
    ext = ".svg"
    match ceil(get_volume()/34):
        case 0:
            return f"{path}muted{ext}"
        case 1:
            return f"{path}low{ext}"
        case 2:
            return f"{path}medium{ext}"
        case 3:
            return f"{path}high{ext}"


match sys.argv[-1]:
    case "icon":
        print(icon())
    case "increment":
        set_volume("1%+")
    case "decrement":
        set_volume("1%-")
    case "toggle":
        toggle()
    case "get":
        print(get_volume())

