# Create a Book class, that has an author, a title and a release year
# Create a constructor for setting those values
# Book should be represented as string in this format:
# Douglas Adams : The Hitchhiker's Guide to the Galaxy (1979)
# Create a BookShelf class that has a list of books in it
# We should be able to add and remove books.
# We should be able to query the favourite author (who has written the most books in the shelf)
# We should be able to query the earliest published books.
# We should be able to query the latest published books.
# Bookself should have a method whitch give us information about the number of books, the earliest and the latest released books, and the favourite author 
   
myshelf = BookShelf()
print(myshelf)
# Should print out:
# You have no books here.
    
myshelf.put("Douglas Adams", "The Hitchhiker's Guide to the Galaxy", 1979)
myshelf.put("Douglas Adams", "Mostly Harmless", 1992)
myshelf.put("Frank Herbert", "Dune", 1965)
myshelf.put("Frank Herbert", "The Dragon in the Sea", 1957)
myshelf.remove("The Dragon in the Sea")

print(myshelf)
# Should print out:
# You have 3 books.
# Earliest released: Frank Herbert : Dune (1965)
# Latest released: Douglas Adams : Mostly Harmless (1992)
# Favourite author: Douglas Adams