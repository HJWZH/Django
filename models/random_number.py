#try
import string
import random
ii=1
result=''
number = 1
length_of_string = 50
for x in range(number):
  #print(''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length_of_string)))
  b=''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length_of_string))
  for i in b:
    if ii==6:
      #print("-")
      result=result+"-"
      ii=1
    #print(i)
    result=result+i
    ii+=1
  print(result)
  result=''
  ii=1