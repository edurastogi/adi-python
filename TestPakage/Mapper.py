inputFile = open("C:\\aditya\\programming\\python\\mapper_input.txt").readlines() 
   
for line in inputFile:
  words = line.split("\t")
  ngrpString = words[0]
  var1 = "religion"
  
  if "alcohol" in ngrpString and "religion" in ngrpString:
    print "%s\t%s\t%s\t%s\t%s\n" % (var1 + words[1], var1, words[1], words[2], words[3])   
  
  if "alcohol" in ngrpString:
      var1 = "alcohol"
      
  print "%s\t%s\t%s\t%s\t%s\n" % (var1 + words[1], var1, words[1], words[2], words[3])
