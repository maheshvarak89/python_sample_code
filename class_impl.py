class Human:
    # class variable
    hm = "I am class variable"

    # Initialize values
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    # public method of a class
    def do_work(self):
        if self.occupation == 'Actor':
            print(self.name, ' acts in film')
        elif self.occupation == 'Tennis':
            print(self.name, ' plays tennis')
        else:
            print('Invalid occupation')


# Creating object of a class
tom = Human('Tom', 'Actor')
tom.do_work()

# Creating object of a class
maria = Human('Maria', 'Tennis')
maria.do_work()