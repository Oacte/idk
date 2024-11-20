setxkbmap -layout fr,ara -option grp:alt_shift_toggle &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
xrdb -merge ~/.Xresources
xset r rate 190 35 &
xwallpaper --zoom Downloads/wallhaven-yxdrex_1920x1080.png
fastcompmgr & 
slstatus &
fast &
unclutter -idle 3 -root &
exec dwm
