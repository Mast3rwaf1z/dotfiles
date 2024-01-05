workspaces() {
	ACTIVE=$(swaymsg -t get_workspaces | jq '.[] | select(.focused==true) | .num')
	OCCUPIED=$(swaymsg -t get_workspaces | jq '.[] | .num')

	printf '(box :valign "center" :halign "start"'

	for i in $(seq 10); do
		if ! [[ "${OCCUPIED}" =~ "$i" ]]; then
			continue
		fi
		if [[ "$i" == "$ACTIVE" ]]; then
			printf "(button :onclick \"swaymsg workspace $i\" :class \"active-workspace\" \"$i\") "
		else
			printf "(button :onclick \"swaymsg workspace $i\" :class \"inactive-workspace\" \"$i\") "
		fi
	done
	printf ")\n"
}
workspaces
swaymsg -t subscribe -m '["workspace"]' | while read -r _; do
	workspaces
done
