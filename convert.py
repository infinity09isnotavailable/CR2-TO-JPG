from PIL import Image
import os

def convert_cr2_to_jpg(source, destination):
    for root, dirs, files in os.walk(source):
        for file in files:
            if file.lower().endswith(".cr2"):
                raw_image = os.path.join(root, file)
                jpg_image = os.path.join(destination, os.path.splitext(file)[0] + ".jpg")
                print(f"Converting the following raw image: {raw_image} to JPG")
                with Image.open(raw_image) as img:
                    img.save(jpg_image, "JPEG")

if __name__ == "__main__":



    #change this, C:\Users\user\Pictures\CR2 'with your actual folder path where your .CR2 files are located.'
    source_dir = r'C:\Users\user\Pictures\CR2' 

    #Do the Same thing here but, put the folder path where you want to save the converted files of .CR2.
    dest_dir = r'C:\Users\user\Pictures\CCR2'  




    convert_cr2_to_jpg(source_dir, dest_dir)
    print("Conversion complete.")
