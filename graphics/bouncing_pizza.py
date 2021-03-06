from superwires import games

path_to_images = '../../Pictures/img/'

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Pizza(games.Sprite):
    '''Bouncing pizza'''
    def update(self):
        '''Changes speed vectors when pizza comes to the screen edge'''
        if self.right > games.screen.width or self.left < 0:
            self.dx = -self.dx
        if self.bottom > games.screen.height or self.top < 0:
            self.dy = -self.dy
        
def main():
    wall_image = games.load_image(path_to_images + "wall.jpg", transparent=False)
    games.screen.background = wall_image

    pizza_image = games.load_image(path_to_images + "pizza.png")
    the_pizza = Pizza(
            image=pizza_image, 
            x = games.screen.width/2,
            y = games.screen.height/2,
            dx = 1,
            dy = 1
        ) 
    games.screen.add(the_pizza)
    games.screen.mainloop()

# go!
# if __name__ == '__main__':
#     main()
main()