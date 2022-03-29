first_string = input("Provide the first string: ")
second_string = input("Provide the second string: ")

def check(first_string, second_string):
    if(sorted(first_string)== sorted(second_string)):
        print("anagrams")
    else:
        print("not anagrams")        
         
check(first_string, second_string)