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

m = Blueprint('member', __name__,
                        template_folder= 'templates/member')



@m.route('/register')
def register():
    return render_template('member/register.html')


@m.route('/login', methods=['GET', 'POST'])
def login():    #登录
    if request.method == 'POST':
        print(request.form)
        n = request.form.get('username')
        p = request.form.get('password')
        u = User.objects(username=n).first()
        if u.password == p:
            session['user'] = u.username
            session['img'] = u.img_url
            print('成功登录')
        else:
            print('登录失败')
        return redirect(url_for('index'))
    return render_template('member/login.html')


@m.route('/signup', methods=['POST'])
def signup():   #注册
    print(request.form)
    if request.method == 'POST':
        n = request.form.get('username')
        p = request.form.get('password')
        for u in  User.objects():
            if u.password == p:
                session['user'] = u.username
            else:
                return ''
    return '注册成功'


@m.route('/user/<name>')
def user(name):
    u = User.objects(username=name).first()
    blog = [b for b in Blog.objects(author=u)]
    return render_template('member/user.html',
                           user=u,
                           blog_list=blog
                           )

@m.route('/logout')
def logout():    #登录
    session.pop('user')
    return redirect(url_for('index'))
