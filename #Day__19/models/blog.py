import datetime
import uuid

from src.database import Database
from src.models.post import Post


class Blog(object):
    def __init__(self, author, title, description, id = None):
        self.author = author
        self.title = title
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id

    def new_post(self):
        title = input("Enter new post title: ")
        content = input("Enter post content: ")
        date = input("Enter date(DDMMYY) or leave it for today: ")
        if date == "":
            date = datetime.datetime.utcnow()
        else:
            date = datetime.datetime.strptime(date, "%d%m%Y")
        post = Post(blog_id=self.id,  # this is blog id in which the post is created
                    title = title,
                    author=self.author,
                    content=content,
                    date = date)
        post.save_to_mongo()

    def get_posts(self):
        return Post.from_blog(self.id)

    def save_to_mongo(self):
        Database.insert(collection='blogs',
                        data=self.json())

    def json(self):
        return {
            'author': self.author,
            'title': self.title,
            'description': self.description,
            'id': self.id
        }

    @classmethod  # Because we not gonna have object of this class so we have to pass id.
    def from_mongo(cls, id):  # for removing self we have to make it staticmethod
        blog_data = Database.find_one(collection='blogs',
                                  query = {'id': id})
        # return blog_data : this will only return the json data then we will not able to call from-mongo methods
        return cls(author=blog_data['author'],
                   title=blog_data['title'],
                   description=blog_data['description'],
                   id = blog_data['id'])  # and from the we call from_mongo
