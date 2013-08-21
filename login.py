from Tkinter import *
import tkMessageBox

class Application(Frame):
    def loginToSpotify(self):
        print ("Let's attempt a login...")
        
        #get the login details into local varibles
        userName = self.UserNameEntryBox.get()
        password = self.PasswordEntryBox.get()
        
        #check for blank entries
        if userName == "" or password == "":
            tkMessageBox.showerror ("Error...", "You must entry both a Username and Password.  Please try again...!")
        else:
            tkMessageBox.showinfo("OK...", "We have something to work with")
            
    def createWidgets(self):
        
        self.UserNameLabel = Label(self)
        self.UserNameLabel["text"] = "Username: "
        
        self.UserNameLabel.pack()
        
        self.UserNameEntryBox = Entry(self)
        
        self.UserNameEntryBox.pack()
        
        self.PasswordLabel = Label(self)
        self.PasswordLabel["text"] = "Password: "
        
        self.PasswordLabel.pack()
        
        self.PasswordEntryBox = Entry(self, show="*")
        
        self.PasswordEntryBox.pack()
        
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.LoginButton = Button(self)
        self.LoginButton["text"] = "Login to Spotify..."
        self.LoginButton["command"] = self.loginToSpotify

        self.LoginButton.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
