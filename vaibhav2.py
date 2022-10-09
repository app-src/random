from dis import dis


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

def workleft(work,f1,d1,f2,d2):
    return(work-(f1*d1)-(f2*d2))

def distance(Ax,Ay,Bx,By):
    return(min(Ax**2+Ay**2,Bx**2+By**2))

def AddTwoNumbers(list1,list2):
    #write your code here
    val1=""
    val2=""
    while list1.next!=None:
        val1+=str(list1.data)
        list1=list1.next
    val1+=str(list1.data)
    while list2.next!=None:
        val2+=str(list2.data)
        list2=list2.next
    val2+=str(list2.data)

    val1=int(val1)
    val2=int(val2)
    val3=val1+val2
    val3=str(val3)
    node=Node(int(val3[0]))
    list3=node
    print(val3[0])
    for i in range(1,len(val3)):
        list3.next=Node(int(val3[i]))
        print(val3[i])
        list3=list3.next

    return node



list1 = Node(1)
list1.next = Node(2)
list1.next.next = Node(3)

list2 = Node(1)
list2.next = Node(2)
list2.next.next = Node(3)

print(AddTwoNumbers(list1, list2))