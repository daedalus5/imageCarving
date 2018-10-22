'''
  File name: rmVerSeam.py
  Author: Zach Corse
  Date created: 10.19.2018
'''

'''
  File clarification:
    Removes vertical seams. You should identify the pixel from My from which 
    you should begin backtracking in order to identify pixels for removal, and 
    remove those pixels from the input image. 
    
    - INPUT I: n × m × 3 matrix representing the input image.
    - INPUT Mx: n × m matrix representing the cumulative minimum energy map along vertical direction.
    - INPUT Tbx: n × m matrix representing the backtrack table along vertical direction.
    - OUTPUT Ix: n × (m - 1) × 3 matrix representing the image with the row removed.
    - OUTPUT E: the cost of seam removal.
'''

import numpy as np

def rmVerSeam(I, Mx, Tbx):
  
  n = I.shape[0]
  m = I.shape[1]

  last_row = Mx[n - 1, :]
  min_col = np.argmin(last_row)
  E = Mx[n - 1, min_col]

  Ix = np.zeros((n, m - 1, 3))

  for i in range(n - 1, -1, -1):
    # get R, G, B channels
    row_R = np.copy(I[i, :, 0])
    row_G = np.copy(I[i, :, 1])
    row_B = np.copy(I[i, :, 2])

    # delete value at path
    row_R = np.delete(row_R, min_col)
    row_G = np.delete(row_G, min_col)
    row_B = np.delete(row_B, min_col)

    # update path column
    min_col += int(Tbx[i, min_col])

    # copy row to reduced image
    Ix[i, :, 0] = row_R
    Ix[i, :, 1] = row_G
    Ix[i, :, 2] = row_B

  return Ix, E
