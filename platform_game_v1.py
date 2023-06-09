#Basic arcade program
#Displays a white window with a blue circle in the middle

#Import
import arcade

#Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Welcome to Arcade"
RADIUS = 150

#Open the window
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

#Set the background color
arcade.set_background_color(arcade.color.BLUE)

#Clear the screen and start drawing
arcade.start_render()

#Draw a white circle
arcade.draw_circle_filled(
    SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, RADIUS, arcade.color.WHITE
)

#Finish drawing
arcade.finish_render()

#Display everything
arcade.run()