width=500
height=440
xpalla=100
ypalla=120
x2=1
y2=1
xrettangolo=((width/2)-25)
yrettangolo=(height-25)
hrettangolo=25
lrettangolo=80
def setup():
    size(width,height)
    background(0,0,255)
    stroke(0,255,0)

    global xpalla,ypalla,x2,y2
    background(255,255,255)
    ellipse(ypalla,xpalla,50,50)
    xpalla+=3*(x2)
    ypalla+=3*(y2)
    if ypalla>=height or ypalla<0:
       y2*= -1
       fill(random(255),random(255),random(255))
    if xpalla>=width  or xpalla<0:
       x2*= -1
       fill(random(255),random(255),random(255))
    rect(xrettangolo,yrettangolo,lrettangolo,hrettangolo)
circonferenza=ypalla+25
def keyPressed():
    global xrettangolo,yrettangolo,width,height,y2,x2,x,circonferenza
    if keyCode == RIGHT and xrettangolo<width-lrettangolo:        
        xrettangolo+=15
    if keyCode == LEFT and xrettangolo>0:
        xrettangolo-=15
    if circonferenza<height-25 and xpalla==xrettangolo and xpalla==xrettangolo+lrettangolo:
        y2*= -1
        
        
      
    
    
    
    

    
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
