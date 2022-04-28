from ursina import *

if __name__ == '__main__':
    app = Ursina()

#to set the camera angle(orthographic projection)
camera.orthographic = True

#to create a field of view
camera.fov = 4

#create another parameter for position
camera.position = (1, 1)
Text.default_resolution *= 2

#creating the entity
player = Entity(name='o',color=color.red)

#creating the variable to pass the object for customizing the game cursor
cursor = Tooltip(player.name, color=player.color, origin=(0,0), scale=4, enabled=True)
cursor.background.color = color.clear

#creating the game background Entity
bg = Entity(parent=scene, model='quad', texture='shore', scale=(16,8), z=10, color=color.blue)
mouse.visible = False
#create a matrix for game board with 3 rows and 3 columns
#declare a variable called 'board'
board = [[None for x in range(3)]for y in range(3)]

#creating the tiles in board by using this for loop traverse
for y in range(3):
    for x in range(3):
        #create a variable b for the creation of buttons
        b = Button(parent=scene, position=(x,y))
        #create a matrix variable board and this variable helps to identify the winner at the end and pass the value as b
        board[x][y] = b
        
        #declare a function
        def on_click(b=b):
            b.text = player.name
            b.color = player.color
            b.collision = False
            check_for_victory()
            
            #create conditions to describe the color of the players
            if player.name == 'o':
                player.name = 'x'
                player.color = color.orange
            else :
                player.name = 'o'
                player.color = color.azure
                
            #inserting the cursor color and cursor text
            cursor.text = player.name
            cursor.color = player.color
            
        b.on_click = on_click
        
#create a function to declare the winner
def check_for_victory():
    name = player.name
    
    #board[row][column]-syntax
    won = (
     (board[0][0].text == name and board[1][0].text == name and board[2][0].text == name) or # across the bottom
     (board[0][1].text == name and board[1][1].text == name and board[2][1].text == name) or # across the middle
     (board[0][2].text == name and board[1][2].text == name and board[2][2].text == name) or # across the top
     (board[0][0].text == name and board[0][1].text == name and board[0][2].text == name) or # down the left side 
     (board[1][0].text == name and board[1][1].text == name and board[1][2].text == name) or # down the middle
     (board[2][0].text == name and board[2][1].text == name and board[2][2].text == name) or # down the right side
     (board[0][0].text == name and board[1][1].text == name and board[2][2].text == name) or # diagonal /
     (board[0][2].text == name and board[1][1].text == name and board[2][0].text == name))   # diagonal \
    
    if won:
        print('Winner is:', name)
        destroy(cursor)
        mouse.visible = True
        Panel(z=1, scale=10, model='quad')
        t = Text(f'player\n{name}\nwon!', scale=3, origin=(0,0), background=True)
        t.create_background(padding=(.5,.25), radius=Text.size/2)
        t.background.color = player.color.tint(-.2)
        
if __name__== '__main__':
    app.run()
        

