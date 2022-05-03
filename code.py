import qrcode
import image
data="https://www.youtube.com/watch?v=onHPipeASdk&list=PLpp8-k7G_6Y3Wj1suZQ-9lATFzFuGw93x"
qr= qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fil="black",back_color="white")
img.save("test.png")
    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    
