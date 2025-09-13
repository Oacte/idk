#!/bin/sh
# Environment variables for login shell; Zsh settings are in ~/.config/zsh/.zshrc

# Default programs
export EDITOR="nvim"
export TERMINAL="st"
export BROWSER="thorium-browser"

# XDG base directories
export XDG_CONFIG_HOME="$HOME/.config"
export XDG_DATA_HOME="$HOME/.local/share"
export XDG_CACHE_HOME="$HOME/.cache"

export NEWSBOAT_DIR="$XDG_CONFIG_HOME/newsboat"
export PKI_DIR="$XDG_CONFIG_HOME/pki"
export W3M_DIR="$XDG_STATE_HOME/w3m"

# Zsh config location
export ZDOTDIR="$XDG_CONFIG_HOME/zsh"

# History files
export LESSHISTFILE="$XDG_CACHE_HOME/less_history"
export PYTHON_HISTORY="$XDG_DATA_HOME/python/history"

# Scripts path (uncomment if needed)
# export PATH="$XDG_CONFIG_HOME/scripts:$PATH"

# X11 related
export XINITRC="$XDG_CONFIG_HOME/x11/xinitrc"
export XPROFILE="$XDG_CONFIG_HOME/x11/xprofile"
export XRESOURCES="$XDG_CONFIG_HOME/x11/xresources"

# GTK
export GTK2_RC_FILES="$XDG_CONFIG_HOME/gtk-2.0/gtkrc-2.0"

# CLI tools config
export WGETRC="$XDG_CONFIG_HOME/wget/wgetrc"
export PYTHONSTARTUP="$XDG_CONFIG_HOME/python/pythonrc"
export GNUPGHOME="$XDG_DATA_HOME/gnupg"
export CARGO_HOME="$XDG_DATA_HOME/cargo"
export GOPATH="$XDG_DATA_HOME/go"
export GOBIN="$GOPATH/bin"
export GOMODCACHE="$XDG_CACHE_HOME/go/mod"
export NPM_CONFIG_USERCONFIG="$XDG_CONFIG_HOME/npm/npmrc"
export GRADLE_USER_HOME="$XDG_DATA_HOME/gradle"
export NUGET_PACKAGES="$XDG_CACHE_HOME/NuGetPackages"
export _JAVA_OPTIONS=-Djava.util.prefs.userRoot="$XDG_CONFIG_HOME/java"
export _JAVA_AWT_WM_NONREPARENTING=1
export PARALLEL_HOME="$XDG_CONFIG_HOME/parallel"
export FFMPEG_DATADIR="$XDG_CONFIG_HOME/ffmpeg"

# FZF options (no subshells)
export FZF_DEFAULT_OPTS="--style minimal --color 16 --layout=reverse --height 30% --preview='bat -p --color=always {}'"
export FZF_CTRL_R_OPTS="--style minimal --color 16 --info inline --no-sort --no-preview"

# Colored less + termcap
export LESS="R --use-color -Dd+r -Du+b"

# Optional auto startx only on first TTY
#if [ -z "$DISPLAY" ] && [ "${XDG_VTNR:-0}" = 1 ]; then
#  exec startx
#fi
