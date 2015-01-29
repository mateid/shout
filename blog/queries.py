from google.appengine.ext import db
from models import Post

def all_posts(page=1, page_size=10):
    query = Post.all()
    query.filter("posted_on !=", "")
    query.order("-posted_on")
    return query.run()
