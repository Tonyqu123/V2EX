from mongoengine import *
import time


class User(Document):
    username = StringField(max_length=50)
    password = StringField()
    img_url = StringField()
    ct = StringField()



def test():
    connect('db2')
    u = User(username='a', password='abc', img_url='/static/img/user.png', ct=str(time.time()))
    print(u)
    print(u.username)
    u.save()
    pass

if __name__ == '__main__':
    test()