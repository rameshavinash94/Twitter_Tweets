from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,SelectField
from wtforms.validators import DataRequired,length

class PostForm(FlaskForm):
	textbox = TextAreaField('Enter the text to tweet',validators=[DataRequired(),length(max=200)])
	Post = SubmitField('Post')
	View= SubmitField('View')
	Delete=SubmitField('Delete')
	Dropdown=SelectField('no.of.tweets to view',choices=['1','2','3','4','5','All'])