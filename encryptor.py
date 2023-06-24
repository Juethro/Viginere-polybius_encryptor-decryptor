#Project UTS Algoritma Pemrograman 1

#Jennifer Christine - 162112133023
#Denis Muhamad Jethro - 162112133028
#Ravikasha Davva Imawant - 162112133034
#Kelompok 14 SD-A1

print("---Welcome to Vigenère Cipher dan Polybius Cipher Encryptor Program---\nPlease input plain text in file .txt")
file_name = str(input("Input txt name: "))
password = str(input("Please input your password: "))

f = open(f"{file_name}", 'r')
plaintext = f.read()
plaintext = plaintext.lower()
plaintext = plaintext.replace(" ","")
plaintext = plaintext.replace("\n","")
for i in range(ord('!'), ord('@')+1):
    plaintext = plaintext.replace(chr(i), '')

#----------Vigenère Cipher----------
#tabel generator
words = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
tabel_awal = []

for i in range(len(words)):
    row = []
    baris = (words[i:]+words[:i])
    for x in baris:
        row.append(x)
    tabel_awal.append(row)

#scanner
list_kolom = []

for i in range(len(plaintext)):
    x = ord(plaintext[i])-96
    list_kolom.append(x)

panjang_kata = len(plaintext)
bandingan = []
for i in range(panjang_kata):
    for x in password:
        if len(bandingan) == panjang_kata:
            break
        else:
            pass
        bandingan.append(x)

list_kolom1 = []

for i in range(len(bandingan)):
    j = ord(bandingan[i]) - 96
    list_kolom1.append(j)

# encrypt
vigenere = []
print("Final Vigenère Cipher Text: ")

for i in range(panjang_kata):
    brs = list_kolom1[i] - 1
    klm = list_kolom[i] - 1
    vigenere.append(tabel_awal[brs][klm])

vigenere_text = " ".join(vigenere)
print(vigenere_text)

#----------Polybius Cipher----------
#tabel generator
password = password.upper()
grid = 6

poly_tabel = []
isi_tabel = []

for i in password:
    isi_tabel.append(i)
for x in range(ord('A'), ord('Z')+1):
    isi_tabel.append(chr(x))

isi_tabel = list(dict.fromkeys(isi_tabel))

y=0
while y < 5:
    baris = isi_tabel[0:6]
    baris = list(baris)
    for x in baris:
        isi_tabel.remove(x)
    poly_tabel.append(baris)
    y = y+1

#encrypt
encrypt = []

for a in vigenere:
    for i, x in enumerate(poly_tabel):
        lister = []
        if a in x:
            lister.append(i+1 )
            lister.append(x.index(a)+1)
            encrypt.append(lister)

poly_text = ''
print("Final Polybius Cipher Text: ")

for i in range(len(vigenere)):
    encrypt1 = encrypt[i]
    a = str(encrypt1[0])
    b = str(encrypt1[1])
    poly_text = poly_text + a + b + ' '

print(poly_text)

finaltext = open(f"{file_name}", 'a')
finaltext.write("\n")
finaltext.write(vigenere_text)
finaltext.write("\n")
finaltext.write(poly_text)
finaltext.close()

