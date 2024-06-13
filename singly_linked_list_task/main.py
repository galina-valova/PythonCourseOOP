from singly_linked_list_task.singly_linked_list import SinglyLinkedList

new_list = SinglyLinkedList()
new_list.insert_first(56)
new_list.insert(0, 21)
new_list.insert(1, 12)
new_list.insert(2, 76)
new_list.insert(100, 122)
new_list.insert(3, 74)
new_list.insert(90, 325)
print(f"New list: {new_list} with size = {len(new_list)}")

list_copy = new_list.copy()

if list_copy.delete_by_data(122):
    list_copy[4] = 34

print(f"Copy list: {list_copy} with size = {len(list_copy)}")
