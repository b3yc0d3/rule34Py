from rule34Py import rule34Py
import random


r34 = rule34Py()

search = r34.search(["miruko"], limit=1001, page_id=1)
print(len(search))
