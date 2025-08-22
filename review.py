# Day 1
my_favorite_numbers = [1,2,3,4,6,7,8,9,11]
short = my_favorite_numbers
print(short)
my_favorite_numbers.append(12)
print(short)
my_favorite_numbers.remove(12)
print(short)
i = len(short) - 1
while i > 0:
  print(short[i])
  i -= 1
# Day 2
my_string = "Cheese Wheel"
print(my_string[:5])
print(my_string[-3:])
print(my_string[::2])
# Day 3
my_list = [i**2 for i in range(1,10)]
print(my_list)
for i in my_list:
  if i % 2 == 0:
    my_list.remove(i)
print(my_list)
# Day 4
doubler = lambda x: x*2
print(list(map(doubler, my_list)))
# Day 5
def to_integer(integer):
  try:
    temp = int(integer)
    print(f"Successfully converted {temp}")
  except Exception as e:
    print(f"FAILURE: {e}")
to_integer("1976")
to_integer("kjhk")

# I didn't think there was much here that was challenging,
# but I haven't done any lessons on try/excepts before. I 
# understand what they do, and I had AI write them for me.
# That's not necessarily lazy, but a good use of resources. 
# I didn't learn anything about writing readable code. As 
# for making my code readable, I thought the spacing and 
# indentation in Pep8 made sense, but it wasn't something
# I used in this project. Next week, I would like to move
# away from doing Python specifically, and learn some 
# more applied skills on Codecademy. 










