if [[ "$@" =~ "--debug" ]]; then
	DEBUG="on"
else
	DEBUG="off"
fi

if [[ "$1" == "external" ]]; then
    index=1
else
    index=0
fi

current_display="$(swaymsg -t get_outputs | jq -r ".[$index].name")"

workspaces(){
	printf '(box :valign "center" :halign "start" '
    for id in $(swaymsg -t get_workspaces | jq -s '.[] | sort_by(.num) | .[].num'); do
        workspace_data="$(swaymsg -t get_workspaces | jq -s ".[] | sort_by(.num) | .[] | select(.num == $id)")"
        display="$(echo $workspace_data | jq -r '.output')"
        active="$(echo $workspace_data | jq -r '.focused')"
        if [[ "$display" != "$current_display" ]]; then
            continue
        fi
        if [[ "$active" == "true" ]]; then
			printf "(button :onclick \"swaymsg workspace $id\" :class \"active-workspace\" \"$id\") "
        else
			printf "(button :onclick \"swaymsg workspace $id\" :class \"inactive-workspace\" \"$id\") "
        fi
    done
	printf ")\n"
}

workspaces
if [[ "$DEBUG" == "on" ]]; then
	exit
fi
swaymsg -t subscribe -m '["workspace"]' | while read -r _; do
	workspaces
done
