from subprocess import check_output, check_call
from math import floor
from time import time, sleep
from json import loads,dumps
import tools
import sys


def get():
    output = check_output(["upower", "-i", "/org/freedesktop/UPower/devices/battery_BAT0"]).decode()
    percentage = [line.split(":")[1].strip().split("%")[0] for line in output.split("\n") if "percentage" in line][0]
    return percentage

def color(): 
    percentage = get()
    color = tools.color(int(percentage))
    return color


def icon():
    value = get()
    chars = [chr(0xf240), chr(0xf241), chr(0xf242), chr(0xf243), chr(0xf244)]
    chars.reverse()

    return chars[floor(int(value) / (len(chars)+16))]


if __name__ == "__main__":
    match sys.argv[-1]:
        case "color":
            print(color())
        case "get":
            print(get())
        case "icon":
            print(icon())
