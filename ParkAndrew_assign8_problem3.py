"""
Assignment #8, Part 3
Andrew Park
"""

#goes through the list and for every item, add 1 to list the length of the list
def listlen(mylist):
    length = 0
    for i in mylist:
        length +=1 
    return length

#set max as 0 and slowly change the choiceues as you go through the list
#if the number in the list is greater than max, update max and go from there
def listmax(mylist):
    max = 0
    for i in mylist:
        if i > max:
            max = i
    return max

#just subsitutes the list into a different variable and print it. (same thing)
def listcopy(mylist):
    lcopy = list(mylist)
    return lcopy

#add the number you wanna add to the list (goes to the end of the list)
def listappend(mylist, number):
    mylist1 = mylist + [number] 
    return mylist1

#adds the number of choice to the placement you put in the middle. :placement means you place the choiceue to the left of the placement
def listinsert(mylist, placement, number):
    mylist1 = mylist[:placement] + [number] + mylist[placement:]
    return mylist1

#remove values based on what you choose
def listremove(mylist, choice):
    original = mylist
    #i = the current iteration and c = the value of the current iteration
    for i,c in enumerate(original):
        if c == choice:
            #remove the choice
            original.pop(i)
        original = mylist
    return(original)

#reorders the list to go backwards
def listreverse(mylist):
    mylist = mylist[::-1]
    return mylist

mylist = [10, 20, 30]
x = listremove(mylist, 20)
print (x)
print (mylist)

