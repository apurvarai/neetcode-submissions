class MinStack:

    def __init__(self):
        self.st=[]
        self.minstack=[]
        

    def push(self, val: int) -> None:
        self.st.append(val)
        if len(self.minstack) and self.minstack[-1]>=val:
            self.minstack.append(val)
        elif len(self.minstack)==0:
            self.minstack.append(val)
        

    def pop(self) -> None:
        c=self.st.pop()
        if self.minstack[-1]==c:
            self.minstack.pop()
        

    def top(self) -> int:
        return self.st[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]

        
