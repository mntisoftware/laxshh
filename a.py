import matplotlib.pyplot as plt
import pandas as pd

iris = pd.read_csv(r"C:\Users\MNTI - 12\Documents\pc\Iris.csv")
print(iris)

fig = iris[iris["Species"] == "Iris-setosa"].plot.scatter(
    x="PetalLengthCm",
    y="PetalWidthCm",
    color="green",
    label="setosa"
)

iris[iris["Species"] == "Iris-versicolor"].plot.scatter(
    x="PetalLengthCm",
    y="PetalWidthCm",
    color="purple",
    label="versicolor",
    ax=fig
)

iris[iris["Species"] == "Iris-virginica"].plot.scatter(
    x="PetalLengthCm",
    y="PetalWidthCm",
    color="orange",
    label="virginica",
    ax=fig
)

fig.set_xlabel("Petal Length (cm)")
fig.set_ylabel("Petal Width (cm)")
fig.set_title("Petal Length vs Petal Width")

plt.gcf().set_size_inches(5, 5)
plt.show()
