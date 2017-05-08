from flask_wtf import Form
from wtforms.validators import Required
from wtforms import TextField, IntegerField, SubmitField

class InputForm(Form):
    ticker_symbol = TextField(
        label='Ticker Symbol', validators=[Required()])
    start = IntegerField(
        label='Start Year', default='', validators=[Required()])
    end = IntegerField(
        label='End Year', default='', validators=[Required()])
    submit = SubmitField('Submit')
