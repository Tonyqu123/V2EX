from flask import (Blueprint,
                   render_template,
                   abort,
                   redirect,
                   url_for,
                   session,
                   request,
                   )
from model.blog import Tag, Blog
from model.blog import Reply
from model.user import User
from mongoengine import connect

w = Blueprint('wen', __name__,
                        template_folder= 'templates/wen')


@w.route('/<name>')
def index(name):
    t = Tag.objects(name=name).first()
    blog_list = [b for b in Blog.objects(tag=t.name)]
    return render_template('wen/wen.html',
                           tag=t,
                           blog_list=blog_list)


@w.route('/blog/<id>', methods=['POST', 'GET'])
def blog(id):
    if request.method == 'POST':
        content = request.form.get('content')
        user = session['user']
        create_reply(content, id, user)
        return redirect(url_for('.blog', id=id))
    reply = []
    for r in Reply.objects(blog=id):
        reply.append(r)
    b = Blog.objects(id=id).first()
    return render_template('wen/blog.html',
                           reply=reply,
                           blog=b,
                           )

@w.route('/new')
def new():
    if session['user']:
        return render_template('wen/edit.html')



@w.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        author = session['user']
        create_new_blog(title, content, author)
        return redirect(url_for('member.user', name=author))
    abort(404)


def create_new_blog(t, c, a):
    connect('db2')
    author = User.objects(username=a).first()
    u = Blog(title=t, author=author, tab='tech', tag='programmer'
             , content=c)
    u.save()

def create_reply(content, id, user):
    connect('db2')
    author = User.objects(username=user).first()
    blog = Blog.objects(id=id).first()
    r = Reply(content=content, author=author, blog=blog)
    r.save()