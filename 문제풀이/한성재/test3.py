import matplotlib.pyplot as plt
data = {'Frogs': 30, 'Hogs': 40, 'Dogs': 10, 'Logs': 20}
print("data = ", data)

data = sorted(data.items(), key=lambda x: x[1])
print("sorted data = ", data)
labels = list()
sizes = list()
for item in data:
    labels.append(item[0])
    sizes.append(item[1])
print("labels=", labels)
print("sizes = ", sizes)
explode = (0, 0, 0, 0.1)
ax = plt.axes()
ax.pie(sizes, explode=explode, labels=labels,
       autopct='%.0f%%', shadow=True, startangle=90)
ax.axis('equal')
plt.show()
