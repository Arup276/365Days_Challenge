from src.database import Database
from src.models.blog import Blog


class Menu(object):
    def __init__(self):
        # check if their have account or not
        # if not then prompt them to create one
        self.user = input("Enter your author name: ")
        self.user_blog = None
        if self._user_has_account():
            print("Welcome back {}.".format(self.user))
        else:
            self._prompt_user_for_account()

    def _user_has_account(self):
        blog = Database.find_one('blogs', {'author': self.user})
        if blog is not None:
            self.user_blog = Blog.from_mongo(blog['id'])  # its a blog object
            return True   # WTF! Problem i faced here
        else:
            return False

    def _prompt_user_for_account(self):
        title = input("Enter a title: ")
        description = input("Enter a discription: ")
        blog = Blog(author=self.user,
                    title=title,
                    description=description,
                    )
        blog.save_to_mongo()
        self.user_blog = blog

    def run_menu(self):
        # user read and write
        # if read:
            # list blog in database
            # allow user to pick one
            # display post
        # if write:
            # check if they have a account or not
            # if have then prompt to write a post
            # else prompt to create a account
        read_write = input("What you want to do Read(R) or Write(W): ")
        if read_write == 'R':
            self._list_blogs()
            self._view_blog()
        elif read_write == 'W':
            self.user_blog.new_post()
        else:
            print("Thanks for visiting my website")

    def _list_blogs(self):
        blogs=Database.find(collection='blogs',
                            query={})  # beacuse we want all blogs
        for blog in blogs:
            print("ID: {}, Ttile: {}, Author: {}".format(blog['id'],blog['title'],blog['author']))

    def _view_blog(self):
        blog_to_see = input("Enter the blog you want to see: ")
        blog = Blog.from_mongo(blog_to_see)
        posts = blog.get_posts()
        for post in posts:
            print("Date: {},Title: {}\n\nContent: {}",format(post['created_date'],post['title'],post['content']))

