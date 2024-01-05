from subprocess import check_output
from math import floor
from json import loads, dumps
import os

def run():
    meas = [[int(col.strip()) for col in line.split(" ") if not col.strip() == "" and not "Mem:" in col] for line in check_output(["free"]).decode().split("\n") if "Mem:" in line][0]

    percentage = (meas[1]/meas[0])*100

    with open("state/memory.json", "r") as file:
        history = loads(file.read())["value"]

    chars = [" "] + [chr(i) for i in range(int("2581", 16), int("2589", 16))]

    next_char = chars[floor(percentage / (len(chars)+3))]

    history = history[1:]+next_char

    with open("state/memory.json", "w") as file:
        file.write(dumps({"value":history}, indent=4))

    return f'{"0" if percentage < 10 else ""}{int(percentage)}%{history}'

if __name__ == "__main__":
    print(run())
