# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True
word="elbow"
anagram="below"

def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = word.lower()
    anagram = anagram.lower()
    
if (len(word) == len(anagram)):
    
    sorted_word = sorted(word)
    sorted_anagram = sorted(anagram)
    
    if(sorted_word == sorted_anagram):
    	print("True")
    else:
    		print("False")
    		
else:
    print("False")
    
word = "Dear"
anagram = "Read"
