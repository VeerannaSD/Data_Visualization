import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec
#Write your code here
'''
create figure of size 8inch width and 6 inch height
add axes to figure of size(1,1,1)
create two data sets t and d
    t=[5,10,15,0,25]
    d=[25,50,75,100,125]
	set following attributes
	title='Time vs Distance Covered'
	xlabel='time (seconds)'
	ylabel='distance (meters)'
	xlim=(0,30)
	ylim=(0,130)
	plot graph with label d-5t 
	Save the graph into scatter.png
'''

def test_my_first_plot():
    fig=plt.figure(figsize=(8,6))
    ax=fig.add_subplot(1,1,1)
    t=[5,10,15,0,25]
    d=[25,50,75,100,125]
    ax.set(title='Time vs Distance Covered',xlabel='time (seconds)',ylabel='distance (meters)',xlim=(0,30),ylim=(0,130))
    plt.plot(t,d,label='d=5t')
    plt.savefig('scatter.png')

if __name__ == "__main__":
    test_my_first_plot()