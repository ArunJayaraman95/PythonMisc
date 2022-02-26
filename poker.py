pot = 0
roundBet = 0
smallBlind = 5
bigBlind = 10
startingCash = 1000
oneRemaining = False

# Check/Call
# Raise
# Fold
# Manual Override

class Player:
    def __init__(self, name):
        self.name = name
        self.cash = startingCash
        self.bet = 0
        self.out = False
        self.matched = False
    
    def __repr__(self):
        return f'{self.name}: ${self.cash}'

    def cashPot(self):
        global pot
        self.cash += pot
        pot = 0
        
    
    def subtract(self, x):
        self.cash -= x

    def add(self, x):
        self.cash += x

    def setOut(self):
        self.out = True
    
    def setIn(self):
        self.out = False

p1 = Player("Arun")
p2 = Player("Neal")
p3 = Player("Ansh")
p4 = Player("Pman")

players = [p1, p2, p3, p4]

def display():
    print(f"\nPOT:  ${pot}!!!")
    print("Name\t\tCash\tBet\tMatch\tOut")
    for p in players:
        print(f"{p.name}\t\t{p.cash}\t{p.bet}\t{p.matched}\t{p.out}")

def menu():
    print("\nOptions:")
    print("1: Check" if roundBet == 0 else "-Can't Check-") #Check if roundbet != 0
    print("2: Call") #Check if player has enough
    print("3: Bet/Raise") #Check if player has enough
    print("4: Fold")
display()

# Preflop
while True:
    for p in players:
        # REFACTOR
        inRound = [m for m in players if not m.out]
        matching = [x.matched for x in inRound]
        # If only 1 person remains OR if everyone has matched
        if len(inRound) == 1 or all(matching):
            if len(inRound) == 1:
                print("1 left")
            else:
                print("All matched")
            break
        for m in inRound:
            print(m, "is in")


        if not p.out:    
            print(f"\n{p.name}'s turn!!!")
            menu()
            option = int(input("Select Option: "))
            if option == 0:
                print("MANUAL OVERRIDE. PRESS X TO CANCEL")
                mo = input("Override Value: ")
                if mo.lower() != 'x':
                    p.manualChange(int(mo))
            else:
                # White invalid option or trying to check during active betting
                while option not in [1,2,3,4] or (option not in [2,3,4] and roundBet != 0):
                    print("Invalid. Try again\n\n")
                    menu()
                    option = int(input("Select Option: "))
                    if option == 0:
                        print("MANUAL OVERRIDE. PRESS X TO CANCEL")
                        mo = input("Override Value: ")
                        if mo.lower() != 'x':
                            p.manualChange(int(mo))
                if option == 1:
                    print(p.name ,"checked")
                    p.matched = True
                while option == 2 and p.cash < roundBet:
                    print("Invalid. Try again\n\n")
                    menu()
                if option == 2:
                    p.bet = roundBet
                    p.matched = True
                while option == 3 and p.cash < roundBet:
                    print("Invalid. Try again\n\n")
                    menu()
                if option == 3:
                    raiseAmt = int(input("Bet/Raise Amt (Total Bet): "))
                    while p.cash < raiseAmt or raiseAmt <= roundBet:
                        if p.cash < raiseAmt:
                            print(p.name, "only has", p.cash, "dollars")
                        if raiseAmt <= roundBet:
                            print("Bet/Raise Amount given is not greater than current table bet.")
                        raiseAmt = int(input("Bet/Raise Amt (Total Bet): "))
                    p.bet = raiseAmt
                    roundBet = raiseAmt
                    for px in players:
                        px.matched = False
                    p.matched = True
                if option == 4:
                    print(p.name, "folded")
                    p.setOut()
            display()
    # REFACTOR
    inRound = [m for m in players if not m.out]
    matching = [x.matched for x in inRound]
    # If only 1 person remains OR if everyone has matched
    if len(inRound) == 1 or all(matching):
        if len(inRound) == 1:
            oneRemaining = True
            print("1 left")
        else:
            print("All matched")
        break

# Throw money into pot and deduct from players accordingly
for p in players:
    p.cash -= p.bet
    pot += p.bet
    p.bet = 0
    p.matched = False

print("DONE")
display()


# Flop
if not oneRemaining:
    while True:
        for p in players:
            # REFACTOR
            inRound = [m for m in players if not m.out]
            matching = [x.matched for x in inRound]
            # If only 1 person remains OR if everyone has matched
            if len(inRound) == 1 or all(matching):
                if len(inRound) == 1:
                    print("1 left")
                else:
                    print("All matched")
                break
            for m in inRound:
                print(m, "is in")


            if not p.out:    
                print(f"\n{p.name}'s turn!!!")
                menu()
                option = int(input("Select Option: "))
                if option == 0:
                    print("MANUAL OVERRIDE. PRESS X TO CANCEL")
                    mo = input("Override Value: ")
                    if mo.lower() != 'x':
                        p.manualChange(int(mo))
                else:
                    # White invalid option or trying to check during active betting
                    while option not in [1,2,3,4] or (option not in [2,3,4] and roundBet != 0):
                        print("Invalid. Try again\n\n")
                        menu()
                        option = int(input("Select Option: "))
                        if option == 0:
                            print("MANUAL OVERRIDE. PRESS X TO CANCEL")
                            mo = input("Override Value: ")
                            if mo.lower() != 'x':
                                p.manualChange(int(mo))
                    if option == 1:
                        print(p.name ,"checked")
                        p.matched = True
                    while option == 2 and p.cash < roundBet:
                        print("Invalid. Try again\n\n")
                        menu()
                    if option == 2:
                        p.bet = roundBet
                        p.matched = True
                    while option == 3 and p.cash < roundBet:
                        print("Invalid. Try again\n\n")
                        menu()
                    if option == 3:
                        raiseAmt = int(input("Bet/Raise Amt (Total Bet): "))
                        while p.cash < raiseAmt or raiseAmt <= roundBet:
                            if p.cash < raiseAmt:
                                print(p.name, "only has", p.cash, "dollars")
                            if raiseAmt <= roundBet:
                                print("Bet/Raise Amount given is not greater than current table bet.")
                            raiseAmt = int(input("Bet/Raise Amt (Total Bet): "))
                        p.bet = raiseAmt
                        roundBet = raiseAmt
                        for px in players:
                            px.matched = False
                        p.matched = True
                    if option == 4:
                        print(p.name, "folded")
                        p.setOut()
                display()
        # REFACTOR
        inRound = [m for m in players if not m.out]
        matching = [x.matched for x in inRound]
        # If only 1 person remains OR if everyone has matched
        if len(inRound) == 1 or all(matching):
            if len(inRound) == 1:
                oneRemaining = True
                print("1 left")
            else:
                print("All matched")
            break

    # Throw money into pot and deduct from players accordingly
    for p in players:
        p.cash -= p.bet
        pot += p.bet
        p.bet = 0
        p.matched = False


print("DONE")
display()

# Turn
if not oneRemaining:
    while True:
        for p in players:
            # REFACTOR
            inRound = [m for m in players if not m.out]
            matching = [x.matched for x in inRound]
            # If only 1 person remains OR if everyone has matched
            if len(inRound) == 1 or all(matching):
                if len(inRound) == 1:
                    print("1 left")
                else:
                    print("All matched")
                break
            for m in inRound:
                print(m, "is in")


            if not p.out:    
                print(f"\n{p.name}'s turn!!!")
                menu()
                option = int(input("Select Option: "))
                if option == 0:
                    print("MANUAL OVERRIDE. PRESS X TO CANCEL")
                    mo = input("Override Value: ")
                    if mo.lower() != 'x':
                        p.manualChange(int(mo))
                else:
                    # White invalid option or trying to check during active betting
                    while option not in [1,2,3,4] or (option not in [2,3,4] and roundBet != 0):
                        print("Invalid. Try again\n\n")
                        menu()
                        option = int(input("Select Option: "))
                        if option == 0:
                            print("MANUAL OVERRIDE. PRESS X TO CANCEL")
                            mo = input("Override Value: ")
                            if mo.lower() != 'x':
                                p.manualChange(int(mo))
                    if option == 1:
                        print(p.name ,"checked")
                        p.matched = True
                    while option == 2 and p.cash < roundBet:
                        print("Invalid. Try again\n\n")
                        menu()
                    if option == 2:
                        p.bet = roundBet
                        p.matched = True
                    while option == 3 and p.cash < roundBet:
                        print("Invalid. Try again\n\n")
                        menu()
                    if option == 3:
                        raiseAmt = int(input("Bet/Raise Amt (Total Bet): "))
                        while p.cash < raiseAmt or raiseAmt <= roundBet:
                            if p.cash < raiseAmt:
                                print(p.name, "only has", p.cash, "dollars")
                            if raiseAmt <= roundBet:
                                print("Bet/Raise Amount given is not greater than current table bet.")
                            raiseAmt = int(input("Bet/Raise Amt (Total Bet): "))
                        p.bet = raiseAmt
                        roundBet = raiseAmt
                        for px in players:
                            px.matched = False
                        p.matched = True
                    if option == 4:
                        print(p.name, "folded")
                        p.setOut()
                display()
        # REFACTOR
        inRound = [m for m in players if not m.out]
        matching = [x.matched for x in inRound]
        # If only 1 person remains OR if everyone has matched
        if len(inRound) == 1 or all(matching):
            if len(inRound) == 1:
                oneRemaining = True
                print("1 left")
            else:
                print("All matched")
            break

    # Throw money into pot and deduct from players accordingly
    # Reset matching
    for p in players:
        p.cash -= p.bet
        pot += p.bet
        p.bet = 0
        p.matched = False

print("DONE")
display()


# River
if not oneRemaining:
    while True:
        for p in players:
            # REFACTOR
            inRound = [m for m in players if not m.out]
            matching = [x.matched for x in inRound]
            # If only 1 person remains OR if everyone has matched
            if len(inRound) == 1 or all(matching):
                if len(inRound) == 1:
                    print("1 left")
                else:
                    print("All matched")
                break
            for m in inRound:
                print(m, "is in")


            if not p.out:    
                print(f"\n{p.name}'s turn!!!")
                menu()
                option = int(input("Select Option: "))
                if option == 0:
                    print("MANUAL OVERRIDE. PRESS X TO CANCEL")
                    mo = input("Override Value: ")
                    if mo.lower() != 'x':
                        p.manualChange(int(mo))
                else:
                    # White invalid option or trying to check during active betting
                    while option not in [1,2,3,4] or (option not in [2,3,4] and roundBet != 0):
                        print("Invalid. Try again\n\n")
                        menu()
                        option = int(input("Select Option: "))
                        if option == 0:
                            print("MANUAL OVERRIDE. PRESS X TO CANCEL")
                            mo = input("Override Value: ")
                            if mo.lower() != 'x':
                                p.manualChange(int(mo))
                    if option == 1:
                        print(p.name ,"checked")
                        p.matched = True
                    while option == 2 and p.cash < roundBet:
                        print("Invalid. Try again\n\n")
                        menu()
                    if option == 2:
                        p.bet = roundBet
                        p.matched = True
                    while option == 3 and p.cash < roundBet:
                        print("Invalid. Try again\n\n")
                        menu()
                    if option == 3:
                        raiseAmt = int(input("Bet/Raise Amt (Total Bet): "))
                        while p.cash < raiseAmt or raiseAmt <= roundBet:
                            if p.cash < raiseAmt:
                                print(p.name, "only has", p.cash, "dollars")
                            if raiseAmt <= roundBet:
                                print("Bet/Raise Amount given is not greater than current table bet.")
                            raiseAmt = int(input("Bet/Raise Amt (Total Bet): "))
                        p.bet = raiseAmt
                        roundBet = raiseAmt
                        for px in players:
                            px.matched = False
                        p.matched = True
                    if option == 4:
                        print(p.name, "folded")
                        p.setOut()
                display()
        # REFACTOR
        inRound = [m for m in players if not m.out]
        matching = [x.matched for x in inRound]
        # If only 1 person remains OR if everyone has matched
        if len(inRound) == 1 or all(matching):
            if len(inRound) == 1:
                oneRemaining = True
                print("1 left")
            else:
                print("All matched")
            break

    # Throw money into pot and deduct from players accordingly
    # RESET ALL
    for p in players:
        p.cash -= p.bet
        pot += p.bet
        p.bet = 0
        p.matched = False
        p.setIn()


print("DONE")
display()
# Cash Out
for i, p in enumerate(players):
    print(f'[{i}] {p.name}')
print("\nChoose winner by number")
roundWinner = int(input("Winning Player Number: "))
players[roundWinner].cashPot()