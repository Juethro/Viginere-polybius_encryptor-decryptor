#Project UTS Algoritma Pemrograman 1

#Jennifer Christine - 162112133023
#Denis Muhamad Jethro - 162112133028
#Ravikasha Davva Imawant - 162112133034
#Kelompok 14 SD-A1

print("---Welcome to Vigenère Cipher dan Polybius Cipher Decryptor Program---\nPlease input plain text in file.txt")

file_name = str(input("Input txt name: "))
password = str(input("Please input your password: "))
password = password.upper()

f = open(f"{file_name}", 'r')
ciphertext = f.read()

#Tabel generator vigenere
words = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

tabel_awal = []
for i in range(len(words)):
    row = []
    baris = (words[i:]+words[:i])
    for x in baris:
        row.append(x)
    tabel_awal.append(row)

#tabel polybius
poly_tabel = []
isi_tabel = []

for i in password:
    isi_tabel.append(i)
for x in range(ord('A'), ord('Z') + 1):
    isi_tabel.append(chr(x))

isi_tabel = list(dict.fromkeys(isi_tabel))

y = 0
while y < 5:
    baris = isi_tabel[0:6]
    baris = list(baris)
    for x in baris:
        isi_tabel.remove(x)
    poly_tabel.append(baris)
    y = y + 1

#menjadikan ke list
ciphertext_list = list(ciphertext.split())

list_input = []

for i in ciphertext_list:
    lister = []
    for x in range(2):
        bagian = i[x]
        lister.append(bagian)
    list_input.append(lister)

#polibius dekriptor
Abjad = []
for i in list_input:
    lister2 = []
    for c in i:
        lister2.append(int(c)-1)
    z = poly_tabel[lister2[0]][lister2[1]]
    Abjad.append(z)

#memanjangkan password
panjang_kata = len(Abjad)
bandingan = []
for i in range(panjang_kata):
    for x in password:
        if len(bandingan) == panjang_kata:
            break
        else:
            pass
        bandingan.append(x)

# mencari baris password
index_baris = []
for i in bandingan:
    baris = ord(i) - 64 - 1
    index_baris.append(baris)

#scann di baris
kolom = []
for x, i in enumerate(index_baris):
    baris1 = tabel_awal[i]
    loa = baris1.index(Abjad[x])
    kolom.append(loa)

#viginere dekriptor
final_text = []

for i in kolom:
    final_text.append(tabel_awal[0][i])

final_text = ''.join(final_text)
print(final_text)

finaloriginaltext = open(f"{file_name}", 'a')
finaloriginaltext.write("\n")
finaloriginaltext.write(final_text)
finaloriginaltext.close()