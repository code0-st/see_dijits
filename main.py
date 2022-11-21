import math

import numpy as np
import os
from PIL import Image

dir = 'data/training'
data = os.scandir(dir)
total_files = len(os.listdir(dir))

OUTPUT_COUNT = 10
LABELS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
NEURONS_COUNT = 784

weights = 2 * np.round(np.random.random((OUTPUT_COUNT, NEURONS_COUNT)), 2) - 1
alpha = 0.1


def create_input(image):
    input = np.zeros(784)
    pix = image.load()
    iter = 0
    for i in range(28):
        for j in range(28):
            input[iter] = round(pix[i, j] / 255, 2)
            iter += 1
    return input


def getSoftmaxPrediction(input, weights):
    pred = np.zeros(OUTPUT_COUNT)
    pred_exp = np.zeros(OUTPUT_COUNT)
    for i in range(len(pred_exp)):
        pred_tmp = input.dot(weights[i])
        pred_exp[i] = pow(math.e, pred_tmp)
    prediction_exp_sum = np.sum(pred_exp)
    for i in range(len(pred_exp)):
        pred[i] = pred_exp[i] / prediction_exp_sum
    return pred

cur_file = 0
for filename in data:
    cur_file += 1
    im = Image.open(filename.path)
    input = create_input(im)
    label = int(filename.path.split('_')[1][0])
    goal_prediction = np.empty(10)
    for i in range(len(LABELS)):
        goal_prediction[i] = int(label == LABELS[i])
    for i in range(50):
        prediction = getSoftmaxPrediction(input, weights)
        error = (goal_prediction - prediction) ** 2
        delta = prediction - goal_prediction
        for j in range(len(weights)):
            weights[j] = np.round(weights[j] - (alpha * input * delta[j]), 2)
    # print(getSoftmaxPrediction(input, weights))
    # print(goal_prediction)
    print(str(cur_file) + "/" + str(total_files))

for i in range(len(LABELS)):
    output_filename = "output\\weights_" + str(LABELS[i]) + ".txt"
    output = open(output_filename, "w+")
    output.write(str(weights[i].tolist()))
    output.close()
