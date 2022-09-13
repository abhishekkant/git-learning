class greeting:
    def __init__(self, args):
        # Check if the args supplied is a string
        if (type(args) == str):
            print(args)
        else:
            print("Please supply a string for greeting")