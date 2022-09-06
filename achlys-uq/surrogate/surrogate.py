import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from twinLab import *

from bokeh.layouts import column, row
from bokeh.models import Slider
from bokeh.plotting import ColumnDataSource, figure, curdoc

parameters = pd.read_csv('parameters.csv')
n_samples = parameters.shape[0]

#model_output = []
#for i in range(n_samples):
#    s = pd.read_csv('samples/sample_{}.csv'.format(i))[['temperature', 'desorption_rate']]
#    model_output.append(s)
    
#grid_projection = Linear1dProjection()
#grid, samples_grid = grid_projection.project(model_output)

grid = np.loadtxt('grid.csv')

pipeline = Pipeline.load('pipeline.pickle')

bounds = np.array([(0.7, 1.0), (0.9, 1.3), (1.1, 1.75), (5e-4, 5e-3), (1e-4, 1e-3)])
default_parameters = bounds.mean(axis=1)

mean, stdev = pipeline.predict(default_parameters[np.newaxis,:])
mean = mean.flatten(); stdev = stdev.flatten()

source = ColumnDataSource(data=dict(grid=grid, mean=mean, lower=mean-1.96*stdev, upper=mean+1.96*stdev))

plot = figure(y_range=(0, 1e19), width=400, height=400)

plot.line('grid', 'mean', source=source, line_width=3, line_color='black', line_alpha=0.8)
plot.line('grid', 'lower', source=source, line_width=2, line_color='black', line_dash='dashed', line_alpha=0.5)
plot.line('grid', 'upper', source=source, line_width=2, line_color='black', line_dash='dashed', line_alpha=0.5)

E1_slider = Slider(start=bounds[0,0], end=bounds[0,1], value=default_parameters[0], step=.01, title="E1")
E2_slider = Slider(start=bounds[1,0], end=bounds[1,1], value=default_parameters[1], step=.01, title="E2")
E3_slider = Slider(start=bounds[2,0], end=bounds[2,1], value=default_parameters[2], step=.01, title="E3")
n1_slider = Slider(start=bounds[3,0], end=bounds[3,1], value=default_parameters[3], step=1e-5, title="n1")
n2_slider = Slider(start=bounds[4,0], end=bounds[4,1], value=default_parameters[4], step=1e-5, title="n2")

def callback(attr, old, new):
    
    E1 = E1_slider.value
    E2 = E2_slider.value
    E3 = E3_slider.value
    n1 = n1_slider.value
    n2 = n2_slider.value
    
    parameters = np.array([[E1, E2, E3, n1, n2]])
    mean, stdev = pipeline.predict(parameters)
    mean = mean.flatten(); stdev = stdev.flatten()
    
    source.data = {'grid': grid, 'mean': mean, 'lower': mean - 1.96*stdev, 'upper': mean + 1.96*stdev}

E1_slider.on_change('value_throttled', callback)
E2_slider.on_change('value_throttled', callback)
E3_slider.on_change('value_throttled', callback)
n1_slider.on_change('value_throttled', callback)
n2_slider.on_change('value_throttled', callback)

layout = row(
    plot,
    column(E1_slider, E2_slider, E3_slider, n1_slider, n2_slider),
)

curdoc().add_root(layout)
