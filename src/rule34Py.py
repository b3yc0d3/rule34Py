import requests
from bs4 import BeautifulSoup


class rule34Py(Exception):
    """rule34.xxx API wraper
    """

    def __init__(self):

        self.__init = True
        self.__base_url = "https://rule34.xxx/index.php"
        self.__urls = {
            'search': '?page=dapi&s=post&q=index&limit=#LIMIT#&tags=#TAGS#',
            'comments': '?page=dapi&s=comment&q=index&post_id=#POST_ID#',
            'user_search': '?page=account&s=profile',  # &uname=#USERNAME# &id=#USERID#
            'user_favorites': '?page=favorites&s=view&id=#USR_ID#',
            'get_post': '?page=dapi&s=post&q=index&id=#POST_ID#'
        }

    def search(self, tags, limit=100):
        """Search for posts

        Args:
            tags (list): Search tags (cheatsheet: https://rule34.xxx/index.php?page=tags&s=list)
            limit (int, optional): Limit for Posts. Max 100.

        Returns:
            list: Posts result list
        """

        if type(tags) != list:
            raise ValueError('Parameter "tags" must be of type "list"!')

        url = self.__urls['search'].replace(
            '#LIMIT#', str(100 if limit > 100 else limit))
        url = url.replace('#TAGS#', '+'.join(tags))

        req = requests.get(
            self.__base_url + url, headers={"User-Agent": f"Mozilla/5.0 (compatible; rule34Py/1.0)"})

        xml_string = req.content.decode()
        xml_string = xml_string.replace(':<', '')
        xml_string = xml_string.strip()

        posts = []

        bfsPosts = BeautifulSoup(xml_string, features="xml")
        xmlPosts = bfsPosts.posts.findAll('post')

        if int(len(xmlPosts) <= 0 or bfsPosts.posts.attrs['count']) <= 0:
            return []

        for post in xmlPosts:
            post_atrr = dict(post.attrs)

            post_id = post_atrr[u'id']
            post_score = post_atrr[u'score']
            post_tags = post_atrr[u'tags']
            post_rating = post_atrr[u'rating']
            creator_id = post_atrr[u'creator_id']
            created_at = post_atrr[u'created_at']
            source = post_atrr[u'source']
            has_notes = post_atrr[u'has_notes']
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

    def getComments(self, post_id):
        """Get Comments from a Post

        Args:
            post_id (int): Id of Post

        Returns:
            list: Comment resulst list
        """

        url = self.__urls['comments'].replace('#POST_ID#', str(post_id))
        req = requests.get(
            self.__base_url + url, headers={"User-Agent": f"Mozilla/5.0 (compatible; rule34Py/1.0)"})

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

            comment_id = comment_attr['id']
            creator_id = comment_attr['creator_id']
            created_at = comment_attr['created_at']
            creator_name = comment_attr['creator']
            creator_id = comment_attr['creator_id']
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

    def getAccount(self, identifier):
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
            self.__base_url + url, headers={"User-Agent": f"Mozilla/5.0 (compatible; rule34Py/1.0)"})

        html_string = req.content.decode()

        user = {

        }

        soup = BeautifulSoup(html_string, 'lxml')
        print(soup.find("div", {'id': 'content'}).prettify())

        return search_type

    def getPost(self, post_id):
        """Get Post by Id

        Args:
            id (int): Post Id

        Returns:
            dict: Post Object
        """

        if not str(post_id).isdigit() or type(post_id) != int:
            raise Exception('Parameter "ID" can only be Digit! (int or str)')
            return

        url = self.__urls['get_post'].replace('#POST_ID#', str(post_id))
        req = requests.get(self.__base_url + url, headers={"User-Agent": f"Mozilla/5.0 (compatible; rule34Py/1.0)"})

        xml_string = req.content.decode()
        xml_string = xml_string.replace(':<', '')
        xml_string = xml_string.strip()

        post_ = []

        bfsPosts = BeautifulSoup(xml_string, features="xml")
        xmlPosts = bfsPosts.posts.findAll('post')

        if int(len(xmlPosts) <= 0 or bfsPosts.posts.attrs['count']) <= 0:
            return []

        for post in xmlPosts:
            post_atrr = dict(post.attrs)

            post_id = post_atrr[u'id']
            post_score =post_atrr[u'score']
            post_tags = post_atrr[u'tags']
            post_rating = post_atrr[u'rating']
            has_children = True if post_atrr[u'has_children'] == 'true' else False
            parent_id = post_atrr[u'parent_id']
            creator_id = post_atrr[u'creator_id']
            created_at = post_atrr[u'created_at']
            source = post_atrr[u'source']
            has_notes = post_atrr[u'has_notes']
            has_comments = post_atrr[u'has_comments']
            img_sample_url = post_atrr[u'sample_url']
            img_file_url = post_atrr[u'file_url']
            img_preview_url = post_atrr[u'preview_url']

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
                "parent_id": parent_id
            }

            post_.append(_post)

        return post_

    def getFavorites(self, user_id, id_only=False):
        """Get Favorites from a user

        Args:
            user_id (int): User ID
            id_only (bool, optional): Specifies whether only Post IDs(True) or Post objects(False) are returned (faster if set to true). Defaults to False.

        Returns:
            [type]: [description]
        """

        if str(user_id).isdigit() or type(user_id) == int:

            url = self.__urls['user_favorites'].replace('#USR_ID#', str(user_id))
            req = requests.get(
                self.__base_url + url, headers={"User-Agent": f"Mozilla/5.0 (compatible; rule34Py/1.0)"})
            html_string = req.content.decode()

            soup = BeautifulSoup(html_string, 'html.parser')

            favorites = []

            for span_tag in soup.select('span[class*="thumb"]'):
                if span_tag['class'][0] != "thumb":
                    continue

                a = span_tag.select('a')[0]
                post_id = a['id'][1:]

                if id_only:
                    favorites.append(post_id)
                elif not id_only:
                    favorites.append(self.getPost(post_id))

            return favorites

        else:
            raise Exception('id must be digits only!')
            return
