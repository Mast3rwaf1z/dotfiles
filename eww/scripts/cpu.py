import json
from math import floor

def run():
    with open("/proc/stat") as file:
        cpus = {line.split(" ")[0]: [float(value) for value in line.split(" ")[1:]] for line in file.read().strip().split("\n")[1:] if "cpu" in line.split(" ")[0]}

    line = ""

    with open("state/cpu.json") as file:
        olddata = json.loads(file.read())
    
    chars = [" "] + [chr(i) for i in range(int("2581", 16), int("2589", 16))]

    percentages = []
    for cpu in cpus.keys():
        if not olddata:
            last_idle = last_total = 0
        else:
            last_idle, last_total = olddata[cpu][3],  sum(olddata[cpu])

        idle, total = cpus[cpu][3], sum(cpus[cpu])
        idle_delta, total_delta = idle - last_idle, total - last_total

        percentage = (1.0 - (idle_delta / total_delta)) * 100.0
    
        line += chars[floor(percentage / (len(chars)+3))]

        percentages.append(percentage)

    with open("state/cpu.json", "w") as file:
        file.write(json.dumps(cpus, indent=4))


    return f"{'0' if int(sum(percentages)/len(percentages)) < 10 else ''}{int(sum(percentages)/len(percentages))}%{line}"

if __name__ == "__main__":
    print(run())

