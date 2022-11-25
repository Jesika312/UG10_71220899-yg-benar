# test 2
print (("==== Selamat Datang di Toko Andi Tersenyum, selamat belanja!===="))
total = int(input("Total belanja:"))
if total <100000:
    print(f'tidak ada diskon! Maka yang Anda bayarkan adalah:Rp.{total}')
elif total >=100000:
    print(f'biaya yang harus dibayar setelah diskon adalah:Rp.{total-(0.2*total)}')
elif total >=500000:
    print(f'biaya yang harus dibayar setelah diskon adalah:Rp.{total-(0.5*total)}')
elif total >=1000000:
    print(f'biaya yang harus dibayar setelah diskon adalah:Rp.{total-(0.1*total)}')