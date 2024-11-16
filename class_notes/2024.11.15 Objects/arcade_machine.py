class ArcadeMachine:
    
    def __init__(self, name):

        self._name = name
        self._num_of_quarters = 0

    

    def insert_quarter(self):
        
        self._num_of_quarters += 1
        
        if self._num_of_quarters == 1:

            print(self._name + " now has " + str(self._num_of_quarters) + " quarter")

        else:
            print(self._name + " now has " + str(self._num_of_quarters) + " quarters")

        



