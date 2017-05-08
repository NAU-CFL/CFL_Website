from flask import render_template, request, Blueprint, jsonify
from .forms import InputForm
from .stock_visual import plot_data

script = Blueprint('script', __name__,
                    url_prefix='/script',
                    template_folder='templates',
                    static_folder='static',
                    static_url_path='/scripts/static')


@script.route('/stock_plot', methods=['GET','POST'])
def stock_plot():
    form = InputForm()
    _ticker = form.ticker_symbol.data
    _start = form.start.data
    _end = form.end.data

    plot_data(_ticker, _start, _end)
    html = render_template( 'embed.html',
            plot_script=script,
            plot_div=div,
            js_resources=js_resources,
            css_resources=css_resources,
            _ticker=_ticker,
            _start=_start,
            _end=_end
        )
    return encode_utf8(html)
