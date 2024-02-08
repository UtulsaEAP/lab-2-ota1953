def telephone():
    phone_number = int(input())
    
    area_ = phone_number//10000000
    prefix_ = phone_number//10000%1000
    suffix_ = phone_number%10000

    print('('+str(area_)+')'+ ' '+str(prefix_)+'-'+str(suffix_))

if __name__ == "__main__":
    telephone()
