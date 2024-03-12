FIFO="$1"

volume(){
    icon=$(python scripts/volume.py icon)
    value=$(python scripts/volume.py get)
    printf "(box "
    printf "(box :style \"background-image: url('%s')\" :class \"trayicon\") " $icon
    printf "(box \"$value%%\")" $value
    printf ")\n"
}


volume
tail -f $FIFO | while read -r _; do
    volume
done
