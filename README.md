# Book_Directory
Book Directory is an interactive book list that allows users to store books information in list organized using different identifiers which are:
Name of the book
Name of the Author
Year Published
ISBN of the book
The graphical interface allows the user to interact with the data without understanding how the code behind the GUI works. The interface includes 4 entry boxes indicated by labels where user can input their set of 4 identifiers mentioned above to add create a completed book feature into the directory for later use.
The buttons that allow the user to interact with the directory are:
View All
Shows the whole directory sorted by order of entry in the list when pressed View All.
Search Entry
If a complete version of search description is inputted into any of the entry boxes, the query will display if it exists when pressed Search Entry.
If the input in any of entry boxes are a incomplete version of the correct entry the user is looking for the search function will not be able to find it.
Add Entry
After inputting the book identifiers, pressing the Add Entry adds to the query.
Updated list will be shown after View All is pressed again.
Update Selected
If any of the book identifiers need to be updated. Pull up the query using search entry or view all directory to bring up the book. Then change any information needed to be changed. Update Selected will update the row with the newly changed information within the directory.
Updated row will be shown after View All is pressed again or searched for directly.
Delete Selected
If any rows need to be deleted. Pull up the book using the selection from View All or search for the book and simply press Delete Selected to delete the query.
Updated list will be shown after View All is pressed again.
Close
To close the program, press Close
The backend of this project utilized Tkinter which is a GUI library created for python that gave this program a interactive look with buttons and entry boxes.
The data entered in entry boxes, retrival of book, and commands for each button was intergrated with SQLite3 to store data and interact with the data based on the buttons pressed.
