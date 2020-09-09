import numpy


def physics_check(x):
    if x < 0:
        return 1
    return 0

def integrate_euler(dq_dt, q0, dt):
    return dq_dt * dt + q0

def integrate_rk4(dq_dt, q0, dt):
    return None

# constants
G = 9.81

# initial conditions
x = 50
v = 0
t0 = 0
tf = 100
dt = 0.1
N = int((tf - t0) / dt) + 1
t = numpy.linspace(0, 100, N)

# solve
a = -G
t_i_old = t[0]
for t_i in t[1:]:
    dt = t_i - t_i_old
    v = integrate_euler(a, v, dt)
    x = integrate_euler(v, x, dt)
    check = physics_check(x)
    if check == 1:
        break
    t_i_old = t_i
