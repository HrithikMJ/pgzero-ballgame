import pgzrun
from random import randint

colour=[(255,255,255),(37,169,240),(216,36,124),(82,26,74),(36,14,40),(0,0,0)]
WIDTH=800
HEIGHT=600
paddle=Actor('paddle')
paddle.bottom = HEIGHT
paddle.left = 0
ball = Actor('ball')
score=0
j=0
ballsx = randint(5,9)
ballsy = randint(5,9)
missed= False
score=0

def position_objects():
    paddle.bottom = HEIGHT
    paddle.left = 0

def on_mouse_move(pos):
  paddle.x= pos[0]
  if paddle.left < 0:
    paddle.left=0
  elif paddle.right> WIDTH:
    paddle.right = WIDTH
  check_coll()



def draw():
  global score,i
  leveler()
  temp=colour[i]
  screen.fill(temp)
  ball.draw()
  paddle.draw()
  draw_textt()


def leveler():
    global score,i,ballsy,j
    i=0
    if score>0 and score<30:
        i=0
    elif score>=30 and score < 60:
        i=i+1
        
    elif score>=60 and score < 90:
        i=i+2
        
    elif score>=90 and score < 120:
        i=i+3
        
    elif score>=120 and score < 150:
        i=i+4                                                                              

    elif score>=150 and score < 1000:
        i=i+5 
        j=1
    else:
        i=0

def check_coll():
  global ballsy,score,j
  if paddle.colliderect(ball):

    ballsy *= -1                                      #nice :)
    sounds.bonk.play()
    score += 10                                                                     
  
      
def draw_textt():
    global score,position
    position = ((WIDTH // 2)-100, HEIGHT // 2)
    screen.draw.text("score:"+str(score),(0,0),fontsize=20,color='cyan')
    if score>0 and score<30:
        screen.draw.text(":)",position, fontsize=50, color="red")
    elif score>=30 and score < 60:
        screen.draw.text("level 1",position, fontsize=50, color="red")
        
    elif score>=60 and score < 90:
        screen.draw.text("level 2",position, fontsize=50, color="red")
        
    elif score>=90 and score < 120:
        screen.draw.text("level 3",position, fontsize=50, color="red")
        
        
    elif score>=120 and score < 150:
        screen.draw.text("level 4",position, fontsize=50, color="red")
        
     
    elif score>=150 and score < 1000:
        screen.draw.text("god tierrrrrrrrrrrrr",position, fontsize=50, color="red")
        ballsy=10 
    if missed:
        
        screen.draw.text("not your day :(((((((",(0,100), fontsize=50, color="red")

def update():
    if not missed:
       animatss()

def animatss():

  ball.y+=ballsy
  ball.x+=ballsx
  music.play('good1')
  checkzz()
  check_coll()
  misser()
 
def misser():
   global ballsy, missed
   if ball.bottom > paddle.top + ballsy +20:
       music.stop()
       music.play('bad1')
       missed = True

def checkzz():
  global ballsx , ballsy
  if ball.right > WIDTH or ball.left < 0:
    ballsx *= -1
  if ball.top < 0 or ball.bottom > HEIGHT:
    ballsy *= -1  


position_objects()
pgzrun.go()