import requests
from bs4 import BeautifulSoup
import urllib.parse as urlparse
from urllib.parse import parse_qs
import random


class rule34Py(Exception):
    """rule34.xxx API wraper
    """

    def __init__(self):

        self.__init = True
        self.__base_url = "https://rule34.xxx/"
        self.__urls = {
            'search': 'index.php?page=dapi&s=post&q=index&limit=#LIMIT#&tags=#TAGS#',
            'comments': 'index.php?page=dapi&s=comment&q=index&post_id=#POST_ID#',
            # &uname=#USERNAME# &id=#USERID#
            'user_search': 'index.php?page=account&s=profile',
            'user_favorites': 'index.php?page=favorites&s=view&id=#USR_ID#',
            'get_post': 'index.php?page=dapi&s=post&q=index&id=#POST_ID#',
            'icameout': 'icameout.php',
            'random': 'index.php?page=post&s=random'
        }
        self._headers = {
            "User-Agent": f"Mozilla/5.0 (compatible; rule34Py/1.0)"
        }

    def search(self, tags: list, page_id: int = None, limit: int = 100):
        """Search for posts

        Args:
            tags (list): Search tags
            page_id (int, optional): Page ID
            limit (int, optional): Limit for Posts. Max 100.

        Returns:
            list: Posts result list

        Tags Cheatsheet: https://rule34.xxx/index.php?page=tags&s=list
        """

        if(limit < 0):
            raise Exception('the minimum value for "limit" is 0')
            return
        elif(limit > 100):
            raise Exception('the maximium value for "limit" is 100')
            return

        url = self.__urls['search'].replace(
            '#LIMIT#', str(100 if limit > 100 else limit))
        url = url.replace('#TAGS#', '+'.join(tags))
        if page_id != None:
            url += "&pid=" + str(page_id)

        req = requests.get(
            self.__base_url + url, headers=self._headers)

        xml_string = req.content.decode()
        xml_string = xml_string.replace(':<', '')
        xml_string = xml_string.strip()

        posts = []

        bfsPosts = BeautifulSoup(xml_string, features="xml")
        xmlPosts = bfsPosts.posts.findAll('post')
        postCount = bfsPosts.posts['count']
        
        # Add post result count to array (first item)
        if(limit < int(postCount)):
            posts.append(int(limit))
        else:
            posts.append(int(postCount))

        if int(len(xmlPosts) <= 0 or bfsPosts.posts.attrs['count']) <= 0:
            return []

        for post in xmlPosts:
            post_atrr = dict(post.attrs)

            post_id = int(post_atrr[u'id'])
            post_score = int(post_atrr[u'score'])
            post_tags = post_atrr[u'tags'].strip().split(" ")
            post_rating = post_atrr[u'rating']
            creator_id = int(post_atrr[u'creator_id'])
            created_at = post_atrr[u'created_at']
            source = post_atrr[u'source']
            has_notes = True if post_atrr[u'has_notes'] == "true" else False
            has_comments = post_atrr[u'has_comments']
            img_sample_url = post_atrr[u'sample_url']
            img_file_url = post_atrr[u'file_url']
            img_preview_url = post_atrr[u'preview_url']

            post = {
                "id": post_id,
                "score": post_score,
                "rating": post_rating,
                "creator_id": creator_id,
                "created_at": created_at,
                "source": source,
                "has_notes": has_notes,
                "tags": post_tags,
                "img_sample_url": img_sample_url,
                "img_file_url": img_file_url,
                "img_preview_url": img_preview_url
            }

            posts.append(post)

        return posts

    def getComments(self, post_id: int):
        """Get Comments from a Post

        Args:
            post_id (int): Id of Post

        Returns:
            list: Comment resulst list
        """

        url = self.__urls['comments'].replace('#POST_ID#', str(post_id))
        req = requests.get(
            self.__base_url + url, headers=self._headers)

        xml_string = req.content.decode()
        xml_string = xml_string.replace(':<', '')
        xml_string = xml_string.strip()

        comments = []

        bfsComments = BeautifulSoup(xml_string, features="xml")
        xmlComments = bfsComments.comments.findAll('comment')

        if int(len(xmlComments)) <= 0:
            return []

        for comment in xmlComments:
            comment_attr = dict(comment.attrs)

            comment_id = int(comment_attr['id'])
            creator_id = int(comment_attr['creator_id'])
            created_at = comment_attr['created_at']
            creator_name = comment_attr['creator']
            content = comment_attr['body']

            comment = {
                "id": comment_id,
                "creator_id": creator_id,
                "created_at": created_at,
                "creator": {
                    "name": creator_name,
                    "id": creator_id
                },
                "content": content
            }

            comments.append(comment)

        return comments

    def __getAccount(self, identifier):
        search_type = ""

        raise Exception('under construction!')
        return
        if type(identifier) == int or identifier.isdigit():
            search_type = f"&id={identifier}"
        elif type(identifier) == str:
            search_type = f"&uname={identifier}"
        else:
            raise Exception('identifier must be int or string!')

        url = self.__urls['user_search'] + search_type
        req = requests.get(
            self.__base_url + url, headers=self._headers)

        html_string = req.content.decode()

        user = {

        }

        soup = BeautifulSoup(html_string, 'lxml')
        print(soup.find("div", {'id': 'content'}).prettify())

        return search_type

    def getPost(self, post_id: int):
        """Get Post by Id

        Args:
            id (int): Post Id

        Returns:
            dict: Post Object
        """

        url = self.__urls['get_post'].replace('#POST_ID#', str(post_id))
        req = requests.get(self.__base_url + url, headers=self._headers)

        xml_string = req.content.decode()
        xml_string = xml_string.replace(':<', '')
        xml_string = xml_string.strip()

        bfsPosts = BeautifulSoup(xml_string, features="xml")
        xmlPosts = bfsPosts.posts.findAll('post')

        post = xmlPosts[0]

        post_atrr = dict(post.attrs)
        post_id = int(post_atrr[u'id'])
        post_score = int(post_atrr[u'score'])
        post_tags = post_atrr[u'tags'].strip()
        post_rating = post_atrr[u'rating']
        has_children = True if post_atrr[u'has_children'] == 'true' else False
        parent_id = None if post_atrr[u'parent_id'] == "" else int(
            post_atrr[u'parent_id'])
        creator_id = int(post_atrr[u'creator_id'])
        created_at = post_atrr[u'created_at']
        source = post_atrr[u'source']
        has_notes = True if post_atrr[u'has_notes'] == "true" else False
        has_comments = True if post_atrr[u'has_comments'] == "true" else False
        img_sample_url = post_atrr[u'sample_url']
        img_file_url = post_atrr[u'file_url']
        img_preview_url = post_atrr[u'preview_url']
        post_tags = post_tags.replace("\"", "\\\"")
        post_tags = post_tags.split(" ")

        _post = {
            "id": post_id,
            "score": post_score,
            "rating": post_rating,
            "creator_id": creator_id,
            "created_at": created_at,
            "source": source,
            "has_notes": has_notes,
            "tags": post_tags,
            "img_sample_url": img_sample_url,
            "img_file_url": img_file_url,
            "img_preview_url": img_preview_url,
            "has_children": has_children,
            "parent_id": parent_id,
            "has_comments": has_comments
        }

        return _post

    def getFavorites(self, user_id: int, id_only: bool = False):
        """Get Favorites from a user

        Args:
            user_id (int): User ID
            id_only (bool, optional): Specifies whether only Post IDs(True) or Post objects(False) are returned (faster if set to true). Defaults to False.

        Returns:
            [type]: [description]
        """

        url = self.__urls['user_favorites'].replace('#USR_ID#', str(user_id))
        req = requests.get(self.__base_url + url, headers=self._headers)
        html_string = req.content.decode()

        soup = BeautifulSoup(html_string, 'html.parser')

        favorites = []

        for span_tag in soup.select('span[class*="thumb"]'):
            if span_tag['class'][0] != "thumb":
                continue

            a = span_tag.select('a')[0]
            post_id = int(a['id'][1:])

            if id_only:
                favorites.append(post_id)
            elif not id_only:
                favorites.append(self.getPost(post_id))

        return favorites

    def iCameList(self):
        """Gets Top 100 came-on characters
        """

        req = requests.get(self.__base_url +
                           self.__urls['icameout'], headers=self._headers)
        html_string = req.content.decode()

        soup = BeautifulSoup(html_string, 'html.parser')
        soup.unicode
        rows = soup.find("table", border=1).find("tbody").find_all("tr")

        came_on_characters = []

        for row in rows:
            if row == None:
                continue

            a = row.select('td > a', href=True)[0]  # .get_text(strip=True)
            count = row.select('td')[1].get_text(strip=True)

            came_on_characters.append({
                "tag": a.get_text(strip=True),
                "icame_count": int(count),
                "tag_url": a["href"]
            })

        return came_on_characters

    def random(self, tags: list = None):
        """Gets a random Post

        Args:
            tags (list, optional): Tag list

        Returns:
            dict: Returns a Post object
        """

        if tags != None:
            search_raw = self.search(tags)
            rand_num = random.randint(0, search_raw[0])

            while(rand_num == 0):
                rand_num = random.randint(0, search_raw[0])
            else:
                return self.getPost(search_raw[rand_num]['id'])
        
        else:
            response = requests.get(self.__base_url + self.__urls['random'])
            parsed = urlparse.urlparse(response.url)
            random_post_id = parse_qs(parsed.query)['id'][0]

            return self.getPost(random_post_id)


