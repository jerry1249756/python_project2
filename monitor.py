

class monitor:
    def __init__(self, str):
        self.data=[]
        self.screen=[[0 for i in range(13)]for j in range(24)]
        rem=len(str)%10

        chunks = [str[i:i+10] for i in range(0, len(str), 10)]
        if len(chunks)==1:
            self.data=[[char for char in str],[' ' for i in range(10)],[' ' for j in range(10)]]
            for i in range (10-rem):
                self.data[0].append(' ')
        elif len(chunks)==2:
            self.data=[[char for char in chunks[0]],[char for char in chunks[1]],[' ' for j in range(10)]]
            for i in range (10-rem):
                self.data[1].append(' ')
        else: 
            self.data=[[char for char in chunks[0]],[char for char in chunks[1]],[char for char in chunks[2]]]
            for i in range (10-rem):
                self.data[2].append(' ')

def main():
    print("please input the string that wants to demonstate:")
    line=input()
    a = monitor(line)
    print(a.data)
        

if __name__ == '__main__':
    main()