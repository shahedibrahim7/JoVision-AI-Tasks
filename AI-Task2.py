from PIL import Image

def to_gray(img):
    img= img.convert("RGBA")
    w,h= img.size
    gray_img= Image.new("RGB",(w,h))
    for x in range(w):
        for y in range(h):
            pxl= img.getpixel((x,y))
            if len(pxl)==4:
                r,g,b,a=pxl  
            else:
                r,g,b=pxl
            gray= (r+g+b)//3
            gray_img.putpixel((x,y),(gray,gray,gray))
    return gray_img

def main():
    path= input("Enter image path: ").strip('"')
    img= Image.open(path)
    gray_img= to_gray(img)
    gray_img.show()
    gray_img.save("gray_img.png")

main()
