from .stack import *


def insertAtBottom(stack, item):  # Recursive function that inserts an element at the bottom of a stack.
    # Base case
    if isEmpty(stack):
        push(stack, item)

    # Recursive case
    else:
        temp = pop(stack)
        insertAtBottom(stack, item)
        push(stack, temp)


def reverse(testVariable):
    # Recursive case
    if not isEmpty(testVariable):
        temp = pop(testVariable)
        reverse(testVariable)
        insertAtBottom(testVariable, temp)


# Driver Code
if __name__ == '__main__':
    myStack = createStack()
    push(myStack, str(8))
    push(myStack, str(5))
    push(myStack, str(3))
    push(myStack, str(2))

    print("Original Stack")
    printStack(myStack)

    reverse(myStack)

    print("\n\nReversed Stack")
    printStack(myStack)