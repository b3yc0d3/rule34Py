from rule34Py import rule34Py, version
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
result_tagmap = r34Py.tagmap()

# Stats
result_topTaggers = r34Py.stats.top_taggers()
result_topCommenters = r34Py.stats.top_commenters()
result_topForumPosters = r34Py.stats.top_forum_posters()
result_topImagePosters = r34Py.stats.top_image_posters()
result_topNoteEditors = r34Py.stats.top_note_editors()
result_topFavorites = r34Py.stats.top_favorites()

print(result_random.id)
print(result_random.image)

print(result_icame[0].character_name) # returns the character name of the first item

print(result_tagmap[0].tagname)