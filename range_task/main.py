from range_task.range import Range

input_start_1 = int(input("Enter start of the first range: "))
input_end_1 = int(input("Enter end of the first range: "))
input_start_2 = int(input("Enter start of the second range: "))
input_end_2 = int(input("Enter end of the second range: "))
input_number = int(input("Enter arbitrary number: "))

input_range_1 = Range(input_start_1, input_end_1)
input_range_2 = Range(input_start_2, input_end_2)

print(f"Length of input ranges is {input_range_1.get_length()} and {input_range_2.get_length()}")
print(f"Is {input_number} in range from {input_range_1.start} to {input_range_1.end} ?",
      input_range_1.is_inside(input_number))

input_range_1.start = 5.5
input_range_1.end = 14.5

print(f"Is {input_number} in range from {input_range_1.start} to {input_range_1.end} ?",
      input_range_1.is_inside(input_number))
print(f"Intersection of {input_range_1} and {input_range_2} is", input_range_1.get_range_intersection(input_range_2))
print(f"Union of {input_range_1} and {input_range_2} is", input_range_1.get_range_union(input_range_2))
print(f"Difference of {input_range_1} and {input_range_2} is", input_range_1.get_range_difference(input_range_2))
