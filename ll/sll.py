class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def traversal(head):
    if not head:
        print("list is empty")
        return

    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")


class SLL:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def remove(self, pos):
        curr = self.head
        prev = None

        if not self.head:
            print("sll is empty")
            return

        if pos == 0:
            self.head = self.head.next
            print("value remove success !") 
        else:
            for _ in range(pos):
                if curr is None:
                    print("out of bound")
                    return  
                prev = curr
                curr = curr.next
            
            
            if curr is None:
                print("out of bound")
                return
            # ---------------

            prev.next = curr.next
            print("value remove success !")



ll=SLL()
while True:
    print("Choose any one of the following")
    print("--------------------------------")
    print("1: Insert in SLL")
    print("2: Remove in SLL")
    print("3: Traverse the list")
    print("--------------------------------")
    user_input=int(input())
    if user_input ==1:
        value=int(input("enter value to insert"))
        ll.append(value)
        print("value insert success !")
    if user_input==2:
        value=int(input("enter position to remove"))
        ll.remove(value)        
    if user_input==3:
        traversal(ll.head)



