def Transaction(moneys):
    thirty = 0
    sixty = 0
    for money in moneys:
        if money == 30:
            thirty += 1
        elif money == 60:
            if thirty >= 1:
                thirty -= 1
                sixty += 1
            else:
                return "Transaction failed"
        elif money == 120:
            if thirty >= 1 and sixty >= 1:
                thirty -= 1
                sixty -= 1
            elif thirty >= 3:
                thirty -= 3
            else:
                return "Transaction failed"
                
    return "Transaction successful"

n = int(input())
moneys = [int(input()) for _ in range(n)]
print(Transaction(moneys))