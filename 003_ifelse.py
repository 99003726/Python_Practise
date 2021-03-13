import math
import os
import random
import re
import sys



a = int(input());  
if (a%2==0 and a>20):  
    print("Not Weird");  
elif(a%2==0 and a<5 and a>2): 
    print("Not Weird");  
else:    
    print("Weird");
