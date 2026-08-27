from PIL import Image
def main():
 image = Image.open("img.png")
 bw_image = image.convert("L")
 bw_image.show()
 bw_image.save("bw_img.png")

if __name__ == "__main__":
    main()