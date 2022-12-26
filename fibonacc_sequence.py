nterms = int(input("Enter the nth number: "))
n1 ,n2 = 1 ,2
count = 0
for i in range (1,nterms):
  while count < nterms:
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1
  
