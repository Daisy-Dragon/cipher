def decrypt_vignere(ciphertext, key):
    ciphertext = ciphertext.replace(" ", "").upper()
    key = key.replace(" ", "").upper()
    plaintext = ""
    keyn = 0
    for letter in ciphertext:
        #plaintext += (letter - key[keyn]) % 26
        plaintext += chr(65+(ord(letter)-64 + (ord(key[keyn])-64)) % 26)
        keyn += 1
        if keyn >= len(key):
            keyn = 0
    return plaintext


ciphertext="TEZEM HNETI EIRND RTEBA AKSFA MTOOT WRAOR RDIBN BGAAN TWHIG EOCMS HOETL DAANS TOHOT SRHUB NOEUY ODDTE PSPAI WAERE PARNC DVEIO EOYNM YUOTB LWLIU DETEN NFDIO ROSUY SLOFE EEWNM SISGD UYCOO INELA FOOWL HAIWR FEYIL AUNWO CWAET XFYIN PUWUO STOHI AEPPM IRNSE WNNEA BMUEA ETNHT LOLUY EATVH MREEO RBTEM EUTSO NAATH UECMM SEIAH FRYIE UUSJO AHDET KAECB ISHTA YAORE VHEAU AETLR SVIEI OBORN NLMYK EYYBA OUUCO TDASL TWHIY MHRET MMBEE ORNNE TOHFE VSEEI PHPAR DNAEE TDWIN DUBLO RVYEE FAODB UYAOR ODRFN FSAIU NYEON UHGOT ITFDH EENRF DSOOT OTGGN ITNTE OANCG ECNIS NEDAC KAILT OGATN NYEON SUITO HEETD ARNGO TZIAI HNETO TAGSL HYOWU ERDIT LXAPE NNGII SIEMH OFBTL LGEDI ERDNA HHAET ADYWR THHAT EDSOE ITKLN CEUXE YEOSS SAOLU DETEN IBNRO ETKHG OYTTE TEOSH OEORR TWHIM WOEUY DETEN TGBEO OCUKA UEIQR NMTEP OERFB YAONE EETGN SNYOS SNTDA SRPTA NKGIO URNOA YIOFD DHNAU OBKRT TNWIE UWLOE BNETD HNITI SPIOS NIAOT ODUYN UECLR IYGBK NITSD IANKT ATTHG OUFTO ROWUY SGYEA HUOSO TLHDU ONFKI SHAIT EAALS NNGIR OPRPO IUTNT DABNY AGTRE LFTUE TAHTH SLSEE ONMCO RSEFE COHFE EROGA OERMN ITNHE EKPEG ROMUY HUSTO DUOTH ETTGN LOOLF AENDW NDTOD IACNP"
guess="relativesinbrooklyn"
for i in range(len(guess)):
    print(decrypt_vignere(ciphertext, guess))
    guess = guess[1:]+guess[0]
    print("")


def decrypt_scytale(ciphertext, cylinder_size):
    ciphertext = ciphertext.replace(" ", "").upper()
    plaintext = ""
    ciphernum = 0
    wraps = 1
    for i in ciphertext:
        plaintext += ciphertext[ciphernum]
        ciphernum += cylinder_size
        if ciphernum >= len(ciphertext):
            ciphernum = wraps
            wraps += 1
    return plaintext

print(decrypt_scytale(ciphertext, 10))

def decrypt_shuffle(ciphertext, key):
    group = 0
    ciphertext = ciphertext.replace(" ", "").upper()
    plaintext = ""
    key_length = len(key)
    for i in range(len(ciphertext)):
        plaintext += ciphertext[(key[i%key_length]-1)+((i//key_length)*key_length)]

    return plaintext

print(decrypt_shuffle(ciphertext, [5,2,4,1,3]))
