from app import db 

class BlogPost(db.Model):

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

    def __init__(self, title, desccription):
        self.title = title
        self.description = desccription

    def __repr__(self):
        return '<{}>'.format(self.title)