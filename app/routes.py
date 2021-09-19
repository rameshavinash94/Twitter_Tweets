from app import app
from app.form import PostForm
from flask import render_template,flash,redirect,request
from app.hello import Twitter
import tweepy

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/tweets_post',methods=['GET','POST'])
def Tweet_post():
	form = PostForm()
	text=''
	if request.method == 'POST':
		if request.form['Post']:
			req=request.form
			data=req["textbox"]
			try:
				text=Twitter().create_tweets(data)
			except:
				flash("An exception occurred")
	return render_template('tweets_post.html',form=form,text=text)


@app.route('/tweets_view',methods=['GET','POST'])
def Tweet_view():
	form = PostForm()
	text=[]
	if request.method == 'POST':
		if request.form['View']:
			try:
				text=Twitter().view_tweets(form.Dropdown.data)
			except:
				flash("An exception occurred")
	return render_template('tweets_view.html',form=form,text=text)


#removed delete route
