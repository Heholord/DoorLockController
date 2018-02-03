#!/usr/bin/python

import keypad16 as matrix

kb = matrix.keypad_module(0x27,1,0)  

while 1:
  ch = kb.getch()
  print ch

  if ch == 'D':
    exit()

