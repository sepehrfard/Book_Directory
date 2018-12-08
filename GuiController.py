
from tkinter import *

from my_module import DbConnection

"""""
Book Directory: 

This is the GUI and controller of this program. The GUI is set up within this 
class and commands are called from dbConnection file. 

"""""
class Window(object):

    # creates the window, labels and buttons
    def __init__(self, root):
        self.root = root
        self.root.wm_title("Book Directory")

        # creates the window canvas
        window = Frame(root)
        # using grid style for the layout
        window.grid(padx=10, pady=10, sticky=N + S + E + W)

        # creating labels for input boxes
        label_title = Label(window, text="Title")
        # position of the label
        label_title.grid(row=0, column=0, sticky=W)

        label_author = Label(window, text="Author")
        # position of the label
        label_author.grid(row=0, column=3, sticky=W)

        label_year = Label(window, text="Year")
        # position of the label
        label_year.grid(row=1, column=0, sticky=W)

        label_isbn = Label(window, text="ISBN")
        # position of the label
        label_isbn.grid(row=1, column=3, sticky=W)

        # creating entry box for title
        self.title_text = StringVar()
        self.entry_title = Entry(window, textvariable=self.title_text)
        # position of the entry box
        self.entry_title.grid(row=0, column=1, sticky=W)

        # creating entry box for author
        self.author_text = StringVar()
        self.entry_author = Entry(window, textvariable=self.author_text)
        # position of the entry box
        self.entry_author.grid(row=0, column=4, sticky=W)

        # creating entry box for year
        self.year_text = StringVar()
        self.entry_year = Entry(window, textvariable=self.year_text)
        # position of the entry box
        self.entry_year.grid(row=1, column=1, pady=5, sticky=W)

        # creating entry box for isbn
        self.isbn_text = StringVar()
        self.entry_isbn = Entry(window, textvariable=self.isbn_text)
        # position of the entry box
        self.entry_isbn.grid(row=1, column=4, pady=5, sticky=W)

        # creates list box to show directory
        self.list_box = Listbox(window, height=10, width=40)
        # position of the entry box
        self.list_box.grid(row=2, column=0, rowspan=6, columnspan=5,
                           sticky=N + S + E + W)

        # vertical scroll bar
        scrll_bar_y = Scrollbar(window)
        scrll_bar_y.grid(row=2, column=5, rowspan=6, sticky=N + S)

        # configuring vertical scroll bar to be used for the listbox
        self.list_box.configure(yscrollcommand=scrll_bar_y.set)
        scrll_bar_y.configure(command=self.list_box.yview)

        # horizontal scroll bar
        scrll_bar_x = Scrollbar(window, orient=HORIZONTAL)
        scrll_bar_x.grid(row=8, column=0, columnspan=5, sticky=W + E )

        # configuring horizontal scroll bar to be used for the listbox
        self.list_box.configure(xscrollcommand=scrll_bar_x.set )
        scrll_bar_x.configure(command=self.list_box.xview )

        # able to select a row in listBox
        self.list_box.bind('<<ListboxSelect>>', self.get_selected_row)

        # creates view button
        view = Button(window, text = "View All", width = 12,
                      command = self.view_command)
        # position of the button
        view.grid(row = 0, column = 6, sticky = N + S + E + W)

        # creates search button
        search = Button(window, text = "Search Entry", width = 12,
                        command = self.search_command)
        # position of the button
        search.grid(row=1, column=6, sticky=N + S + E + W)

        # creates search button
        add = Button(window, text="Add Entry", width=12,
                     command=self.add_command)
        # position of the button
        add.grid(row=2, column=6, sticky=N + S + E + W)

        # creates search button
        update = Button(window, text="Update Selected", width=12,
                        command=self.update_command)
        # position of the button
        update.grid(row=3, column=6, sticky=N + S + E + W)

        # creates search button
        delete = Button(window, text="Delete Selected", width=12,
                        command=self.delete_command)
        # position of the button
        delete.grid(row=4, column=6, sticky=N + S + E + W)

        # creates search button
        close = Button(window, text="Close", width=12, command=window.quit)
        close.grid(row=5, column=6, sticky=N + S + E + W)

    # based on which row is selected displays each section in appropriate box
    def get_selected_row(self, event):
        # used to get tuples with of info based on category
        global selected_tuple

        # throws exception if double clicked on entry box
        try:
            # tries to get index and tuple
            index = self.list_box.curselection()[0]
            selected_tuple=self.list_box.get(index)

        # catches errors resulting from double clicking
        except IndexError:
            pass
        except UnboundLocalError:
            pass

        # returns values to show on the title box
        self.entry_title.delete(0, END)
        self.entry_title.insert(END, selected_tuple[1])

        # returns values to show on the author box
        self.entry_author.delete(0, END)
        self.entry_author.insert(END, selected_tuple[2])

        # returns values to show on the year box
        self.entry_year.delete(0, END)
        self.entry_year.insert(END, selected_tuple[3])

        # returns values to show on the isbn box
        self.entry_isbn.delete(0, END)
        self.entry_isbn.insert(END, selected_tuple[4])

    # view commands gets all rows of books and displays it in the list box
    def view_command(self):
        self.list_box.delete(0, END)

        # display row by row
        for row in DbConnection.view_all():
            self.list_box.insert(END, row)

    # can pull up a book by entering any of the 4 features of the book
    def search_command(self):
        self.list_box.delete(0, END)

        # searches by any 4 entries
        for row in DbConnection.search(self.title_text.get(), self.author_text.get(),
                                       self.year_text.get(),
                                       self.isbn_text.get()): self.list_box.insert(END, row)

    # add command inserts new row with the information given
    def add_command(self):
        # connects to database and inserts new data
        DbConnection.insert(self.title_text.get(), self.author_text.get(),
                            self.year_text.get(), self.isbn_text.get())
        self.list_box.delete(0, END)
        # self.list_box.insert(END, (self.title_text.get(), self.author_text.get(),
        #                         self.year_text.get(), self.isbn_text.get()))

    # delete command deletes a row when row is selected
    def delete_command(self):
        DbConnection.delete(selected_tuple[0])

    # when a row is updated with new information update will make new changes to the row
    def update_command(self):
        # connects to database and replaces old info with new
        DbConnection.update(selected_tuple[0], self.title_text.get(),
                            self.author_text.get(), self.year_text.get(),
                            self.isbn_text.get())

# used to run the class
root = Tk()
Window(root)
root.mainloop()
