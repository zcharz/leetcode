from linkedlist import *



# O(N) memory solution
def hasCycle(head: ListNode) -> bool:
    seen = set()

    curr = head

    while curr != None:
        if curr in seen:
            return True
        

        # since values can repeat, add node objects in set instead of value
        seen.add(curr)
        curr = curr.next
    
    return False

# Floyd's tortise and hare algo
def hasCycleTH(head: ListNode) -> bool:
    tort = head
    hare = head

    # both are not None
    while tort and hare:
        tort = tort.next
        hare = hare.next

        # offset at the end since both are set to head
        if tort == hare:
            return True
        
    return False

        

test = [-21,10,17,8,4,26,5,35,33,-7,-16,27,-12,6,29,-12,5,9,20,14,14,2,13,-24,21,23,-21,5]
for i in test:
    print(test.count(i))

