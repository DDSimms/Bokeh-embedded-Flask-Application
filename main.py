
from flask import Flask, request
from flask import render_template

from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html

app=Flask(__name__)

@app.route('/')
def hello():
    return render_template('WebPage1.html')

@app.route('/',methods=['POST'])
def input_box():
    text = request.form['x_values']
    x_input = text.upper()

    text = request.form['y_values']
    y_input = text.upper()

    x = list(map(int, x_input.split()))
    y = list(map(int, y_input.split()))

    plot = figure()
    plot.circle(x,y)
    fig = file_html(plot, CDN, "my plot")

    return fig


if __name__ == "__main__":
    app.run(host='localhost',debug='TRUE')
