class Castmurange:
    def __init__(self,strat, end,step=None):
        self.current=strat
        self.end=end
        self.step=step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current<=self.end:
            result=self.current
            if self.step is None:
                self.current+=1
            else:
                self.current+self.step
            return result
        else:
            raise StopIteration

for num in Castmurange(4,15):
    print(num)
