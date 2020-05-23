import requests
import json
from bs4 import BeautifulSoup

res = requests.get("https://digitalinnovation.one/blog/")
res.encoding = 'utf-8'

soup = BeautifulSoup(res.text, 'html.parser')

links = soup.find(class_="pagination").find_all('a')

#all_posts = soup.find_all(class_="posts")

#print(all_posts)

all_pages = []
for link in links:
  page = requests.get(link.get('href'))
  all_pages.append(BeautifulSoup(page.text, 'html.parser'))

print(len(all_pages))

all_posts = []

for posts in all_pages:
  posts = soup.find_all(class_="post")
  for post in posts:
    info = post.find(class_="post-content")
    title = info.h2.text
    preview = info.p.text
    author = info.find(class_="post-author").text
    #time = info.footer.date['datetime']
    time = info.find(class_="post-date") ['datetime']
    #img = info.find(class_="wp-post-image")
    all_posts.append({
      'title': title,
      'preview': preview,
      'author': author,
      'img': img,
      'time': time
    })

  #print(post.find('h2').text)

  print(all_posts)
  with open('posts.json', 'w') as json_file:
    json_dump(all_posts, json_file, indent=3, ensure_ascii=False)