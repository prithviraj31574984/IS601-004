from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class CreateRoleForm(FlaskForm):
    name = StringField('Role Name', validators=[DataRequired()])
    submit = SubmitField('Create')
