import matplotlib.pyplot as plt
import random

x = []
y = []

for a in range(0,3000):
   i = random.uniform(0,1000)
   j = random.uniform(0,1000)

   x.append(i)
   y.append(j)
   

for item in range(len(x)):
    plt.plot(x[item],y[item], c="cyan", marker=".")
    plt.plot(x[item]-10,y[item], c="red", marker=".")

plt.show()

for item in range(len(x)):
    plt.plot(x[item],y[item], c="cyan", marker=".")
    plt.plot(x[item]-20,y[item], c="red", marker=".")

plt.show()



