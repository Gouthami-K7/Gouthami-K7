
def units_convert( num : int ,in_unit : float ,out_unit: float ):
    if in_unit=='km' and out_unit=='m':
        return num*1000
    elif in_unit=='m' and out_unit=='km':
        return num/1000
    elif in_unit=='m' and out_unit=='cm':
        return num*100
    elif in_unit=='cm' and out_unit=='m':
        return num/100
    elif in_unit=='cm' and out_unit=='mm':
        return num*10
    elif in_unit=='F' and out_unit=='C':
        return (num - 32) * 5/9
    elif in_unit=='C' and out_unit=='F':
        return (num * 9/5) + 32
    elif in_unit=='kg' and out_unit=='g':
        return float ( num*1000)
    elif in_unit=='g' and out_unit=='mg':
        return num*1000
    else:
        return "invalid units"
    
print(units_convert(1.5,'cm','mm'))
print(units_convert(56,'m','cm'))
print(units_convert(40,'g','mg'))
print(units_convert(23.5,'kg','g'))
print(units_convert(35,'F','C'))
print(units_convert(67,'kg','tones'))


    
    


