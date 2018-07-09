#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 21:06:10 2018

@author: siddesh
"""
from tkinter import * 
from datetime import datetime as dt
import time
import os

root = Tk()
time1 = ''
clock = Label(root, font=('DejaVu Sans Mono', 20), bg='white')
clock.pack(fill=BOTH, expand=1)
def my_clock():
      global time1
      l= dt.now()
      h=23-(l.hour)
      m=59-(l.minute)
      s=59-(l.second)
      
      time1=("Remaining: %d:%d:%d"%(h,m,s))
      clock.config(text=time1)
      clock.after(200,my_clock)
    
my_clock()
root.mainloop()   
