'''
program: cython_functions.pyx
author: tc
created: 2016-02-25 -- 9 CEST
'''


cdef extern from "math.h":
    double exp(double)


cdef double get_vx(double x, double y, double alpha, double beta, double s):
    '''
    Returns the x component of the velocity vector.
    '''
    return - x + 1.0 / (1.0 + exp(- beta * (alpha * s - y)))


cdef double get_vy(double x, double y, double alpha, double beta, double s):
    '''
    Returns the y component of the velocity vector.
    '''
    return - y + 1.0 / (1.0 + exp(- beta * ((1.0 - alpha) * s - x)))


def evolution(double x, double y, double alpha, double beta, double s,
              double dt, int itmax):
    '''
    Performs a full evolution, starting from (x, y)
    '''
    cdef int it
    cdef double xold, yold
    xold = x
    yold = y
    for it in range(itmax):
        x = xold + dt * get_vx(xold, yold, alpha, beta, s)
        y = yold + dt * get_vy(xold, yold, alpha, beta, s)
        xold = x
        yold = y
    return x, y


cdef int basin(double x, double y, double alpha, double beta, double s,
               double dt, int itmax):
    '''
    Checks whether x>y or x<=y, at the end of a full evolution.
    '''
    x, y = evolution(x, y, alpha, beta, s, dt, itmax)
    if x > y:
        return 0
    else:
        return 1


def bisection(double x, double alpha, double beta, double s, double dt,
              int itmax, double tol):
    '''
    Returns (for a given x) the y component of the line separating the two
    basins.
    '''
    cdef double y0 = 0.0
    cdef double y1 = 1.0
    f0 = basin(x, y0, alpha, beta, s, dt, itmax)
    f1 = basin(x, y1, alpha, beta, s, dt, itmax)
    if f0 == 1:
        return y0
    elif f1 == 0:
        return y1
    while y1 - y0 > tol:
        ymid = (y0 + y1) * 0.5
        fmid = basin(x, ymid, alpha, beta, s, dt, itmax)
        if fmid == f1:
            y1 = ymid
            f1 = fmid
        else:
            y0 = ymid
            f0 = fmid
    return y0
