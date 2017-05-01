from flask import render_template, request, Blueprint, jsonify
from .function import compute
from .model import InputForm

script = Blueprint('script', __name__,
                    url_prefix='/script',
                    template_folder='templates',
                    static_folder='static',
                    static_url_path='/scripts/static')

@script.route('/function_visual', methods=['GET','POST'])
def view_function():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        result = compute(form.A.data, form.b.data,
                         form.w.data, form.T.data)
    else:
        result = None

    return render_template('view_function.html', form=form, result=result)
