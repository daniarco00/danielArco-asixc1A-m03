cabells = str(input("Per descriure els cabells tens les opcions: ARRISSATS, LLISOS, PENTINATS: "))
ulls = str(input("Per descriure els ulls tens les opcions: ACLUCATS, RODONS, ESTRELLATS:"))
nas = str(input("Per descriure el nas tens les opcions: AIXAFAT, ARROMANGAT, AGILENC: "))
boca = str(input("Per descrire la boca tens les opcions: NORMAL, BIGOTI, DENTS SORTIDES: "))

match cabells.upper():
    case "ARRISSATS":
        cabells_final = "@@@@"
    case "LLISOS":
        cabells_final = "VVVVV"
    case "pentinats":
        cabells_final = "XXX"
match ulls.upper():
    case "ACLUCATS": ulls_final = ".-.-."
    case "RODONS": ulls_final = ".o-o."
    case "ESTRELLATS": ulls_final = ".*-*"
match nas.upper():
    case "AIXAFAT": nas_final = "..0.."
    case "ARROMANGAT": nas_final = "..C.."
    case "AGILENC": nas_final = "..V.."
match boca.upper():
    case "NORMAL": boca_final = ".===."
    case "BIGOTI": boca_final = "-~~~."
    case "DENTS SORTIDES": boca_final =".www."

cara = cabells_final, ulls_final, nas_final, boca_final
print(f"{cara}")


