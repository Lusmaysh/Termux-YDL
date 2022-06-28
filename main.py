import os,sys,time
from random import choice
from argparse import ArgumentParser,SUPPRESS

def _parse():
	parser=ArgumentParser(add_help=False,
		usage="%(prog)s [URL]",
		epilog="Thanks for youtube-dl author.",
		description="This originaly from Youtube-dl package, i just made it easier to use and did a little decoration.")
	parser.add_argument("url",
		nargs="*",
		metavar="URL",
		help="Youtube video url, you want to download.")
	parser.add_argument("-p","--path",
		metavar="PATTERN",
		default=os.path.join(os.getcwd(),'Downloads'),
		help="Path to store video you have downloaded, Default: %(default)s.")
	parser.add_argument("-l","--latest",
		action="store_true",
		help="Using url lately.")
	parser.add_argument("-m","--mp3",
		action="store_true",
		help="If download audio only, the downloaded format is MP3 not M4A, (M4A is better).")
	parser.add_argument("-v","--verbose",
		action="store_true",
		help="Show various debugging information.")
	parser.add_argument("-U","--update",
		action="store_true",
		help="Update the project to latest version.")
	parser.add_argument("-h","--help",
		action="help",
		help="Show help message and exit.")
	parser.add_argument("-V","--version",
		action="version",
		version=__version__,
		help="Show project version and exit.")
	return parser.parse_args()

def _update():
	try:
		from requests import get,ConnectionError
		f1 = open(os.path.abspath(__file__)).read()
		f2 = get("https://raw.githubusercontent.com/Lusmaysh/termux-ydl/main/main.py", timeout=5).text
		if f1 != f2:
			with open(__file__,"w") as f:
				f.write(f2)
			f.close()
			die("scritp has been updated.")
		else:
			die("script is up to date.")
	except ImportError:
		die('"requests" is not installed.') if not _special else os.system("pip3 install requests")
	except ConnectionError:
		die("Connection error, please check your connection.")

def banner():
	clear()
	print(f"""\33[1;31m
          ▄▀▄     ▄▀▄
         ▄█░░▀▀▀▀▀░░█▄
     ▄▄  █░░░░░░░░░░░█  ▄▄
    █▄▄█ █░░█░░┬░░█░░█ █▄▄█{brm}
╔══════━━━━━━────── • ──────━━━━━━══════╗
║{ijm} ♚ Project : ᴛᴇʀᴍᴜx-ʏᴅʟ™               {brm}║
║{ijm} ♚ Author  : {author}                  {brm}║
║{ijm} ♚ Github  : github.com/Lusmaysh       {brm}║
║{ijm} ♚ Date    : {time.strftime('%d-%b-%Y')}               {brm}║
╠══════━━━━━━────── • ──────━━━━━━══════╝""")

def die(s=None):
	sys.exit(s)

def clear():
	os.system("cls" if os.name=="nt" else "clear")

def _special():
	dev = os.path.join(os.path.dirname(os.path.abspath(__file__)),"dev")
	if os.path.isfile(dev) and open(dev).readline().strip() == "Lusmaysh":
		return True
	else:
		return False

def _rerun(s):
	banner()
	format = input(f"""{brm}╠═{ijm}▶ 1. Music Mp3♫
{brm}╠═{ijm}▶ 2. Video 360p
{brm}╠═{ijm}▶ 3. Video 480p
{brm}╠═{ijm}▶ 4. Video 720p  (FHD)
{brm}╠═{ijm}▶ 5. Video 1080p (QHD)
{brm}╠═{ijm}▶ 6. Video 1440p (UHD)
{brm}╠═{ijm}▶ 7. Video 2160p (4K)
{brm}╠═{ijm}▶ 8. Video 4320p (8K)
{brm}╠═{ijm}▶ 9. Video Recomendation
{brm}╚═{ijm}▶ [𝗦𝗲𝗹𝗲𝗰𝘁 𝗔 𝗙𝗼𝗿𝗺𝗮𝘁] ➳ """)
	if format == '1':
		s='-f "bestaudio[ext=m4a]" '+s
	elif format == '2':
		s='-f "bestvideo[height<=360][fps<=60][ext=mp4]+bestaudio[ext=m4a]" '+s
	elif format == '3':
		s='-f "bestvideo[height<=480][fps<=60][ext=mp4]+bestaudio[ext=m4a]" '+s
	elif format == '4':
		s='-f "bestvideo[height<=720][fps<=60][ext=mp4]+bestaudio[ext=m4a]" '+s
	elif format == '5':
		s='-f "bestvideo[height<=1080][fps<=60][ext=mp4]+bestaudio[ext=m4a]" '+s
	elif format == '6':
		s='-f "bestvideo[height<=1440][fps<=60][ext=mp4]+bestaudio[ext=m4a]" '+s
	elif format == '7':
		s='-f "bestvideo[height<=2160][fps<=60][ext=mp4]+bestaudio[ext=m4a]" '+s
	elif format == "8" or not format and _special():
		s='-f "bestvideo[height<=4320][fps<=60][ext=mp4]+bestaudio[ext=m4a]" '+s
	else:
		s='-f "best[height<=4320][fps<=60][ext=mp4]+bestaudio[ext=m4a]" '+s
	clear()
	print(f"{ijm}【 Video url 】{brm}{url}\n{ijm}【 Starting The Process.. 】{brm}")
	if args.mp3:s=s+"--audio-format mp3 -x"
	if args.verbose:s=s+"--verbose"
	if not args.path.endswith("/"):args.path=args.path+"/"
	if os.path.exists("/data/data/com.termux/files/home") and args.path!=os.path.join(os.getcwd(),"Downloads"):os.system(f"youtube-dl {url} --no-mtime -o /data/data/com.termux/files/home/storage/shared/Youtube/%\(title\)s.%\(ext\)s {s}")
	else:os.system(f"mkdir -p Downloads && youtube-dl {url} --no-mtime -o {args.path}%\(title\)s.%\(ext\)s {s}")

def _verify_version(x,y):
	from re import match
	with open(x) as f:
		for s in f:
			v=match(y,s)
			if v:
				return v.group(1)

def _subtitle():
	subtitle=['af','am','ar','az','be','bg','bn','bs','sq','ca','ceb','co','cs','cy','da','de','el','es','en','en-US','eo','et','eu','fa','fi','fil','fr','fy','ga','gd','gl','gu','ha','haw','hi','ht','hmn','hu','hr','hy','iw','is','ig','id','it','ja','jv','ka','kn','kk','km','ko','ku','ky','lo','la','lv','lt','lb','my','mk','mg','ms','ml','mt','mi','mr','mn','nl','ne','no','ny','or','ps','pl','pt','pa','rw','ro','ru','sm','sr','sn','sd','si','sk','sl','so','st','su','sw','sv','tg','ta','tt','te','th','tr','tk','uk','ur','ug','uz','vi','xh','yi','yo','zu','zh-Hans','zh-Hant',]
	banner()
	for x in range(len(subtitle)):
		print(f"{brm}╠═{ijm}▶ {x+1}."+subtitle[x])
	lang = input(f"{brm}╚═{ijm}▶【𝗦𝗲𝗹𝗲𝗰𝘁 The Language】➳ ")
	lang = int(lang) if lang.isdigit() and int(lang) <= 110 and int(lang) >= 1 else 19
	w = subtitle[lang-1]
	if _special():w=w+" --convert-subs srt"
	return "--sub-lang "+w

def main():
	file_path = os.path.dirname(os.path.abspath(__file__))
	HOME = os.getenv("HOME")
	if os.path.exists("/data/data/com.termux"):
		if not os.path.exists(HOME+"/storage"):
			os.system("termux-setup-storage && mkdir -p ~/storage/shared/Youtube")
		if not os.path.exists(HOME+"/.config/youtube-dl/"):
			os.system("mkdir -p ~/.config/youtube-dl")
			with open(HOME+"/.config/youtube-dl/config","w") as config:
				config.write('--no-mtime -o /data/data/com.termux/files/home/storage/shared/Youtube/%(title)s.%(ext)s -f "best[height<=4320][fps<=60][ext=mp4]+bestaudio[ext=m4a]"')
			config.close()
		if not os.path.exists(HOME+"/bin/") or __version__ != _verify_version(HOME+"/bin/termux-url-opener","# __Version__ = '(.*)'"):
			os.system("mkdir -p ~/bin")
			with open(HOME+"/bin/termux-url-opener","w") as eat:
				eat.write(f"""# __Version__ = '{__version__}'
echo "\33[31;1m
          ▄▀▄     ▄▀▄
         ▄█░░▀▀▀▀▀░░█▄
     ▄▄  █░░░░░░░░░░░█  ▄▄
    █▄▄█ █░░█░░┬░░█░░█ █▄▄█{brm}
╔════════════════════════════════════════╗
║{ijm} ♚ Project : ᴛᴇʀᴍᴜx-ʏᴅʟ™                {brm}║
║{ijm} ♚ Author  : Lusmaysh                   {brm}║
║{ijm} ♚ Github  : github.com/Lusmaysh        {brm}║
╠════════════════════════════════════════╝
{brm}╠═{ijm}▶ {brm}[ {ijm}𝗦𝗲𝗹𝗲𝗰𝘁 𝗔 𝗙𝗼𝗿𝗺𝗮𝘁 {brm}] ➳
{brm}╠═{ijm}▶ {brm}[{ijm}1{brm}] {ijm}Music M4a♫
{brm}╠═{ijm}▶ {brm}[{ijm}2{brm}] {ijm}Video 360p
{brm}╠═{ijm}▶ {brm}[{ijm}3{brm}] {ijm}Video 480p
{brm}╠═{ijm}▶ {brm}[{ijm}4{brm}] {ijm}Video 720p  (FHD)
{brm}╠═{ijm}▶ {brm}[{ijm}5{brm}] {ijm}Video 1080p (QHD)
{brm}╠═{ijm}▶ {brm}[{ijm}6{brm}] {ijm}Video 1440p (UHD)
{brm}╠═{ijm}▶ {brm}[{ijm}7{brm}] {ijm}Video 2160p (4K)
{brm}╠═{ijm}▶ {brm}[{ijm}8{brm}] {ijm}Video 4320p (8K)
{brm}╠═{ijm}▶ {brm}[{ijm}9{brm}] {ijm}Video Recomendation"
while :
do
	read -p "{brm}╚═{ijm}▶ " opt
	case $opt in
		1)
			clear
			echo "--no-mtime -o /data/data/com.termux/files/home/storage/shared/YouTube/%(title)s.%(ext)s -f 'bestaudio[ext=m4a]'" > ~/.config/youtube-dl/config
			youtube-dl $1
			sleep 1
			exit
		;;
		2)
			clear
			echo "--no-mtime -o /data/data/com.termux/files/home/storage/shared/YouTube/%(title)s.%(ext)s -f 'bestvideo[height<=360][ext=mp4][fps<=60]+bestaudio[ext=m4a]'" > ~/.config/youtube-dl/config
			youtube-dl $1
			sleep 1
			exit
		;;
		3)
			clear
			echo "--no-mtime -o /data/data/com.termux/files/home/storage/shared/YouTube/%(title)s.%(ext)s -f 'bestvideo[height<=480][ext=mp4][fps<=60]+bestaudio[ext=m4a]'" > ~/.config/youtube-dl/config
			youtube-dl $1
			sleep 1
			exit
		;;
		4)
			clear
			echo "--no-mtime -o /data/data/com.termux/files/home/storage/shared/YouTube/%(title)s.%(ext)s -f 'bestvideo[height<=720][ext=mp4][fps<=60]+bestaudio[ext=m4a]'" > ~/.config/youtube-dl/config
			youtube-dl $1
			sleep 1
			exit
		;;
		5)
			clear
			echo "--no-mtime -o /data/data/com.termux/files/home/storage/shared/YouTube/%(title)s.%(ext)s -f 'bestvideo[height<=1080][ext=mp4][fps<=60]+bestaudio[ext=m4a]'" > ~/.config/youtube-dl/config
			youtube-dl $1
			sleep 1
			exit
		;;
		6)
			clear
			echo "--no-mtime -o /data/data/com.termux/files/home/storage/shared/YouTube/%(title)s.%(ext)s -f 'bestvideo[height<=1440][ext=mp4][fps<=60]+bestaudio[ext=m4a]'" > ~/.config/youtube-dl/config
			youtube-dl $1
			sleep 1
			exit
		;;
		7)
			clear
			echo "--no-mtime -o /data/data/com.termux/files/home/storage/shared/YouTube/%(title)s.%(ext)s -f 'bestvideo[height<=2160][ext=mp4][fps<=60]+bestaudio[ext=m4a]'" > ~/.config/youtube-dl/config
			youtube-dl $1
			sleep 1
			exit
		;;
		8)
			clear
			echo "--no-mtime -o /data/data/com.termux/files/home/storage/shared/YouTube/%(title)s.%(ext)s -f 'bestvideo[height<=4320][ext=mp4][fps<=60]+bestaudio[ext=m4a]'" > ~/.config/youtube-dl/config
			youtube-dl $1
			sleep 1
			exit
		;;
		9)
			clear
			echo "--no-mtime -o /data/data/com.termux/files/home/storage/shared/YouTube/%(title)s.%(ext)s -f 'best[height<=4320][ext=mp4][fps<=60]+bestaudio[ext=m4a]'" > ~/.config/youtube-dl/config
			youtube-dl $1
			sleep 1
			exit
		;;
		*)
			break
	esac
done""")

	global url
	history_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),".history")
	banner()
	if not args.url and not args.latest and not os.path.isfile(history_path):
		url = input(f"{brm}╚═{ijm}▶ [Input URL] ➳ ")
	elif not args.url and not args.latest and os.path.isfile(history_path) and len(open(history_path).readlines()) >= 1:
		url = input(f"{brm}╚═{ijm}▶ [Input URL] (latest) ➳ ")
		if not url:
			args.latest=True
	elif args.url and not args.latest:
		url=args.url[0]

	if args.latest or url.lower()=="latest":
		if not os.path.isfile(history_path) or len(open(history_path).readlines()) == 0:
			with open(history_path,"a"):
				pass
			banner()
			die(f"{brm}╚═{ijm}▶ You don't have history yet.")
		else:
			file = open(history_path,"r").readlines()
			url = file[len(file)-1].strip()
	if "short" in url.lower() and "?feature=share" in url.lower():
		url = url.replace("youtube.com/shorts/","youtu.be/").replace("?feature=share","")
	if "youtu" in url.lower():
		if not os.path.isfile(history_path):
			history=open(history_path,"a").write(f"{url}\n")
		else:
			file = open(history_path,"r").readlines()
			if url!=file[len(file)-1].strip():
				history=open(history_path,"a").write(f"{url}\n")

	banner()
	type = input(f"""{brm}╠═{ijm}▶ 1. Video Only\n{brm}╠═{ijm}▶ 2. Video With Subtitle\n{brm}╠═{ijm}▶ 3. Video With Descripton\n{brm}╠═{ijm}▶ 4. Video With Descripton And Subtitle\n{brm}╠═{ijm}▶ 5. See Video Information\n{brm}╚═{ijm}▶ [𝗦𝗲𝗹𝗲𝗰𝘁 The Option] ➳ """) if not _special() else input(f"""{brm}╠═{ijm}▶ 1. Video Only\n{brm}╠═{ijm}▶ 2. Video With Subtitle\n{brm}╠═{ijm}▶ 3. Video With Descripton\n{brm}╠═{ijm}▶ 4. Video With Descripton And Subtitle\n{brm}╠═{ijm}▶ 5. See Video Information\n{brm}╠═{ijm}▶ 0. Download Video Desc/Sub\n{brm}╚═{ijm}▶ [𝗦𝗲𝗹𝗲𝗰𝘁 The Option] ➳ """)
	if type == '1' or not type:
		_rerun("")
	elif type == '2' or type == "4":
		l=_subtitle()
		if type=="4":l=l+" --write-description"
		_rerun("--write-sub "+l)
	elif type == '3':
		_rerun("--write-description")
	elif type == '5':
		clear()
		print(f"【 Video 】{brm}{url}")
		print(f"{ijm}【 Title 】{brm}")
		os.system("youtube-dl --skip-download --get-title --no-warning "+url)
		print(f"{ijm}【 Description 】{brm}")
		os.system(f'youtube-dl {url} --no-mtime --get-description')
		print(f"{ijm}【 Format 】{brm}")
		os.system(f'youtube-dl {url} --no-mtime -F')
		print(f"{ijm}【 Subtitle 】{brm}")
		os.system(f'youtube-dl {url} --no-mtime --list-subs')
	elif type=="0" and _special():
		banner()
		extr=input(f"""{brm}╠═{ijm}▶ {brm}[{ijm} Select Options {brm}]\n{brm}╠═{ijm}▶ {brm}[{ijm}1{brm}] {ijm}All Subtitle\n{brm}╠═{ijm}▶ {brm}[{ijm}2{brm}] {ijm}All Auto Subtitle\n{brm}╠═{ijm}▶ {brm}[{ijm}3{brm}] {ijm}Description\n{brm}╠═{ijm}▶ {brm}[{ijm}4{brm}] {ijm}Auto Subtitle\n{brm}╠═{ijm}▶ {brm}[{ijm}5{brm}] {ijm}Subtitle\n{brm}╚═{ijm}▶ {ijm}""")
		if extr=="1":
			d="--all-subs"
		elif extr=="2":
			d="--write-auto-sub --all-subs"
		elif extr=="3":
			d="--write-description"
		elif extr=="4" or extr=="5":
			d=_subtitle()
			if extr=="4":d="--write-auto-sub "+d
			elif extr=="5":d="--write-sub "+d
		clear()
		print(f"{ijm}【 Video url 】{brm}{url}\n{ijm}【 Starting The Process.. 】{brm}")
		os.system(f"youtube-dl {url} -o {HOME}/storage/shared/Youtube/%\(title\)s.%\(ext\)s {d} --skip-download")

if __name__=='__main__':
	if sys.version[0]!="3":die("Sorry this script not avaiable on python2.")
	__version__, ijm, brm, author = "2022.02.17", "\33[32;1m", "\33[36;1m", choice(["Lusmaysh","L2D     ","MoonCake"])
	args = _parse()
	if not os.path.exists(os.getenv("PREFIX")+"/lib/python3.10/site-packages/youtube_dl/__init__.py"):
		if _special():
			os.system("pip3 install youtube-dl")
		else:
			die('"youtube-dl" is not installed.')
	if not os.path.isfile(os.getenv("PREFIX")+"/bin/ffmpeg"):
		if _special():
			os.system("pkg install ffmpeg")
		else:
			die('"ffmpeg" is not installed.')
	if args.update:_update()
	while True:
		try:
			main()
			retry = input(f"{ijm}【 Try again? 】(Y/N) {brm}")
			args.latest=False
			if not retry.lower() == "y" and not retry.lower() == "yes":
				die()
		except KeyboardInterrupt:
			die()
