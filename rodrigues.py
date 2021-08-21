import numpy as np

# TODO: define a function that converts a rotation vector in 3D 
# of shape (3,) to its coressponding skew-symmetric representation
# of shape (3, 3). This funciton will prove useful in the next question.
def skew_3d(omega):
    """
    Converts a rotation vector in 3D to its corresponding skew-symmetric matrix.
    
    Args:
    omega - (3,) ndarray: the rotation vector
    
    Returns:
    omega_hat - (3,3) ndarray: the corresponding skew symmetric matrix
    """
    if not omega.shape == (3,):
        raise TypeError('omega must be a 3-dim column vector')
    
    # YOUR CODE HERE

# TODO: define a function that when given an axis of rotation omega
# and angle of rotation theta, uses the Rodrigues' Formula to compute
# and return the corresponding 3D rotation matrix R.
# The Function has already been partially defined out for you below.
def rodrigues(omega, theta):
    """
    Computes a 3D rotation matrix given a rotation axis and angle of rotation.

    Args:
    omega - (3,) ndarray: the axis of rotation
    theta: the angle of rotation

    Returns:
    R - (3,3) ndarray: the resulting rotation matrix
    """
    if not omega.shape == (3,):
        raise TypeError('omega must be a 3-dim column vector')

    # YOUR CODE HERE
