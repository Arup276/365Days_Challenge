import pymongo
from src.database import Database
from src.models.blog import Blog
from src.models.post import Post

Database.initialize()
'''post = Post(blog_id=None,
            content="This is content",
            author='Arup',
            title='This is title',
            )
post.save_to_mongo()
post.from_mongo('2cdb3c23f72a4c0598692a125a242b69')

post = Post.from_mongo('2cdb3c23f72a4c0598692a125a242b69')
print(post)  # or we can query using blog_ib: post = Post.from_blog("blog_id") .print(post)'''

blog = Blog(author="Arup",
            title="This is title",
            description="This is description"
            )
blog.new_post()

blog.save_to_mongo()

from_database = Blog.from_mongo(blog.id)

print(blog.get_posts())

