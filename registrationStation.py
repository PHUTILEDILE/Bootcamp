"""
Registration Station project
"""

def read_file(file_name):
    
    """
    Read and return contents of text file
    """
    file_name = "bootcampers.txt"
    f = open(file_name,"r")
    content = f.readlines()
    return content


def input_user_name():

    """
    Takes username as input
    """
    username = input("Select username: ")
    return username
    


def correct_or_incorrect():
 
    """
    Prompt to ask if details are correct or not
    @return correct or incorrect
    """
    correct_data = input("Is this correct? (Y/n): " )
    if correct_data.lower() == "y":
        return "correct"
    elif correct_data.lower() == "n":
        return "incorrect"    
    
    

def correct_details():

    """
    Prompt to correct and write user details to text file, which includes:
    * Username
    * Date
    * Location
    * Experience
    """
    details = input("Username - Date - Location - Experience: ")
    user_name = details.split(" - ")[0]
    data_file = read_file("bootcampers.txt")
    writing_data = ""
    
    for det in data_file:
        if det.split(" - ")[0] == user_name:
            writing_data += details + "\n"
        else:
            writing_data += det
        
    # print(writing_data)
    
    with open("bootcampers.txt","w") as fil_name:
        fil_name.write(writing_data)
        
    print(details.split(" - ", 1)[1].strip())

    

def get_file_contents():

    """Return desired text file"""
    


def find_username(file_name):

    """
    Main functiontion for running Registration Station, which inlcude:
       * get username input from user
       * check if username exists and print corresponding details
    @return corresponding information for username
       """
    file_data = read_file("bootcampers.txt")
    input_function = input_user_name()
    num = 0
    while not False:
        for i in file_data:
            num = num + 1 
            if input_function in i:
                i = i.split("-",1)
                print(i[1].strip())
                return i[1]
            elif num == len(file_data):
                break 
        print("Please enter valid existing username")
        input_function = input_user_name()
    


 
if __name__ == "__main__":
    registrations_file = get_file_contents()
    information = find_username(registrations_file)
    while True:
        answer = correct_or_incorrect()
        if answer == "correct":
            print(information)
            break
        else:
            correct_details()
