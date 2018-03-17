from mongoengine import *
from model.user import User

class Blog(Document):
    title = StringField(max_length=120, required=True)
    author = ReferenceField(User)
    tag = StringField(max_length=30)
    tab = StringField()
    content = StringField()

class Tag(Document):
    name = StringField()
    tab = StringField()
    chinese = StringField()
    img_url = StringField()
    info = StringField()

class Reply(Document):
    blog = ReferenceField(Blog)
    author = ReferenceField(User)
    content = StringField()

class Collect(Document):
    user = ReferenceField(User)
    blog = ReferenceField(Blog)

def test():
    connect('db2')
    u = Blog(title='test for jobs', author=User.objects(username='a').first(), tab= 'jobs', tag= 'programmer'
             ,content = '找工作')
    print(u)
    print(u.tag)
    u.save()
    pass

def test_search():
    connect('db2')
    for post in Blog.objects:
        for p in post.tags:
            if p == 'a':
                print(post.title)

def test_tag():
    connect('db2')
    t = Tag(
        name='python',
        tab='tech',
        chinese='py',
        img_url='/static/img/python.png',
        info='aaaaaainfo',
            )
    print(t)
    print(t.chinese)
    t.save()

def test_reply():
    connect('db2')
    r = Reply(
        blog=Blog.objects(title='test').first(),
        author=User.objects(username='a').first(),
        content='能找到'
    )
    print(r.blog, r.author, r.content)
    r.save()

def test_collect():
    connect('db2')
    r = Collect(
        blog=Blog.objects(title='test').first(),
        user=User.objects(username='a').first(),
    )
    print(r.blog, r.user,)
    r.save()

if __name__ == '__main__':
    test_collect()