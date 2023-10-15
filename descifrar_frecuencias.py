
texto_cifrado = "RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE. AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJE, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE."


frecuencia = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'Ñ':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'v':0,'X':0,'Y':0,'Z':0}

frecuencia_aparicion_español = ["e", "a", "o", "l", "s", "n", "d", "r", "u", "i", "t", "c", "p", "n", "y", "q", "b", "h", "g", "f", "v", "j", "ñ", "z", "x", "k", "w"]

sustituciones = {"A": "d", "T": "l", "V": "y", "I": "o", "C": "i", "J": "n", "R": "c", "N": "s", "K": "r", "Q": "b", "S": "q", "Z": "u", "P": "m", "H": "t", "U": "g", "G": "j", "F": "x", "D": "p", "O": "f", "M": "h"}

for letra in texto_cifrado:
    if letra in frecuencia:
        frecuencia[letra] += 1


frecuencias_ordenadas = sorted(frecuencia.keys(),key = lambda k: frecuencia[k], reverse=True) [:2]
print(frecuencias_ordenadas)

sustituciones.update({frecuencias_ordenadas[0]:frecuencia_aparicion_español[0], frecuencias_ordenadas[1]:frecuencia_aparicion_español[1]})

texto_desc= ''

for letra_texto in texto_cifrado:
    if letra_texto in sustituciones:
        texto_desc += sustituciones[letra_texto]
    else:
        texto_desc += letra_texto

print(sustituciones)
print(texto_desc)