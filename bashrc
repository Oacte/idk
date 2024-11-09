# Ensure that we are running an interactive shell
[[ $- != *i* ]] && return

### "nvim" as manpager
export MANPAGER="nvim +Man!"

### ARCHIVE EXTRACTION

# Usage: ex <file>
function ex {
  if [ -z "$1" ]; then
    echo "Usage: ex <path/file_name>.<zip|rar|bz2|gz|tar|tbz2|tgz|Z|7z|xz|ex|tar.bz2|tar.gz|tar.xz>"
    echo "       extract <path/file_name_1.ext> [path/file_name_2.ext] [path/file_name_3.ext]"
  else
    for n in "$@"; do
      if [ -f "$n" ]; then
        ext="${n##*.}"
        case "${ext,,}" in
          cbt|tar.bz2|tar.gz|tar.xz|tbz2|tgz|txz|tar)
            tar xvf "$n"
            ;;
          lzma)
            unlzma ./"$n"
            ;;
          bz2)
            bunzip2 ./"$n"
            ;;
          cbr|rar)
            unrar x -ad ./"$n"
            ;;
          gz)
            gunzip ./"$n"
            ;;
          cbz|epub|zip)
            unzip ./"$n"
            ;;
          z)
            uncompress ./"$n"
            ;;
          7z|arj|cab|cb7|chm|deb|dmg|iso|lzh|msi|pkg|rpm|udf|wim|xar)
            7z x ./"$n"
            ;;
          xz)
            unxz ./"$n"
            ;;
          exe)
            cabextract ./"$n"
            ;;
          cpio)
            cpio -id < ./"$n"
            ;;
          cba|ace)
            unace x ./"$n"
            ;;
          *)
            echo "ex: '$n' - unknown archive method"
            return 1
            ;;
        esac
      else
        echo "'$n' - file does not exist"
        return 1
      fi
    done
  fi
}

### Aliases

alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias sd="sudo shutdown -P now"
alias SD="sudo shutdown -P now"
alias e="exit"
alias yta="yt-dlp --no-playlist --extract-audio"
alias f="fastfetch"
alias unused="sudo pacman -Rns $(pacman -Qtdq)"
alias db="sudo updatedb"
alias up="sudo pacman -Syu"
alias ..="cd .."
alias l="ls"
alias b="btop"
alias s="startx"
alias vim="nvim"
alias pkill="sudo pkill"
alias yt="yt-dlp -f 'bestvideo[height<=1080][fps<=30]+bestaudio'"
alias scr="scrcpy --max-size 1600 --max-fps=60 --video-bit-rate=20M"

# PS1 prompt customization
export PS1="\[\033[38;5;188m\]\u\[\033[38;5;183m\]@\[\033[38;5;243m\]\h \[\033[38;5;141m\]\w\[\033[0m\]$ "
