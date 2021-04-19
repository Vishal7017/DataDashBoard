from worldbankapp import app

from flask import render_template
import pandas as pd
from wrangling_scripts.wrangling import data_wrangling
import plotly.graph_objs as go
import plotly.graph_objs as graph_objs
import plotly, json
data = data_wrangling()

print(data)

country = data[0][0]
x_val = data[0][1]
y_val = data[0][2]

graph_one = [go.Scatter(
    x = data[0][1],
    y = data[0][2],
    mode = 'lines',
    name = country
)]

layout_one = dict(title = 'Change in Hectares Arable Land <br> per Person 1990 to 2015',
                    xaxis = dict(title = 'Year',
                        autotick=False, tick0=1990, dtick=25),
                    yaxis = dict(title='HEctares')
                    )




figures = []
figures.append(dict(data=graph_one,layout=layout_one))

ids = ['figure-{}'.format(i) for i, _ in enumerate(figures)]



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', data_set = data)
     

