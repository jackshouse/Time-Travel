# In this example, the function schw_field defines the set of 4 coupled ODEs
# that describe the Schwarzschild metric field equations.
# The solve_ivp function from the scipy.integrate module is
# used to numerically solve these equations over a specified
# time range. The resulting solution is plotted using the matplotlib module.


import numpy as np
from scipy.integrate import solve_ivp

def schw_field(t, y, M):
    """
    Schwarzschild metric field equations for a static, spherically symmetric 
    gravitational field. This function defines the set of 4 coupled ODEs that 
    describe the field equations.
    """
    r, a, b, c = y
    f = np.zeros_like(y)
    f[0] = a
    f[1] = b
    f[2] = c
    f[3] = -(M * r) / (2 * r**2 - 2 * M * r)
    return f

# Define parameters
M = 1.0  # Mass of central object
r0 = 0.1  # Initial radial position
a0 = 1.0  # Initial value of a
b0 = 0.0  # Initial value of b
c0 = r0**2  # Initial value of c

# Set initial conditions
y0 = [r0, a0, b0, c0]

# Set time range for simulation
t_span = [0, 10]

# Solve ODEs numerically
sol = solve_ivp(lambda t, y: schw_field(t, y, M), t_span, y0)

# Plot results
import matplotlib.pyplot as plt

r = sol.y[0]
plt.plot(sol.t, r)
plt.xlabel('t')
plt.ylabel('r')
plt.show()


