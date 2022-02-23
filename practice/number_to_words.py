print("Welcome to the number word maker.\n"
                        "Simply type the number you would like to convert to words and hit 'Enter'\n"
                        "(The max number is 9999)\n")
running = True
while running:
    num = int(input("Number: "))
    ones = num%10 #find the ones digit
    tens = (num%100 - num%10)//10 #find the tens digit
    hundreds = (num%1000 - num%100)//100 #find the hundreds digit
    thousands = (num%10000 - num%1000)//1000 #find the thousands digit

    onesPre = ''
    if num == 0:
        print('zero')           #prints 'zero' if number is zero
    elif ones > 0:
        if ones == 1:
            onesPre = 'one'         #set the numbers of ones to be words
        elif ones == 2:
            onesPre = 'two'
        elif ones == 3:
            onesPre = 'three'
        elif ones == 4:
            onesPre = 'four'
        elif ones == 5:
            onesPre = 'five'
        elif ones == 6:
            onesPre = 'six'
        elif ones == 7:
            onesPre = 'seven'
        elif ones == 8:
            onesPre = 'eight'
        elif ones == 9:
            onesPre = 'nine'
            
    tensPre = ''
    if tens > 0:
        if tens == 1:
            if ones == 0:
                tensPre = 'ten'
            if ones == 1:                 #special tens numbers wording
                tensPre = 'eleven'
                onesPre = ''
            elif ones == 2:
                tensPre = 'tweleve'
                onesPre = ''
                
            elif ones >= 3:
                onesPre = 'teen'            #teens numbers wording
                if ones == 3:
                    tensPre = 'thir'
                elif ones == 4:
                    tensPre = 'four'
                elif ones == 5:
                    tensPre = 'fif'
                elif ones == 6:
                    tensPre = 'six'
                elif ones == 7:
                    tensPre = 'seven'
                elif ones == 8:
                    tensPre = 'eigh'
                elif ones == 9:
                    tensPre = 'nine'
                    
        elif tens == 2:               #regular tens place wording
            tensPre = 'twenty'
        elif tens == 3:
            tensPre = 'thirty'
        elif tens == 4:
            tensPre = 'fourty'
        elif tens == 5:
            tensPre = 'fifty'
        elif tens == 6:
            tensPre = 'sixty'
        elif tens == 7:
            tensPre = 'seventy'
        elif tens == 8:
            tensPre = 'eighty'
        elif tens == 9:
            tensPre = 'ninety'

    if ones > 0:            #adds a hyphen if the ones digit is more than zero (e.x. twenty-three vs twenty)
        if tens >= 2:
            tensPre = tensPre+'-'

    hundredsPre = ''
    hundred = 'hundred '
    if hundreds == 0:
        hundred = ''            #removes the word hundred if the hundreds place is a zero (e.x. seven thousand twenty-three)
    elif hundreds > 0:
        if hundreds == 1:
            hundredsPre = 'one '
        elif hundreds == 2:
            hundredsPre = 'two '
        elif hundreds == 3:
            hundredsPre = 'three '
        elif hundreds == 4:
            hundredsPre = 'four '
        elif hundreds == 5:
            hundredsPre = 'five '
        elif hundreds == 6:
            hundredsPre = 'six '
        elif hundreds == 7:
            hundredsPre = 'seven '
        elif hundreds == 8:
            hundredsPre = 'eight '
        elif hundreds == 9:
            hundredsPre = 'nine '

    thousandsPre = ''
    thousand = 'thousand '
    if thousands == 0:
        thousand = ''            #removes the word thousand if the thousands place is a zero (e.x. seven hundred twenty-three)
    elif thousands > 0:
        if thousands == 1:
            thousandsPre = 'one '
        elif thousands == 2:
            thousandsPre = 'two '
        elif thousands == 3:
            thousandsPre = 'three '
        elif thousands == 4:
            thousandsPre = 'four '
        elif thousands == 5:
            thousandsPre = 'five '
        elif thousands == 6:
            thousandsPre = 'six '
        elif thousands == 7:
            thousandsPre = 'seven '
        elif thousands == 8:
            thousandsPre = 'eight '
        elif thousands == 9:
            thousandsPre = 'nine '
        
            
    print(thousandsPre+thousand+hundredsPre+hundred+tensPre+onesPre,'\n')     #prints result (except if it is zero)
