
import random

while True:
    odpoved = input("Ahoj, jmenujes se Bond, James Bond a jsi na ceste do Brazilie, kde zacina tvoje mise (ziskat ukradenou kralovskou korunu). Chces se ji zucastnit? ano/ne ")
    if odpoved == "ano":
        odpoved = input("Jaky dopravni prostredek si vyberes? lod/letadlo ")        
        if odpoved == "lod":
            odpoved = input("Jedes lodi a asi po 4 hodinach cesty vidis pred sebou ledovou kru. Tvoje lod ma vybavu pro rozrazeni ledu. Jedes do nej? ano/ne ")
            if odpoved == "ano":
                print("Do ledu se jezdit nevyplaci. Mas diru v lodi a zacnes se potapet. Game over. ")
                break

            
            elif odpoved == "ne":
                odpoved = input("Ledovou kru jsi objel. Po nudne ceste uspesne dorazis do Sao Paula. Potkavas velitele mistni jednotky agentu MI6, ktery se te pta jak provedete utok na drogovy kartel, kde je ukryta kralovska koruna. Bud zautocite tajne nebo akcne. tajne/akcne ")
                if odpoved == "tajne":
                    odpoved = input("Vybral sis tajny utok. Jdes do drogoveho kartelu sam. Mezi tebou a kralovskou korunou je nekolik vojaku. Budes se snazit mezi nimi nenapadne proniknout a vzit korunu nebo je postupne vsechny potichu omracis? nenapadne/omracit ")
                    if odpoved == "nenapadne":
                        sance = random.randint(1,5)
                        if sance == 1 or 2:
                            print("Ziskal jsi korunu! Tvoje mise byla splnena. Vracis se domu do Velke Britanie. Zde na tebe ceka kralovna, aby ti pogratulovala k dobre splnene misi. Vetsi pocty se nemuzes dockat. ")
                            break
                        
                        else:
                            print("Vojaci si te vsimli a zajali te. Game over. ")
                            break

                    elif odpoved == "omracit":
                        sance = random.randint(1,5)
                        if sance == 1 or 2 or 3:
                            print("Ziskal jsi korunu! Tvoje mise byla splnena. Vracis se domu do Velke Britanie. Zde na tebe ceka kralovna, aby ti pogratulovala k dobre splnene misi. Vetsi pocty se nemuzes dockat. ")
                            break
                        
                        else:
                            print("Vojaci si te vsimli a zajali te. Game over. ")
                            break

                    else:
                        print("neznama odpoved")

                elif odpoved == "akcne":
                    print("Se vsemi tanky, letadly a agenty MI6 v Brazilii dorazite pred drogovy kartel. Drogovy kartel absolutne vybombite. Hledas kralovskou korunu. Jedine co najdes jsou rozsypane drahokamy a zlaty prasek. Game over. ")

                else:
                    print("neznama odpoved")

                
            else:
                print("neznama odpoved")
        elif odpoved == "letadlo":
            odpoved = input("Letis letadlem a asi po 2 hodinach cesty vidis na hladine namorni bitvu. Tvoje letadlo ma vybavu pro boj na vode. Zapojis se? ano/ne ")
            if odpoved == "ano":
                print("Letis do boje, ale je to past. Zahy se objevi 10 stihacek KGB a tvoje letadlo zasahnou. Game over. ")
                break

            
            elif odpoved == "ne":
                odpoved = input("Do boje ses nezapojil. Po nudne ceste uspesne dorazis do Sao Paula. Potkavas velitele mistni jednotky agentu MI6, ktery se te pta jak provedete utok na drogovy kartel, kde je ukryta kralovska koruna. Bud zautocite tajne nebo akcne. tajne/akcne ")
                if odpoved == "tajne":
                    odpoved = input("Vybral sis tajny utok. Jdes do drogoveho kartelu sam. Mezi tebou a kralovskou korunou je nekolik vojaku. Budes se snazit mezi nimi nenapadne proniknout a vzit korunu nebo je postupne vsechny potichu omracis? nenapadne/omracit ")
                    if odpoved == "nenapadne":
                        sance = random.randint(1,5)
                        if sance == 1 or 2:
                            print("Ziskal jsi korunu! Tvoje mise byla splnena. Vracis se domu do Velke Britanie. Zde na tebe ceka kralovna, aby ti pogratulovala k dobre splnene misi. Vetsi pocty se nemuzes dockat. ")
                            break
                        else:
                            print("Vojaci si te vsimli a zajali te. Game over. ")
                            break

                    elif odpoved == "omracit":
                        sance = random.randint(1,5)
                        if sance == 1 or 2 or 3:
                            print("Ziskal jsi korunu! Tvoje mise byla splnena. Vracis se domu do Velke Britanie. Zde na tebe ceka kralovna, aby ti pogratulovala k dobre splnene misi. Vetsi pocty se nemuzes dockat. ")
                            break
                        
                        else:
                            print("Vojaci si te vsimli a zajali te. Game over. ")
                            break

                    else:
                        print("neznama odpoved")
                elif odpoved == "akcne":
                    print("Se vsemi tanky, letadly a agenty MI6 v Brazilii dorazite pred drogovy kartel. Drogovy kartel absolutne vybombite. Hledas kralovskou korunu. Jedine co najdes jsou rozsypane drahokamy a zlaty prasek. Game over. ")

                else:
                    print("neznama odpoved")

                
            else:
                print("neznama odpoved")  
        else:
            print("neznama odpoved")
    elif odpoved == "ne":
        print("To je skoda, tvou misi si vezme jiny agent. Tak treba priste! ")
        break
    else:
        print("neznama odpoved")
        
