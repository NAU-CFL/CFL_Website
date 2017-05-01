from wtforms import Form, TextField, validators

class InputForm(Form):
    ticker_symbol = TextField(
        label='Ticker Symbol', validators=[validators.InputRequired()])
    start = TextField(
        label='Start Date', default='', validators=[validators.InputRequired()])
    end = TextField(
        label='End Date', default='', validators=[validators.InputRequired()])
