import urllib.request
import re

def URLSearch(search_keyword):
	html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
	video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
	vysledek="https://www.youtube.com/watch?v=" + video_ids[0]
	return vysledek