from flask_wtf import Form
from wtforms import TextAreaField
from wtforms.validators import DataRequired

class GatherConfigs(Form):
    configuration = TextAreaField('configuration', validators=[DataRequired()])
