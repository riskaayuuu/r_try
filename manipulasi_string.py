#menyatukan kalimat 
string1 = 'Hello'
string2 = 'World'
int1 = '10'
print(string1 + " " + string2)
print((string1 + " ") * 10) 
print(string1 + str(int1))

#list menjadi kalimat()
daftar_kata = ['aku', 'seorang', 'kapiten']
kalimat = " ".join(daftar_kata)
print(kalimat)

#kalimat menjadi list(memisahkan kata)
daftar_kata1 = 'Aku seorang programmer, dia juga programmer'
pisah_kata = daftar_kata1.split()
print(pisah_kata)

#mengganti substring(kata dalam suatu kalimat)
substring = daftar_kata1.replace('programmer','design')
print(substring)
print(daftar_kata1[0:11])

#merubah huruf kecil dan besar 
nama = 'batman hitam'
print(nama.upper()) #jadi besar
print(nama.lower()) #jadi kecil
print(nama.capitalize()) #huruf pertama pada awal kata besar
print(nama.title()) #huruf pertama pada setiap kata besar

#merubah penulisan uang 
uang = 271000000000000
print('{:,}'.format(uang))#ada koma
print('{:.2f}'.format(uang))#nambah 0 sebanyak 2 dibelakang 
print('{:,.2f}'.format(uang)) #gabungan ke 1 dan 2

print(f'{uang:,}')


