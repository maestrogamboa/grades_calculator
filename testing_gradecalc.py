# Python program to create a simple GUI 
# calculator using Tkinter 

# import everything from tkinter module 
from tkinter import *


# create a GUI window 
gui = Tk() 


# Function to update expressiom 
# in the text entry box 
def determine_grd(average): 
    """
        function to calculate letter grd as per average
        @Param: Average weighted score    
        Return: Letter grd  
    """
    if average >= 89.45:
        return "A"
    elif average >= 79.45:
        return "B"
    elif average >= 69.45:
        return "C"
    elif average >= 59.45:
        return "D"
    else:
        return "F"


# Function to evaluate the final expression 
def calc_average(): 
    """
        function to calculate weighted average
        @Param: Marks of different exms and categories     
        Return: weighted average with letter grd  
    """
    # initialize
    avg = 0

    # if all marks are float/ integer the calculate
    # or throw exception 
    try:
        disc = float(discStr.get())
        revel = float(revelStr.get())
        quiz = float(quizStr.get())
        prog = float(projectStr.get())
        exm1 = float(exm1Str.get())
        fexm = float(finalStr.get())

        # calculate
        avg = avg + disc * 0.05
        avg = avg + revel * 0.15
        avg = avg + quiz * 0.15
        avg = avg + prog * 0.15
        avg = avg + exm1 * 0.20
        avg = avg + fexm * 0.30

        # find the grd
        grd = str(round(avg, 2))+"/"+determine_grd(avg)

        # set value
        resultStr.set(grd)

    except:
        messagebox.showinfo("Error!", "Non-Numeric or Blank Data Eneterd") 



def clear_entries():
    """
        function to clear all the field
        @Param:   
        Return:  
    """
    discStr.set("")
    revelStr.set("")
    quizStr.set("")
    projectStr.set("")
    exm1Str.set("")
    finalStr.set("")
    resultStr.set("")
    

def quit_program():
    """
        function to quit window
        @Param:   
        Return:  
    """
    gui.destroy()
    

# Driver code 
if __name__ == "__main__": 

        # set title of GUI window 
        gui.title("Weighted Average/grd Calculator") 

        # set size of GUI window
        gui.geometry("400x400") 

        # header of GUI window
        introLabel = Label(gui, text = "Enter your raw score for the following assignments and exams:")
        introLabel.grid(columnspan=2, rowspan = 2)
        
        discLabel = Label(gui, text = "\t\tDiscussions (5 % of total)")
        discLabel.grid(row=2, column=0, columnspan=1)
        discStr = StringVar() 
        discEntry = Entry(gui, textvariable = discStr)
        discEntry.grid(row=2, column=1, columnspan=2)
        
        revelLabel = Label(gui, text = "\t\tRevel Labs (15 % of total)")
        revelLabel.grid(row=3, column=0, columnspan=1)
        revelStr = StringVar()
        revelEntry = Entry(gui, textvariable = revelStr)
        revelEntry.grid(row=3, column=1)
        
        quizLabel = Label(gui, text = "\t\t     Quizzes (15 % of total)")
        quizLabel.grid(row=4, column=0)
        quizStr = StringVar()
        quizEntry = Entry(gui, textvariable = quizStr)
        quizEntry.grid(row=4, column=1)

        projectLabel = Label(gui, text = "\t     Program/Project (15 % of total)")
        projectLabel.grid(row=5, column=0)
        projectStr = StringVar()
        projectEntry = Entry(gui, textvariable = projectStr)
        projectEntry.grid(row=5, column=1)

        exm1Label = Label(gui, text = "\t\t       Mid-Term Exam (20 % of total)")
        exm1Label.grid(row=6, column=0)
        exm1Str = StringVar()
        exm1Entry = Entry(gui, textvariable = exm1Str)
        exm1Entry.grid(row=6, column=1)

    
        finalLabel = Label(gui, text = "\t\tFinal exm (30 % of total)")
        finalLabel.grid(row=8, column=0)
        finalStr = StringVar()
        finalEntry = Entry(gui, textvariable = finalStr)
        finalEntry.grid(row=8, column=1)

        blankLabel = Label(gui, text = "")
        blankLabel.grid(row=9)

        calButton = Button(gui, text='Calculate Weighted Average/grd', fg='black',\
                           command=lambda: calc_average())
        #disc, revel, quiz, prog, exm1, exm2, fexm
        calButton.grid(row=10, column=0)
        resultStr = StringVar()
        resultLabel = Label(gui, textvariable = resultStr, borderwidth=2, relief="solid", width = 12)
        resultLabel.grid(row=10, column=1)

        blank1Label = Label(gui, text = "")
        blank1Label.grid(row=11)

        clearButton = Button(gui, text=' Clear ', fg='black', command=lambda: clear_entries())
        clearButton.grid(row=12, column=0, sticky= E)
        clearButton.columnconfigure(1, weight = 1)

        quitButton = Button(gui, text=' Quit ', fg='black', command=lambda: quit_program())
        quitButton.grid(row=12, column=1, sticky= W)
        quitButton.columnconfigure(1, weight = 1)

        # start the GUI 
        gui.mainloop() 
