
def caffeine():
    caffeine_mg = float(input())
    
    six_hour = (caffeine_mg/2)
    twelve_hour = (six_hour/2)
    twenty_four_hour = (twelve_hour/4)

    print("After 6 hours:",f'{six_hour:.2f}',"mg,","After 12 hours:",f'{twelve_hour:.2f}',"mg,","After 24 hours:",\
          f'{twenty_four_hour:.2f}',"mg")
    
if __name__ == "__main__":
    caffeine()
