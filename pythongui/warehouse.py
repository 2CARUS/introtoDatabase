import tkinter as tk
# import pandas as pd 
# may be needed to display information from SQL
from mysql.connector import (connection)

theme = {
    '0':'#1a1e26',  # dusk
    '1':'#383f51',  # charcoal
    '2':'#dddbf1',  # azurish white
    '3':'#3c4f76',  # independence
    '4':'#d1beb0',  # dark vanilla
    '5':'#ab9f9d'   # rose quartz
}



# make a page
class Page(tk.Frame):
    # Frame is a rectangular area of a window
    # inherit page from Frame as a simple superclass to other Pages

    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master=master, cnf=cnf, **kw)
        '''
        auto-generated initializer method
         note: all tkinter objects need a master Frame/Window/Whatever
         with which to latch onto. see ROOT
        ''' 
    def show(self):
        self.lift()
        '''
        show will do the lift method, which lifts to the top of window
        stack
        ''' 

# Home Page
class Home(Page):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master=master, cnf=cnf, **kw)
        intro_text = 'Welcome! Please choose from the options above to navigate the warehouse'
        intro=tk.Label(self,text=intro_text)
        intro.config(font='none 12 bold',bg=theme['4'])
        intro.pack(side='right')
        boxCover = tk.Frame(self, bg=theme['4'])
        boxCover.pack(side='top')

# Simple record pull
class PKLookup(Page):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master=master, cnf=cnf, **kw)
        intro_text = '''
        Enter the unique ID of the tool you're searching for            
        '''
        intro = tk.Label(self,text=intro_text,bg=theme['5'],fg=theme['2'])
        intro.config(font='none 12 bold')
        intro.pack()



























# Main view window (initializes everything else)

class MainView(tk.Frame):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master=master, cnf=cnf, **kw)
        
        '''
        This mainview class may or may not be
        an actual main view. Instead of calling
        self.title(), it tries to pull from the toplevel
        structure (which could be itself) and change
        that title
        '''
        self.winfo_toplevel().title("Toolhouse Search")

        self.config(bg=theme['5'])
        # initialize pages
        p1 = Home(self)
        p2 = PKLookup(self)
        #   ...
        
        # initialize naviagation frames
        buttonframe = tk.Frame(self,bg=theme['5'])    # to hold buttons
        bannerframe = tk.Frame(self,bg='black',height='200',width='600')    # to hold the banner
        content = tk.Frame(self,bg=theme['2'],height='800')      # to hold the page-content stuff

        buttonframe.pack    (side="top", fill="x", expand=False)    # pack the buttons up top
        bannerframe.pack    (side='top',fill='y',expand=True)    # pack the banner up top
        content.pack      (side="top", fill="both", expand=True)  # put contianer underneath

        # placing pages inside content content
        p1.place(in_=content)
        # p2.place(in_=content, x=0,y=0,relwidth=.7,relheight=1)
        p2.place(in_=content)
        
        # create banner and put into bannerframe under the buttons
        banner = tk.PhotoImage(file='house.png')
        banner_label = tk.Label(bannerframe, image=banner)
        banner_label.image = banner
        banner_label.pack()

        # create buttons to navigate to pages
        b1 = tk.Button(buttonframe,bg=theme['3'],fg=theme['2'],command=p1.show,text='Home')
        b2 = tk.Button(buttonframe,bg=theme['3'],fg=theme['2'],command=p2.show,text='Single Tool Lookup')

        # packing buttons into button frame
        b1.pack(side='left')
        b2.pack(side='left')


        p1.show()

### Initialize 

'''
This file could be imported somewhere else later
A python convention is to check if it's the main,
then execute what should be main-type code stuff
'''


if __name__ == "__main__":
    square_side = 604
    size = str(square_side) + "x" + str(square_side)
    root = tk.Tk()
    # ROOT
    # proper tkinter programs have a root which the other
    #   frames(pieces of window) and widgets (things in frames)
    #   are rooted into
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry(size)
    root.mainloop()