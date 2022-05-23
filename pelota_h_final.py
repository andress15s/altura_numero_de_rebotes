print("---------------")
print("----ALTURA-----")
print("---------------")

h = int(input("Ingresar el valor de la altura: "))

q=h/5
n=0

while h > q: 
  h=0.9*h
  n=n+1
  
print(str(n))