def standaardprijs(afstandKM):
    if afstandKM <= 50 and afstandKM >= 0:
        totaalprijs = float(0.80 * afstandKM)
        return totaalprijs
    else:
        if afstandKM > 50:
            totaalprijs = float(15 + 0.60 * (afstandKM - 50))
            return totaalprijs
    if afstandKM < 0:
        totaalprijs = float(0)
        return totaalprijs


def ritprijs(leeftijd, weekendrit, afstandKM):
    if afstandKM <= 50 and afstandKM >= 0:
            totaalprijs = float(0.80 * afstandKM)
    else:
        if afstandKM > 50:
            totaalprijs = float(15 + 0.60 * (afstandKM - 50))
        if afstandKM < 0:
            totaalprijs = float(0)
    if leeftijd < 12 or leeftijd >= 65 and weekendrit is False:
        korting1 = totaalprijs * float(0.3)
    if weekendrit is True and leeftijd < 12 or leeftijd >= 65:
        korting1 = totaalprijs * float(0.35)
    if weekendrit is True and leeftijd >= 12 or leeftijd < 65:
            korting1 = totaalprijs * float(0.40)
    if weekendrit is False and leeftijd >= 12 or leeftijd < 65:
            korting1 = float(0.0)
    return totaalprijs - korting1














