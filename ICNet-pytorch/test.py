from PIL import Image

im_red = Image.open('./red.png')

im_mask = Image.open('./mask.png')

combined = im_red.putalpha(im_mask)

combine.save('./combined.png')



