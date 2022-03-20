from flaskblog import app
from flaskblog import db
from flaskblog.models import Post
import json

with open('commands/posts.json') as f:
    posts_json = json.load(f)

for post in posts_json:
    post = Post(title=post['title'], content=post['content'], user_id=post['user_id'])
    db.session.add(post)
    db.session.commit()
