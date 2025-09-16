original_array = [2, 8, 9, 48, 8, 22, -12, 2]
#บวก 2 แล้วให้ตัวที่มากกว่า 5 ใน array
new_array = [x + 2 for x in original_array if x > 5]

print(original_array)
print(new_array)
