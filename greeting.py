class greeting:
    def __init__(self, args):
        # Check if the args supplied is a string
        if (type(args) == str):
            self.message = args
        else:
            print("Please supply a string for greeting")


    def hello(self):
        try:
            print(self.message)
        except:
            print("Something went wrong. Please contact the developer.")