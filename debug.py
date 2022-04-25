from rule34Py import rule34Py, version
#import random

r34Py = rule34Py()
#search = r34Py.search(["miruko"], limit=1000, page_id=1)
#print(len(search))

comments = r34Py.get_comments(5992731)
print(comments)

post = r34Py.get_post(5992731)
print(post.image)

icame = r34Py.icame()
print(icame)
