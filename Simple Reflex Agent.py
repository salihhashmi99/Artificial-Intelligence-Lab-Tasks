Loc = str(input("Enter the Location of dirt: "))
Stat = str(input("Now Enter the Status of location: "))

def Reflex_Vacuum_Agent(Loc, Stat) -> str:
    if Stat == "Dirty":
        return "Suck"
    elif Loc == "A":
        return "Right"
    elif Loc == "B":
        return "Left"

print(Reflex_Vacuum_Agent(Loc, Stat))
