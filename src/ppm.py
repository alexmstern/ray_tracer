import sys
from tqdm import tqdm

def main():

    # Image Dimensions
    image_width = 256
    image_height = 256

    # Progress Bar
    total_pixels = image_width * image_height
    progress_bar = tqdm(total=total_pixels, unit="pixels")

    # Render Image
    print("P3\n" + str(image_width) + ' ' + str(image_height) + "\n255\n", file=sys.stdout)

    for j in range(image_height):
        for i in range(image_width):
            r = i / (image_width - 1)
            g = j / (image_height - 1)
            b = 0

            ir = (int)(255.999 * r)
            ig = (int)(255.999 * g)
            ib = (int)(255.999 * b)

            print(str(ir) + ' ' + str(ig) + ' ' + str(ib), file=sys.stdout)
            progress_bar.update(1)

    progress_bar.close()

if __name__ == "__main__":
    main()