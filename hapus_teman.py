#!/usr/bin/python3
# coding by : KhamdihiXD

import requests,re,os,json
from bs4 import BeautifulSoup as par

ok,user,loop = [],[],0

def login():
	cokies = input(" [?] Cokies : ")
	try:
		head = {
		"user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36",
		"referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8","cookie":cokies}
		_url_ = requests.get("https://business.facebook.com/business_locations", headers=head)
		_tok_ = re.search("(EAAG\w+)", _url_.text).group(1)
		if "EAAG" in _tok_:
			open("Data/Token.txt","w").write(_tok_);open("Data/Cokie.txt","w").write(cokies)
			dump_teman()
	except Exception as e:
		exit("\n %s[%s×%s] Cookie invalid : %s"%(N,M,N,e))

def dump_teman():
	os.system("clear")
	idt = input(" [?] Ketik 'me' untuk mengambil semua id anda : ")
	try:
		pantek = requests.get("https://graph.facebook.com/%s?fields=friends.limit(5001)&access_token=%s"%(idt, open("Data/Token.txt","r").read()), cookies={"cookie":open("Data/Cokie.txt","r").read()}).json()
		for khamdihi in pantek["friends"]["data"]:
			user.append(khamdihi["id"])
	except KeyError:
		exit("\n [×] Cokie invalid/tidak punya teman")
	for id in user:
		main("https://m.facebook.com/profile.php?id=%s&fref=fr_tab&refid=17"%(id))
	exit("\n [✓] Proses selesai!")

def main(file):
	global loop
	print("\n [✓] Total teman anda : {}".format(len(user)))
	print(" [✓] Proses penghapusan sedang berjalan\n")
	ex = par(requests.get(file, cookies={"cookie":open("Data/Cokie.txt","r").read()}).text,"html.parser")
	for a in ex.find_all("a", href=True):
		if "/removefriend.php?" in a["href"]:
			get_data = par(requests.get("https://m.facebook.com"+a["href"],cookies={"cookie":open("Data/Cokie.txt","r").read()}).text,"html.parser")
			find_url = get_data.find("form", method="post")["action"]
			cari_data = requests.get("https://m.facebook.com"+a["href"], cookies={"cookie":open("Data/Cokie.txt","r").read()})
			data_data = {
"fb_dtsg":re.search('name="fb_dtsg" value="(.*?)"', str(cari_data.text)).group(1),
"jazoest":re.search('name="jazoest" value="(.*?)"', str(cari_data.text)).group(1),
"confirm":"Konfirmasi"}
			post_unf = requests.post("https://m.facebook.com"+find_url, data=data_data, cookies={"cookie":open("Data/Cokie.txt","r").read()})
			if "Anda tidak lagi berteman dengan" in post_unf.text:
				print(" [✓] Berhasil menghapus !")
			else:
				print(" [×] Gagal menghapus")
	loop +=1



if __name__ == "__main__":
	try:
		cok = open("Data/Cokie.txt","r").read()
	except FileNotFoundError:
		login()
	dump_teman()
