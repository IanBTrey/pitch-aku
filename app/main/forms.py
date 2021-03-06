from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField,ValidationError
from wtforms.validators import Required,Email,EqualTo
from ..models import User,Pitch,Comment,Upvote,Downvote

class UpdateProfile(FlaskForm):
    bio = TextAreaField('who are you mate?',validators=[Required()])
    submit=SubmitField("Submit")

class PitchForm(FlaskForm):
    Category_id=SelectField("Select Category :", choices=[('c','select'),('AI','Artifitial Intelegence'),('R','Robotics'),('D','Drones'),('IOT','IoT'),('D','Data Science')])
    pitch=TextAreaField("In about 200 words post your pitch",validators=[Required()])
    submit=SubmitField("Add your pitch mate")

class CommentForm(FlaskForm):
    comment=TextAreaField("post your comments",validators=[Required()])
    submit=SubmitField("Add your comments mate")
