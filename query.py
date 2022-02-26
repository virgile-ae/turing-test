# Contains functions used to query google and get the answer
import requests
from bs4 import BeautifulSoup

base_url = "https://www.google.com/search?q="
headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3283.186 Safari/537.36"
}

# Contains the css classes of the answer box for different types of questions
qsubject_class = {
	"age": "Z0LcW",
	"birthday": "Z0LcW",
	"backup": "hgKElc",
	"date": "zCubwf",
	"description": "PZPZlf hb8SAc",
}

def build_url(question):
	formatted = "+".join(question)
	return base_url + formatted + "&hl=en"

# Scrapes google for answers with a backup
def fetch_answer(question, q_type):
	url = build_url(question)
	req = requests.get(url, headers=headers)
	soup = BeautifulSoup(req.text, "html.parser")
	try:
		_class = qsubject_class[q_type] if qsubject_class[q_type] != None else ""
		res = soup.find("div", class_=_class)
		return res.text
	except:
		try:
			res = soup.find("span", class_=qsubject_class["backup"])
			return res.text
		except:
			return "i dunno"