import os
from multiprocessing import Pool
from sys import argv

write = lambda obj, end="": print(obj, end=end)

directory = "/run/current-system/sw/share/applications"

def get_data(filename):
    with open(f'{directory}/{filename}', "r") as file:
        lines = file.read().split("\n")
        _exec = ([""]+[line.split("=")[-1] for line in lines if "Exec=" in line])[-1]
        _name = ([_exec]+[line.split("=")[-1] for line in lines if "Name=" in line])[-1]
        return (_exec, _name)


write("(box :orientation \"v\" :vexpand true")

files = os.listdir(directory)

for file in files:
    get_data(file)

with Pool(8) as p:
    data = p.map(get_data, files)

for exec, name in data:
    if exec and name:
        write(f" (button :class \"launcher_application_button\" :onclick \"{exec} & eww close launcher\" \"{name}\")")

print(")\n")