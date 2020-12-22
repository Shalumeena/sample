# Rail fence cipher encryption:
def transpose(l1, l2): 
    for i in range(len(l1[0])): 
        row =[] 
        for item in l1: 
            row.append(item[i]) 
        l2.append(row) 
    return l2 

keys = 3
plaintext = "SSN College Of Engineering"

le = len(plaintext)
rails = []
for zz in range(le):
  z=[]
  for yy in range(keys):
    z.append('-')
  rails.append(z)
i=0
k=0
while i<le:
  while k<keys and k<le and i<le:
    rails[i][k] = plaintext[i]
    k+=1
    i+=1
  k-=2
  while k>-1 and k<le and i<le:
    rails[i][k] = plaintext[i]
    k-=1
    i+=1
  k+=2
encrypted = ""
railt = []
transpose(rails,railt)
for r in railt:
  print(r)
for r in range(keys):
  for i in range(le):
    if rails[i][r]!='-':
      encrypted += rails[i][r]
print("\nPlainText: "+plaintext)
print("Encrypted Output: "+encrypted)
print("\n")

#	Rail fence cipher decryption:
le = len(encrypted)
rails = []
for zz in range(le):
  z=[]
  for yy in range(keys):
    z.append('-')
  rails.append(z)
i=0
k=0
while i<le:
  while k<keys and k<le and i<le:
    rails[i][k] = '1'
    k+=1
    i+=1
  k-=2
  while k>-1 and k<le and i<le:
    rails[i][k] = '1'
    k-=1
    i+=1
  k+=2
i,ini,ii=0,0,0
for k in range(keys):
  while i<le:
    if rails[i][k]=='1':    
      rails[i][k] = encrypted[ii]
      ii+=1
    i+=1
  ini+=1
  i=ini
railt = []
transpose(rails,railt)
for r in railt:
  print(r)

i=0
k=0
ptext=""
while i<le:
  while k<keys and k<le and i<le:
    ptext += rails[i][k]
    k+=1
    i+=1
  k-=2
  while k>-1 and k<le and i<le:
    ptext += rails[i][k]
    k-=1
    i+=1
  k+=2
print("\nDecrypted Output: "+ptext)

