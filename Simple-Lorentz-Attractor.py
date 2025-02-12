import matplotlib.pyplot as plt
import numpy as np
from numba import njit, jit
from io import BytesIO
from PIL import Image

num_steps = 5000 
dt = 0.02

imlist = []
dif = np.empty((num_steps + 1, 3))
dif_1 = np.empty((num_steps + 1, 3))
dif_2 = np.empty((num_steps + 1, 3))
dif[0] = [3., 2., 0.]
dif_1[0] = [0., 1., 1.05]
dif_2[0] = [0., 1., 1.05]




@njit
def strange_attractors(sigma, beta, rho, xyz):
    dx = sigma * (xyz[1]-xyz[0])
    dy = xyz[0] * (rho - xyz[2]) - xyz[1]
    dz = (xyz[0] * xyz[1]) - (beta * xyz[2])
    return np.array([dx, dy, dz])

for i in range(num_steps):
    ax = plt.figure(figsize=(6,6)).add_subplot(projection="3d")
    ax.set_axis_off()
    ax.set_title("Lorenz Attractor")
    plt.grid(False)
    ax.plot(dif[i][0],dif[i][1],dif[i][2], "o")
    """ax.plot(dif_1[i][0],dif_1[i][1],dif_1[i][2], "o")
    ax.plot(dif_2[i][0],dif_2[i][1],dif_2[i][2], "o")"""
    ax.plot(*dif.T, color="red", lw=0.5)
    """ax.plot(*dif_1.T, lw=0.5, color="green")
    ax.plot(*dif_2.T, lw=0.5, color="blue")"""
    dif[i+1] = dif[i] + strange_attractors(sigma=2, beta=(8/3), rho=13,xyz=dif[i])*dt
    """dif_1[i+1] = dif_1[i] + strange_attractors(sigma=10, beta=(8/3), rho=15,xyz=dif_1[i])*dt
    dif_2[i+1] = dif_2[i] + strange_attractors(sigma=10, beta=(8/3), rho=16,xyz=dif_2[i])*dt"""
    buf = BytesIO()
    plt.savefig(buf)
    buf.seek(0)
    im = Image.open(buf)
    imlist.append(im)
    #plt.savefig(f"..\images\{i}.png")
    #plt.show()
imlist[0].save('animated.gif', save_all=True, append_images=imlist[1:])


