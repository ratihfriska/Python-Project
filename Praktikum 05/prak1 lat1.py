bindo = int(input("Masukkan nilai Bahasa Indonesia : "))
ipa = int(input("Masukkan nilai IPA : "))
mat = int(input("Masukkan nilai Matematika : "))
if (bindo >= 60) and (ipa >= 60) and (mat >= 60):
    if (mat>70):
        status='LULUS'
    else:
        status='TIDAK LULUS'
else:
    status='TIDAK LULUS'
print("Status Kelulusan     :       ", status)