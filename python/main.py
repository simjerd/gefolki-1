#!/usr/bin/python

import numpy as np
from scipy.ndimage import imread
from skimage.io import imsave

from algorithm import GEFolki, EFolki
from tools import wrapData


def demo():
    print("Debut recalage Lidar/Radar")
    radar = imread('../datasets/radar_bandep.png')
    Ilidari = imread('../datasets/lidar_georef.png')

    Iradar = radar[:, :, 0]
    Iradar = Iradar.astype(np.float32)/255
    Ilidar = Ilidari.astype(np.float32)/255

    u, v = EFolki(Iradar, Ilidar, iteration=2, radius=[32, 24, 16, 8], rank=4, levels=5)

    Ilidar_resampled = wrapData(Ilidar, u, v)

    out = (255 * (Ilidar_resampled - Ilidar_resampled.min()) /
           (Ilidar_resampled.max() - Ilidar_resampled.min())).astype(np.uint8)

    imsave('../datasets/lidar_georef_resampled.png', out)

    print("Fin recalage Lidar/Radar \n")

    print("Debut recalage optique/Radar")
    radar = imread('../datasets/radar_bandep.png')
    Ioptique = imread('../datasets/optiquehr_georef.png')

    Iradar = radar[:, :, 0]
    Iradar = Iradar.astype(np.float32)
    Ioptique = Ioptique[:, :, 1]
    Ioptique = Ioptique.astype(np.float32)

    u, v = GEFolki(Iradar, Ioptique, iteration=2, radius=range(32, 4, -4), rank=4, levels=6)

    Ioptique_resampled = wrapData(Ioptique, u, v)

    out = (255 * (Ioptique_resampled - Ioptique_resampled.min()) /
           (Ioptique_resampled.max() - Ioptique_resampled.min())).astype(np.uint8)

    imsave('../datasets/optiquehr_georef_resampled.png', out)

    print("Fin recalage optique/Radar \n")


if __name__ == '__main__':
    demo()
else:
    demo()
