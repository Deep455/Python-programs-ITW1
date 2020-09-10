import matplotlib.pyplot as plt
x=[32,45,67,83,88,95]
y=[3,29,37,55,64,72]

plt.figure(1)
plt.hist(x,y)

plt.figure(2)
plt.bar(x,y)

plt.figure(3)
plt.plot(x,y)

plt.figure(4)
plt.scatter(x,y)

plt.show()