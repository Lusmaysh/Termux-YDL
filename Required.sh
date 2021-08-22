clear
pkg update && pkg upgrade -y
termux-setup-storage
pkg install python -y
pip2 install youtube-dl -y
pkg install ffmpeg -y
mkdir ~/.config/youtube-dl
mkdir ~/storage/shared/Youtube
mkdir ~/bin
echo 'youtube-dl $1' > ~/bin/termux-url-opener
python ydl.py
