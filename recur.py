def recString(inps):
    if(inps==""):
        return
    elif(len(inps)==1):
        return(inps)
    else:
        nextVal=recString(inps[1:])
        if(nextVal!=None):
            if(inps[0]==nextVal[0]):
                return(nextVal)
            else:
                return(inps[0]+nextVal)
    
print(recString("aaabbbbccb"))