#Covered call strategy

def covered_call(a_price,s_price,x_price,c_premium):
    if s_price >= x_price:
        return float(x_price - a_price + c_premium)
    else:
        return float(s_price - a_price + c_premium)

print('Payoff',covered_call(25,20,30,1))