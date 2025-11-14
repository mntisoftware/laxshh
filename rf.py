import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
iris=pd.read_csv(r"C:\Users\MNTI - 12\Documents\pc\Iris.csv")
print(iris)
fig=iris[iris["Species"]=="Iris-setosa"].plot.scatter(x="PetalLengthCm",y="PetalWidthCm",color="green",label="setosa")
iris[iris["Species"]=="Iris-versicolor"].plot.scatter(x="PetalLengthCm",y="PetalWidthCm",color="purple",label="versicolor",ax=fig)
iris[iris["Species"]=="Iris-virginica"].plot.scatter(x="PetalLengthCm",y="PetalWidthCm",color="orange",label="virginica",ax=fig)
fig.set_xlabel("petal_length")
fig.set_ylabel("petal_width")
fig.set_title("petal length and width")
fig=plt.gcf()
fig.set_size_inches(5,5)
plt.show()
