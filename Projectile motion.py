# Before Run the COde, Do "pip install sympy matplotlib"

from sympy import *
from sympy.abc import *
from sympy import pi
import matplotlib.pyplot as plt

var('y0 v0')
ybeta =  y0 + 1/beta * v0 * (1-exp(-beta*t)) - 1/beta**2 * g * (beta*t - (1 - exp(-beta*t)))
limit(ybeta, beta, 0)

def X(T, th):
    return T * cos(th*pi/180)

def Y(T, th):
    return T * sin(th*pi/180) - 0.5 * T**2

def T1(th):
    return 2 * sin(th*pi/180)

p1 = plot_parametric(
    (X(T, 45), Y(T, 45), (T, 0, T1(45))), 
    (X(T, 44), Y(T, 44), (T, 0, T1(44))), 
    (X(T, 46), Y(T, 46), (T, 0, T1(46))),
    legend=True,
    title="no air resistance"
)

p1[0].line_color="red"
p1[1].line_color="blue"
p1[2].line_color="green"
p1[0].label="θ = 45°"
p1[1].label="θ = 44°"
p1[2].label="θ = 46°"

p1.show()
p1.xlim=(0.998, 1.001)
p1.ylim=(0, 0.002)
p1.axis_center=(0.998, 0)
p1.show()

def x(T, b, th):
    return (1-exp(-b*T))/b*cos(th*pi/180)

def y(T, b, th):
    return (1-exp(-b*T))/b*sin(th*pi/180)-(b*T-(1-exp(-b*T)))/(b**2)

b = 0.5

p3 = plot_parametric(
    (x(T, b, 45), y(T, b, 45)), 
    (x(T, b, 44), y(T, b, 44)), 
    (x(T, b, 46), y(T, b, 46)),
    (T, 0, 3),
    legend=True,
    xlim=(0, 1.1),
    ylim=(0, 0.3),
    title="Air Resistance Exist b = 0.5"
)

p3[0].label="θ = 45°"
p3[1].label="θ = 44°"
p3[2].label="θ = 46°"
p3[0].line_color="red"
p3[1].line_color="blue"
p3[2].line_color="green"

p3.show()
p3.xlim=(0.662, 0.68)
p3.ylim=(0, 0.003)
p3.axis_center=(0.662, 0)
p3.show()

b = 0.5

p4 = plot_parametric(
    (x(T, b, 45), y(T, b, 45)), 
    (x(T, b, 42), y(T, b, 42)), 
    (x(T, b, 41), y(T, b, 41)), 
    (x(T, b, 40), y(T, b, 40)), 
    (x(T, b, 39), y(T, b, 39)), 
    (x(T, b, 38), y(T, b, 38)), 
    (T, 0, 3),
    legend=True,
    xlim=(0, 1.1),
    ylim=(0, 0.3),
    title="Air Resistance Exist b = 0.5",
    show=False
)

p4[0].label="θ = 45°"
p4[1].label="θ = 42°"
p4[2].label="θ = 41°"
p4[3].label="θ = 40°"
p4[4].label="θ = 39°"
p4[5].label="θ = 38°"
p4[0].line_color="red"
p4[1].line_color="blue"
p4[2].line_color="lightblue"
p4[3].line_color="darkblue"
p4[4].line_color="pink"
p4[5].line_color="lightgreen"

p4.xlim=(0.665, 0.682)
p4.ylim=(0, 0.003)
p4.axis_center=(0.665, 0)

p4.show()
