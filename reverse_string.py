#!/usr/bin/python

print "Enter the text: "
txt = raw_input();
print "Text entered is: "+ txt + "" 
splt = txt.split()
i=len(splt) - 1
while (i >= 0):
  print splt[i] + '\t'
  i -= 1
