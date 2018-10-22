
import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image

# import functions
from carv import carv

test_energy = np.array([
    [5.5, 8.0, 4.5, 6.0, 3.0, 20.0],
    [13.0, 9.0, 30.0, 27.0, 19.0, 20.0],
    [6.5, 7.0, 6.0, 12.5, 8.0, 20.0],
    [16.0, 24.0, 27.0, 11.0, 13.0, 20.0],
    [3.0, 6.0, 4.5, 8.0, 5.5, 20.0]])

def main():
    folder = ""
    im_name = "wall.jpg"

    im_path = os.path.join(folder, im_name)
    img_in = np.array(Image.open(im_path).convert('RGB')) 

    img_out, T = carv(img_in, 5, 5)
    print(T)
    plt.imshow(img_out / 255.0)
    plt.show()

if __name__ == "__main__":
    main()
