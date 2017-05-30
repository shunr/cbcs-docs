s = input()
bool = False
if 'True' in s:
  bool = True
  
s = s.replace('True', '').replace('False', '')
if (len(s)/4) % 2 == 1:
  bool = not bool
  
print(bool)