from PIL import Image;
import numpy as np
from colorama import Fore, Style

img=Image.open("sukuna.jpg")
ASCII_CHARS = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
MAX_PIXEL_VALUE=255



def get_pixel_matrix(img,height):

    img.thumbnail((height,200))
    pixels=list(img.getdata()) #each element of the list is a pixel represented in RGB
    #pixel_matrix=[]
    # for i in range(0,len(pixels),img.width):
     #  row=pixels[i:i+img.width]
       #pixel_matrix.append(row)
    return [pixels[i:i+img.width] for i in range(0, len(pixels), img.width)]


def get_average_matrix(pixel_matrix):
    average_matrix = []
    for row in pixel_matrix:
        average_row = []
        for p in row:
            average = (p[0] + p[1] + p[2]) / 3.0
            average_row.append(average)
        average_matrix.append(average_row)
    return average_matrix



def normalize_average_matrix(average_matrix):
    normalized_average_matrix = []
    max_pixel = max(map(max, average_matrix))
    min_pixel = min(map(min, average_matrix))
    for row in average_matrix :
        rescaled_row = []
        for p in row:
            r = 255 * (p - min_pixel) / float(max_pixel - min_pixel)
            rescaled_row.append(r)
        normalized_average_matrix.append(rescaled_row)

    return normalized_average_matrix

def invert_average_matrix(average_matrix):
    inverted_average_matrix = []
    for row in average_matrix:
        inverted_row = []
        for p in row:
            inverted_row.append(255- p)
        inverted_average_matrix.append(inverted_row)

    return inverted_average_matrix
        

def convert_to_ascii(average_matrix, ascii_chars):
    ascii_matrix = []
    for row in average_matrix:
        ascii_row = []
        for p in row:
            index = int(p / MAX_PIXEL_VALUE * len(ascii_chars))
            index = max(0, min(index, len(ascii_chars) - 1))  # Ensure the index stays within bounds
            ascii_row.append(ascii_chars[index])
        ascii_matrix.append(ascii_row)

    return ascii_matrix


def print_ascii_matrix(ascii_matrix, text_color):
    for row in ascii_matrix:
        line = [p+p+p for p in row]
        print(text_color + "".join(line))

    print(Style.RESET_ALL)

   
pixels = get_pixel_matrix(img, 1000)    
average_matrix = get_average_matrix(pixels)
average_matrix = normalize_average_matrix(average_matrix) 
ascii_matrix = convert_to_ascii(average_matrix, ASCII_CHARS)
print_ascii_matrix(ascii_matrix, Fore.CYAN)






        
        



