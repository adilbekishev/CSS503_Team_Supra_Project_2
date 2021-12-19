import cv2
import numpy as np
import argparse
import ntpath
import os


def threshold_image(path_image, threshold_percent):

    grayscale_image = cv2.cvtColor(cv2.imread(path_image), cv2.COLOR_BGR2GRAY)
    original_rows, original_cols = grayscale_image.shape

    window_height = int(np.floor(original_rows / 16) + 1)
    window_width = int(np.floor(original_cols / 16) + 1)

    height = round(window_height / 2) - 1
    width = round(window_width / 2) - 1

    aux = cv2.copyMakeBorder(grayscale_image, top=height, bottom=height, left=width, right=width, borderType=cv2.BORDER_REFLECT)

    windows = np.zeros((window_height, window_width), np.int32)

    image_integral = cv2.integral(aux, windows, -1)
    integral_rows, integral_cols = image_integral.shape

    result = np.zeros((original_rows, original_cols))

    for i in range(integral_rows - window_height):
        for j in range(integral_cols - window_width):
            result[i, j] = image_integral[i + window_height, j + window_width] - image_integral[i, j + window_width] + image_integral[i, j] - image_integral[i + window_height, j]

    binary_image = np.ones((original_rows, original_cols), dtype=np.bool)
    binary_image[(grayscale_image).astype('float64') * window_height * window_width <= result * (100.0 - threshold_percent) / 100.0] = False
    binary_image = (255 * binary_image).astype(np.uint8)

    return binary_image

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='applies adaptive binarization and saves the output.')
    parser.add_argument('-i', '--input_path', dest="input_path", type=str, required=True, help="image path")
    parser.add_argument("-t", "--threshold", dest='threshold', type=float, default=25, help="binarization threshold")

    args = parser.parse_args()

    if not os.path.exists(args.input_path):
        raise IOError('the input file cannot be found')

    if not 0 < args.threshold < 100:
        raise IOError('threshold percent must be between 0 and 100')

    output = threshold_image(args.input_path, args.threshold)

    image_name = ntpath.basename(args.input_path)

    cv2.imwrite(os.path.splitext(image_name)[0] + '_bin' + os.path.splitext(image_name)[1], output)