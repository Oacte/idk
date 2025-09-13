# Minimal, instant-loading Zsh config

# Ensure XDG vars (if shell is started without .zprofile)
: "${XDG_CONFIG_HOME:=$HOME/.config}"
: "${XDG_CACHE_HOME:=$HOME/.cache}"

# Source aliases if present
[ -f "$XDG_CONFIG_HOME/shell/als" ] && source "$XDG_CONFIG_HOME/shell/als"

# Load only necessary modules
zmodload zsh/complist

# Fast completion init: use cached dump, skip checks
autoload -U compinit
if [[ ! -f $XDG_CACHE_HOME/zcompdump ]] || [[ $XDG_CONFIG_HOME/zsh/.zshrc -nt $XDG_CACHE_HOME/zcompdump ]]; then
    compinit -C -d $XDG_CACHE_HOME/zcompdump
else
    compinit -C -d $XDG_CACHE_HOME/zcompdump
fi

# Completion styles
zstyle ':completion:*' menu select
zstyle ':completion:*' special-dirs true
zstyle ':completion:*' list-colors ${(s.:.)LS_COLORS} ma=0\;33
zstyle ':completion:*' squeeze-slashes false
unsetopt NOMATCH

# History (small for instant load/save)
HISTSIZE=5000
SAVEHIST=5000
HISTFILE="$XDG_CACHE_HOME/zsh_history"

# History options
setopt append_history inc_append_history share_history
HISTCONTROL=ignoreboth

# Main opts
setopt auto_menu menu_complete
setopt autocd
setopt auto_param_slash
setopt no_case_glob no_case_match
setopt globdots
setopt extended_glob
setopt interactive_comments
unsetopt prompt_sp

# Disable accidental Ctrl+S
stty stop undef

# Lazy-load fzf on demand
_fzf_setup() { source <(fzf --zsh) }
zle -N _fzf_setup
fzf-history-widget() {
    zle -I
    unfunction fzf-history-widget
    _fzf_setup
    zle fzf-history-widget
}
zle -N fzf-history-widget
bindkey '^R' fzf-history-widget

# Keybindings
bindkey "^a" beginning-of-line
bindkey "^e" end-of-line
bindkey "^k" kill-line
bindkey "^j" backward-word
bindkey "^H" backward-kill-word
bindkey "^J" history-search-forward
bindkey "^K" history-search-backward

# Minimal, zero-subshell prompt
PROMPT='%m %~ %# '

if [ "$TERM" = "linux" ]; then
    PS1=$'\033[37;1m'"$PS1"
fi

# Created by `pipx` on 2025-08-15 02:02:06
export PATH="$PATH:/home/mus/.local/bin"

