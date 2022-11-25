#test 3
nilai1 =int(input('masukan nilai soal 1':))
nilai2 =int(input('masukan nilai soal 2':))
nilai3 =int(input('masukan nilai soal 3':))
umur = int(input('masukan unur anda':))
no1 = (nilai1*50/100)
no2 =(nilai2*50/100)
no3 =(nilai3*50/100)
rata2=(nilai1+nilai2+nilai3)
print("Rata-rata nilai anda: "+str(rata2))
if umur<=25:
    if rata2>=80:
        print("selamat anda lulus!")
    else :
        print("coba lagi tahun depan!")
else :
    if rata2>=90:
        print("selamat anda lulus!")
    else :
        print("coba lagi tahun depan!")

