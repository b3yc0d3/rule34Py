from rule34Py import rule34Py
import json


r34Py = rule34Py()

print(r34Py.version)

post = r34Py.get_post(4931536)
print(post.thumbnail)

icame = r34Py.icame()
print(icame)

comments = r34Py.get_comments(13647055)
print(comments)

search = r34Py.search(["neko"], page_id=2, limit=50)
print(search)

pool = r34Py.get_pool(25938)
print(pool)

rpost = r34Py.random_post()
print(rpost)

tag_map = r34Py.tag_map()
print(tag_map)

top_tags = r34Py.top_tags()
print(top_tags)
