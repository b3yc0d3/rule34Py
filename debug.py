from rule34Py import rule34Py
import json
#import random


r34Py = rule34Py()

print(r34Py.version)

result_comments = r34Py.get_comments(4153825)
result_post = r34Py.get_post(4931536)
result_icame = r34Py.icame()
result_search = r34Py.search(["neko"], page_id=2, limit=50)
result_pool = r34Py.get_pool(17509) # or r34Py.get_pool(17509, false)
result_random = r34Py.random_post(["neko"]) # or r34Py.random_post()
result_tag_map = r34Py.tag_map()
result_top_tags = r34Py.top_tags()

print(result_random.id)
print(result_random.image)

print(result_icame[0].character_name, result_icame[0].count) # returns the character name of the first item

print(result_top_tags[0].tagname)
