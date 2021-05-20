import numpy as np
import math
import matplotlib.pyplot as plt

import pdb

np.random.seed(20)  # Set seed to get the same values always

def fn(x):
    return np.cos(x) * np.exp(x)

def plot_fn():
    x = np.linspace(-2 * np.pi, 2 * np.pi, 100, endpoint=True)
    # x = [val for val in range(-2 * 180, 4 * 180, 10)]
    # y = [fn(val) for val in x]
    y = fn(x)

    plt.scatter(x, y)
    plt.savefig("cos-Exp.jpg")
    plt.cla()

def new_question():
    sigma = 2
    mu = 5.0
    normal_dist = [sigma * np.random.randn() + mu for num in range(100000)]
    uniform_dist = np.random.uniform(0, 10, 100000)

    print("Normal Distribution ---> Mean: {}; StdDev: {}".format(np.mean(normal_dist), np.std(normal_dist)))
    print("Uniform Distribution ---> Mean: {}; StdDev: {}".format(np.mean(uniform_dist), np.std(uniform_dist)))

    _, bins, _ = plt.hist(normal_dist, bins=100, density=True)
    plt.plot(bins, np.exp(-(bins - mu) * (bins - mu) / (2 * sigma * sigma)) / (sigma * np.sqrt(2 * np.pi)), 'r')
    plt.xlabel('Samples')
    plt.ylabel('Values')
    plt.title("Normal Distribution")
    plt.savefig('Normal-Distribution-Histogram.jpg')
    plt.cla()

    _, bins, _ = plt.hist(uniform_dist, bins=100, density=True)
    plt.plot(bins, np.ones_like(bins) * 0.1, 'r')
    plt.xlabel('Samples')
    plt.ylabel('Values')
    plt.title("Uniform Distribution")
    plt.savefig('Uniform-Distribution-Histogram.jpg')
    plt.cla()

if __name__ == '__main__':
    new_question()
    plot_fn()
