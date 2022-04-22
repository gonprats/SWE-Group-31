option = 0
while option != "5":
    
    print("Welcome to Unimake rating system, select one of the options offered below:")
    print("1. Rate a teammate")
    print("2. See past ratings")
    print("3. Modify a rating")
    print("4. See my rating")
    print("5. Exit")

    option = input("Select number: ")

    if option == "1":
        tm_name = input("Introduce teammate's name: ")
        rf = open("rating_sheet.txt", 'a+')
        fileFull = rf.read()
        rf.close()
        if tm_name not in fileFull:
            rf = open('rating_sheet.txt', 'a+')
            tm_rating = input("Introduce the rating for your teammate: ")
            fullString = tm_name + " " + str(tm_rating) + "\n"
            rf.write(fullString)
            rf.close()
            print("Teammate rated! Going back to home page...")
        else:
            print("Sorry, you have already ranked your teammate. Going back to home page...")
    
    elif option == "2":
        rf = open('rating_sheet.txt', 'r+')
        print("Here is a list of all your past ratings:")
        print(rf.read())
        rf.close()

    elif option == "3":
        tm_name = input("Introduce the name of the teammate: ")
        rf = open("rating_sheet.txt", 'r+')
        fullFile = rf.readlines()
        found = False
        for i in range(len(fullFile)):
            if tm_name in fullFile[i]:
                remove_line = fullFile[i]
                found = True
        rf.close()
        if found:
            with open("rating_sheet.txt", "r+") as rf:
                d = rf.readlines()
                rf.seek(0)
                for i in d:
                    if i != remove_line:
                        rf.write(i)
                rf.truncate()
            tm_rating = input("Introduce the new rating: ")
            new_line = tm_name + str(tm_rating) + "\n"
            rf.write(new_line)
            rf.close()
        else:
            print("Teammate not found or not rated before. Going back to home page...")
        
    elif option == "4":
        # We need to figure out how to obtain one's own username from
        # the SQL database so that we can look up one's rating
        pass

    elif option == "5":
        print("Exiting...")
