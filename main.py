from tkinter import*
import random


questions_and_answers={
1:["What are the most common symptoms of covid-19?",'dry cough, fever, tiredness','headaches, neck pain, sore throat', 'chest pain, conjunctivitis, sneezing', 'rashes','chest pain, hair loss',1]
2:["What is the most commonly used covid-19 vaccine used in New Zealand?",'Moderna Vaccine', 'Johnson & Johnson’s Janssen Vaccine' , 'Pfizer-BioNTech Vaccine',3]
3:["What does wearing a mask do to prevent getting covid-19?",'Nothing.', 'It helps by keeping your mouth covered and not exposed to bacteria and other peoples germs' , 'It prevents people from looking at your face.',3]
4:["Which Alert Level insrtucts you to stay inside your bubble, only going out for the essentials?",'Alert Level 3','Alert Level 4', 'Alert Level 5',3]
5:[]

}


class Quiz:
    def __init__(self, parent):#constructor, The __init__() function is called automatically every time the class is being used to create a new object.
 
        background_color="lightgrey"# to set it as background color for all the label widgets

        #frame set up
        self.quiz_frame=Frame(parent, bg = background_color, padx=100, pady=100)
        #padx, pady How many pixels to pad widget, horizontally (x) and vertically (y), outside widget's borders.
        self.quiz_frame.grid()#This geometry manager organizes widgets in a table-like structure in the parent widget.
               
        #widgets goes below
        self.heading_label=Label(self.quiz_frame, text="The Covid-19 Quiz", font=("Comic Sans MS","39","bold"),bg=background_color)
        self.heading_label.grid(row=0, padx=20) 
        self.var1=IntVar() #holds value of radio buttons
        
        #label for username
        self.user_label=Label(self.quiz_frame, text="What's your name?: ", font=("Tw Cen MT","16"),bg=background_color)
        self.user_label.grid(row=1, padx=20, pady=20) 
        
        #entry box
        self.entry_box=Entry(self.quiz_frame)
        self.entry_box.grid(row=2,padx=20, pady=20)
        
        #continue button
        self.continue_button = Button(self.quiz_frame, text="Continue", font=("Comic Sans MS", "13", "bold"), bg="yellow", command=self.name_collection)
        self.continue_button.grid(row=3,  padx=20, pady=20)        
        
      #image
      #logo = PhotoImage(file="road.gif")
      #self.logo = Label(self.quiz_frame, image=logo)  
      #self.logo.grid(row=4,padx=20, pady=20) 
       

    def name_collection(self):
        name=self.entry_box.get()
        name.append(name) #add name to names list declared at the beginning
        self.continue_button.destroy()
        self.entry_box.destroy() #Destroy name frame then open the quiz runner
      
           

if __name__ == "__main__":
    root = Tk()
    root.title("NZ Road Rules Quiz") 

    quiz_instance = Quiz(root) #instantiation, making an instance of the class Quiz
    root.mainloop()#so the frame doesnt dissapear
 
  
   #starting point of our program

randomiser()
if __name__ =="__main__":
    root = Tk()  #create the window 
    root.title("NZ Road Rules Quiz")   #title of the window
    quiz_instance = QuizStarter(root)
    root.mainloop()  #so the window doesn't disappear   


"""Whenever the Python interpreter reads a source file, it does two things:

it sets a few special variables like __name__, and then
it executes all of the code found in the file.

If you are running your module (the source file) as the main program, e.g. guiQuizPart1.py
the interpreter will assign the hard-coded string "__main__" to the __name__ variable

global questions_and_answers
name_list = []
asked = []
score = 0
"""

""""