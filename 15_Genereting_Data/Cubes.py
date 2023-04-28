import matplotlib.pyplot as plt

x_values = range(1,5001)
y_values = [x**3 for x in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Oranges,s=4)

ax.axis([0, 5100, 0, 130_000_000_000])

plt.show()