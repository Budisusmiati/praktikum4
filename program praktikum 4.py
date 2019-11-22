j = 0
nama = []
nim = []
tugas = []
uts = []
uas = []
nilai = []
Jawab ="y"
while Jawab == "y":
    Nama = str(input ("Nama  :  "))
    nama.append(Nama)
    if Nama == "z":
        break
    NIM = int(input ("NIM   :  "))
    nim.append(NIM)
    Tugas = float(input ("Tugas :  "))
    tugas.append(Tugas)
    UTS = float(input ("UTS   :  "))
    uts.append(UTS)
    UAS = float(input ("UAS   :  "))
    uas.append(UAS)
    Nilai = round ((Tugas)*30/100 + (UTS)*35/100 + (UAS)*35/100)
    nilai.append(Nilai)
    Jawab = input (" Tambahkan Data (y/t)?")
print ("\n===========================================================================")
print ("\n Daftar Nilai Mahasiswa UPB")
print ("=============================================================================")
print (" |  No |  Nama  |  NIM   |  Tugas |   UTS  |   UAS  | Nilai|" )
print ("=============================================================================")
for j in range (len(nama)):
    print (" | " ,j+1," | " , nama[j] ," | " , nim[j]," | " , tugas[j] ," | " , uts[j] ," | " , uas[j] ," | " , nilai[j]," | ")
    print ("============================================================================")

