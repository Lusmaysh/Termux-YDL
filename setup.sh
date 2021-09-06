pkg install ffmpeg -y
pip install youtube-dl -y
mkdir ~/.config/youtube-dl
mkdir ~/storage/shared/Youtube
mkdir ~/bin
echo 'youtube-dl $1' > ~/bin/termux-url-opener
echo '--no-mtime -o /data/data/com.termux/files/home/storage/shared/Youtube/%(title)s.%(ext)s -f "mp4[height<=2160]"' > ~/.config/youtube-dl/config
