class bye:

    def bye(self,args):
        if (type(args) == str):
            print(self.message)
        else:
            print("Please supply a string for greeting")