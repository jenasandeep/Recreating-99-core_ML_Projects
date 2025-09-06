import numpy as np
def batch_gradient_descent(X, y, learning_rate, num_iterations):
    m, n = X.shape

    theta = np.random.randn(n+1, 1)
    for _ in range(num_iterations):
        gradients = 2/m * X.T.dot( theta.T.matmul(X) - y)
        theta = theta - learning_rate * gradients
        # theta (n+1, 1) X (n+1, m)

    return theta

