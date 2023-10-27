
def is_two(num):
    if num in ('two', 2, 2.0):
        return True
    else:
        return False
    

def is_vowel(string):
    vowels = list('aeiouAEIOU')
    if string[0] in vowels:  
        return True
    else:
        return False
    

def is_consonant(string):
    if not is_vowel(string):
        return True
    else:
        return False
    

def cap_first_letter_if_consonant(string):
    if not is_vowel(string):  
        return string[0].upper() + string[1:]
    else:
        return word



def calculate_tip(bill, tip_percent):
    return bill * tip_percent


def apply_discount(op, dp): 
    return op * (1-dp)


def handle_commas(number_string):
    number_string = number_string.replace(",", "")
    return int(number_string)


def get_letter_grade(grade_input):
    
    grades = {
    'A' : (88,100),
    'B' : (80,87),
    'C' : (67,79),
    'D' : (60, 66),
    'F' : (0, 65)
}
    for grade, (lower,upper) in grades.items():
        if lower <= grade_input <= upper:
            return grade

def remove_vowels(word):
    new_word = " "
    for letter in word:
        if not is_vowel(letter):
            new_word += letter
    return new_word

def normalize_name(string):
    normalize_name = string.strip().lower()
    normalize_name = normalize_name.replace(' ', '_')
    valid_py_ids = 'abcdefghijklmnopqrstuvwxyz0123456789_'
    normalize_name = ''.join(char for char in normalize_name if char in valid_py_ids)

    return normalize_name


def cumulative_sum(num_list):
    cumulative = []  
    total = 0  

    for num in num_list:
        total += num  
        cumulative.append(total)  

    return cumulative

