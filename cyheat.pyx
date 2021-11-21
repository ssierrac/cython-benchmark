#cython: language_level=3
cimport cython

cdef evolve(double [:, :] u, double [:, :] u_previous, double a, double dt, double dx2, double dy2):
    """Explicit time evolution.
       u:            new temperature field
       u_previous:   previous field
       a:            diffusion constant
       dt:           time step. """

    cdef Py_ssize_t n, m, i, j
    cdef double nu

    n = u.shape[0]
    m = u.shape[1]

    for i in range(1, n-1):
        for j in range(1, m-1):
            nu = ((u_previous[i-1, j] - 2*u_previous[i, j] + u_previous[i+1, j]) / dx2 + (u_previous[i, j-1] - 2*u_previous[i, j] + u_previous[i, j+1]) / dy2 )
            u[i, j] = u_previous[i, j] + a * dt * nu

    u_previous[:] = u[:]

@cython.boundscheck(False)  # Deactivate bounds checking
@cython.wraparound(False)   # Deactivate negative indexing.
def iterate(double [:, :] field, double [:, :] field0, double a, double dx, double dy, int timesteps):
    """Run fixed number of time steps of heat equation"""

    cdef double dx2 = dx * dx
    cdef double dy2 = dy * dy

    # For stability, this is the largest interval possible
    # for the size of the time-step:    
    cdef double dt = dx2*dy2 / ( 2*a*(dx2+dy2) )    

    cdef int i
    for i in range(1, timesteps+1):
        evolve(field, field0, a, dt, dx2, dy2)
