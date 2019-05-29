
class UpdateProfile(FlaskForm):
    bio = TextAreaField('who are you mate?',validators=[Required()])
    submit=SubmitField("Submit")
