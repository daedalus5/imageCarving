'''
  File name: cumMinEngHor.py
  Author: Zach Corse
  Date created: 10.19.2018
'''

'''
  File clarification:
    Computes the cumulative minimum energy over the horizontal seam directions.
    
    - INPUT e: n × m matrix representing the energy map.
    - OUTPUT My: n × m matrix representing the cumulative minimum energy map along horizontal direction.
    - OUTPUT Tby: n × m matrix representing the backtrack table along horizontal direction.
'''
## x is rows
## y is columns

import numpy as np

def cumMinEngHor(e):

  n = e.shape[0]
  m = e.shape[1]

  My = np.zeros((n, m))
  Tby = np.zeros((n, m))
  My[:,0] = e[:,0]

  Y = np.arange(n)
  Yp = np.clip(Y + 1, 0, n - 1)
  Ym = np.clip(Y - 1, 0, n - 1)

  for i in range(1,  m):
    # consider element [j, i - 1] first by column
    col_value = np.copy(My[:, i - 1])
    col_path = np.zeros(n)

    # compare these values with the values above them
    shift_up = My[Yp, i - 1]
    check_up = np.less(shift_up, col_value)
    # replace if less
    col_value[check_up] = shift_up[check_up]
    col_path[check_up] = 1

    # compare these values with values below them
    shift_dn = My[Ym, i - 1]
    check_dn = np.less(shift_dn, col_value)
    # replace if less
    col_value[check_dn] = shift_dn[check_dn]
    col_path[check_dn] = -1

    # update value and path matrices
    My[:, i] = col_value + e[:, i]
    Tby[:, i] = col_path

  return My, Tby