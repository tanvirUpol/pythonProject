import courses_info as courses

while True:
    choice = input("\n\n Choose you options:\n\n 1.Add new course \n 2.Update course \n 3.Delete course \n 4.Display course \n 5.Search course \n 6.Store course \n 0.Quit App \n Enter your option: ")
    if choice== "1":
        courses.add_course()
    elif choice== "2":
        courses.update_course()
    elif choice == "3":
        courses.delete_course()
    elif choice == "4":
        courses.display()
    elif choice == "5":
        courses.search_course()

    elif choice == "6":
        courses.store()
    elif choice == "0":
        break
    else:
        print("wrong input")
