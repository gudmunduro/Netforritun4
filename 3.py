"""
Exercise  12.3: Use urllub to replicate the previous exercise of (1) retrieving
the document from a URL, (2) displaying up to 3000 characters, and (3) counting
the overall characters in the document. Don't worry about the headers for this
exercise, simply show the first 3000 characters of the document contents.
Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
Solution by Jamison Lahman, June 4, 2017
"""
import urllib.request, urllib.parse, urllib.error
import sys

url: str = input("URL: ")

fhand = urllib.request.urlopen(url)

characters: int = 0
fullDocument: str = ''

for line in fhand:
    words = line.decode()           #\n is considered a character
                                    #amend to line.decode().rstrip() if need
    characters = characters + len(words)
    if characters < 3000:
        fullDocument += line.decode().strip()

if characters < 3000:
    print("Less than 3000")
    print(fullDocument)
else:
    print("More than 30000")
    print(fullDocument[:3000])