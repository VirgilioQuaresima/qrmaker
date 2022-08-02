import qrcode
from PIL import Image

class Link:
    def __init__(self, url):
        self.url=url

    def crate_qr(self):
        url=self.url
        img = qrcode.make('Your input text')
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
        return img

    def add_logo(self, img):
        logo_display = Image.open('/Users/virgilio/VxX/qrnew/profile.png')
        logo_display.thumbnail((180, 180))
        logo_pos = ((img.size[0] - logo_display.size[0]) // 2, (img.size[1] - logo_display.size[1]) // 2)
        img.paste(logo_display, logo_pos)
        return img
        

def main():
    url=input("inserisci url: \n")
    link=Link(url)
    img=link.crate_qr()
    choise=input("vuoi inserire il logo? (y/n): ")
    if choise=='y':
        print(choise)
        img=link.add_logo(img)

    img.save("sample.png")

if __name__ == "__main__":
    main()