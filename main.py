
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Face_Recognisation_System:

    def __init__(self,root):

        self.root = root
        self.root.geometry("1530x800+0+0")  #heightxwidth+x-axis+ y-axis
        self.root.title("Face Recognisation System")

        # creating object of 1 Image
        img = Image.open(r"C:\Users\HP Pavilion\OneDrive\Desktop\Face-Recognition-System\college_images\Stanford.jpg")
        img = img.resize((500,130),Image.AFFINE)
        self.photoimg = ImageTk.PhotoImage(img)

        # placing it on window
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

         # creating object of 2 Image
        img1 = Image.open(r"C:\Users\HP Pavilion\OneDrive\Desktop\Face-Recognition-System\college_images\facialrecognition.png")
        img1 = img1.resize((500,130),Image.BILINEAR)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        # placing it on window
        f_lb2 = Label(self.root, image=self.photoimg1)
        f_lb2.place(x=500,y=0,width=500,height=130)

         # creating object of 3 Image
        img2 = Image.open(r"C:\Users\HP Pavilion\OneDrive\Desktop\Face-Recognition-System\college_images\u.jpg")
        img2 = img2.resize((500,130),Image.AFFINE)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        # placing it on window
        f_lb3 = Label(self.root, image=self.photoimg2)
        f_lb3.place(x=1000,y=0,width=550,height=130)

         # creating object of background Image
        img3 = Image.open(r"C:\Users\HP Pavilion\OneDrive\Desktop\Face-Recognition-System\college_images\wp2551980.jpg")
        img3 = img3.resize((1530,710),Image.AFFINE)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        # placing it on window
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        # title
        title_lb1 = Label(bg_img,text="FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lb1.place(x=0,y=0,width=1530,height=50)

        # student button
        img4 = Image.open(r"C:\Users\HP Pavilion\OneDrive\Desktop\Face-Recognition-System\college_images\gettyimages-1022573162.jpg")
        img4 = img4.resize((220,220),Image.AFFINE)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img,image=self.photoimg4,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1= Button(bg_img,text="Student Details",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)

        # face detector
        img5 = Image.open(r"C:\Users\HP Pavilion\OneDrive\Desktop\Face-Recognition-System\college_images\face_detector1.jpg")
        img5 = img5.resize((220,220),Image.AFFINE)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=500,y=100,width=220,height=220)

        b1_1= Button(bg_img,text="Face Detector",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)

        # Attendence 
        img6 = Image.open(r"C:\Users\HP Pavilion\OneDrive\Desktop\Face-Recognition-System\college_images\report.jpg")
        img6 = img6.resize((220,220),Image.AFFINE)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=800,y=100,width=220,height=220)

        b1_1= Button(bg_img,text="Attendence",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)

        # Help Desk 
        img7 = Image.open(r"C:\Users\HP Pavilion\OneDrive\Desktop\Face-Recognition-System\college_images\help-desk-customer-care-team-icon-blue-square-button-isolated-reflected-abstract-illustration-89657179.jpg")
        img7 = img7.resize((220,220),Image.AFFINE)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1= Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)

        # Train 
        img8 = Image.open(r"C:\Users\HP Pavilion\OneDrive\Desktop\Face-Recognition-System\college_images\Train.jpg")
        img8 = img8.resize((220,220),Image.AFFINE)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img,image=self.photoimg8,cursor="hand2")
        b1.place(x=200,y=380,width=220,height=220)

        b1_1= Button(bg_img,text="Train Data",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=580,width=220,height=40)

        # photos 
        img9 = Image.open(r"C:\Users\HP Pavilion\OneDrive\Desktop\Face-Recognition-System\college_images\opencv_face_reco_more_data.jpg")
        img9 = img9.resize((220,220),Image.AFFINE)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img,image=self.photoimg9,cursor="hand2")
        b1.place(x=500,y=380,width=220,height=220)

        b1_1= Button(bg_img,text="Photos",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=580,width=220,height=40)

         # Developer 
        img10 = Image.open(r"C:\Users\HP Pavilion\OneDrive\Desktop\Face-Recognition-System\college_images\developer.jpg")
        img10 = img10.resize((220,220),Image.AFFINE)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=800,y=380,width=220,height=220)

        b1_1= Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=580,width=220,height=40)

         # Exit button 
        img11 = Image.open(r)
        img11 = img11.resize((220,220),Image.AFFINE)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=1100,y=380,width=220,height=220)

        b1_1= Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=580,width=220,height=40)



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognisation_System(root)
    root.mainloop()
        