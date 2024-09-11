import matplotlib.pyplot as plt

import data


x_coord = data.x_coord()
print(x_coord)
y_coord = data.y_coord(x_coord)
print(y_coord)


plt.plot(x_coord,y_coord)
plt.show()

