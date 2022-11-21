import math

import numpy as np
import os
from PIL import Image

OUTPUT_COUNT = 10
LABELS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

dir = 'drawn'
data = os.scandir(dir)
total_files = len(os.listdir(dir))

weights = np.zeros((OUTPUT_COUNT, 784))

for i in range(len(LABELS)):
    input_filename = "output\\weights_" + str(LABELS[i]) + ".txt"
    input = open(input_filename).read()[1:-1]
    weights[i] = np.array(input.split(',')).astype(np.float)


def create_input(image):
    input = np.zeros(784)
    pix = image.load()
    iter = 0
    for i in range(28):
        for j in range(28):
            input[iter] = round(pix[i, j][0] / 255, 2) # For drawn in paint
            # input[iter] = round(pix[i, j] / 255, 2)
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


errors_count = 0
errors = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for filename in data:
    im = Image.open(filename.path)
    input = create_input(im)
    label = int(filename.path.split('_')[1][0])
    prediction = getSoftmaxPrediction(input, weights)
    index = np.where(prediction == max(prediction))[0][0]
    if (LABELS[index] != label):
        errors_count += 1
        errors[index] += 1
        # print(np.round(prediction, 2))
    # print("Prediction: " + str(LABELS[index]) + " Correct: " + str(label))
print("Total errors count = " + str(round(errors_count / total_files, 2)) + " (" + str(errors_count) + " / " + str(
    total_files) + ")")

for i in range(len(errors)):
    print("Ошибок для " + str(i) + ": " + str(errors[i]))
