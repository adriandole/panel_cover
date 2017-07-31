import numpy as np
from skimage import color
from skimage.io import imread


def algorithm(image: np.ndarray, mask) -> float:
    im = color.rgb2grey(image)
    im = im[mask]
    return (np.sum(im > 0.8) / np.sum(mask)) / 0.887
