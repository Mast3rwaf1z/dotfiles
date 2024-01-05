get_date() {
	printf "(box :halign \"end\" \"$(date)\")\n"
}

get_date
while true; do
	get_date
done
