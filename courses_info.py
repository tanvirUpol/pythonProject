import json
filename = "courses.json"
courses = {}

try:
    with open(filename) as f:
        courses = json.load(f)
except FileNotFoundError:
    with open(filename , 'w') as f:
        json.dump(courses,f)



def add_course():
    code = input("Enter course code: ")
    course_status= check_course(code=code)
    if course_status:
        title = input("Enter course title: ")
        credit = input("Enter course credit amount: ")
        num_of_prerequisites = int(input("Enter the number of prerequisites you want: "))
        prerequisites = []
        if(num_of_prerequisites == 0):
            courses[code] ={"Code": code,
                            "Title": title,
                            "credit": credit,
                            "prerequisite": "None"}
        else:
            print("Enter prerequisite codes: ")
            for x in range(num_of_prerequisites):
                prerequisite = input()
                course_status= check_course(pre_req=prerequisite)
                if course_status:
                    prerequisites.append(prerequisite)
                    continue
                
                break
                
            if course_status:
                courses[code] ={"Code": code,
                                "Title": title,
                                "credit": credit,
                                "prerequisite": prerequisites}

                print("\nFiles saved successfully\n")
        
    


def search_course():
    search = input("\n Enter the course code you want to search: ")
    show_individual_course(search)
    
def check_course(code="",pre_req=""):
    if code:
        if code in courses:
            print(f"This course {code} already exists")
            return False
    elif pre_req not in courses:
        print(f"This course {pre_req} does not exists")
        return False

    return True
    


def display():
    print(f"\tCode\t\tTitle\t\tCredits\t\tPrerequisite")
    for details in courses.values():
        print("\n")
        for detail in details.values():
            print(f"\t{detail}\t",end="")
def store():
    with open(filename , 'w') as f:
        json.dump(courses,f)
    print("\nFile saved successfully\n")

def show_individual_course(search):
    if search in courses:
        course = courses[search]
        for key,val in course.items():
            print(f"Course {key}: {val} ")
        return course
    else:
        print("This course does not exist")
        return False

def update_course():
    update = input("\n Enter the course code you want to update: ")
    course = show_individual_course(update)
    if course is not False:
        del courses[course["Code"]]
        print("Update Course: \n")
        add_course()
        print("\nFiles updated successfully\n")

def delete_course():
    del_course = input("\n Enter the course code you want to delete:  ")
    course = show_individual_course(del_course)
    if course is not False:
        del courses[course["Code"]]
