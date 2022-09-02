import arcade
  
# Creating MainGame class       
class MainGame(arcade.Window):
    def __init__(self):
        super().__init__(600, 600, title="Player Movement")
  
        # Initializing the initial x and y coordinated
        self.x = 250 
        self.y = 250
  
        # Initializing a variable to store
        # the velocity of the player
        self.vel = 300
  
    # Creating on_draw() function to draw on the screen
    def on_draw(self):
        arcade.start_render()
  
        # Drawing the rectangle using
        # draw_rectangle_filled function
        arcade.draw_rectangle_filled(self.x, self.y,50, 50,
                                     arcade.color.GREEN )
    # Creating on_update function to
    # update the x coordinate
    def on_update(self,delta_time):
        self.x += self.vel * delta_time
  
        # Changing the direction of
        # movement if player crosses the screen
        if self.x>=550 or self.x<=50:
            self.vel *= -1
          
# Calling MainGame class       
MainGame()
arcade.run()