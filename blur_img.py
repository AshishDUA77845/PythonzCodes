from PIL import Image, ImageFilter

path = input("Enter the path where the image is located:")

img = Image.open(path)

img = img.filter(ImageFilter.BoxBlur(8))

# If you got an error like OSError: cannot write mode RGBA as JPEG,
# Convert image to RGB mode before saving as JPEG 
img = img.convert("RGB")

img.save("blurredimage.jpg")
img.show()
