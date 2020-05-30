Total_Degrees=360
radius=0
def setup():
    global displayWidth, displayHeight, radius  
    #displayWidth and displayHeight are the variables that stores the width and height of the entire screen display
    
    size(displayWidth / 2,displayHeight)
    #size() defines the dimensions of the display window width and height in units of pixels.
    
    background(0)
    
    noFill()
    # noFills() Disables filling geometry. 
    
    stroke(255,20)
    # stroke() Sets the color used to draw lines and borders around shapes.
    
    radius=height/2
    
def draw():
    center_x=width/2
    center_y=height/2
     
    global Total_Degrees
    
    beginShape()
    # beginShape() begins recording vertices for a shape and endShape() stops recording.
    
    for i in range(Total_Degrees):
        
        noisefactor=noise(i*0.02,float(frameCount)/150) 
        # The system variable frameCount() contains the number of frames that have been displayed since the program started.
        # noise() is a random sequence generator producing a more natural, harmonic succession of numbers than that of the standard random() function.
       
        x=center_x+radius*cos(radians(i))*noisefactor
        y=center_y+radius*sin(radians(i))*noisefactor
        curveVertex(x,y)
        #  curveVertex() Specifies vertex coordinates for curves. This function may only be used between beginShape() and endShape()
    
    endShape(CLOSE)
    radius-=1
   
    if radius==0:
        noLoop()
    # noLoop() Stops Processing from continuously executing the code within draw(). 
