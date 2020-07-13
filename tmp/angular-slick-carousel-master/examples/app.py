
import json

from flask import Flask, flash, redirect, render_template, request, session, abort,url_for,logging,Markup,jsonify #For work with HTTP and templates
import requests # For HTTP requests


app = Flask(__name__)

def home():
    a=1
    return redirect(url_for('dashbord'))

'''
@app.route('/test1')
def test():
    msg = py()
    return render_template('home.html', articles=msg)
'''


#Dashbord 
@app.route('/main',methods=['GET','POST'])
def main():
    #msg = py()
    #return render_template('index.html')
	
	return render_template('index.html')
	
	
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
