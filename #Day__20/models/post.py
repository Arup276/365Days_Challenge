import uuid  # Universal unique identifier
from src.database import Database
import datetime


class Post(object):
    def __init__(self, blog_id, content,  title, author, date = datetime.datetime.utcnow(), id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = date
        self.id = uuid.uuid4().hex if id is None else id # and uuid4() generate random numbers and hex = 32 character string

    def save_to_mongo(self):
        Database.insert(collection = 'posts',
                        data = self.json())

    def json(self):
        return {
            'id': self.id,
            'blog_id': self.blog_id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'created_date': self.created_date
        }

    @classmethod  # now we are not only returning json data also post data
    def from_mongo(cls, id): # given id and return the posts from database
        post_data = Database.find_one(collection='posts', query = {'id': id}) # this id we find
        return cls(blog_id=post_data['blog_id'],  # this is return the object type of post data
                   title=post_data['title'],
                   content=post_data['content'],
                   author=post_data['author'],
                   date=post_data['created_date'],
                   id=post_data['id'])

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='posts', query={'blog_id': id})]  # because its return a pymongo object
