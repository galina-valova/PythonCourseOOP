from range_task.range import Range

start_1 = float(input("Enter start of the first range: "))
end_1 = float(input("Enter end of the first range: "))

start_2 = float(input("Enter start of the second range: "))
end_2 = float(input("Enter end of the second range: "))

number = float(input("Enter arbitrary number: "))

range_1 = Range(start_1, end_1)
range_2 = Range(start_2, end_2)

print(f"Length of input ranges is {range_1.get_length()} and {range_2.get_length()}")
print(f"Is {number} in range from {range_1.start} to {range_1.end} ?",
      range_1.is_inside(number))

range_1.start = 5.8
range_1.end = 14.3

print(f"Is {number} in range from {range_1.start} to {range_1.end} ?",
      range_1.is_inside(number))
print(f"Intersection of {range_1} and {range_2} is", range_1.get_intersection(range_2))
print(f"Union of {range_1} and {range_2} is", range_1.get_union(range_2))
print(f"Difference of {range_1} and {range_2} is", range_1.get_difference(range_2))
