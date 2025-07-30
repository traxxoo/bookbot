def return_count(file_text):
    total_count_list = file_text.split()
    total_count = 0
    for letter in total_count_list:
        total_count += 1
    return total_count

def letter_count(file_text):
    each_letter_count = {}
    file_text = file_text.lower()
    for letter in file_text:
        if letter in each_letter_count:
            each_letter_count[letter] +=1
        else:
            each_letter_count[letter]= 1
    
    return each_letter_count
