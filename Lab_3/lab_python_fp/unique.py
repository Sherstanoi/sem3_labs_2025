from gen_random import Gen_random

class Unique():
    def __init__(self,object,ignore_case = False, **kwargs):
        self.ignore_case = ignore_case
        self.data = object
        self.answer = []
        self.limit = 1
        self.counter = 0

    def __next__(self):
        if(self.counter == self.limit):
            raise StopIteration
        if (self.ignore_case):
            for i in self.data:
                if(isinstance(i,str)):
                    if(not(i.lower() in self.answer)):
                       self.answer.append(i.lower())
            self.counter += 1
            return self.answer
        else:
            for i in self.data:
                if(not(i in self.answer)):
                   self.answer.append(i)
            self.counter += 1
            return self.answer

    def __iter__(self):
        return self