#Substituir letras por outras
dicionarioLetras = {
'F': 'N','Y': 'F',
'G': 'O', 'O': 'I', 
'I': 'H', 'H': 'P', 
'P': 'J', 'J': 'Q', 
'Q': 'A', 'L': 'S', 
'S': 'L', 'K': 'R', 
'R': 'D', 'D': 'M', 
'M': 'Z', 'Z': 'T', 
'T': 'E', 'E': 'C', 
'C': 'V', 'B': 'X', 
'X': 'U', 'U': 'G'
}

txtCripto = 'GOTT, FQG QEIGX JXT LTKOQ YQEOS RTLLQ CTM FT? LG JXTKOQ ZT RTLTPQK XD YTSOM QFOCTKLQKOG T YQSQK JXT TLLT QFG CGET DT RTOBGX DXOZG GKUXSIGLQ HGK ZXRG JXT EGFJXOLZGX. ZT QDG DXOZG. YTSOM QFOCTKLQKOG'

#Em uma única string, substitui todos os caracteres de txtCripto pelos caracteres do Dicionario //.get(chave, valor_padrao)
txtDecifra = ''.join(dicionarioLetras.get(letra, letra) for letra in txtCripto)

print(txtDecifra)
