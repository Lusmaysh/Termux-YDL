import os,sys,time
from random import choice
from argparse import ArgumentParser,SUPPRESS

if sys.version[0]!="3":sys.exit()
author=choice(["Lusmaysh","L2D     ","MoonCake"])
__version__ = "2022.02.17"
ijm="\33[32;1m";brm="\33[36;1m"

if not os.path.exists(os.getenv("PREFIX")+"/lib/python3.10/site-packages/youtube_dl/__init__.py"):
	os.system("pip3 install youtube-dl")
if not os.path.isfile(os.getenv("PREFIX")+"/bin/ffmpeg") and os.getlogin()=="u0_a465":
	os.system("pkg install ffmpeg")

parser=ArgumentParser(add_help=False,usage="%(prog)s [options]",epilog="Thanks for youtube-dl author.",description="I just made it easier to use and did a little decoration.")
parser.add_argument("-u","--url",help="Youtube video url, you want to download.")
parser.add_argument("-p","--path",metavar="PATTERN",default=os.path.join(os.getcwd(),'Downloads'),help="Path to store video you have downloaded, Default: %(default)s.")
parser.add_argument("-l","--latest",action="store_true",help="Using url lately.")
parser.add_argument("-m","--mp3",action="store_true",help="If download audio only, the downloaded format is MP3 not M4A, (M4A is better).")
parser.add_argument("-v","--verbose",action="store_true",help="Show various debugging information.")
parser.add_argument("-U","--update",action="store_true",help="Update the project to latest version.")
parser.add_argument("-h","--help",action="help",help="Show help message and exit.")
parser.add_argument("-V","--version",action="version",version=__version__,help="Show project version and exit.")
args=parser.parse_args()

def update():
	os.system(f"curl -s https://raw.githubusercontent.com/Lusmaysh/termux-ydl/main/main.py | diff -u \"{sys.argv[0]}\" - | patch \"{sys.argv[0]}\"")
	sys.exit("The Script Has Been Updated.")

def banner():
	os.system('cls' if os.name=='nt' else 'clear')
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

def rerun(s):
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
	elif format == "8" or not format and os.getlogin()=='u0_a465':
		s='-f "bestvideo[height<=4320][fps<=60][ext=mp4]+bestaudio[ext=m4a]" '+s
	else:
		s='-f "best[height<=4320][fps<=60][ext=mp4]+bestaudio[ext=m4a]" '+s
	os.system('cls' if os.name=='nt' else 'clear')
	print(f"{ijm}【 Video url 】{brm}{url}\n{ijm}【 Starting The Process.. 】{brm}")
	if args.mp3:s=s+"--audio-format mp3 -x"
	if args.verbose:s=s+"--verbose"
	if not args.path.endswith("/"):args.path=args.path+"/"
	if os.path.exists("/data/data/com.termux/files/home") and args.path!=os.path.join(os.getcwd(),"Downloads"):os.system(f"youtube-dl {url} --no-mtime -o /data/data/com.termux/files/home/storage/shared/Youtube/%\(title\)s.%\(ext\)s {s}")
	else:os.system(f"mkdir -p Downloads && youtube-dl {url} --no-mtime -o {args.path}%\(title\)s.%\(ext\)s {s}")

def verify_version(x,y):
	from re import match
	with open(x) as f:
		for s in f:
			v=match(y,s)
			if v:
				return v.group(1)

def subtitle():
	subtitle=['af','am','ar','az','be','bg','bn','bs','sq','ca','ceb','co','cs','cy','da','de','el','es','en','en-US','eo','et','eu','fa','fi','fil','fr','fy','ga','gd','gl','gu','ha','haw','hi','ht','hmn','hu','hr','hy','iw','is','ig','id','it','ja','jv','ka','kn','kk','km','ko','ku','ky','lo','la','lv','lt','lb','my','mk','mg','ms','ml','mt','mi','mr','mn','nl','ne','no','ny','or','ps','pl','pt','pa','rw','ro','ru','sm','sr','sn','sd','si','sk','sl','so','st','su','sw','sv','tg','ta','tt','te','th','tr','tk','uk','ur','ug','uz','vi','xh','yi','yo','zu','zh-Hans','zh-Hant',]
	banner()
	for x in range(len(subtitle)):
		print(f"{brm}╠═{ijm}▶ {x+1}."+subtitle[x])
	lang = input(f"{brm}╚═{ijm}▶【𝗦𝗲𝗹𝗲𝗰𝘁 The Language】➳ ")
	if lang=='1':w=subtitle[0]
	elif lang=='2':w=subtitle[1]
	elif lang=='3':w=subtitle[2]
	elif lang=='4':w=subtitle[3]
	elif lang=='5':w=subtitle[4]
	elif lang=='6':w=subtitle[5]
	elif lang=='7':w=subtitle[6]
	elif lang=='8':w=subtitle[7]
	elif lang=='9':w=subtitle[8]
	elif lang=='10':w=subtitle[9]
	elif lang=='11':w=subtitle[10]
	elif lang=='12':w=subtitle[11]
	elif lang=='13':w=subtitle[12]
	elif lang=='14':w=subtitle[13]
	elif lang=='15':w=subtitle[14]
	elif lang=='16':w=subtitle[15]
	elif lang=='17':w=subtitle[16]
	elif lang=='18':w=subtitle[17]
	elif lang=='19':w=subtitle[18]
	elif lang=='20':w=subtitle[19]
	elif lang=='21':w=subtitle[20]
	elif lang=='22':w=subtitle[21]
	elif lang=='23':w=subtitle[22]
	elif lang=='24':w=subtitle[23]
	elif lang=='25':w=subtitle[24]
	elif lang=='26':w=subtitle[25]
	elif lang=='27':w=subtitle[26]
	elif lang=='28':w=subtitle[27]
	elif lang=='29':w=subtitle[28]
	elif lang=='30':w=subtitle[29]
	elif lang=='31':w=subtitle[30]
	elif lang=='32':w=subtitle[31]
	elif lang=='33':w=subtitle[32]
	elif lang=='34':w=subtitle[33]
	elif lang=='35':w=subtitle[34]
	elif lang=='36':w=subtitle[35]
	elif lang=='37':w=subtitle[36]
	elif lang=='38':w=subtitle[37]
	elif lang=='39':w=subtitle[38]
	elif lang=='40':w=subtitle[39]
	elif lang=='41':w=subtitle[40]
	elif lang=='42':w=subtitle[41]
	elif lang=='43':w=subtitle[42]
	elif lang=='44':w=subtitle[43]
	elif lang=='45':w=subtitle[44]
	elif lang=='46':w=subtitle[45]
	elif lang=='47':w=subtitle[46]
	elif lang=='48':w=subtitle[47]
	elif lang=='49':w=subtitle[48]
	elif lang=='50':w=subtitle[49]
	elif lang=='51':w=subtitle[50]
	elif lang=='52':w=subtitle[51]
	elif lang=='53':w=subtitle[52]
	elif lang=='54':w=subtitle[53]
	elif lang=='55':w=subtitle[54]
	elif lang=='56':w=subtitle[55]
	elif lang=='57':w=subtitle[56]
	elif lang=='58':w=subtitle[57]
	elif lang=='59':w=subtitle[58]
	elif lang=='60':w=subtitle[59]
	elif lang=='61':w=subtitle[60]
	elif lang=='62':w=subtitle[61]
	elif lang=='63':w=subtitle[62]
	elif lang=='64':w=subtitle[63]
	elif lang=='65':w=subtitle[64]
	elif lang=='66':w=subtitle[65]
	elif lang=='67':w=subtitle[66]
	elif lang=='68':w=subtitle[67]
	elif lang=='69':w=subtitle[68]
	elif lang=='70':w=subtitle[69]
	elif lang=='71':w=subtitle[70]
	elif lang=='72':w=subtitle[71]
	elif lang=='73':w=subtitle[72]
	elif lang=='74':w=subtitle[73]
	elif lang=='75':w=subtitle[74]
	elif lang=='76':w=subtitle[75]
	elif lang=='77':w=subtitle[76]
	elif lang=='78':w=subtitle[77]
	elif lang=='79':w=subtitle[78]
	elif lang=='80':w=subtitle[79]
	elif lang=='81':w=subtitle[80]
	elif lang=='82':w=subtitle[81]
	elif lang=='83':w=subtitle[82]
	elif lang=='84':w=subtitle[83]
	elif lang=='85':w=subtitle[84]
	elif lang=='86':w=subtitle[85]
	elif lang=='87':w=subtitle[86]
	elif lang=='88':w=subtitle[87]
	elif lang=='89':w=subtitle[88]
	elif lang=='90':w=subtitle[89]
	elif lang=='91':w=subtitle[90]
	elif lang=='92':w=subtitle[91]
	elif lang=='93':w=subtitle[92]
	elif lang=='94':w=subtitle[93]
	elif lang=='95':w=subtitle[94]
	elif lang=='96':w=subtitle[95]
	elif lang=='97':w=subtitle[96]
	elif lang=='98':w=subtitle[97]
	elif lang=='99':w=subtitle[98]
	elif lang=='100':w=subtitle[99]
	elif lang=='101':w=subtitle[100]
	elif lang=='102':w=subtitle[101]
	elif lang=='103':w=subtitle[102]
	elif lang=='104':w=subtitle[103]
	elif lang=='105':w=subtitle[104]
	elif lang=='106':w=subtitle[105]
	elif lang=='107':w=subtitle[106]
	elif lang=='108':w=subtitle[107]
	elif lang=='109':w=subtitle[108]
	elif lang=='110':w=subtitle[109]
	else:w=subtitle[18]
	if os.getlogin()=="u0_a465" and os.path.exists("/data/data/com.termux"):w=w+" --convert-subs srt"
	return "--sub-lang "+w

def main():
	if os.path.exists("/data/data/com.termux"):
		if not os.path.exists(os.getenv("HOME")+"/storage") and not os.path.exists("/sdcard/script"):
			os.system("termux-setup-storage && mkdir -p ~/storage/shared/Youtube")
		if not os.path.exists(os.getenv("HOME")+"/.config/youtube-dl/"):
			os.system("mkdir -p ~/.config/youtube-dl")
			with open(os.getenv("HOME")+"/.config/youtube-dl/config","w") as config:
				config.write('--no-mtime -o /data/data/com.termux/files/home/storage/shared/Youtube/%(title)s.%(ext)s -f "best[height<=4320][fps<=60][ext=mp4]+bestaudio[ext=m4a]"')
		if not os.path.exists(os.getenv("HOME")+"/bin/") or __version__ != verify_version(os.getenv("HOME")+"/bin/termux-url-opener","# __Version__ = '(.*)'"):
			os.system("mkdir -p ~/bin")
			with open(os.getenv("HOME")+"/bin/termux-url-opener","w") as eat:
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
	banner()
	if not args.url and not args.latest and not os.path.isfile(".history"):
		url = input(f"{brm}╚═{ijm}▶ [Input URL] ➳ ")
	elif os.path.isfile(".history") and len(open(".history").readlines())>=1:
		url = input(f"{brm}╚═{ijm}▶ [Input URL] (latest) ➳ ")
		if not url:
			args.latest=True
	else:url=args.url
	if args.latest or url.lower()=="latest":
		if not os.path.isfile(".history") or len(open(".history").readlines())==0:
			os.system("touch .history")
			banner()
			sys.exit(f"{brm}╚═{ijm}▶ You don't have history yet.")
		else:
			file = open(".history","r").readlines()
			url = file[len(file)-1].strip()
	if "youtu" in url.lower():
		if not os.path.isfile(".history"):
			history=open(".history","a").write(f"{url}\n")
		else:
			file = open(".history","r").readlines()
			if url!=file[len(file)-1].strip():
				history=open(".history","a").write(f"{url}\n")
	banner()
	type = input(f"""{brm}╠═{ijm}▶ 1. Video Only
{brm}╠═{ijm}▶ 2. Video With Subtitle
{brm}╠═{ijm}▶ 3. Video With Descripton
{brm}╠═{ijm}▶ 4. Video With Descripton And Subtitle
{brm}╠═{ijm}▶ 5. See Video Information
{brm}╠═{ijm}▶ 0. Download Video Desc/Sub
{brm}╚═{ijm}▶ [𝗦𝗲𝗹𝗲𝗰𝘁 The Option] ➳ """)
	if type == '1' or not type and os.getlogin()=='u0_a465':
		rerun("")
	elif type == '2' or type == "4":
		l=subtitle()
		if type=="4":l=l+" --write-description"
		rerun("--write-sub "+l)
	elif type == '3':
		rerun("--write-description")
	elif type == '5':
		os.system('cls' if os.name=='nt' else 'clear')
		print(f"【 Video 】{brm}{url}")
		print(f"{ijm}【 Title 】{brm}")
		os.system("youtube-dl --skip-download --get-title --no-warning "+url)
		print(f"{ijm}【 Description 】{brm}")
		os.system(f'youtube-dl {url} --no-mtime --get-description')
		print(f"{ijm}【 Format 】{brm}")
		os.system(f'youtube-dl {url} --no-mtime -F')
		print(f"{ijm}【 Subtitle 】{brm}")
		os.system(f'youtube-dl {url} --no-mtime --list-subs')
	elif type=="0":
		banner()
		extr=input(f"""{brm}╠═{ijm}▶ {brm}[{ijm} Select Options {brm}]
{brm}╠═{ijm}▶ {brm}[{ijm}1{brm}] {ijm}All Subtitle
{brm}╠═{ijm}▶ {brm}[{ijm}2{brm}] {ijm}All Auto Subtitle
{brm}╠═{ijm}▶ {brm}[{ijm}3{brm}] {ijm}Description
{brm}╠═{ijm}▶ {brm}[{ijm}4{brm}] {ijm}Auto Subtitle
{brm}╠═{ijm}▶ {brm}[{ijm}5{brm}] {ijm}Subtitle
{brm}╚═{ijm}▶ {ijm}""")
		if extr=="1":
			d="--all-subs"
		elif extr=="2":
			d="--write-auto-sub --all-subs"
		elif extr=="3":
			d="--write-description"
		elif extr=="4" or extr=="5":
			d=subtitle()
			if extr=="4":d="--write-auto-sub "+d
			elif extr=="5":d="--write-sub "+d
		os.system('cls' if os.name=='nt' else 'clear')
		print(f"{ijm}【 Video url 】{brm}{url}\n{ijm}【 Starting The Process.. 】{brm}")
		os.system(f"youtube-dl {url} -o /data/data/com.termux/files/home/storage/shared/Youtube/%\(title\)s.%\(ext\)s {d} --skip-download")

if __name__=='__main__':
	if args.update:update()
	while True:
		try:
			main()
			retry = input(f"{ijm}【 Try again? 】(Y/N) {brm}")
			if not retry.lower() == "y" and not retry.lower() == "yes":
				sys.exit()
		except KeyboardInterrupt:
			sys.exit()
