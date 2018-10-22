'''
  File name: carv.py
  Author: Zach Corse
  Date created: 10.22.2018
'''

'''
  File clarification:
    Aimed to handle finding seams of minimum energy, and seam removal, the algorithm
    shall tackle resizing images when it may be required to remove more than one seam, 
    sequentially and potentially along different directions.
    
    - INPUT I: n × m × 3 matrix representing the input image.
    - INPUT nr: the numbers of rows to be removed from the image.
    - INPUT nc: the numbers of columns to be removed from the image.
    - OUTPUT Ic: (n − nr) × (m − nc) × 3 matrix representing the carved image.
    - OUTPUT T: (nr + 1) × (nc + 1) matrix representing the transport map.
'''

import numpy as np
import matplotlib.pyplot as plt

from cumMinEngVer import cumMinEngVer
from cumMinEngHor import cumMinEngHor
from rmHorSeam import rmHorSeam
from rmVerSeam import rmVerSeam
from genEngMap import genEngMap
import imageio

class Img:
  def __init__(self, I, r, c):
    #self.I = np.array((r, c, 3))
    self.I = np.zeros((r, c, 3))
    self.I = I

def carv(I, nr, nc):

  T = np.zeros((nr + 1, nc + 1))
  img_array = np.empty((nr + 1, nc + 1), dtype = Img)
  img_array[0, 0] = Img(I, I.shape[0], I.shape[1]) # first element

  # first fill in top row of T and img_array
  E_total = 0
  I_copy = np.copy(I)
  for j in range(1, nc + 1, 1):
    e = genEngMap(I_copy)
    Mx, Tbx = cumMinEngVer(e)
    I_copy, E = rmVerSeam(I_copy, Mx, Tbx)
    E_total += E
    T[0, j] = E_total
    #img_array[0, j] = Img(I_copy, I_copy.shape[0], I_copy.shape[1])
    img_array[0, j] = Img(I_copy, I.shape[0], I.shape[1])

  # next fill in left column of T and img_array
  E_total = 0
  I_copy = np.copy(I)
  for i in range(1, nr + 1, 1):
    e = genEngMap(I_copy)
    My, Tby = cumMinEngHor(e)
    I_copy, E = rmHorSeam(I_copy, My, Tby)
    E_total += E
    T[i, 0] = E_total
    #img_array[i, 0] = Img(I_copy, I_copy.shape[0], I_copy.shape[1])
    img_array[i, 0] = Img(I_copy, I.shape[0], I.shape[1])

  # fill in all remaining elements by comparing above and to the left
  for i in range(1, nr + 1, 1):
    for j in range(1, nc + 1, 1):
      # get image above and to the left
      I_up = np.copy(img_array[i - 1, j].I)
      I_left = np.copy(img_array[i, j - 1].I)
      e_up = genEngMap(I_up)
      e_left = genEngMap(I_left)
      My, Tby = cumMinEngHor(e_up)
      Mx, Tbx = cumMinEngVer(e_left)
      I_up, E_up = rmHorSeam(I_up, My, Tby)
      I_left, E_left = rmVerSeam(I_left, Mx, Tbx)

      # compare the cost of removing a row vs column
      # to determine what the mimimal cost of generating this sub-image is
      if(E_up < E_left):
        T[i, j] = T[i - 1, j] + E_up
        #img_array[i, j] = Img(I_up, I_up.shape[0], I_up.shape[1])
        img_array[i, j] = Img(I_up, I.shape[0], I.shape[1])
      else:
        T[i, j] = T[i, j - 1] + E_left
        #img_array[i, j] = Img(I_left, I_left.shape[0], I_left.shape[1])
        img_array[i, j] = Img(I_left, I.shape[0], I.shape[1])

  Ic = img_array[nr, nc].I

  # --uncomment-- for making a gif
  '''
  gif_images = np.empty(nr + nc + 1, dtype = Img)
  gif_images[0] = img_array[nr, nc]

  idx = 1
  i = nr
  j = nc
  while(i > 0 or j > 0):
    # look left
    if(T[i - 1, j] < T[i, j - 1]):
      gif_images[idx] = img_array[i - 1, j]
      i -= 1
    # look up
    else:
      gif_images[idx] = img_array[i, j - 1]
      j -= 1
    idx += 1

  gif_images[nr + nc] = img_array[0, 0]

  res_list = []
  k = nr + nc
  while k >= 0:
    res_list.append(gif_images[k].I[:, :, :])
    k -= 1

  # generate gif file
  imageio.mimsave('./eval_testimg.gif', res_list)

  '''
  
  return Ic, T
