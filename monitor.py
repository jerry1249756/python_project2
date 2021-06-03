class monitor:
    def __init__(self, str):
        self.data=[]
        quo=len(str)/10
        rem=len(str)%10

        chunks = [str[i:i+10] for i in range(0, len(str), 10)]
        if len(chunks)==1:
            self.data=[[char for char in str],[0 for i in range(10)],[0 for j in range(10)]]
            for i in range (10-rem):
                self.data[0].append(0)
        elif len(chunks)==2:
            self.data=[[char for char in chunks[0]],[char for char in chunks[1]],[0 for j in range(10)]]
            for i in range (10-rem):
                self.data[1].append(0)
        else: 
            self.data=[[char for char in chunks[0]],[char for char in chunks[1]],[char for char in chunks[2]]]
            for i in range (10-rem):
                self.data[2].append(0)

def main():
    print("please input the string that wants to demonstate:")
    line=input()
    a = monitor(line)
    print(a.data)    

if __name__ == '__main__':
    main()