
battery(){
    value=$(python scripts/battery.py get)
    color=$(python scripts/battery.py color)
    icon=$(python scripts/battery.py icon)
    printf "(box :style \"color: %s;\" " $color
    printf "\"%s\t%s%%\")\n" "$icon" "$value"
}


battery
upower -i /org/freedesktop/UPower/devices/battery_BAT0 --monitor | while read -r _; do
    battery
done