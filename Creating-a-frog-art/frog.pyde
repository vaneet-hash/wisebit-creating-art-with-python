def setup():
    size(1400,930)
    frog=loadImage("frog3.jpg")
    for i in range(0,100):
        x=random(width)
        y=random(height)
        c=frog.get(int(x),int(y))
        fill(c)
        ellipse(x,y,14,14)
