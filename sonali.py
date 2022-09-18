def fun(st):
        #write code here
        words=st.split(" ")
        stri=[]
        for i in words:
            lets=[letter for letter in i]
            lets=lets[::-1]
            w="".join(lets)
            w=w.capitalize()
            stri.append(w)
        return(stri)

# print(" ".join(fun(input())))

def fun2(input1):


        #write code here
        ops=input1.split("/")
        stak=0
        for i in ops:
            if i == "..":
                if stak>0:
                    stak-=1
            elif i == ".":
                pass
            elif i == " ":
                pass
            else:
                stak+=1
        return(str(stak))

def fun3(input1,input2):
        #write code here
        s=[sum(input2) for i in input2]
        for i in range(0,len(input2)):
            s[i]=sum(input2[:i])+sum([-i for i in input2[i:]])
            print(s)
        return(max(s))

def fun4(input1,input2):
        #write code here
        av = sum(input2)/input1
        dif=0
        for i in input2:
            dif+= abs(av-i)
        return(int(dif/2))

print(fun3(5,[-5,4,3,2]))