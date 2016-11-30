import random
from tkinter import*
from tkinter import ttk

class MyGame:
    def __init__(self):
        # Create the main window widget.
        root = Tk()

        #Put label. for the window
        labelText = StringVar()
        labelText.set('Dont die.')

        # Create a Button widget. 
        # should appear on the face of the Button. The
        # do_something method should be executed when
        # the user clicks the Button.
        self.my_button = Button(root, \
                                        text='Start', \
                                        command=self.do_something)

        
        
        # Pack the Button.
        self.my_button.pack()

        
        
        # Enter the Tkinter main loop.
        root.mainloop()

   
        
    def do_something(self):
        #Create a new window for the incounter
        top = Toplevel()
        top.title('Dont die.')
        
        #Display incounter
        message = Message(top, text='A troll stands before you what do you do?')
        message.pack()

        #Display options for user
        button = Button(top,text='Hit',command=self.hit)
        button1 = Button(top,text='Block',command=self.block)
        button.pack()
        button1.pack()

    #The hit option trys to hit the troll
    def hit(self):
    
        top = Toplevel()
        top.title('Dont die.')

        hit_miss = random.randint(0,99)

        if hit_miss >= 50:
            message = Message(top, text='You hit the troll and you dun pissed it off.')
            message.pack()
        elif hit_miss<20:
            message = Message(top,text='You killed the troll you monster he had children.')
            message.pack()
        elif hit_miss>=20 and hit_miss<50:
            message = Message(top,text='You missed')
            message.pack()

    #Block funtion trys to block the trolls attack
    def block(self):
        top = Toplevel()
        top.title('Dont die.')

        block = random.randint(0,4)

        if block>1:
            message = Message(top, text="You block the troll's attack.")
            message.pack()
        else:
            message = Message(top, text='The troll clubs you in the face.')
            message.pack()

        
        

# Create an instance of the MyGUI class.
my_gui = MyGame()
