def setup():
    size(600,600)
    noFill()
    strokeWeight(3)
    colorMode(HSB)
t=0 #time variable
NUM_TRIES = 90
 
def draw():
    global t
    background(0)
    translate(width/2, height/2)           #moving the origin to center of the screen
    for i in range(int(NUM_TRIES)):
        rotate(radians(360/NUM_TRIES))
        pushMatrix() #save this orientation
        translate(200,0)
        rotate(radians(t+2*NUM_TRIES))
        stroke(3*i,255,255)
        tri(100)
        popMatrix() #return to save orientation
    t += 0.5
def tri(length):
    triangle(0,-length,-length*sqrt(3)/2,length/2,length*sqrt(3)/2,length/2)
