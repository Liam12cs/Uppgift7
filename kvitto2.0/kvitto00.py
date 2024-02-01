def skapa_kvitto(varor):
    total_pris = 0
    kvitto_text = "Kvitto\n2\n"
    
    for vara, pris in varor.items():
        kvitto_text += f"{vara}: {pris} kr\n"
        total_pris += pris
    
    kvitto_text += f"\nTotalt: {total_pris} kr"
    
    with open("kvitto.txt", "w") as kvitto_fil:
        kvitto_fil.write(kvitto_text)

def main():
    fasta_varor = {'Nocco': 25, 'Egg': 40,'Golden_apple':500,'cola':19}
    varor = {}
    
    for vara, pris in fasta_varor.items():
        antal = int(input(f"Ange antal {vara}: "))
        varor[vara] = pris * antal

    skapa_kvitto(varor)
    print("Kvitto har skapats och sparats som 'kvitto.txt'.")

if __name__ == "__main__":
    main()
