import numpy as np
import matplotlib.pyplot as plt

def normalize_probabilities(belief):
    N = belief.shape[0]
    tot_sum = 0.0

    for idx in range(0, N):
        tot_sum += belief[idx]

    for idx in range(0, N):
        belief[idx] /= tot_sum

    return belief

def plot_belief(bel):
    states = []
    for i in range(bel.shape[0]):
        states.append(str(i))

    y_pos = np.arange(bel.shape[0])
    plt.bar(y_pos, bel, align='center', alpha=0.5)
    plt.xticks(y_pos, states)
    plt.ylabel('Probability')
    plt.xlabel('States')
    plt.title('Belief')
    plt.show()

def control_update(initial_belief, direction):
    N = initial_belief.shape[0]
    new_bel = np.zeros(N)
    for index in range(0, N):
        if direction == FORWARD:
            if index == N - 1:
                new_bel[index] = initial_belief[index]
            elif index == N - 2:
                new_bel[index] += initial_belief[index] * 0.25
                new_bel[index + 1] += initial_belief[index] * 0.75
            else:
                new_bel[index] += initial_belief[index] * 0.25
                new_bel[index + 1] += initial_belief[index] * 0.50
                new_bel[index + 2] += initial_belief[index] * 0.25
        else:
            if index == 0:
                new_bel[index] = initial_belief[index]
            elif index == 1:
                new_bel[index - 1] += initial_belief[index] * 0.75
                new_bel[index] += initial_belief[index] * 0.25
            else:
                new_bel[index - 2] += initial_belief[index] * 0.25
                new_bel[index - 1] += initial_belief[index] * 0.50
                new_bel[index] += initial_belief[index] * 0.25

    return new_bel # new_bel / np.sum(new_bel)

if __name__ == '__main__':
    FORWARD, BACKWARD = 1, 0
    bel = np.hstack((np.zeros(9), 1.0, np.zeros(10)))  # 20 possible states

    for i in range(0, 9):
        bel = control_update(bel, FORWARD)
        # plot_belief(bel)

    for i in range(0, 3):
        bel = control_update(bel, BACKWARD)
        # plot_belief(bel)

    print(bel)
    tot_sum = 0.0
    for i in range(0, 20):
        tot_sum += bel[i]

    print(np.sum(bel))

    plot_belief(bel)






