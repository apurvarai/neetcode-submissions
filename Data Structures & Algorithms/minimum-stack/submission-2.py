class MinStack:

    def __init__(self):
        self.st=[]
        self.minst=[]       

    def push(self, val: int) -> None:
        self.st.append(val)
        if len(self.minst) and self.minst[-1]>=val:
            self.minst.append(val)
        if len(self.minst)==0:
            self.minst.append(val)

    def pop(self) -> None:
        c=self.st.pop()
        if self.minst[-1]==c:
            self.minst.pop()
    
    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        # if len
        return self.minst[-1]
        
