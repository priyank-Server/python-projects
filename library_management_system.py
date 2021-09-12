class Library:

    def __init__(self, listofbooks, libraryname):
        self.userdata = {}
        self.listofbooks = listofbooks
        self.libraryname = libraryname

        for books in self.listofbooks:
            self.userdata[books] = None


    def displaybooks(self):
        for books in self.listofbooks:
            print(books)

    def withdrawbook(self, nm1, book):
        if book in self.listofbooks:
            if self.userdata[book] is None:
                self.userdata[book] = nm1
                print("done")
            elif self.userdata[book] == nm1:
                print("you already have that book")
            else:
                print(f" this book is already taken by {self.userdata[book]}.")
        else:
            print(f"Invalid book name!")

    def returnbook(self, nm2, book):
        if book in self.listofbooks:
            if self.userdata[book] is not None:
                if self.userdata[book] == nm2:
                    self.userdata[book] = None
                    print("done")
                else:
                    print("this book is not belongs to you")
            else:
                print("this book is not withdraw by anyone")
        else:
            print("invalid book")

    def addbook(self, nbook):
        self.listofbooks.appand(nbook)
        self.userdata[nbook] = None
        print("done")

    def deletebook(self, delbook):
        self.listofbooks.remove(delbook)
        self.userdata.pop(delbook)
        print("done")

    def showuser(self):
        print("books                 users\n")
        for bk in self.userdata:
            print(bk,"               ", self.userdata[bk])

def main():
    booksList = ["2666", "All About Love", "Desert Solitaire", "Geek Love", "Giovanni's Room", "The Handmaid's Tale"]
    libName = "OrangeRock Library"
    key = 7575

    lib1 = Library(booksList, libName)

    print("=" * 70)
    print(f"                    Welcome to {lib1.libraryname}")
    print("=" * 70)
    print("to display all books type 'd'")
    print("to withdraw a book type 'w'")
    print("to return a book type 'r'")
    print("to add a book type 'a'")
    print("to delete a book type 'del'")
    print("to check a books data type 'del'")
    print("to quit type 'del'")

    loop = True
    while loop == True:
        inp = input("option :")

        print("-" * 20)
        if inp == "d":
            lib1.displaybooks()

        elif inp == "w":
            nm1 = input("Enter Your Name :")
            bk2 = input("Enter Book Name :")
            lib1.withdrawbook(nm1, bk2)

        elif inp == "r":
            nm2 = input("Enter Your Name :")
            bk3 = input("Enter Book Name :")
            lib1.returnbook(nm2, bk3)

        elif inp == "a":
            bk2 = input("Enter Book Name")
            lib1.addbook(bk2)

        elif inp == "del":
            bk4 = input("Enter Book Name :")
            ky = input("Enter the key password :")
            if ky == key:
                lib1.deletebook(bk4)
            else:
                print("you don't have access")

        elif inp == "data":
            lib1.showuser()

        else:
            print("invalid input")
        print("-" * 20)

if __name__ == "__main__":
    main()
