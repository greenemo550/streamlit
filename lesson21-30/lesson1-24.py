def is_anagram(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    word1 = "".join(e for e in word1 if e.isalnum())
    word2 = "".join(e for e in word2 if e.isalnum())
    return sorted(word1) == sorted(word2)

def frequency_counter(word):
    freq_dict = {}
    for i in word:
        if i in freq_dict:
            freq_dict[i] += 1
        else:
            freq_dict[i] = 1
    return freq_dict

def has_duplicates(lst):
    unique_list = set(lst)
    return len(unique_list) != len(lst)

print(is_anagram("anagra", "graana"))
print(frequency_counter("apple"))  
print(has_duplicates([1, 2, 3, 4, 5]))  
print(has_duplicates([1, 2, 3, 4, 5, 3]))  
