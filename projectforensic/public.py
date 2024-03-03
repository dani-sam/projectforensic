from flask import *
from database import *

public = Blueprint('public',__name__)




@public.route('/')
def publicHome():
    return render_template('publicHome.html')

@public.route('/home')
def home():
    return render_template('publicHome.html')

@public.route('/login',methods=['get','post'])

def login():
    if 'submit' in request.form :
        username = request.form['username']
        password = request.form['password']

        q = "select * from login where username = '%s' and password = '%s' "%(username,password)
        res = select(q)

        if res:
            session['login_id'] = res[0]['login_id'] #reptition avishyam ola line aanu
            if res[0]['usertype'] == 'admin':
                return """
                    <script>
                    alert('login successful');
                    window.location='/admin_home'
                    </script>"""
            
            elif res[0]['usertype'] == 'user':
                q2 = "select * from user where login_id = '%s' "%(session['login_id'])
                res1 = select(q2)
                if res1:
                    session['user_id'] = res1[0]['user_id']

                    return """
                    <script>
                    alert('login successful');
                    window.location='user_home'
                    </script>"""
                
            elif res[0]['usertype'] == 'police':
                q2 = "select * from police where login_id = '%s' "%(session['login_id'])
                res1 = select(q2)
                if res1:
                    session['police_id'] = res1[0]['police_id']

                    return """
                    <script>
                    alert('login successful');
                    window.location='police_home'
                    </script>"""
            
            elif res[0]['usertype'] == 'staff':
                q2 = "select * from staff where login_id = '%s' "%(session['login_id'])
                res1 = select(q2)
                if res1:
                    session['staff_id'] = res1[0]['ft_id']

                    return """
                    <script>
                    alert('login successful');
                    window.location='staff_home'
                    </script>"""
            elif res[0]['usertype'] == 'court':
                q2 = "select * from court where login_id = '%s' "%(session['login_id'])
                res1 = select(q2)
                if res1:
                    session['court'] = res1[0]['court_id']

                    return """
                    <script>
                    alert('login successful');
                    window.location='court_home'
                    </script>"""    
            

    return render_template('login.html')