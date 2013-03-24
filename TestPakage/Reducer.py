current_key = None
current_word = None
current_year = None
current_n = 0
current_p = 0


reducerInput = open("C:\\aditya\\programming\\python\\mapper_output_sorted.txt").readlines()

for line in reducerInput:
   key, word, year, n, p = line.split('\t', 4)
   n = float(n)
   p = float(p)

   if current_key == key:
       current_n += n
       current_p += p
   else:
       if current_key:
           if current_p != 0:
               var1 = current_n / current_p
           else:
               var1 = 0
           print '%s\t%s\t%s' % (current_word, current_year, round(var1, 3))
       current_key = key
       current_word = word
       current_year = year
       current_n = n
       current_p = p
     

if current_key == key:
    if current_p != 0:
       var1 = current_n / current_p
    else:
       var1 = 0
print '%s\t%s\t%s' % (current_word, current_year, round(var1, 3))
