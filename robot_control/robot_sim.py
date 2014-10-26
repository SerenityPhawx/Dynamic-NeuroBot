#!/usr/bin/env python

# robot simulator
# reads single character commands and prints what it got.
# exits on reading the character 'q'.

i = None

print("Entering terminal mode.")

while (i != 'q'):
  i = raw_input("Cmd: ")
  print("got %s" % i)
