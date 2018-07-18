def setup():
    size(500,500)
    dog=loadImage("dog.jpg")
    image(dog,0,0)
    c=color(255,255,0)
    loadPixels()
    print(pixels[57])
    print(red(pixels[57]), green(pixels[57]),blue(pixels[57]))
    pixels[57]=c
    updatePixels()
