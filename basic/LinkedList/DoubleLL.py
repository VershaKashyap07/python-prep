class Node:
    def __init__(self, data, next_node=None, back_node=None):
        """
        Constructor for a Node with data, a reference to the next node, and a reference to the previous node.
        """
        self.data = data
        self.next = next_node
        self.back = back_node

def convertArr2DLL(arr):
    """
    Function to convert an array to a doubly linked list.
    """
    # Create the head node with the first element of the array
    head = Node(arr[0])
    # Initialize 'prev' to the head node
    prev = head

    for i in range(1, len(arr)):
        # Create a new node with data from the array and set its 'back' pointer to the previous node
        temp = Node(arr[i], None, prev)
        # Update the 'next' pointer of the previous node to point to the new node
        prev.next = temp
        # Move 'prev' to the newly created node for the next iteration
        prev = temp

    # Return the head of the doubly linked list
    return head

def print_list(head):
    """
    Function to print the elements of the doubly linked list.
    """
    while head is not None:
        # Print the data in the current node
        print(head.data, end=" ")
        # Move to the next node
        head = head.next

def insert_at_tail(head, k):
    """
    Function to insert a new node with value 'k' at the end of the doubly linked list.
    """
    # Create a new node with data 'k'
    new_node = Node(k)

    # If the doubly linked list is empty, set 'head' to the new node
    if head is None:
        return new_node

    # Traverse to the end of the doubly linked list
    tail = head
    while tail.next is not None:
        tail = tail.next

    # Connect the new node to the last node in the list
    tail.next = new_node
    new_node.back = tail

    return head


def delete_tail(head):
    if head is None or head.next is None:
        return None  # If the list is empty or has only one node, return None

    tail = head
    while tail.next is not None:
        # Traverse to the last node (tail)
        tail = tail.next

    new_tail = tail.back
    new_tail.next = None
    tail.back = None

    # Free memory of the deleted node
    del tail

    return head



    

# Main program
arr = [12, 5, 8, 7, 4]
head = convertArr2DLL(arr)
print(“\nDoubly Linked List Initially:”)
print_list(head)
print("\nDoubly Linked List After Inserting at the tail with value 10:")
# Insert a node with value 10 at the end
head = insert_at_tail(head, 10)
print_list(head)

print("\nAfter deleting the tail node:", end=" ")
head = delete_tail(head)
print_list(head)