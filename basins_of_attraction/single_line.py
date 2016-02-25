'''
program: single_line.py
created: 2016-02-25 -- 9 CEST
'''


import numpy
import scipy.integrate
import matplotlib.pyplot as plt

from cython_functions import bisection


def separator(x_sep, alpha, beta, s, dt, itmax, tol):
    '''
    Constructs the full separator line.
    '''
    y_sep = numpy.empty_like(x_sep)
    for ix, x in enumerate(x_sep):
        y_sep[ix] = bisection(x, alpha, beta, s, dt, itmax, tol)
    return y_sep


# model parameters
beta = 10.0
s = 0.4
alpha = 0.6
ID = 'beta%.4f_s%.4f_alpha%s' % (beta, s, alpha)

# time parameters
dt = 1e-3
tmax = 20.0
itmax = int(tmax / dt + 0.5)

# parameters for separator line
tol = 1e-3
num_x = 81
x_sep = numpy.linspace(0.0, 1.0, num_x)

# other initializations
fig, ax = plt.subplots(1, 1)
# find separator line
y_sep = separator(x_sep, alpha, beta, s, dt, itmax, tol)
# compute integral under the curve
integ = scipy.integrate.simps(y_sep, x_sep)
print 'integral = %f' % integ

# finalize plot
ax.plot(x_sep, y_sep, 'k-', lw=2)
ax.set_aspect(1)
ax.set_xlabel('$x$', fontsize=18)
ax.set_ylabel('$y$', fontsize=18)
ax.set_title(ID)
ax.set_xlim(0.0, 1.0)
ax.set_ylim(0.0, 1.0)
ax.grid()
plt.title(ID)
plt.show()
