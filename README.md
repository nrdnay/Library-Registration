## The features of this simple library registration system built with Python

**1. Tasks:**
• Create a Base Class: LibraryItem
• Purpose: To contain common properties (title, publication year) of all library items.

• Requirements:
• Create the LibraryItem class.
• Define parameters such as title and publication_year in the constructor method.
• Print the basic information of the item to the screen with the display_info method.

**2. Book and Magazine Classes (Inheritance)**
• Purpose: Add custom properties based on the LibraryItem class.

• For Book:
• Create the Book class and inherit from the LibraryItem class.
• Add additional author information.
• Redefine the display_info method to display the basic information first, then the author information.
• For Magazine:
• Create the Magazine class and inherit from the LibraryItem class.
• Add additional issue information.
• Redefine the display_info method to display the basic information first, then the issue of the magazine.

**3. Mixin Class for Digital Features: DigitalItem**
• Purpose: To provide the downloadable feature of digital content.

• Requirements:
• Create a mixin class named DigitalItem.

• Define the download method in this class and print a message indicating that the item has been downloaded when called.

**4. E-Book Class: Multiple Inheritance (Book and DigitalItem)**
• Purpose: To combine both the book features and the digital content features.

• Requirements:
• Create the EBook class and derive it from the Book and DigitalItem classes using multiple inheritance.

• Additionally, add the file_size information.

• Redefine the display_info method to display the book information and file size.

• After creating the e-book object, have students test the digital downloadable feature by running the download method.
**5. Library Member Class: Member**
• Purpose: To manage the borrowing and returning processes of library members.
• Requirements:
• Create the Member class.
• Define the name, borrowed_items (list of borrowed items) and borrow_limit (maximum number of borrowed items) properties for each member.
• borrow_item method: Allow the member to borrow an item without exceeding the specified limit.
• return_item method: Allow the member to return the items they borrowed.
• display_borrowed method: List all the items the member has borrowed.
**6. Testing and Implementation**
• Purpose: To test that the developed classes and methods work correctly.
• Requirements:
• Create different types of library items (books, magazines, e-books) and print the information on the screen with the display_info methods.
• Test the digital download process by running the download method for the EBook object.
• Create a Member object and test limit checking, borrowing and returning by borrowing different items.

• Finally, list the items that the member borrowed on the screen.
