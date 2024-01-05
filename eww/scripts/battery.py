from subprocess import check_output, check_call
from math import floor
from time import time
from json import loads,dumps
import tools

def run():
    chars = [chr(0xf240), chr(0xf241), chr(0xf242), chr(0xf243), chr(0xf244)]
    chars.reverse()


    output = check_output(["upower", "-i", "/org/freedesktop/UPower/devices/battery_BAT0"]).decode()
    percentage = [line.split(":")[1].strip().split("%")[0] for line in output.split("\n") if "percentage" in line][0]
    state = [not line.split(":")[1].strip() == "discharging" for line in output.split("\n") if "state" in line][0]

    color = tools.color(int(percentage))
    return f'{f"{chr(0xf1e6)} " if state else ""}{chars[floor(int(percentage) / (len(chars)+16))]}  {percentage}%'

if __name__ == "__main__":
    print(run())
