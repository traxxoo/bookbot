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

def listing_the_dict(letter_data):
    character_metadata = []
    for key,value in letter_data.items():
        meta_data_dict = {}
        meta_data_dict["char"] = key
        meta_data_dict["num"] = value
        character_metadata.append(meta_data_dict)
    character_metadata.sort(reverse = True, key = sort_on )
    return character_metadata



def sort_on(items):
    return items["num"]
