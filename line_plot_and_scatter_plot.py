import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec
from matplotlib.testing.decorators import image_comparison
#Write your code here
#Task 1---------->line plot to draw sinewave
def test_sine_wave_plot():
    fig=plt.figure(figsize=(12,3))
    ax=fig.add_subplot(111)
    t=np.linspace(0.0,2.0,num=200)
    v=np.sin(2.5*np.pi*t)
    ax.set(title='Sine Wave',xlabel='Time (seconds)',ylabel='Voltage (mv)',xlim=(0,2),ylim=(-1,1))
    ax.set_xticks([0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0])
    ax.yticks([-1,0,1])
    plt.grid()
    ax.plot(t,v,color='red',label='sin(t)',linestyle='--')
    plt.legend()
    plt.savefig('sinewave.png')


#Task 2-------->linear, Quadratic and Cubic Eqaution lines plotted
def test_multi_curve_plot():
    fig=plt.figure(figsize=(12,3))
    ax=fig.add_subplot(111)
    x=np.linspace(0.0,5.0,num=20)
    y1=x
    y2=x**2
    y3=x**3
    ax.set(xlabel='X',ylabel='f(x)',title='Linear, Quadratic,and Cubic Equations')
    ax.plot(x,y1,marker='o',label='y=x')
    ax.plot(x,y2,marker='s',label='y=x**2')
    ax.plot(x,y3,marker='v',label='y=x**3')
    plt.legend()
    plt.savefig('multicurve.png')

#Task 3-------------> Scatter plot to plot Cars Sold by Company in year 2017

def test_scatter_plot():
    fig=plt.figure(figsize=(12,3))
    ax=fig.add_subplot(111)
    s=[50,60,55,50,70,65,75,65,80,90,93,95]
    months=[i for i in range(1,13)]
    ax.set(title='Cars Sold by Company \'X\' in 2017',xlabel='Months',ylabel='No. of Cars Sold',xlim=(0,13),ylim=(20,100))
    ax.set_xticks([1,3,5,7,9,11])
    ax.set_xtickslabels(['Jan','Mar','May','Jul','Sep','Nov'])
    ax.scatter(months,s,c='red')
    plt.savefig('scatter.png')
    
if __name__ == "__main__":
    test_sine_wave_plot()
    test_multi_curve_plot()
    test_scatter_plot()
    