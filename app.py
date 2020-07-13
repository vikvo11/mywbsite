#import pymongo
#from pymongo import MongoClient
import json
#import pymongo
#from bson import BSON
#from bson import json_util
from flask import Flask, flash, redirect, render_template, request, session, abort,url_for,logging,Markup,jsonify,Response #For work with HTTP and templates
import requests # For HTTP requests
from data import source,header,mob_menu,menu,block2,carousel_items,carousel_items_bottles,cart_items,cart_items_bottles,type_index,type_index_bottles,type_index_shablon,type_index_examples,shopwindow_items
import json
from jinja2 import Template

from flask_wtf import FlaskForm
from wtforms.fields import TextField
from wtforms.fields.html5 import  URLField
from wtforms.validators import DataRequired, URL
from wtforms import Form, BooleanField, StringField, PasswordField, validators

#from functools import wraps # For lock access
#from HTTP_basic_Auth import auths # For lock access

#client = MongoClient("ds141786.mlab.com:41786", username = 'podarkin', password = 'podarkin', authSource = 'heroku_q51pzrtm')
#db = client["heroku_q51pzrtm"]
#bookings_coll = db.bookings

app = Flask(__name__)
app.config['SECRET_KEY'] = 'morkovka18'
#Check if user logged in
#def is_logged_in(f):
#    @wraps(f)
#    def wrap(*args,**kwargs):
#        if 'logged_in' in session:
#            return f(*args,**kwargs)
#        else:
            #flash('Unauthorized, Please login', 'danger')
#            return redirect(url_for('login'))
#    return wrap

#@app.route('/')
#@is_logged_in


class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Name',validators=[DataRequired(message="Enter Your Name Please")])
    testemail = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])

class OrderForm(Form):
    names = StringField('Name', [validators.Length(min=4, max=25),validators.Required(message='Введите текст гравировки')])
    date = StringField('Date', [validators.Length(min=4, max=25),validators.Required(message='Введите текст')])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email',[validators.Length(min=4, max=25),validators.Required(message='Введите текст гравировки')])
    testemail = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])		
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data,
                    form.password.data)
        db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)
	
def home():
    a=1
    return redirect(url_for('dashbord'))

'''
@app.route('/test1')
def test():
    msg = py()
    return render_template('home.html', articles=msg)
'''
#Logout
#Dashbord
@app.route('/dashbord1',methods=['GET','POST'])
def dashbord1():
    msg = py()
    return render_template('main.html', articles='test')

'''@app.route('/test',methods=['GET','POST'])
def test():
    return app.send_static_file('template/_u_slick_1.html')
'''	
@app.route('/cart',methods=['GET','POST'])
def cart():
    #test=render_template('bottles_u.html',glasses=carousel_items())
    #Template(test).stream(glasses=carousel_items()).dump('static/template/_u_bottles.html')
    return render_template('cart.html', header=header(),source=source(),mob_menu=mob_menu(),menu=menu(),block2=block2(),carousel_items=carousel_items(),cart_items=cart_items())
	
@app.route('/adm_restart',methods=['GET','POST'])
def adm_restart():
    test=render_template('uiview/bottles_u.html',items=carousel_items_bottles(),source=source())
    Template(test).stream(glasses=carousel_items()).dump('static/template/_u_bottles.html')
    test=render_template('uiview/glasses_u.html',items=carousel_items(),source=source())
    Template(test).stream(glasses=carousel_items()).dump('static/template/_u_glasses.html')
    test=render_template('uiview/examples_u.html',items=type_index_examples())
    Template(test).stream(items=type_index_examples()).dump('static/template/_u_examples_1.html')
	
    test=render_template('uiview/product_u.html',shopwindow_items=shopwindow_items(),source=source(),product_title='ВЫБЕРИТЕ СВОЙ БОКАЛ')
    Template(test).stream(items=type_index_examples()).dump('static/template/_u_product_glasses.html')
	
    test=render_template('uiview/product_u.html',shopwindow_items=shopwindow_items(),source=source(),product_title='ВЫБЕРИТЕ СВОЙ ЗАМОЧЕК')
    Template(test).stream(items=type_index_examples()).dump('static/template/_u_product_locks.html')
	
    return 'Restart completed  '+	'<a href="main">ГЛАВНАЯ</a>'
@app.route('/logout')
def logout():
    session.clear()
    flash('You are now logged out','success')
    return redirect(url_for('login'))

#User Login
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        #Get Form fields
        username = request.form['username']
        password_candidate = request.form['password']
        #users=auths()
        if auths(username,password_candidate):
            session['logged_in']= True
            return redirect(url_for('dashbord'))
        else:
                error='Invalid login'
                return render_template('login.html',error=error)

    return render_template('login.html')
@app.route('/start', methods=['POST'])
def get_counts():
    # get url
    data = json.loads(request.data.decode())
    #print(data['data']['subTotal'])
    subTotal=data['data']['subTotal']
    url = '123' #data["tax"]
    if 'http://' not in url[:7]:
        url = 'http://' + url

    return str(subTotal)	
@app.route('/glasses',methods=['GET','POST'])
def glasses():
    item_id = request.args.get('item_id', default = 0, type = int)
    filter = request.args.get('filter', default = '*', type = str)
    grav_id = request.args.get('grav_id', default = 0, type = int)
    form = OrderForm(request.form)
    #form.validate()
    #print(form.errors)
	#/my-route?page=10&filter=test   -> page: 10  filter: 'test'
	
    #item_id=0;
    if request.method == 'POST':
        #Get Form fields
        form.validate()
        print(form.errors)
        #item_id = request.form['item_id']
        #item_img = request.form['item_img']
        #users=auths()
	#print(data.header)
    if grav_id == 0: return render_template('glasses.html',form=form, header=header(),source=source(),mob_menu=mob_menu(),menu=menu(),block2=block2(),shopwindow_items=shopwindow_items(),check_items=cart_items(),item_id=item_id,type_index=type_index(),text='ВЫБЕРИТЕ СВОЮ ГРАВИРОВКУ')
    else: return render_template('glasses.html',form=form, header=header(),source=source(),mob_menu=mob_menu(),menu=menu(),block2=block2(),shopwindow_items=type_index_shablon(),check_items=carousel_items(),item_id=grav_id,type_index=type_index(),text='ВЫБЕРИТЕ СВОЙ БОКАЛ')
@app.route('/bottles',methods=['GET','POST'])
def bottles():
    item_id = request.args.get('item_id', default = 0, type = int)
    filter = request.args.get('filter', default = '*', type = str)
    form = OrderForm(request.form)
	#/my-route?page=10&filter=test   -> page: 10  filter: 'test'
	
    #item_id=0;
    if request.method == 'POST':
        #Get Form fields
        item_id = request.form['item_id']
        item_img = request.form['item_img']
        #users=auths()
	#print(data.header)
    return render_template('bottles.html',form=form, header=header(),source=source(),mob_menu=mob_menu(),menu=menu(),block2=block2(),carousel_items=carousel_items_bottles(),cart_items=cart_items_bottles(),item_id=item_id,type_index=type_index_bottles())

#Dashbord
@app.route('/dashbord',methods=['GET','POST'])
def dashbord():
    msg = py()
    return render_template('index.html', articles='test')

#Dashbord 
@app.route('/main',methods=['GET','POST'])
def main():
    #msg = py()
    #return render_template('index.html')
	
	return render_template('dashbord_lady.html', header=header(),source=source(),mob_menu=mob_menu(),menu=menu(),block2=block2(),carousel_items=carousel_items())
	
@app.route('/main_view_g',methods=['GET','POST'])
def main_view_g():
	#return carousel_items()
	#data = request.get_json()
    return jsonify(carousel_items())
	#return jsonify({'123':'123'})

@app.route('/main_view_gravs',methods=['GET','POST'])
def main_view_gravs():
	#return carousel_items()
	#data = request.get_json()
    return jsonify(type_index_shablon())
	#return jsonify({'123':'123'})
	
@app.route('/main_view_examples',methods=['GET','POST'])
def main_view_examples():
	#return carousel_items()
	#data = request.get_json()
    return jsonify(type_index_examples())
	#return jsonify({'123':'123'})
	
@app.route('/glass/<glasses_id>',methods=['GET','POST'])
def glass(glasses_id):
	#return carousel_items()
	#data = request.get_json()
	glasses=[]
	for item in cart_items():
		if item['id']==int(glasses_id):
			glasses.append(item)
	return jsonify(glasses)
	#return jsonify({'123':'123'})
##ARTISTS THEME
@app.route('/art',methods=['GET','POST'])
def art():
    #msg = py()
    #return render_template('index.html')
	
	return render_template('/art/index.html',block2=block2())

@app.route('/lady',methods=['GET','POST'])
def lady():
    #msg = py()
    #return render_template('index.html')
	
	return render_template('/lady/index.html',block2=block2())

@app.route('/proj/<projname>')
def proj1(projname=None):
    
    return render_template('/art/proj-'+str(projname)+'.html')
def py():
    #client = MongoClient("ds141786.mlab.com:41786", username = 'podarkin', password = 'podarkin', authSource = 'heroku_q51pzrtm')
    #db = client["heroku_q51pzrtm"]
    #bookings_coll = db.bookings
    #doc = bookings_coll.find_one()
    #asa = json.dumps(doc, sort_keys=True, indent=4, default=json_util.default)
    #docs = bookings_coll.find()
    #id = docs[0]['name']
    #return docs
	return None

def main():
    #doc = bookings_coll.find_one()


    pass
   # a = [x for x in bookings_coll.find()]


if __name__ == '__main__':
	app.run(debug=True)
    #main()
