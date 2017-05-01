from flask import render_template, request, Blueprint, jsonify
from .stock_visual import plot_data
from .forms import InputForm

script = Blueprint('script', __name__,
                    url_prefix='/script',
                    template_folder='templates',
                    static_folder='static',
                    static_url_path='/scripts/static')

@script.route('/stock_plot', methods=['GET','POST'])
def stock_plot():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        result = compute(form.A.data, form.b.data,
                         form.w.data, form.T.data)
    else:
        result = None
    return render_template('graph.html', script=script, div=div)
