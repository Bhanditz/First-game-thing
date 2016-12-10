import random
import sys

from tkinter import*
from tkinter import ttk

class MyGame:
    def __init__(self):
        # Create the main window widget.
        root = Tk()
        root.geometry('{}x{}'.format(100, 100))

        #Put label. for the window
        labelText = StringVar()
        labelText.set('Dont die.')

        message = Message(root,text='Dont die.')
        message.pack(side='top')
               
        # Create a Button widget. 
        # should appear on the face of the Button. The
        # do_something method should be executed when
        # the user clicks the Button.
        self.my_button = Button(root, \
                                        text='Start', \
                                        command=self.do_something)
        
        
        
        # Pack the Button.
        self.my_button.pack(side = 'bottom',fill='both')

        
        
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
        button1 = Button(top,text='Run',command=self.run)
        button.pack()
        button1.pack()

    #The hit option trys to hit the troll
    def hit(self):
    
        top = Toplevel()
        top.title('Dont die.')

        hit_miss = random.randint(0,99)

        if hit_miss >= 50:
            message = Message(top, text='You hit the troll and you dun pissed it off.')
            message1 = Message(top, text='The troll loses 50% life.')
            
            message1.pack(side='bottom')
            message.pack()
            
            button = Button(top,text='Next',command=self.troll50)
            button.pack()
        elif hit_miss<20:
            message = Message(top,text='You killed the troll you monster he had children.')
            message.pack()
            
            button = Button(top,text='Next',command=self.win)
            button.pack()
        elif hit_miss>=20 and hit_miss<50:
            message = Message(top,text='You missed')
            message1 = Message(top, text='The troll clubs you in the face.')
            message2 = Message(top, text='YOU DIED!')

            message.pack()
            message1.pack()
            message2.pack()
            
            button = Button(top, text='Next.',command=self.death)
            button.pack()


    #Block funtion trys to block the trolls attack
    def run(self):
        top = Toplevel()
        top.title('Dont die.')

        run = random.randint(0,4)

        if run>2:
            message = Message(top, text="You run away from the troll.")
            message.pack()
            
            button = Button(top, text='Next.',command=self.nothing)
            button.pack()
        else:
            message = Message(top, text='The troll clubs you in the face.')
            message1 = Message(top, text='YOU DIED!')
            message.pack()
            message1.pack()

            button = Button(top, text='Next.',command=self.death)
            button.pack()

    def troll50(self):
        top = Toplevel()
        top.title('Dont die.')
        
        message = Message(top, text='The wounded troll stands before you. He is on high alert and wont let you run away.')
        message.pack()
        button = Button(top, text='Hit.',command=self.hit2)
        button.pack()

    def hit2(self):
        top = Toplevel()
        top.title('Dont die.')

        hit_miss = random.randint(0,1)

        if hit_miss==1:
            message = Message(top, text='You have defeated the troll and have won the game.')

            message.pack()
            button = Button(top,text='Next',command=self.win)
        else:
            message = Message(top,text='You get clubbed in the face.')
            message1 = Message(top,text='YOU DIED')

            message.pack(side='top')
            message1.pack(side='bottom')

            button = Button(top, text='Next.',command=self.death)
            button.pack()

    def death(self):
        top = Toplevel()
        top.title('Dont die.')
        
        message = Message(top,text='You died to the troll and lost.', fg='red')
        message.pack()

        button = Button(top,text='Quit',command=self.quit)
        button.pack()

    def quit(self):
        sys.exit()

    def win(self):
        top = Toplevel()
        top.title('Dont die.')

        message = Message(top, text='You have won the game.', fg='blue')
        message.pack()
                               
        button = Button(top,text='Quit',command=self.quit)
        button.pack()

    def nothing(self):
        top = Toplevel()
        top.title('Dont die.')

        message = Message(top, text='You run away and never come back.')
        message.pack()

        button = Button(top,text='Quit',command=self.quit)
        button.pack()

my_game = MyGame()
