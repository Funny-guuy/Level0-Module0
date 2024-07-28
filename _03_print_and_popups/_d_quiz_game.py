from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
        # Make a new window variable, window = Tk()
            window = Tk()
        # Hide the window using the window's .withdraw() method
            window.withdraw()
        # 1. Create a variable to hold the user's score. Set it equal to zero.
            score = 0
# ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
            answer = simpledialog.askstring(title = 'quizbot', prompt = "what is 5+10")
    #      // 3.  Use an if statement to check if their answer is correct
            if answer == "15":
                messagebox.showinfo(title = "quizbot" ,message = "Correct")
                score = score + 15
            else:
                messagebox.showinfo(title = "quizbot" ,message = "INCORRECT")
    #      // 4.  if the user's answer was correct, add one to their score 
            answer = simpledialog.askstring(title = 'quizbot', prompt = "what is 2+49")
    #      // 3.  Use an if statement to check if their answer is correct
            if answer == "51":
                messagebox.showinfo(title = "quizbot" ,message = "Correct")
                score = score + 51
            else:
                messagebox.showinfo(title = "quizbot" ,message = "INCORRECT")

            answer = simpledialog.askstring(title = 'quizbot', prompt = "what is 7+157")
    #      // 3.  Use an if statement to check if their answer is correct
            if answer == "174":
                messagebox.showinfo(title = "quizbot" ,message = "Correct")
                score = score + 174
            else:
                messagebox.showinfo(title = "quizbot" ,message = "INCORRECT")
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
            messagebox.showinfo(title = "quizbot", message = "your score is " + str(score))
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    
    # Run the window's .mainloop() method
            window.mainloop()
