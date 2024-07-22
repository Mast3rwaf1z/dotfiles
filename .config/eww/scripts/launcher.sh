launcher(){
    printf '(box :orientation "v" :vexpand true '
    i=0
    dir="/run/current-system/sw/share"
    for file in $(ls $dir/applications); do
        _exec="$(python -c "import sys; print(sys.argv[-1].split('=')[-1])" "$(cat $dir/applications/$file | grep Exec=)")"
        _name="$(python -c "import sys; print(sys.argv[-1].split('=')[-1])" "$(cat $dir/applications/$file | grep Name=)")"
        printf "(button :class 'launcher_application_button' :onclick \"$_exec & eww close launcher\" \"$_name\") "
    done
    printf ')\n'
    sleep 1
}

launcher