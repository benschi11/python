goals_team1 = int(input("Wie viele Tore hat Mannschaft 1 erziehlt?"));
goals_team2 = int(input("Wie viele Tore hat Mannschaft 2 erziehlt?"));

if goals_team1 > goals_team2:
    print("Mannschaft 1 hat gewonnen");
elif goals_team1 < goals_team2:
    print("Mannschaft 2 hat gewonnen");
else:
    print("untentschieden");