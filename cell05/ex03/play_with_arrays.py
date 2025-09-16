original_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = {x + 2 for x in original_array if x > 5} 
#รูปแบบ set ไม่ซ้ำกับที่มีอยู่เหมือนงานที่แล้ว

print(original_array)
print(new_array)
