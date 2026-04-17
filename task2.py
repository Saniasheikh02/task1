from PIL import Image
import numpy as np


# ENCRYPTION FUNCTION
def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    img_array = np.array(img)

    # Get image dimensions
    rows, cols, channels = img_array.shape

    # Step 1: Pixel value transformation (Add key)
    encrypted_array = (img_array.astype('int32') + key) % 256

    # Step 2: Pixel swapping (shuffle rows)
    for i in range(rows):
        swap_index = (i + key) % rows
        encrypted_array[[i, swap_index]] = encrypted_array[[swap_index, i]]

    encrypted_img = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_img.save(output_path)
    print("✅ Image Encrypted Successfully!")



# DECRYPTION FUNCTION 
def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    img_array = np.array(img)

    rows, cols, channels = img_array.shape

    # Step 1: Reverse pixel swapping
    for i in range(rows-1, -1, -1):
        swap_index = (i + key) % rows
        img_array[[i, swap_index]] = img_array[[swap_index, i]]

    # Step 2: Reverse pixel value transformation
    decrypted_array = (img_array.astype('int32') - key) % 256

    decrypted_img = Image.fromarray(decrypted_array.astype('uint8'))
    decrypted_img.save(output_path)
    print("✅ Image Decrypted Successfully!")



# MAIN PROGRAM
if __name__ == "__main__":
    key = 50

    # Encrypt
    encrypt_image("img.jpg", "encrypted.png", key)

    # Decrypt
    decrypt_image("encrypted.png", "decrypted.png", key)