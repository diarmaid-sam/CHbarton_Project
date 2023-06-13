## tkinter style-based module (needed for window class that allows for widget themes)
import ttkbootstrap as tb

# mainframe class
from mainframe import MainFrame

    
if __name__ == "__main__":
    
    app = tb.Window("Software", themename="superhero", minsize=(800, 800))
    # get the roots screen width and height
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    # Set the window size to the screen size
    app.geometry(f"{screen_width}x{screen_height}")

    # Mainframe created with app being parent 
    MainFrame(app)
    app.place_window_center()
    
    app.mainloop()
    
def run_app():
    return
    
