# User Driven Program For A Single Linked List:
# Function Are :
# Insert A Node At Begin
# Insert A Node At Pos
# Insert A Node At Last
# Delete A Node At Begin
# Delete A node At Pos
# Delete A Node from Last
# Search A Element
# View The List
# Find The Lenght
# Exit from The Linked List
class Node(object):
    def init(self,value):
        self.data = value 
        self.next = None
class Linked_List(object):
    def init(self):
        self.head = None
    def insert_node_at_start(self,value):
        newnode = Node(value)
        if self.head == None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode
        return 1
    def insert_node_at_pos(self,value,pos,counter):
        if(pos >= (counter + 2) or pos <= 0):
            return 0
        elif(pos == (counter + 1)):
            self.insert_node_at_last(value)
        elif(pos == 1):
            self.insert_node_at_start(value)
        else:
            newnode = Node(value)
            temp = self.head
            i = 1
            while(i < pos-1):
                temp = temp.next
                i = i + 1
            store = temp.next
            temp.next = newnode
            newnode.next = store
        return 1
    def insert_node_at_last(self,value):
        newnode = Node(value)
        if self.head == None:
            self.head = newnode
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = newnode
        return 1
    def delete_node_at_start(self):
        if self.head == None:
            print("\nLinked List Empty:")
        else:
            self.head = self.head.next
            return 1
    def delete_node_at_pos(self,pos,counter):
        if self.head == None:
            print("\nLinked List Is Empty:")
        elif pos == 1:
            self.delete_node_at_start()
        elif pos == counter:
            self.delete_node_at_last()
        elif pos <= 0 or pos > counter:
            return 0
        else:
            i = 1
            temp = self.head
            while(i <= (pos -1)):
                prev = temp
                temp = temp.next
                i = i + 1
            prev.next = temp.next
            return 1
    def delete_node_at_last(self):
        if self.head == None:
            print("\nLinked List Is Empty:")
        elif self.head.next == None:
            self.head = None
            return 1
        else:
            temp = self.head
            while(temp.next != None):
                prev = temp
                temp = temp.next
            prev.next = None
            return 1
    def search_node(self,num):
        pos = 1
        if self.head == None:
            print("\nLinked Is Empty: ")
        else:
            temp = self.head
            while(temp != None):
                if temp.data == num:
                    print("\nNode", num, "is Found at position",pos)
                    return 1
                temp = temp.next
                pos = pos + 1
            return 0
    def display(self):
        if(self.head == None):
            print("\nThe Current Linked List IS Empty: ")
        else:
            temp = self.head
            print("\nThe Current Linked List IS : ")
            while(temp != None):
                print(temp.data,"->",end='')
                temp = temp.next
    def length_linked_list(self,counter):
        print("The lenght Of Linked List Is:" ,counter)
def checks(choice):
    if(choice.isdigit()):
        return 1
    else:
        return 0
if __name__ == "__main__":
    mylist = Linked_List()
    counter = 0
    while(1):
        print("\nThe Menu Driven Are: ")
        print("Press 1 for Insert A node At start")
        print("Press 2 for Insert A node from any position")
        print("Press 3 for Insert A node from last")
        print("Prees 4 for Delete A node from Start")
        print("Prees 5 for Delete A node from any Position")
        print("Prees 6 for Delete A node from last")
        print("Press 7 for to serach A element")
        print("Press 8 to display the Len of Linked List")
        print("Press 9 to display Linked List")
        print("Press 10 to exit from the linked_list")
        choice = input("\nEnter your Choice:")
        result = checks(choice)
        if(result):
            choice = int(choice)
            if(choice == 1):
                num = int(input("Enter the data: "))
                result = mylist.insert_node_at_start(num)
                if result == 1:
                    print("\nNode Added Sucessfully In List at start: ")
                    counter = counter + 1
            elif(choice == 2):
                num = int(input("Enter the data: "))
                pos = int(input("Enter the Pos: "))
                result = mylist.insert_node_at_pos(num,pos,counter)
                if result == 0:
                    print("\nNot A Valid Position: ")
                else:
                    print("\nNode Added Sucessfully In List at position",pos)
                    counter = counter + 1
            elif(choice == 3):
                num = int(input("Enter the data: "))
                result = mylist.insert_node_at_last(num)
                if result == 1:
                    print("\nNode Added Sucessfully In List at Last: ")
                    counter = counter + 1
            elif(choice == 4):
                result = mylist.delete_node_at_start()
                if result == 1:
                    print("\nNode Deleted Sucessfully In List from Start: ")
                    counter = counter - 1
            elif(choice == 5):
                pos = int(input("Enter the Pos: "))
                result = mylist.delete_node_at_pos(pos,counter)
                if result == 0:
                    print("\nNot A Valid Position: ")
                else:
                    print("\nNode Deleted Sucessfully In List at position",pos)
                    counter = counter - 1
            elif(choice == 6):
                result = mylist.delete_node_at_last()
                if result == 1:
                    print("\nNode Deleted Sucessfully In List from End: ")
                    counter = counter - 1
            elif(choice == 7):
                num = int(input("Enter the num which You Want To serch: "))
                result = mylist.search_node(num)
                if result == 0:
                    print("\nNode is not Found: ")
            elif(choice == 8):
                mylist.length_linked_list(counter)
            elif(choice == 9):
                mylist.display()
            elif(choice == 10):
                exit()
            else:
                print("Please Input Numeric Input: ")
                print("Do U wanna Continue ?")
                choice = input()
                if(choice != 'y' or choice != 'Y'):
                    exit()  