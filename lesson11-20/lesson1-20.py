def is_even(number):
    if number%2 == 0:
        return True
    return False

#def factorial(number):
 #   total = 1
 #   while number > 0:
  #      total *= number
 #       number -= 1
 #   return total

def factorial(number):
    total = 1
    for i in range(1, number + 1):
        total *= i
    return total

#def find_multiples(limit, divisor):
  #  new_list = []
   # while limit > 0:
   #     if limit % divisor == 0:
    #        new_list.append(limit)
   #     limit -= 1
  #  return new_list

def find_multiples(limit, divisor):
    return [i for i in range(limit + 1) if i % divisor == 0]

print(is_even(10))
print(factorial(3))
print(find_multiples(10, 5))

