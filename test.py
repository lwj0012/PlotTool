__author__ = 'Wenjie'
from Plot.reader import xlsReader, txtReader
from Plot.draw import make_fig, output, draw_hist, draw_stack, draw_line, draw_cdf


datas, legends, xaxiss = xlsReader("/home/liu/Dropbox/ICPP'2016/data-draw.xlsx")

path = "/home/liu/test_pic/"

data = datas['IPC']
legend = legends['IPC']
xaxis = xaxiss['IPC']
fig, ax = make_fig(1)
para = {
    'y_start' : 0.9,
    'y_end': 1.2
}
draw_hist(fig, ax, data, legend, xaxis, 'Normalized IPC', **para)
output(fig, path + 'IPC.pdf')

data = datas['Energy']
legend = legends['Energy']
xaxis = xaxiss['Energy']
fig, ax = make_fig(1)
para = {
    'y_start': 0,
    'y_end': 1
}
draw_hist(fig, ax, data, legend, xaxis, 'Normalized Energy', **para)
output(fig, path + 'Energy.pdf')

data = datas['Access_latency']
legend = legends['Access_latency']
xaxis = xaxiss['Access_latency']
fig, ax = make_fig(1)
para = {
    'y_start' : 0,
    'y_end': 1.1
}
draw_hist(fig, ax, data, legend, xaxis, 'Normalized Access Latency', **para)
output(fig, path + 'Access_latency.pdf')

data = datas['Queue_latency']
legend = legends['Queue_latency']
xaxis = xaxiss['Queue_latency']
fig, ax = make_fig(1)
para = {
    'y_start': 0,
    'y_end': 1.22
}
draw_hist(fig, ax, data, legend, xaxis, 'Normalized Queue Latency', **para)
output(fig, path + 'Queue_latency.pdf')

data = datas['near_far']
legend = legends['near_far']
xaxis = xaxiss['near_far']
fig, ax = make_fig(0)
para = {
    'y_start': 0,
    'y_end': 1,
    'use_percent': 1
}
draw_stack(fig, ax, data, legend, xaxis, '\% of near or far request', **para)
output(fig, path + 'near_far.pdf')

data = datas['PFP']
legend = legends['PFP']
xaxis = xaxiss['PFP']
fig, ax = make_fig(0)
para = {
    'y_start': 1.18,
    'y_end': 1.36
}
draw_line(fig, ax, data, legend, xaxis, 'Average PFP slowdown', **para)
output(fig, path + 'PFP.pdf')


data, legend, xaxiss = txtReader("/home/liu/Macos2014-cbr-rewrite-info")

path = "/home/liu/test_pic/"

fig, ax = make_fig(0)
# draw_cdf(fig, ax, data, legend, xaxiss, 'Average PFP slowdown', {'y_start':0, 'y_end':1, 'use_percent':1})
draw_cdf(fig, ax, data, legend, xaxiss, 'Average PFP slowdown', y_start=0, y_end=1, use_percent=1, lw=1, x_star=0, x_end=250)
output(fig, path + 'cdf.pdf')
