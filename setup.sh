pkg install python
pip install youtube-dl -y
pkg install ffmpeg -y
mkdir ~/.config/youtube-dl
mkdir ~/storage/shared/Youtube
mkdir ~/bin
echo 'youtube-dl $1' > ~/bin/termux-url-opener
