'''
  File name: cumMinEngVer.py
  Author: Zach Corse
  Date created: 10.18.2018
'''

'''
  File clarification:
    Computes the cumulative minimum energy over the vertical seam directions.
    
    - INPUT e: n × m matrix representing the energy map.
    - OUTPUT Mx: n × m matrix representing the cumulative minimum energy map along vertical direction.
    - OUTPUT Tbx: n × m matrix representing the backtrack table along vertical direction.
'''

import numpy as np

def cumMinEngVer(e):

  n = e.shape[0]
  m = e.shape[1]

  Mx = np.zeros((n, m))
  Tbx = np.zeros((n, m))
  Mx[0,:] = e[0,:]

  X = np.arange(m)
  Xp = np.clip(X + 1, 0, m - 1)
  Xm = np.clip(X - 1, 0, m - 1)

  for i in range(1,  n):
    # consider element [i - 1, j] first by row
    row_value = np.copy(Mx[i - 1, :])
    row_path = np.zeros(m)

    # compare these values with their right neighbors
    shift_r = Mx[i - 1, Xp]
    check_r = np.less(shift_r, row_value)
    # replace if less
    row_value[check_r] = shift_r[check_r]
    row_path[check_r] = 1

    # compare these values with center's left neighbors
    shift_l = Mx[i - 1, Xm]
    check_l = np.less(shift_l, row_value)
    # replace if less
    row_value[check_l] = shift_l[check_l]
    row_path[check_l] = -1

    # update value and path matrices
    Mx[i, :] = row_value + e[i, :]
    Tbx[i, :] = row_path

  return Mx, Tbx