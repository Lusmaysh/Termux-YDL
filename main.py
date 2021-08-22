import os
ijm="\33[32;1m";brm="\33[36;1m";
console='--no-mtime -o /data/data/com.termux/files/home/storage/shared/Youtube/%\(title\)s.%\(ext\)s '

def banner():
	os.system('clear')
	print(f"""\33[1;31m
          ▄▀▄     ▄▀▄
         ▄█░░▀▀▀▀▀░░█▄
     ▄▄  █░░░░░░░░░░░█  ▄▄
    █▄▄█ █░░█░░┬░░█░░█ █▄▄█{brm}
╔════════════════════════════════════════╗
║{ijm} ♚ Project : ᴛᴇʀᴍᴜx-ʏᴅʟ™                {brm}║
║{ijm} ♚ Author  : Lusmaysh                   {brm}║
║{ijm} ♚ Github  : github.com/Lusmaysh        {brm}║
║{ijm} ♚ Website : -                          {brm}║
╠════════════════════════════════════════╝""")

def Rerun(option):
	os.system("clear")
	print(f"{ijm}[•]Starting The Process..")
	os.system(f"youtube-dl {url} {console} {option}")

def init():
	banner()
	global url
	url = input(f"{brm}╚═{ijm}▶ [Input URL] ➳ ")
	while len(url) == 0:
		init()
	history = open(".history.txt","a")
	history.write(f"\n{url}")
	history.close()
	if url == 'list':
		exit(os.system("nano .history.txt"))
	elif url == 'req':
		banner()
		print(f"{brm}╚═{ijm}▶ Success")
		with open("/data/data/com.termux/files/home/bin/termux-url-opener","w") as eat:
			eat.write("youtube-dl $1")
			eat.close()
			exit()
	banner()
	type = input(f"""{brm}╠═{ijm}▶ 1. Video Only
{brm}╠═{ijm}▶ 2. Video With Subtitle
{brm}╠═{ijm}▶ 3. Video With Descripton
{brm}╠═{ijm}▶ 4. See Video Info
{brm}╚═{ijm}▶ [𝗦𝗲𝗹𝗲𝗰𝘁 The Option] ➳ """)
	if type == '1':
		banner()
		format = input(f"""{brm}╠═{ijm}▶ 1. Music Mp3♫
{brm}╠═{ijm}▶ 2. Video 360p
{brm}╠═{ijm}▶ 3. Video 480p
{brm}╠═{ijm}▶ 4. Video 720p
{brm}╠═{ijm}▶ 5. Video 1080p
{brm}╠═{ijm}▶ 6. Video 2160p
{brm}╠═{ijm}▶ 7. Video Recomendation
{brm}╚═{ijm}▶ [𝗦𝗲𝗹𝗲𝗰𝘁 𝗔 𝗙𝗼𝗿𝗺𝗮𝘁] ➳ """)
		if format == '1':
			Rerun("-f 140")
		elif format == '2':
			Rerun('-f "mp4[height<=360]"')
		elif format == '3':
			Rerun('-f "mp4[height<=480]"')
		elif format == '4':
			Rerun('-f "mp4[height<=720]"')
		elif format == '5':
			Rerun('-f "mp4[height<=1080]"')
		elif format == '6':
			Rerun('-f "mp4[height<=2160]"')
		elif format == '7':
			Rerun('-f "best[height<=2160]"')
		else:
			exit(os.system('clear'))
	elif type == '2':
		banner()
		lang = input(f"""{brm}╠═{ijm}▶ 1. id (Indonesia Subtitle)
{brm}╠═{ijm}▶ 2. en (English Subtitle)
{brm}╠═{ijm}▶ 3. en-US (English-US Subtitle)
{brm}╚═{ijm}▶ [𝗦𝗲𝗹𝗲𝗰𝘁 The Language] ➳ """)
		if lang == 'id' or lang == 'en' or lang == 'en-US':
			banner()
			format = input(f"""{brm}╠═{ijm}▶ 1. Music Mp3♫
{brm}╠═{ijm}▶ 2. Video 360p
{brm}╠═{ijm}▶ 3. Video 480p
{brm}╠═{ijm}▶ 4. Video 720p
{brm}╠═{ijm}▶ 5. Video 1080p
{brm}╠═{ijm}▶ 6. Video 2160p
{brm}╠═{ijm}▶ 7. Video Recomendation
{brm}╚═{ijm}▶ [𝗦𝗲𝗹𝗲𝗰𝘁 𝗔 𝗙𝗼𝗿𝗺𝗮𝘁] ➳ """)
			if format == '1':
				Rerun("-f 140 --write-sub --sub-lang {lang} --convert-subs ass")
			elif format == '2':
				Rerun('-f "mp4[height<=360]" --write-sub --sub-lang {lang} --convert-subs ass')
			elif format == '3':
				Rerun('-f "mp4[height<=480]" --write-sub --sub-lang {lang} --convert-subs ass')
			elif format == '4':
				Rerun('-f "mp4[height<=720]" --write-sub --sub-lang {lang} --convert-subs ass')
			elif format == '5':
				Rerun('-f "mp4[height<=1080]" --write-sub --sub-lang {lang} --convert-subs ass')
			elif format == '6':
				Rerun('-f "mp4[height<=2160]" --write-sub --sub-lang {lang} --convert-subs ass')
			elif format == '7':
				Rerun('-f "best[height<=2160]" --write-sub --sub-lang {lang} --convert-subs ass')
			else:
				exit(os.system('clear'))
		else:
			exit(os.system('clear'))
	elif type == '3':
		banner()
		format = input(f"""{brm}╠═{ijm}▶ 1. Music Mp3♫
{brm}╠═{ijm}▶ 2. Video 360p
{brm}╠═{ijm}▶ 3. Video 480p
{brm}╠═{ijm}▶ 4. Video 720p
{brm}╠═{ijm}▶ 5. Video 1080p
{brm}╠═{ijm}▶ 6. Video 2160p
{brm}╠═{ijm}▶ 7. Video Recomendation
{brm}╚═{ijm}▶ [𝗦𝗲𝗹𝗲𝗰𝘁 𝗔 𝗙𝗼𝗿𝗺𝗮𝘁] ➳ """)
		if format == '1':
			Rerun("-f 140 --write-description")
		elif format == '2':
			Rerun('-f "mp4[height<=360]" --write-description')
		elif format == '3':
			Rerun('-f "mp4[height<=480]" --write-description')
		elif format == '4':
			Rerun('-f "mp4[height<=720]" --write-description')
		elif format == '5':
			Rerun('-f "mp4[height<=1080]" --write-description')
		elif format == '6':
			Rerun('-f "mp4[height<=2160]" --write-description')
		elif format == '7':
			Rerun('-f "best[height<=2160]" --write-description')
		else:
			exit(os.system('clear'))
	elif type == '4':
		os.system('clear')
		print(f"[•]Get Description Info..{brm}")
		os.system(f'youtube-dl {url} --no-mtime --get-description')
		print(f"{ijm}[•]Get Format Info..{brm}")
		os.system(f'youtube-dl {url} --no-mtime -F')
		print(f"{ijm}[•]Get Subtitle Info..{brm}")
		os.system(f'youtube-dl {url} --no-mtime --list-subs')
	else:
		exit(os.system('clear'))

if __name__=='__main__':
	banner()
	try:
		init()
	except:
		exit(os.system('clear'))
