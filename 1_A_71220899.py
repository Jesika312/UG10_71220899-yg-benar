Nama=input("Masukan nama mahasiswa:")
Nim= input("Masukan NIM-nya:")
if ((int(str(Nim)[2:4])==22 or 21 or 20) and ((int(str(Nim)[0:2])==71))):
    print(Nama+("merupakan mahasiswa informatika angkatan 22 hingga 22"))
else :
    print(Nama+("bukan mahasiswa informatika angkatan 20 hingga 22"))

