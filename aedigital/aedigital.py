from flask import Flask


application = Flask(__name__)

@application.route('/')
def blog_home():
    return 'AEDigital home!'
