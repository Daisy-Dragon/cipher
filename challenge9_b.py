ciphertext = "MFMTT NRHKH EBRKP SFPCE YCRZS HSDBD MTMFM TTNQP TMENA QKBQS BTOCK NEBDP QODES KELGH RTDSS DTMEB RSFST QDSPK BCBGC YCVSH XHSUT EAQYD SFYZD SKMQE CVGME DRSQN DZADA LABQA LXRMN ARANO CYKHE PELBA HRRSB TECYC KCENR KFDIQ CVEBB TKMEB PTRKN KCVTS TBPAK BQBNC WFOZD TVFKY RSDBN TTNDF TPBDM THLKD EBCEB IPTYD DEYCR KFDHY ZLKCH SFDKB SBDPS FYFRX KSGOD TKBZM ELQPE TBVKM SKRDD TSPEB FPCEY CRENT KDZYC EEQGH YFYZF SCGKB QBCVQ RVFKY RSGPE LKMSR KBPHF GREDK ETDPF VBZKS KRGMT DLPCV EBTBT RFDRK DIZFT ZZITC DFRWQ PHPMC RWRHN RDSCA TBBHS ZRKPS HXCVS NYCSD ZYEBM TDSPQ VFKYR SKSQA OBDBK SMQPT PMQCS EYZFP DKECV MTHCG KHALG PELKB TBHRY CRKFD KQKMS DSUTN EACVS NZMEL MQEDD BRKPS LXMFP ACYSQ PALAC VSNPE BSDTT PEBRK PSFPC VSNYC QKGXB KBTGC QODQN TILKB EDDBC YQNPT IPEBH XFSSC QMXGB DPTRI BZNTT FYCXR CEDQV FKYRS GPELK MSPEN CGOBK CPHQN MQOBH LKDEB LPCVS NBAEM THXCC YPACY RMHSP ABVKS KRGMT DVGPY DTHSD SPVCM MSDTR SKBZB PIHRP EHSNA SKDLZ TSZQA RKBAN WSPTR AQCOD BCNCV YPWNR ADTCO ZAKRK MQECV RKFDI HVMZT BRXLS PFDMT NTPSG PDLGH MXKSI RZAKM DFEBG XHBZC SNCOB VMQIT CEEPA LGPDL YCSRA DPIGC QSKBP RNTZY LPBTS PFDQN NCZCE BQCSB BDQYD OTBTD ELDBP TSQCY FOPTD SKMQE CVSBY ZFPDT XHSUT AKMYF DSKBV MQTEP SUQCX HYFRK PQYAK FPVPY MFMTP ASDQS COPKE LPKEC ATPQB ZPSMF CYRKP QDKEL DEQAB FMTOB DSNCW LPASK CYRHE LKBAP TDCGP HRWRS BTECD LVFKY RSRKP SRKHR TPABS DMFYC QCFNA PECEB XHSUR NNZTD ESAQT MNXAN RKPQB ZGMBD TDQWD EPQZA GKPSD KPODE TMKYE SKMQE CVSQK DESAY OYQMF SABFD NCWLL PKBAB CEBHX HSURF OZDEC MMTSK DFLZE TDTTP EBZES KSFTB ANGXD PECMC QCFNH XCVSN PTGEC VYCSZ QAVQK SDPKO FDRKY ZCNOK DPEBO BPMAD MTCEA NRIOZ DSPID ECWMF HLCOA BCEBH CWRSM SDAMT NKMQO BABDS FDHVK SKRKB MSDTH BDESK APDUY CRKOZ BABVF STRPM ADBYD VNCWL BHRST BRWRH YFATP KPRVG FSDKT BKBMT TDGCS MBTKM MRRKB APQSK OMMQS PELCZ BHDEA NCGOB SFKNC ENPMT DZBTB HAFDE RW".replace(" ", "")#[::-1]
plaintext = ""

"""
for c in ciphertext:
    print(c)

ciphertext_pairs = ['MF', 'MT', 'TN' ... ]

for c in ciphertext_pairs:
    print(c[0])
    print(c[1])

for i in range(ciphertext): # nope
    print(ciphertext[i])
    print(ciphertext[i+1])

for i in range(len(ciphertext)/2):
    print(ciphertext[i*2])
    print(ciphertext[i*2 + 1])

i = 0
while i < len(ciphertext):
    print(ciphertext[i])
    print(ciphertext[i+1])
    i += 2
"""

key = """
    HAVEB
    CDFGI
    KLMNO
    PQRST
    UWXYZ
"""[1:].replace(" ", "").splitlines()

key = """
    COMPA
    NYBDE
    FGHIK
    LQRST
    UVWXZ
"""[1:].replace(" ", "").splitlines()
# RH => 
#   WR
#   SI
print(key)

import re
from pathlib import Path
for password in ["company"]:#re.sub("[^A-Za-z]+", " ", Path('passwords.txt').read_text()).split(" "):
    plaintext = ""
    #password = "becalqsi"
    key = ""
    for x in (password + "ABCDEFGHIJKLMNOPQRSTUVWXYZ").upper().replace("J", "I"):
        if key.find(x) == -1:
            key += x
    key = [key[i:i+5] for i in range(0, 25, 5)]

    def key_lookup(letter):
        row_number = 0
        for row in key:
            column = row.find(letter)
            if column > -1:
                return [row_number, column]
            row_number += 1

    i = 0
    while i < len(ciphertext):
        j = i + 1
        [a,b] = key_lookup(ciphertext[i])
        [x,y] = key_lookup(ciphertext[j])
        if a == x:
            #plaintext += key[a][(b - 1) % 5]
            #plaintext += key[x][(y - 1) % 5]
            #replaced with a deliberately unusual implementation:
            plaintext += key[a][(b + 1) % 5]
            plaintext += key[x][(y + 1) % 5]
        elif b == y:
            #plaintext += key[(a + 1) % 5][b]
            #plaintext += key[(x + 1) % 5][y]
            #replaced with a deliberately unusual implementation:
            plaintext += key[a][(b + 1) % 5]
            plaintext += key[x][(y + 1) % 5]
        else:
            plaintext += key[a][y]
            plaintext += key[x][b]
        i += 2

    #if plaintext.find("CHARLES") >= 0:
    print(password + ": " + plaintext)#[0:100]) 