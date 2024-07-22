from subprocess import check_output
from json import loads, dumps
from math import floor, ceil


def run():
    with open("state/gpu.json", "r") as file:
        history = loads(file.read())["value"]

    gpu_usage = int([line.split(":")[1].split("%")[0].strip() for line in check_output(["nvidia-smi", "-q"]).decode().split("\n") if "Gpu" in line][0])

    chars = [" "] + [chr(i) for i in range(int("2581", 16), int("2589", 16))]

    next_char = chars[floor(gpu_usage / (len(chars)+3))]

    history = history[1:]+next_char

    with open("state/gpu.json", "w") as file:
        file.write(dumps({"value":history}, indent=4))

    return f"{'0' if gpu_usage < 10 else ''}{gpu_usage}%{history}"

if __name__ == "__main__":
    print(run())
