
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
    im_name = "landscape.jpg"

    im_path = os.path.join(folder, im_name)
    img_in = np.array(Image.open(im_path).convert('RGB')) 

    img_out, T = carv(img_in, 30, 30)

    # --uncomment-- for making a single image

    fig, axes = plt.subplots(1, 2, gridspec_kw = {'width_ratios':[img_in.shape[1], img_out.shape[1]]})
    axes[0].imshow(img_in / 255.0)
    axes[0].axis('off')
    axes[0].set_title('Image In : [' + str(img_in.shape[0]) + ', ' + str(img_in.shape[1]) + ']')

    axes[1].imshow(img_out / 255.0)
    axes[1].axis('off')
    axes[1].set_title('Image Out : [' + str(img_out.shape[0]) + ', ' + str(img_out.shape[1]) + ']')

    fig.tight_layout()
    fig.savefig("wall_carved.jpg")

if __name__ == "__main__":
    main()
