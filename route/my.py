from flask import (
    Blueprint,
    render_template,
    abort,
    request,
    redirect,
    url_for,
    session,

)
from model.user import User
from model.blog import Blog
from model.blog import Collect
from mongoengine import connect
my = Blueprint('my', __name__,
                        template_folder= 'templates/my')


@my.route('/topics')
def topic():
    if session['user']:
        u_name = session['user']
        user = User.objects(username=u_name).first()
        collect_list = []
        # for c in Collect.objects(user=user):
        #     collect_list.append([c, ])
        collect_list = [ c for c in Collect.objects(user=user)]

        return render_template('my/topics.html',
                               user=user,
                               collect_list= collect_list)
    return redirect(url_for('member.login'))


@my.route('/add_topic',)
def add():
    print('访问到了', request.args)
    if session.get('user') is not None:
        u_name = session['user']
        user = User.objects(username=u_name).first()
        blog = request.args.get('blog')
        create_collect(blog, user)
        print(blog, user)
        return redirect(url_for('member.user', name=session['user']))
    else:
        return redirect(url_for('member.login'))


def create_collect(blog, user):
    print(blog, user)
    connect('db2')
    c = Collect(blog = blog, user = user)
    print(c.blog)
    c.save()