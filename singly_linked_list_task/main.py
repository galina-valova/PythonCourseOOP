from singly_linked_list_task.singly_linked_list import SinglyLinkedList

new_list = SinglyLinkedList()
new_list.push_front(56)
new_list.insert(0, 21)
new_list.insert(1, 12)
new_list.insert(2, 76)
new_list.insert(1, 122)
new_list.insert(3, 74)
new_list.insert(5, 325)

print(f"New list: {new_list} with size = {new_list.size}")

copy_list = new_list.copy()
if copy_list.delete_item_by_value(122):
    copy_list[4] = 34

print(f"Copy list: {copy_list} with size = {copy_list.size}")
