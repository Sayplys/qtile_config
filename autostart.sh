#!/bin/sh

nitrogen --restore &
picom &

alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '

export PATH=$PATH:$HOME/bin
xrandr --output HDMI-A-0 --primary --output DisplayPort-0 --right-of HDMI-A-0
