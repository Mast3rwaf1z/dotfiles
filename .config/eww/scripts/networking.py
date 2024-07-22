from subprocess import check_output
from math import ceil
import tools

def run():
    ssid = check_output(["nmcli", "-t", "c"]).decode().split("\n")[0].split(":")[0]
    ip = [line for line in check_output(["nmcli", "-t", "c", "show", ssid]).decode().split("\n") if "IP4.ADDRESS[1]" in line][0].split(":")[1].split("/")[0]
    return f"{chr(0xf1eb)} {ssid} - {ip}" if not ssid == "lo" else "Disconnected"

if __name__ == "__main__":
    print(run())
