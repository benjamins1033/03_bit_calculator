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

keep_going = ""
while keep_going== "":
    print()
    var_integer = num_check("enter an integer: ", 0)
    print()

    image_width = num_check("image width? ", 1)
    print()
    image_height = num_check("image height? ", 1)