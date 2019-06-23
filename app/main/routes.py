from flask import render_template, request, Blueprint
from app.models import Post

main = Blueprint('main', __name__)

@main.route("/")
def root():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=10)
    return render_template('home.html', posts=posts)
