import numpy as np

# Define variables
N = 11  # number of nodes
xmin = 0  # min value of x
xmax = 1  # max value of x
dt = 0.05  # time step
v = 1  # velocity
t = 0  # initial value of t

# Calculate node positions
dx = (xmax - xmin) / (N - 1)
x = np.linspace(xmin, xmax, N)

# Calculate initial conditions
u = np.exp(-100 * (x - 0.4) ** 2)

# Output column headings and initial conditions to the command window
print("-" * (9 * (N + 1) + 1))
print("    t   |", end="")
for i in range(N):
    print("   u_%1i  " % i, end="")
print("\n" + "-" * (9 * (N + 1) + 1))
print("%6.2f |" % t, end="")
for val in u:
    print("%7.4f " % val, end="")
print()

# pre-calculate C = v * dt / dx
C = v * dt / dx

# Perform 3 iterations of the FDS
for _ in range(3):
    # Calculate boundary conditions
    u[0] = 0
    u[-1] = 0

    # Calculate new values of u
    unew = u.copy()

    for i in range(1, N - 1):
        unew[i] = u[i] - C * (u[i] - u[i - 1])

    # Update t and u
    t += dt
    u = unew

    # Output current solution
    print("%6.2f |" % t, end="")
    for val in u:
        print("%7.4f " % val, end="")
    print()

print("-" * (9 * (N + 1) + 1))
