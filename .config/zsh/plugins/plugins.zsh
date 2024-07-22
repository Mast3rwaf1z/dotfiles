for dir in $(ls /usr/share/zsh/plugins); do
    source /usr/share/zsh/plugins/$dir/$dir.zsh
done
