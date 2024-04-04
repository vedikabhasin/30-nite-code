from PIL import Image
import qrcode

website_link = 'https://www.vedikabhasin.com/'

qr = qrcode.QRCode(version = 1, box_size = 7, border = 2)
qr.add_data(website_link)
qr.make()


img = qr.make_image(fill_color = 'grey', back_color = 'transparent')

#transparent bg
background = Image.new('RGBA', img.size, (255, 255, 255, 0)) 
background.paste(img)

background.save('website_qr_tp.png')
background.show()



# img.save('website_qr.png')
# img = qr.make_image(fill_color = 'white', back_color = 'black')
# img.show()

# /Users/vedikabhasin/desktop/fun projects/30-nite-code/