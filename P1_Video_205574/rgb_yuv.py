import ffmpeg
from PIL import Image
import numpy as np

def rgb_to_yuv(r, g, b):
    y = 0.299 * r + 0.587 * g + 0.114 * b
    u = -0.147 * r - 0.289 * g + 0.436 * b
    v = 0.615 * r - 0.515 * g - 0.100 * b
    return y, u, v

def resize_image(input_file, output_file, width, height):
    ffmpeg.input(input_file).filter('scale', width, height).output(output_file).run()
    
def serpentine(input_file):
    img = Image.open(input_file)
    img = np.array(img)
    serpentine_pixels = []
    rows, cols, _ = img.shape
    for i in range(rows):
        #if the row is even go from left to right
        if i % 2 == 0:
            serpentine_pixels.extend(img[i, :, :].tolist())
        #if the row is odd go from right to left
        else:
           serpentine_pixels.extend(reversed(img[i, :, :].tolist()))
    return serpentine_pixels

def bw_and_compress(input_file, output_file):
    ffmpeg.input(input_file).output(output_file, vf ='hue=s=0', qscale = '1').run()

def all_operations(input_file):
    #RGB to YUV
    r, g, b = 128, 64, 32
    y, u, v = rgb_to_yuv(r, g, b)
    print(f"RGB to YUV: Y = {y}, U = {u}, V = {v}")
    #We can see the values converted into YUV

    #resize image
    resize_image(input_file, 'P1_Video_205574/resized_output.jpeg', 320, 240)
    print("Image resized.")
    #The image resizes thus lowering in quality

    #read in serpentine pattern
    pixels = serpentine(input_file)
    print(f"First 10 pixels read in serpentine pattern: {pixels[:10]}")


    #convert to black and white and compress
    bw_and_compress(input_file, 'P1_Video_205574/compressed_bw_output.jpeg')
    print("Image converted to black and white and heavily compressed.")

def RLE(sequence):
    rle_sequence = ""
    prev_byte = sequence[0]
    count = 1
    
    for byte in sequence[1:]:
        if byte == prev_byte:
            count += 1
        else:
            rle_sequence += str(count) + str(prev_byte)
            prev_byte = byte
            count = 1
    sequence += str(count) + str(prev_byte)
    return rle_sequence

all_operations('P1_Video_205574/resize_input.jpeg')

byte_sequence = "AAABBBCCDDA"
encoded_sequence = RLE(byte_sequence)
print(f"Original sequence: {byte_sequence}")
print(f"Run-length encoded sequence: {encoded_sequence}")