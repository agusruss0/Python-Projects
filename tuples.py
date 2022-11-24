#tuple
from cgitb import text


x=('agus','cande','lari')
print(x[2])
y=(1,45,76,100)
print(y)
print(max(y))
for n in y:
    print(n)

#Dos variables asignadas   
(a,b)=('Agus',24)
print(a)
print(b)
print(a,b)

#tuples y diccionarios
d=dict()
d['Agus']=1997
d['Clara']=1999
d['Fran']=2004
for k,v in d.items():
    print(k,v)
tups=d.items()
print(tups)

#comparando tups
t=(0,1,2)<(5,8,1)
f=('Agus','Lara')>('Agus','Lari')
print(t)
print(f)

#ordenando listas de tups (por el key)
s={'a':2,'c':6,'e':3,'d':5,'f':8,'b':5}
print(s.items())
print(sorted(s.items()))

#con loop
sor=sorted(s.items())
for k,v in sor:
    print(k,v)

#Para ordenar segun value
tmp=list()
for k,v in s.items():
    tmp.append((v,k))
print(tmp)
print(sorted(tmp,reverse=True))

#las 10 palabras mas comunes
txt=open('Chopin.txt')
cuenta=dict()
for linea in txt:
    palabras=linea.split()
    for palabra in palabras:
        cuenta[palabra]=cuenta.get(palabra,0)+1
diez=list()
for k,v in cuenta.items():
    diez.append((v,k))
diez=sorted(diez,reverse=True)
for v,k in diez[:10]:
    print(k,v)

#List Comprehension
c=s
print(sorted([(v,k)for k,v in c.items()]))

