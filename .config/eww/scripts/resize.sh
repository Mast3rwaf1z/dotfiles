resize(){
    if [[ "$(swaymsg -t get_binding_state | jq -r '.name')" == "resize" ]]; then
        printf "(box :class \"resize\" \"Resize\")\n"
    else
        printf "(box :class \"no-resize\" \"\")\n"
    fi
}

resize
swaymsg -t subscribe -m '["binding"]' | while read -r _; do
    resize
done