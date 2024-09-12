from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com")

yc_web_page = response.text


soup = BeautifulSoup(yc_web_page,"html.parser")
article_tag = soup.find(name="span", class_="titleline")
article_text = article_tag.get_text()
article_link = article_tag.get("href")
article_upvote = soup.find(name="span", class_="score").getText()

print(article_text)
print(article_link)
print(article_link)

# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.name)
# #
# # print(soup.prettify()) # prettify will intend.
# # print(soup.p) #will print the first p
#
# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     # print(tag.get("href"))
#     pass
#
# heading = soup.find(name="h1", id="name") # we can do same with the class attribute, but with class_
# # print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading)
#
# company_url = soup.select_one(selector="p a") # we can use CSS as well.
# # print(company_url)
#
# name = soup.select_one(selector="#name") # we can use CSS as well.
# # print(name)
#
# headings = soup.select(selector=".heading")
# print(headings)