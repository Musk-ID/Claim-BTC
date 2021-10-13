#!/usr/bin/python3
# Author : Kingtebe
# Jangan lupa follow my github https://github.com/Musk-ID
import os,sys,re,json,random,logging,subprocess
try:
	import requests
	from time import sleep
	from datetime import datetime
	from bs4 import BeautifulSoup as put
except ImportError:
	exit("\n Module not installed !\n")

c = '\033[1;36m'
p = '\033[1;37m'
h = '\033[1;32m'
k = '\033[1;33m'
m = '\033[1;31m'
q = '\033[1;30m'
z = '\033[101m'
o = '\033[0m'

Browser = [
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9",
]
req = requests.Session()
logging.basicConfig(format="%(message)s", level=logging.INFO)
clear = (lambda: subprocess.call(["clear"]))


def waktu(second):
	while second:
		mins,secs = divmod(second,60)
		timer = "  \033[1;33m▶ \033[1;37mWaiting\033[1;37m \033[37m⟨\033[0;36m{:02d}:{:02d}\033[1;37m⟩".format(mins,secs)
		print(timer,end="\r")
		sleep(1)
		second -= 1

def message(kata):
	for bitcoin in kata +"\n":
		sys.stdout.write(bitcoin)
		sys.stdout.flush()
		sleep(0.001)

def _login(username,password):
	global time,date,find_ip
	time = datetime.now().strftime("%H.%M.%S")
	date = datetime.now().strftime("%d/%m/%Y")
	req.headers.update({"User-Agent":random.choice(Browser)})
	find_ip = req.get("https://api.myip.com").json()
	site = put(req.get("https://xauusd.biz/gold/dashboard").text, "html.parser")
	token = site.find("input",{"type":"hidden","name":"_token"})
	login = req.post("https://xauusd.biz/auth/login/post",data={
		"_token":token["value"],
		"username":username,
		"password":password,
		"redirect":"https://xauusd.biz/gold/dashboard",
	})

def _main():
	if not os.path.exists("usr.json"):
		clear()
		time1 = datetime.now().strftime("%H.%M.%S")
		date1 = datetime.now().strftime("%d/%m/%Y")
		message(f"\n  {p}Time : {time1}           Date : {date1}\n {m}╔{c}═════════════════════════════════════════════{m}╗\n {c}║ {m}██████{c}╗  {m}██████{c}╗  {m}██████{c}╗ {m}████████{c}╗{m}███████{c}╗ {c}║\n {c}║ {m}██{c}╔══{m}██{c}╗{m}██{c}╔═══{m}██{c}╗{m}██{c}╔═══{m}██{c}╗{c}╚══{m}██{c}╔══╝{m}██{c}╔════╝ {c}║\n {c}║ {m}██████{c}╔╝{m}██{c}║   {m}██{c}║{m}██{c}║   {m}██{c}║   {m}██{c}║   {m}███████{c}╗ {c}║\n {c}║ {m}██{c}╔══{m}██{c}╗{m}██{c}║   {m}██{c}║{m}██{c}║   {m}██{c}║   {m}██{c}║   {c}╚════{m}██{c}║ {c}║\n {c}║ {m}██████{c}╔╝{c}╚{m}██████{c}╔╝{c}╚{m}██████{c}╔╝   {m}██{c}║   {m}███████{c}║ {c}║\n {c}║ ╚═════╝  ╚═════╝  ╚═════╝    ╚═╝   ╚══════╝ {c}║\n {c}║{k}---------------------------------------------{c}║\n {c}║ {k}▶ {p}Author {k}: {p}Kingtebe                         {c}║\n {c}║ {k}▶ {p}Github {k}: {p}github.com/Musk-ID      {m}[{p}ONLINE{m}] {c}║\n {m}╚{c}═════════════════════════════════════════════{m}╝\n {q}<═════════════[{k}{z} • FREE SCRIPT • {o}{q}]═════════════>\n  {c}▶ {p}Version {k}: {p}1.1\n  {c}▶ {p}IP Kamu {k}: {h}114.285.98.91\n  {c}▶ {p}Youtube {k}: {p}FaaL TV\n {q}<═════════════════════════════════════════════>")
		logging.info(f"       {q}-{q}-{q}={q}[{p}{z} Login to web Xauusd.biz {o}{q}]{q}={q}-{q}-\n")
		nickname = input(f"  {m}▶ {p}Username/Email {m}: {k}")
		password = input(f"  {m}▶ {p}Password {m}: {k}")
		with open("usr.json","w") as file:
			json.dump({"username":nickname,"password":password},file,sort_keys=True,indent=4)
	file = json.loads(open("usr.json").read())
	username = file["username"]
	password = file["password"]
	try:
		_login(username,password);clear()
		message(f"\n  {p}Time : {time}             Date : {date}\n {m}╔{c}═════════════════════════════════════════════{m}╗\n {c}║ {m}██████{c}╗  {m}██████{c}╗  {m}██████{c}╗ {m}████████{c}╗{m}███████{c}╗ {c}║\n {c}║ {m}██{c}╔══{m}██{c}╗{m}██{c}╔═══{m}██{c}╗{m}██{c}╔═══{m}██{c}╗{c}╚══{m}██{c}╔══╝{m}██{c}╔════╝ {c}║\n {c}║ {m}██████{c}╔╝{m}██{c}║   {m}██{c}║{m}██{c}║   {m}██{c}║   {m}██{c}║   {m}███████{c}╗ {c}║\n {c}║ {m}██{c}╔══{m}██{c}╗{m}██{c}║   {m}██{c}║{m}██{c}║   {m}██{c}║   {m}██{c}║   {c}╚════{m}██{c}║ {c}║\n {c}║ {m}██████{c}╔╝{c}╚{m}██████{c}╔╝{c}╚{m}██████{c}╔╝   {m}██{c}║   {m}███████{c}║ {c}║\n {c}║ ╚═════╝  ╚═════╝  ╚═════╝    ╚═╝   ╚══════╝ {c}║\n {c}║{k}---------------------------------------------{c}║\n {c}║ {k}▶ {p}Author {k}: {p}Kingtebe                         {c}║\n {c}║ {k}▶ {p}Github {k}: {p}github.com/Musk-ID      {m}[{p}ONLINE{m}] {c}║\n {m}╚{c}═════════════════════════════════════════════{m}╝\n {q}<═════════════[{k}{z} • FREE SCRIPT • {o}{q}]═════════════>\n  {c}▶ {p}Version {k}: {p}1.1\n  {c}▶ {p}IP Kamu {k}: {h}{find_ip['ip']}\n  {c}▶ {p}Youtube {k}: {p}FaaL TV\n {q}<═════════════════════════════════════════════>")
		url = put(req.get("https://xauusd.biz/gold/dashboard").text,"html.parser")
		find_element = url.findAll("p")
		logging.info(f"    {p}Login as{c}{find_element[8].text} {p}balance {h}{find_element[7].text} ");logging.info(f" {q}<═════════════════════════════════════════════>")
		while True:
			url = put(req.get("https://xauusd.biz/gold/dashboard").text,"html.parser")
			find_element = url.findAll("p")
			base = put(req.get("https://xauusd.biz/gold/faucet").text,"html.parser")
			token = base.find("input",{"type":"hidden","name":"_token"})
			verify = req.post("https://xauusd.biz/auth/faucet/claim",data={"_token":token["value"]})
			get_claim = put(req.get("https://xauusd.biz/gold/faucet").text,"html.parser")
			#timer = re.search("var\searning_seconds\s=\s(.*?)",str(get_claim)).group(1)
			if get_claim.find("div",attrs={"class":"alert alert-success text-center"}) is None:
				logging.info(f"  {m}▶ {p}Sorry bro, Failed claim {m}!\n")
				exit()
			else:
				logging.info(f"  {m}▶ {h}Successful claim! {p}••{m}> {p}Now {q}[ {c}{find_element[7].text} {q}]");waktu(60)
	except IndexError:
		sleep(1.6)
		exit(f"\n  {c}~{c}> {p}Username/E-Mail or Password is incorrect {m}!\n")
		os.remove("usr.json")


if __name__=='__main__':
	_main()
