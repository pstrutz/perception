import matplotlib.pyplot as plt
import random


def rds_assist():
   x = []
   y = []

   # generate 3000 random dots and save their coordinates
   for a in range(0,3000):
      i = random.uniform(0,1000)
      j = random.uniform(0,1000)

      x.append(i)
      y.append(j)

   # plot the dots in cyan and red, with a slight offset
   for item in range(len(x)):
       plt.plot(x[item],y[item], c="cyan", marker=".")
       plt.plot(x[item]-10,y[item], c="red", marker=".")

   plt.show()

   # plot the coordinates again, with a larger offset
   for item in range(len(x)):
       plt.plot(x[item],y[item], c="cyan", marker=".")
       plt.plot(x[item]-20,y[item], c="red", marker=".")

   plt.show()



