'''
  File name: rmHorSeam.py
  Author: Zach Corse
  Date created: 10.19.2018
'''

'''
  File clarification:
    Removes horizontal seams. You should identify the pixel from My from which 
    you should begin backtracking in order to identify pixels for removal, and 
    remove those pixels from the input image. 
    
    - INPUT I: n × m × 3 matrix representing the input image.
    - INPUT My: n × m matrix representing the cumulative minimum energy map along horizontal direction.
    - INPUT Tby: n × m matrix representing the backtrack table along horizontal direction.
    - OUTPUT Iy: (n − 1) × m × 3 matrix representing the image with the row removed.
    - OUTPUT E: the cost of seam removal.
'''

import numpy as np

def rmHorSeam(I, My, Tby):

  n = I.shape[0]
  m = I.shape[1]

  last_col = My[:, m - 1]
  min_row = np.argmin(last_col)
  E = My[min_row, m - 1]

  Iy = np.zeros((n - 1, m, 3))

  for i in range(m - 1, -1, -1):
    # get R, G, B channels
    col_R = np.copy(I[:, i, 0])
    col_G = np.copy(I[:, i, 1])
    col_B = np.copy(I[:, i, 2])

    # delete value at path
    col_R = np.delete(col_R, min_row)
    col_G = np.delete(col_G, min_row)
    col_B = np.delete(col_B, min_row)

    # update path column
    min_row += int(Tby[min_row, i])

    # copy row to reduced image
    Iy[:, i, 0] = col_R
    Iy[:, i, 1] = col_G
    Iy[:, i, 2] = col_B

  return Iy, E
