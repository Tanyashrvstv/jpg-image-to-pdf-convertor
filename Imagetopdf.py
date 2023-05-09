from PIL import Image

image = Image.open('input.jpg')
pdf_file = 'output.pdf'
image.save(pdf_file, 'PDF', resolution=100.0)
