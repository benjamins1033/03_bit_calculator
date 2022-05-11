from cgitb import text


def statement_generator(text, decoration) :

    ends = decoration * 5

    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


def user_choice():
    text_ok = ["text", "t", "txt"]
    integer_ok = ["integer", "int", "#", "number"]
    image_ok = ["image", "img", "pix", "picture", "pic"]

    valid = False
    while not valid:

        response = input("file type (integer / text / image): ").lower()

        if response in text_ok:
            return "text"

        elif response in integer_ok:
            return "integer"
        
        elif response in image_ok:
            return "image"
        
        elif response == "i":
            want_integer = input("press <enter> for an integer or any key for an image: ")
            if want_integer == "":
                return "integer"
            else:
                return "image"
        
        else:
            print("please choose a valid file type")
            print()


def num_check(question, low):
    valid = False
    while not valid:

        error = "please enter an integer that is more than "
        "(or equal to) {}".format(low)

        try: 

            response = int(input(question))

            if response > low:
                return response
            
            else:
                print(error)
                print() 

        except ValueError: 
            print(error)

statement_generator("Bit Calculator for Integers, Text & Images", "-")



keep_going = ""
while keep_going == "":
    
    data_type = user_choice()
    print("you chose", data_type)

    if data_type =="integer":
        var_integer = num_check("enter an integer: ", 0)
        
    elif data_type == "image":
         image_width = num_check("image width? ", 1)
         print()
         image_height = num_check("image height? ", 1)
         
    else:
        var_text = input("enter some text: ")



