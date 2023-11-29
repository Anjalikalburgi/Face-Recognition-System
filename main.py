from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class FaceRecognitionSystem:

    def __init__(self,root):
        self.root = root
        self.root.geometry("1590x790+0+0")  #heightxwidth+x-axis+y=axis
        self.root.title("Face Recognition System")
# Add a comment to demonstrate Git changes

        print("This is a new line added for Git demonstration.")
        # Add another line for Git demonstration
        print("This is another line added for Git demonstration.")

if __name__ == "__main__":
    # Create the main Tkinter window
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
        
        