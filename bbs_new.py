from flask import Flask, render_template, request
from model.blog import Blog, Tag
from route.wen import w
from route.member import m
from route.my import my
from mongoengine import *
from model.blog import Reply


connect('db2')
app = Flask(__name__)
app.register_blueprint(w, url_prefix='/wen')
app.register_blueprint(m, url_prefix='/member')
app.register_blueprint(my, url_prefix='/my')

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'abc'
'''
这里是所有路由视图的汇总
要尽可能的去解耦
利用blueprint 把 所有视图分解开
暂时分两个板块，技术和城市
'''


@app.route('/')
def index():
    blog_list, tags = [], []
    if request.args:
        s = request.args['tab']
    else:
        s = 'tech'
    for blog in Blog.objects:
        if blog.tab == s:
            c = Reply.objects(blog=blog.id).count()
            blog_list.append([blog, c])
    for tag in Tag.objects:
        if tag.tab == s:
            tags.append(tag)

    return render_template('index.html',
                           blog_list=blog_list,
                           tags=tags,

                           )


if __name__ == '__main__':
    app.run()
