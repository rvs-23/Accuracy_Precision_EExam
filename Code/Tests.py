#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
This file contains some test code to figure out 
the details of the animation.
"""

%%time

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from IPython.display import HTML


# In[2]:


plt.style.use('fivethirtyeight')


# In[3]:


fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = ax.plot([], [], 'k+')

def init_func():
    ax.clear()
    ax.set(xlim=(-0.5,0.5), ylim=(-0.5,0.5), title='Accuracy Precision')
    ax.scatter(0, 0, s= 40000, color='green', edgecolor='black', alpha=0.5, linewidth=1)
    ax.scatter(0, 0, s= 20000, color='royalblue', edgecolor='black', alpha=0.5, linewidth=1)
    ax.scatter(0, 0, s= 5000, color='yellow', edgecolor='black', alpha=0.5, linewidth=1.5)
    return ln,

def animate(frame):
    xdata.append(0+frame/50)
    ydata.append(0+frame/50)
    ax.plot(xdata, ydata, 'k+')
    return ln,

ani = FuncAnimation(fig, animate, frames=10,
                    init_func=init_func, interval=500, blit=True)
plt.close()
HTML(ani.to_html5_video())


# In[4]:


fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = ax.plot([], [], 'kX')

def init():
    ax.set(xlim=(-0.5,0.5), ylim=(-0.5,0.5))
    ax.set_title('Accuracy Precision', fontsize=20)
    ax.scatter(0, 0, s= 40000, color='royalblue', edgecolor='black', alpha=0.5, linewidth=1)
    ax.scatter(0, 0, s= 20000, color='whitesmoke', edgecolor='black', alpha=0.8, linewidth=0.75)
    ax.scatter(0, 0, s= 5000, color='royalblue', edgecolor='black', alpha=0.75, linewidth=1.25)
    return ln,

prec_x = [0.18, 0.20, 0.22, 0.21, 0.19, 0.20]
prec_y = [0.2, 0.19, 0.2, 0.215, 0.21, 0.20]

def animate(frame):
    
    xdata.append(prec_x[frame]-0.2)
    ydata.append(prec_y[frame]-0.2)
        
    ln.set_data(xdata, ydata)
    
    return ln,

ani = FuncAnimation(fig, animate, frames=6,
                    init_func=init, interval=500, blit=True)
plt.close()
HTML(ani.to_html5_video())

