
def real_estate():
    
    current_price = int(input())
    last_month_price = int(input())
    month_mortgage = ((current_price*0.051)/12)
    print("This house is $"+str(current_price)+". The change is $"+str(current_price - last_month_price)+" since last month.")
    print("The estimated monthly mortgage is $"+str(f'{month_mortgage:.2f}')+".")

if __name__ == "__main__":
    real_estate()