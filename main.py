"""
Propagator
"""

import math
import sys
from typing import Callable

import numpy
from nptyping import NDArray


def arange(start: float, end: float, step: float) -> NDArray[float]:
    """Implementation of numpy.arange to include end."""
    return numpy.linspace(start, end, math.ceil((end - start) / step) + 1)


def physics_check(state_vector: NDArray[float]) -> int:
    """Check when physics is broken."""
    # Bellow ground
    if state_vector[2] < 0:
        return 1
    return 0


def integrate(
    dynamical_model: Callable,
    state_vector: NDArray[float],
    delta_time: float,
    method="euler",
) -> NDArray[float]:
    """Numerical integration methods."""
    if method == "euler":
        state_vector_new = integrate_euler(
            dynamical_model, state_vector, delta_time
        )
    else:
        sys.exit(f"ERROR: method {method} not implemented.")

    return state_vector_new


def integrate_euler(
    dynamical_model: Callable, state_vector: NDArray[float], delta_time: float
) -> NDArray[float]:
    """Numerical integration with the Euler method:
    $q_{n+1}=\frac{dq}{dt}dt+q_{n}$"""
    acceleration = dynamical_model(state_vector)
    return (
        numpy.concatenate((state_vector[3:], acceleration)) * delta_time
        + state_vector
    )


def integrate_rk4(
    _dynamical_model: Callable,
    _state_vector: NDArray[float],
    _delta_time: float,
) -> NDArray[float]:
    """Numerical integration with the Runge-Kutta 4 method"""
    return None


def dynamical_model(_state_vector: NDArray[float]) -> NDArray[float]:
    """Dynamical model to compute acceleration from state vector (position and
    velocity)."""
    return numpy.array([0, 0, -G])


# Constants
G = 9.809

# Initialization
# q: [position, velocity]
state_vector = numpy.array([0, 0, 50, 0, 0, 0])
time_vector = arange(0, 100, 0.1)

# Solve
time_previous = time_vector[0]
for time_current in time_vector[1:]:
    delta_time = time_current - time_previous
    state_vector = integrate(dynamical_model, state_vector, delta_time)
    CHECK = physics_check(state_vector)
    if CHECK == 1:
        break
    time_previous = time_current
