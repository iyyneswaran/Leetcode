def autoImmune(ages, L):
    if L == 1:
        return str(len(ages)) + " Days"
        
    high_risk = 0
    low_risk = 0
    high_risk_days = 0
    low_risk_days = 0
    for age in ages:
        if  (0 < age and age <= 10) or (age >= 81):
            high_risk += 1
        else:
            low_risk += 1
    
    high_risk_days = (high_risk + L - 1) // L
    low_risk_days = (low_risk + L - 1) // L
    
    return str(high_risk_days + low_risk_days) + " Days"

N, L = map(int, input().split())
ages = list(map(int, input().split()))
print(autoImmune(ages, L))
