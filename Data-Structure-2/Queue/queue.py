queue = []

def enqueue():
    print('enter a element')
    element = int(input())
    queue.append(element)
    print(element, 'added to queue')
    
def dequeue():
    if not queue:
        print('queue is empty') 
    else:
        element = queue.pop(0)
        print('removed element', element)       
    
def display():
    if not queue:
        print('queue is empty')
    else:
        print(queue)
        
def display_rev():
    if not queue:
        print('queue is empty')
    else:
        print(queue[::-1])        
        
        
while True:
    print('choose a option 1.enqueue 2.dequeue 3.display 4.reverse 5.quit')
    choice = int(input())
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        display_rev()
    elif choice == 5:   
        break
    else:
        print('choose any of the mentioned options')
                                 