"""
Project from Chris Foster

https://fosterelli.co/executing-gradient-descent-on-the-earth

accessed 2018-04-19

"""


import rasterio, sys
import numpy as np

# Fetch the elevation
def get_elevation(lat, lon):
    vals = src.index(lon, lat)
    return band[vals]


# Calculate our 'cost function'
def compute_cost(theta):
    """
    :param theta: [latitude, longitude]
    :return:
    """
    lat, lon = theta[0], theta[1]
    j = get_elevation(lat, lon)
    return j


def gradient_descent(theta, alpha = 0.01, num_iters = 1000):
    """
    vanilla gradient descent

    :param theta: [latitude, longitude]
    :param alpha: learning rate
    :param num_iters: number of iterations
    :return:
    """
    j_history = np.zeros((num_iters, 3))

    for i in range(num_iters):

        cost = compute_cost(theta)

        j_history[i] = [cost, theta[0], theta[1]]

        if cost <= 0.0001:
            return theta, j_history

        # Fetch elevations at offsets in each dimension
        elev1 = get_elevation(theta[0] + 0.001, theta[1])
        elev2 = get_elevation(theta[0] - 0.001, theta[1])
        elev3 = get_elevation(theta[0], theta[1] + 0.001)
        elev4 = get_elevation(theta[0], theta[1] - 0.001)

        # Calculate slope
        lat_slope = elev1 / elev2 - 1
        lon_slope = elev3 / elev4 - 1

        # Update variables
        theta[0] -= alpha * lat_slope
        theta[1] -= alpha * lon_slope

    return theta, j_history


def gradient_descent_momentum(theta, alpha=0.01, gamma=0.1, num_iters=1000):
    """
    Gradient descent with momentum

    :param theta:
    :param alpha:
    :param gamma:
    :param num_iters:
    :return:
    """

    J_history = np.zeros((num_iters, 3))
    velocity = [ 0, 0 ]

    for i in range(num_iters):

        cost = compute_cost(theta)

        j_history[i] = [cost, theta[0], theta[1]]

        if cost <= 0.0001:
            return theta, j_history

        # Fetch elevations at offsets in each dimension
        elev1 = get_elevation(theta[0] + 0.001, theta[1])
        elev2 = get_elevation(theta[0] - 0.001, theta[1])
        elev3 = get_elevation(theta[0], theta[1] + 0.001)
        elev4 = get_elevation(theta[0], theta[1] - 0.001)

        # Calculate slope
        lat_slope = elev1 / elev2 - 1
        lon_slope = elev3 / elev4 - 1

        # Calculate update with momentum
        velocity[0] = alpha * (gamma * velocity[0] + (1-gamma) * lat_slope)
        velocity[1] = alpha * (gamma * velocity[1] + (1-gamma) * lon_slope)

        # Update variables
        theta[0] -= velocity[0]
        theta[1] -= velocity[1]

    return theta, J_history


if __name__ == "__main__":

    theta = [37.745956, -119.533279] # Half Dome summit
    alpha = 0.01
    gamma = 0.15

    print("Starting at lat: {}, lon: {}".format(theta[0], theta[1]))
    num_iters = 1000

    src = rasterio.open("srtm_12_04/srtm_12_04.hdr")
    band = src.read(1)

    if len(sys.argv) > 1 and 'm' in sys.argv[1].lower():
        theta, j_history = gradient_descent(theta, alpha, num_iters)
    else:
        theta, j_history = gradient_descent_momentum(theta, alpha, gamma, num_iters)

    print("Ended at lat: {}, lon: {}".format(theta[0], theta[1]))

