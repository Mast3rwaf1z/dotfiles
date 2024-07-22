# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000
bindkey -e
# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '/home/mast3r/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall
#

for dir in $(ls ~/.config/zsh); do
    source ~/.config/zsh/$dir/$dir.zsh
done

PROMPT="%F{166}%n%f@%F{166}%m%f %F{7}%~%f%F{166} > %f"

alias neofetch=hyfetch

if command -v pyenv &>/dev/null; then
    export PYENV_ROOT="$HOME/.pyenv"
    [[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
    eval "$(pyenv init -)"
fi

if command -v direnv &>/dev/null; then
    eval "$(direnv hook zsh)"
fi

export PATH=$PATH:/home/mast3r/.local/bin

alias cat='bat -pp'

alias vim=nvim
alias vi=nvim

export EDITOR=nvim
