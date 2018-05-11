ones = {
"0":'',
"1":'one',
"2":'two',
"3":'three',
"4":'four',
"5":'five',
"6":'six',
"7":'seven',
"8":'eight',
"9":'nine'
}


teens = {
"10":'ten',
"11":'eleven',
"12":'twelve',
"13":'thirteen',
"14":'fourteen',
"15":'fifteen',
"16":'sixteen',
"17":'seventeen',
"18":'eighteen',
"19":'nineteen'
}

tens = {

"0":'',
"2":'twenty',
"3":'thirty',
"4":'forty',
"5":'fifty',
"6":'sixty',
"7":'seventy',
"8":'eighty',
"9":'ninety'
}

def num_to_word(n):
    n = list(str(n))
    lg = len(n)
    if lg == 1:
        ones_place = n[0]
        return ones[ones_place]
    elif lg == 2:
        tens_place, ones_place = n
        if tens_place == '1':
            return teens[tens_place + ones_place]
        elif tens_place != "1" and ones_place != "0":
            return tens[tens_place] + ones[ones_place]
        elif tens_place != "1" and ones_place == "0":
            return tens[tens_place]

    elif lg == 3:
            hund_place, tens_place, ones_place = n
            #even multiple of 100
            if tens_place == '0' and ones_place == '0':
                return ones[hund_place] + 'hundred'
            #hundreds and a teen
            elif tens_place == '1':
                return ones[hund_place] + 'hundredand'+ teens[tens_place + ones_place]
            #hundreds and somethign other than a teen
            elif tens_place != "1" and ones_place == '0':
                return ones[hund_place] + 'hundredand' + tens[tens_place]
            elif tens_place == '0' and ones_place != '0':
                return ones[hund_place] + 'hundredand' + ones[ones_place]
            elif tens_place != '1' and ones_place != '0':
                return ones[hund_place] + 'hundredand'+ tens[tens_place] + ones[ones_place]
    elif lg == 4:
        return 'onethousand'

if __name__ == '__main__':
    low = int(input('low = '))
    high = int(input('high = '))
    val = sum(len(num_to_word(i)) for i in range(low, high+1))
    print(val)
    #for val in range(low, high+1):
    #    print(num_to_word(val))
