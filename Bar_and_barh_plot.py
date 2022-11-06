import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec
#Write your code here
#Task 1
def test_barplot_of_iris_sepal_length():
    
    fig=plt.figure(figsize=(8,6))
    ax=fig.add_subplot(111)
    species=['setosa','versicolor','viriginica']
    index=[0.2,1.2,2.2]
    sepal_len=[5.01,5.94,6.59]
    ax.set(title='Mean Sepal Length of Iris Species',
          xlabel='Species',
          ylabel='Sepal Lenght(cm)',
          xlim=(0,3),
          ylim=(0,7))
    ax.set_xticks([0.45,1.45,2.45])
    ax.set_xticklabels(species)
    ax.bar(index,sepal_len,width=0.5,color='red',edgecolor='black')
    fig.savefig('bar_iris_sepal.png')
    
#Task 2
def test_barplot_of_iris_measurements():
    fig=plt.figure(figsize=(8,6))
    ax=fig.add_subplot(111)
    sepal_len=[5.01,5.94,6.59]
    sepal_wd=[3.42,2.77,2.97]
    petal_len=[1.46,4.26,5,55]
    petal_wd=[0.24,1.33,2.03]
    species=['setosa','versicolor','viriginica']
    species_index1=[0.7,1.7,2.7]
    species_index2=[0.9,1.9,2.9]
    species_index3=[1.1,2.1,3.1]
    species_index4=[1.3,2.3,3.3]
    ax.set(title='Mean Measurements of Iris Species',
          xlabel='Species',
          ylabel='Iris Measurement (cm)',
          xlim=(0.5,3.7),
          ylim=(0,10),
          xticks=[1.1,2.1,3.1],
          xticklabels=species)
    ax.bar(species_index1,sepal_len,
           color='c',
           edgecolor='black',
           width=0.2,
           label='Sepal Length')
    ax.bar(species_index2,sepal_wd,
           color='m',
           edgecolor='black',
           width=0.2,
           label='Sepal_Width')
    ax.bar(species_index3,sepal_len,
           color='y',
           edgecolor='black',
           width=0.2,
           label='Petal Length')
    ax.bar(species_index4,petal_wd,
           color='orange',
           edgecolor='black',
           width=0.2,
           label='Petal Width')
    plt.legend()
    plt.savefig('bar_iris_measure.png')

#Task 3
def test_hbarplot_of_iris_petal_length():
    fig=plt.figure(figsize=(12,5))
    ax=fig.add_subplot(111)
    species=['setosa','versicolor','viriginica']
    index=[0.2,1.2,2.2]
    petal_len=[1.46,4.26,5.55]
    
    ax.set(title='Mean Petal Length of Iris Species',
          ylabel='Species',
          xlabel='Petal Length (cm)',
          yticks=[0.45,1.45,2.45],
          yticklabels=species)
    ax.barh(index,petal_len,
           height=0.5,color='c',
           edgecolor='black')
    plt.savefig('bar_iris_petal.png')
#     plt.show()

if __name__ == "__main__":
    test_barplot_of_iris_sepal_length()
    test_barplot_of_iris_measurements()
    test_hbarplot_of_iris_petal_length()