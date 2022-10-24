import tkinter as tk


def main(): 
    root = tk.Tk()
    root.title('Move Animation')
  
    WIDTH = 500
    HEIGHT = 500
  
    canvas = tk.Canvas(root, width = WIDTH, height = HEIGHT)
    canvas.pack()
  
    x1 = WIDTH / 2
    y1 = HEIGHT / 2
  
    # Center on x axis, at the bottom of y axis
    text = canvas.create_text(x1, y1 * 2 - 20, text = "Use arrow keys to move")
    image = canvas.create_rectangle(x1, y1, x1 + 15, y1 + 15)
 
    def move(event):
        if event.keysym == "Left":
            current_coords = canvas.coords(image)
            if current_coords[0] <= 0:
                canvas.move(image, WIDTH, 0)
            else:
                canvas.move(image, -10, 0)
        elif event.keysym == "Right":
            current_coords = canvas.coords(image)
            if current_coords[0] >= WIDTH:
                canvas.move(image, -WIDTH, 0)
            else:
                canvas.move(image, 10, 0)
        elif event.keysym == "Up":
            current_coords = canvas.coords(image)
            if current_coords[1] <= 0:
                canvas.move(image, 0, HEIGHT)
            else:
                canvas.move(image, 0, -10)
         
        elif event.keysym == "Down":
            current_coords = canvas.coords(image)
            if current_coords[1] >= HEIGHT:
                canvas.move(image, 0, -HEIGHT)
            else:
                canvas.move(image, 0, 10)
  
    root.bind("<KeyPress>", move)
    root.mainloop()

if __name__ == '__main__':
   main()