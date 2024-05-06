nilai = 80
# # if nilai > 70:
# #     print('A')
# # else:
# #     print('B')

# nilai = int(input("Masukkan nilai [Range : 0-100] : "))
# if nilai < 0 or nilai > 100:
#     print('Error : Nilai Range 0-100')
#     exit()
# print('Benar')

# if nilai >= 80:
#     print('Index A')
# elif nilai > 65 and nilai < 80:
#     print('Index B')
# elif nilai > 50 and nilai < 65:
#     print('Index C')
# else:
#     print('Index D')
 
umur = int(input('Masukkan umur: '))
if umur > 17:
    undangan = input('Punya undangan [Y/T] : ').upper()
    if undangan == 'Y':
        print('Boleh nyoblos')
    else:
        print('Daftar Pemilu')
else:
    print('Umur tidak memenuhi')                



           
