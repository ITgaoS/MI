from django.test import TestCase

# Create your tests here.
list1=[1,2,3,4,5,6,7,8,10]
list2=[]


if len(list1) -3 < i:
    list2=list(range(len(list1)-3,len(list1)+2))
    print('ssdds')
elif i>1:
    list2=list1[i-3:i+2]
print(list2)
