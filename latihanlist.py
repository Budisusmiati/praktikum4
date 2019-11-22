list_a= [7,8,9,10,11];
list_b= [];
print("LATIHAN LIST")
print("===================================")
print("+++++++++++++++++++++++++++++++++++")
print("===================================")
print ("list_a     :[7,8,9,10,11]")

print("Akses List")
print("list_a[2]  :",list_a[2])
print("list_a[1:4]:",list_a[1:4])
print("list_a[-1] :",list_a[-1])
print("===================================")

print("Ubah Elemen List")
list_a[3]=2
print("list_a     :",list_a[:])
list_a[3:]=[1,4]
print("list_a     :",list_a[:])
print("===================================")

print("Tambah elemen list")
list_b = list_a[0:2]
print("List_b     :",list_b[:])
list_b.extend('b')
print("list_b     :",list_b[:])
list_b.append([1,2,3])
print("list_b     :",list_b[:])
list_c = list_a + list_b
print("list_c     :",list_c[:])

         

