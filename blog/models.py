from google.appengine.ext import db


class Post(db.Model):

    title = db.StringProperty()
    content = db.TextProperty()
    url = db.StringProperty()
    created_on = db.DateProperty()
    posted_on = db.DateProperty()