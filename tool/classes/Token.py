###############################################################################
#                                                                             #
#  TOKEN CLASS                                                                #
#                                                                             #
###############################################################################

# The token class that handles the standard that is used to divide tokens into certain types.
class Token(object):

    # Method that whenever an object of the class has been created, assigns the values asked to their corresponding varuables(base method in python).
    def __init__(self, type, value):
        self.type = type
        self.value = value

    # Method returning the token as a string(base method in python).
    def __str__(self):
        return "Token({type}, {value})".format(type=self.type, value=repr(self.value))

    # Method returning the token as a string(base method in python).
    def __repr__(self):
        return self.__str__()