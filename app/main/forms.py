from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField,SubmitField
from wtforms.validators import Required


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write a brief bio about you your.',validators = [Required()])
    submit = SubmitField('Save')


    class PitchForm(FlaskForm):
        title = StringField('Title', validators=[Reuired()])
        category = SelectField('Category',choices=['Technology','Technology'])