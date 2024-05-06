# TASK

# 1. verilmiş listdəki ədədlərin hansılarının hər hansı bir ədədin kvadratı olduğunu define funksiyasında yazıb və listin içərisində ekrana çıxarın.

mylist=[-4,-16,0,1,4,5,9,16,25,36,49,64,81,100]
list=[]
root=[]

def define():
    for i in mylist:
        if i>0:
         square=i**0.5
         if square==int(square):
            list.append(i)
            root.append(square)
    return list, root
print(define())            


# 2)Funksiya yazin list qebul etsin ve tekrarlanmayan elementleri bizə qaytarsın:
# input:[-1,1,2,2,6,7,7,'say']

list = []
newlist = []

def myfunction():
    for i in range(0, 10):
        data = input("elementleri qeyd et: ")
    return list
print(myfunction())

for i in list:
    if list.count(i) == 1:
        newlist.append(i)

print(newlist)


# 3) Verilmiş inputdakı bütün rəqəmlərin bir birlərinə hasilini icra edən funksiya yazın

def product(lst):
    h = 1  
    for i in lst:
        if isinstance(i, int):
            h *= i
    return h

list = [1,2,3,4,5, 'say']  

print(product(list))


# 4) verilmiş ədədin bölənlərini list comprehension istifadə edərək yazın

n=int(input("rəqəm daxil edin:"))
print(list(i for i in range(1,n+1) if n%i==0))


# 5)Əlinizdə ayların olduğu bir list var siz ay qarşısında uzunluğu olduğu
# bir dictionary yaradın və bunu comprehension ilə edin və alınan listi print etdirin.

mylist = ['yanvar', 'fevral', 'mart']
mydict = dict((i, len(i)) for i in mylist)
print(mydict)



# 6)names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
# verilmiş list-dən yalnız adların olduğu və kiçik hərflərlə yazıldığı list düzəldin və
# bunu conprehension ilə edin (əlavə olaraq funksiya da istifadə edəbilərsiz).
# ['rick', 'morty', 'summer', 'jerry', 'beth']

names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
namelower=[name.lower().split(" ")[0] for name in names]
print(namelower)

# 7) verilmiş iki listdəki ədədlərin indexlərinə uyğun olaraq ortalamasını tapın.

nums1 = [10, 20, 30,40]
nums2 = [11, 12, 13,14]
results=[]
for i in range (0,len(nums1)):
    average=(nums1[i]+nums2[i])/2
    results.append(average)
print(results)    
