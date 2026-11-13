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


ciphertext="RISYI TAUON TEOOY STETI FNITS IROTS OSNEH TUBMF OICEY CMWRB NNESO UHKHQ NOTEY HATXT EWNAS WEVME EELHN LAAHH LFFIM NATCO CNEAD ETOXH SHDPW STSPE EEIOE HSUTH DNRRE DISGU SBHSO HHLIA EAMRT OSSIE AOPLS TUEYT OWOME RLENA OGNTE TEHOT ETAUI ATHIE FNLAG RILSL SFEDO LTIMN EFMEE ATNTE MARAT UHRDH LOEIT RANAO AAENS OEEIU EIBOO DOFMU SLEGO ONORO ASWAA URSDE REFEL IOYEA OIYUT SHSAT AOWTM VLADC TRYLA OHWOE TIUIT HOTDO LPTSA ETDOS RAADE RYWRE TRCOM HTIOI HPNER MKOCT CIAIL SAAPO SSEEO HONIF OOTOL OHOEI EARRE TLIEU OKORT IGDOS EPRIA YFSEP OPORH GOOAU LOSUT SNTAM OIORE DFNIN ITDUH DOOTO MUKSC YTNMD NRIGU THTUI OTSMS OSUSF AMYTI MTRDI IAGSS HELUR INSPT LIOEO NHWNH HIEAL IAHEW MTLAM UMHOR SEEMT IUARO ETAHV UPTUD YDETA EDWII UEAIS FOETA MTPIU AIATS NEBKG ENOOE TFEPP NERLO NETEU GSOSA INMBN NGUNR NHOAQ NPDMM SSTIT NRRPH GINVT CLORT NHEDA MYTNU YDNAR GSOTI WTAEG OLTSW EATOR SSEES NATII HGNRT IBEFS NEAMA NATEI IIODR OTOAN MLETU ESHDC OCPDE ADEEG BNONS ERATA DTOTA ANEUD FEHOL IOHEH STIGE LSADT CHSAT AGSMM TOHQN AIPRH LNGLO NTPGC UEORA NNLHB RORGC RUTGM STWAC FEGNI AEATH GOESE AWUSR TEEHS HNITO BEAOS AESUA YAHDI TIBDB TDRAA IMLFN OHRAD NTLAE RNHEO RCEUE TEEIA IHTTO AEGFT AHRRA NOTIU REGCS STDOE SHHTL IESRT EDANN IAHRH ITEAG HWTAA ELIKE AIMIA GHNNS HETEM ERDIE ITBHR CDSTU SATTO YEMEB ENSNO TNWTT USEER NUIFD IDRRM NLIND PLCIE RAREL DALCN ONWOY TYTBE PTKWS EMKNA LNNEC LELRE TNIEX REELS OGBNU ISRIH EDVOE AOHSA HSDOK EYUOT RIUUH QTDUV THTSA HDEHN ETFTT ACAYO YHDVN SNAAO IMDTW DPWND UABEN AEGGY ETFHE KNTER ESHLH IRMTN PSGTI OEWDN CIMEE HCHCY ELEOI AJSHS HIABI NAUIS ORAAY GHCNB LEITT SOVNE IIAUE IOATE THPIU HIRHP NICEY BNITH WHUSS KEHOO IDAOI TNAFU AVTIT RERRM TASNO GOOEO HSBHI OTENG UYHCT BNTIY TSLON IETMP HTNGT AEOTO IIRNR CIHEH MEGNL DUSEM EUINO FWECH PRLOO STADE EWDRM ABLNT EELIT TTOBH STTDS TSAUC PESER LIAHU ACHAD PLETR IEEYE TNHTT TMILE IRREA TLXTY EMRUI TATRR TNICR CSNRB NWYRL GNUOV ILHVO UOFUT DNRIA SEODP NOEDY SATON INIRC PTAOE LINIG NMYR"
guess="relativesinbrooklyn"
for i in range(len(guess)):
    #print(decrypt_vignere(ciphertext, guess))
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
            plaintext += " "
            ciphernum = wraps
            wraps += 1
    return plaintext

print(decrypt_scytale(ciphertext, 29*8))

def decrypt_shuffle(ciphertext, key):
    group = 0
    ciphertext = ciphertext.replace(" ", "").upper()
    plaintext = ""
    key_length = len(key)
    for i in range(len(ciphertext)):
        j = (key[i%key_length]-1)+((i//key_length)*key_length)
        if j < len(ciphertext):
            plaintext += ciphertext[j]

    return plaintext
print(decrypt_shuffle(decrypt_scytale(ciphertext, 29*8), [4,6,5,1,7,2,3]))
#print(decrypt_shuffle(ciphertext, [1,4,2,3,5,6]))
