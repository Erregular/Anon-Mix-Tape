#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import Tkinter 
import tkMessageBox

class loginToSpotifyApp (Tkinter.Tk):
    def __init__(self, parent):
        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()
                
        
        
    def initialize(self):
        self.grid()
        
        #Local varibles for username and password info
        self.userNameVariable = Tkinter.StringVar()
        self.passwordVariable = Tkinter.StringVar()
        
        #Add username entry elements
        UserNameLabel = Tkinter.Label(self)
        UserNameLabel["text"] = "Username: "
        UserNameLabel.grid(column=0, row=0, sticky='EW')
        
        UserNameEntryBox = Tkinter.Entry(self, textvariable=self.userNameVariable)
        UserNameEntryBox.grid(column=1, row=0, sticky='EW')
                 
        #Add password entry elements
        PasswordLabel = Tkinter.Label(self)
        PasswordLabel["text"] = "Password: "
        PasswordLabel.grid(column =0, row=1)
            
        PasswordEntryBox = Tkinter.Entry(self, show="*", textvariable=self.passwordVariable)
        PasswordEntryBox.grid(column =1, row=1)
        
        #Add button/action elements
        LoginButton = Tkinter.Button(self, text = u"Login to Spotify...")
        LoginButton["text"] = "Login to Spotify..."
        LoginButton["command"] = self.doLogin
        LoginButton.grid(column =0, row=2)
        
        quitButton = Tkinter.Button(self)
        quitButton["text"] = "QUIT"
        quitButton["command"] =  self.quit
        quitButton.grid(column =1, row=2)
        
        #Paint widgets and ready for input
        self.grid_columnconfigure(0,weight=1)
        self.resizable(False, False)
        UserNameEntryBox.focus_set()
        UserNameEntryBox.selection_range(0, Tkinter.END)
    
    # Perform validation on login details enter and start Spotify login
    def doLogin(self):
        
        #Get the user credentials and put into local varbiles
        userCredentials = [self.userNameVariable.get(), self.passwordVariable.get()]
        
        print "Username = " + userCredentials[0]
        print "Password = " + userCredentials[1]
        
        if userCredentials[0] == "" or userCredentials[1] == "":
            tkMessageBox.showerror ("Error...", "You must entry both a Username and Password.  Please try again...!")
            return 
        else:
            tkMessageBox.showinfo("OK...", "We have something to work with")
            return userCredentials
            

#Main App
if __name__ == "__main__":
        app = loginToSpotifyApp(None)
        app.title('Login in to Spotify...')
        app.mainloop()
        

