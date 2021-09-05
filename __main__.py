
from GetNames import call_playlist
from YoutubeSearch import URLSearch
from downloaderYT import YTDownload
import urllib
import sys
import re


def main(argv):

    a = str(sys.argv[1])
    IDplaylist = re.search("playlist\/(.*)\?si", a).group(1)
    print(IDplaylist)
    if IDplaylist:

        playlist = call_playlist('spotify', IDplaylist)
        UrlsOfSongs = []
        print(a)

        for string in playlist:
            new_string = urllib.parse.quote_plus(string)
            new_string = URLSearch(new_string)
            UrlsOfSongs.append(new_string)
            print (new_string)
            YTDownload(new_string)
    else:
        print("Playlist wasnt found.")


if __name__ == '__main__':
    main(sys.argv[1:])
