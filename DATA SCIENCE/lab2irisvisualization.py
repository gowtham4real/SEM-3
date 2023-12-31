# -*- coding: utf-8 -*-
"""LAB2irisvisualization.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HIffgFfDHHd7vdX_A52_FxCX94lMmd-8
"""

import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

iris=sns.load_dataset("iris")

iris.head()

iris.tail()

#histogram(uni)
plt.figure(figsize=(8,6))
sns.histplot(iris['sepal_length'],bins=20,kde=True)
plt.xlabel("sepal length(cm)")
plt.ylabel("frequency")
plt.title("histogram of sepal length")
plt.show()

"""You may find that sepal length follows a somewhat normal distribution. There may be two peaks or modes in the distribution, which could indicate the presence of different species"""

#quartile plot(uni)
plt.figure(figsize=(8,6))
sns.boxplot(x="species",y="sepal_length",data=iris)
plt.xlabel("species")
plt.ylabel("sepal length(cm)")
plt.title("boxplot of sepal length")
plt.show()

"""Setosa may have shorter sepal lengths with no or few outliers. Versicolor and Virginica may have longer sepal lengths, with some outliers."""

#distribution chart(uni)
plt.figure(figsize=(8,6))
sns.kdeplot(iris['sepal_width'],shade=True)
plt.xlabel("sepal width(cm)")
plt.ylabel("density")
plt.title("distribution chart of sepal width")
plt.show()

"""Sepal width may exhibit a roughly normal distribution. There is a peak in the distribution indicating a common sepal width value."""

#scatter plot
plt.figure(figsize=(8,6))
sns.scatterplot(x="sepal_length",y="sepal_width",hue="species",data=iris)
plt.xlabel("sepal length(cm)")
plt.ylabel("sepal width(cm)")
plt.title("scatterplot of sepal length vs sepal width")
plt.show()

"""Setosa species is clustered with shorter sepal lengths and wider sepals. Versicolor and Virginica may have longer sepal lengths with varying sepal widths."""

#scatter plot multiple
plt.figure(figsize=(8,6))
sns.scatterplot(x="petal_length",y="petal_width",hue="species",size="sepal_length",data=iris)
plt.xlabel("petal length(cm)")
plt.ylabel("petal width(cm)")
plt.title("scatterplot of petal length vs petal width coloured by species,sized by special length")
plt.show()

"""Setosa species likely has the smallest petals (short length and width). Virginica tends to have the largest petals. Versicolor is intermediate in terms of petal length and width.

"""

#scatter matrix
sns.set(style="ticks")
sns.pairplot(iris,hue="species",markers=["p","s","D"])

plt.suptitle("scatter matrix",y=1.02)
plt.show()

"""Sepal length and petal length are positively correlated with petal width, especially for Setosa. Setosa is more distinct from the other species in terms of feature combinations."""

#bubble chart
plt.figure(figsize=(8,6))
sns.scatterplot(x="sepal_length",y="sepal_width",hue="species",size="petal_length",data=iris)
plt.xlabel("sepal length(cm)")
plt.ylabel("sepal width(cm)")
plt.title("bubble chart of sepal length vs sepal width coloured by species,sized by petal length")
plt.show()

"""The bubble chart may reinforce the observation of Setosa having shorter sepal lengths and wider sepals. Petal length differentiation may be noticeable."""

#density chart
plt.figure(figsize=(8,6))
sns.kdeplot(x=iris["petal_length"],y=iris["petal_width"],cmap="Blues",shade=True,cbar=True)
plt.xlabel("petal length(cm)")
plt.ylabel("petal width(cm)")
plt.title("density chart of petal length vs petal width")
plt.show()

"""The chart highlight the high density areas for petal length and width. Setosa have a distinct peak for smaller petals."""

#parallel coordinates chart
from pandas.plotting import parallel_coordinates
plt.figure(figsize=(8,6))
sns.set(style="whitegrid")
parallel_coordinates(iris,"species",colormap="viridis")
plt.title("parallel coordinates chart")
plt.show()

"""species differ across all features. Setosa have distinct patterns and shorter feature values compared to other species"""

#deviation chart
feature="sepal_length"
mean_value=iris[feature].mean()
iris["deviation"]=iris[feature]-mean_value
plt.figure(figsize=(8,6))
plt.plot(iris.index,iris["deviation"],marker='o',linestyle='-',color='b')
plt.xlabel("data points")
plt.ylabel(f"feDeviation from mean{feature.capitalize()}(CM)")
plt.title(f"Deviation chart for {feature.capitalize()}")
plt.grid(True)
plt.show()

"""This chart will display how each data point deviates from the mean. we can identify clusters or patterns in the deviation."""

from pandas.plotting import andrews_curves
plt.figure(figsize=(8,6))
sns.set(style="ticks")
andrews_curves(iris,"species",colormap="viridis")
plt.title("andrews curves")
plt.show()

"""Andrews Curves provide a visual representation of the feature combinations for each species. Setosa exhibit the simplest and most distinguishable pattern."""