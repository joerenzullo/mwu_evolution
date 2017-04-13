from matplotlib import pyplot as plt
import numpy as np

with open('output', 'r') as in_file:
    data = in_file.readlines()
    for i in range(len(data)):
        if i % 1000 == 0:
            items = data[i].split()
            intensity = []
            for item in items:
                intensity.append(float(item.strip('[,]')))
            intensity = np.array(intensity)
            intensity = intensity.reshape((1, 31))
            print(intensity)
            print(intensity.shape)

            plt.imshow(intensity, cmap='gist_heat', interpolation='nearest', vmin=0, vmax=0.1)
            plt.colorbar()
            plt.savefig(filename=str(int(i / 1000)).zfill(3) + '.svg')
            plt.clf()
