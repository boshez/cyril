import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from tqdm import tqdm
from bs4 import BeautifulSoup
from newspaper import Article
import os

DIR = os.path.dirname(os.path.abspath(__file__))

main_url = "https://www.dawn.com/authors/193/cyril-almeida/"
def main_list(main_url):
	ret = []
	for i in range(1,21):
		ret.append(main_url+str(i))
	return ret

def retry_session(retries, session=None, backoff_factor=0.1, status_forcelist=(500, 502, 503, 504, 403)):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session

session = retry_session(retries=5)

def rget(url):
    return session.get(url)


article_pages = main_list(main_url)

f = open(DIR+"/text.txt","w+")

for article_url in article_pages:

	resp = rget(article_url)

	soup = BeautifulSoup(resp.text, features="lxml")

	for a in tqdm(soup.select('.mr-4.m-2 h2 a[href]')):
		down_url = a['href']
		print(down_url)
		url_resp = rget(down_url)
		article = Article(down_url)
		article.set_html(url_resp.text)
		article.parse()
		title = article.title
		body = article.text
		to_write = "{}\n\n{}\n\n".format(title, body)
		f.write(to_write)

f.close()