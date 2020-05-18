# Exercise 21 (and Solution)
#
# Take the code from the How To Decode A Website exercise (if you didn’t do it or just want to play
# with some different code, use the code from the solution), and instead of printing the results to a screen,
# write the results to a txt file. In your code, just make up a name for the file you are saving to.
#
# Extras:
# Ask the user to specify the name of the output file that will be saved.


#  Exercise 17 Code

import bs4, requests

url = "https://www.nytimes.com/"
r = requests.get(url)
r_html = r.text

soup = bs4.BeautifulSoup(r_html, "html.parser")
title = soup.find_all("h2", class_="esl82me0")

ny_times_titles = [i.text for i in title]

# Writing to a file

with open("nytimes_titles.txt", "w") as open_file:
    open_file.write(str(ny_times_titles))
