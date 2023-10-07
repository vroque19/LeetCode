# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def combine(words, data_type):
    if data_type == "C":
        return "".join(word.capitalize() for word in words)
    elif data_type =="M":
        return words[0] + "".join(word.capitalize() for word in words[1:]) + '()'
    else:
        return words[0] + "".join(word.capitalize() for word in words[1:])

def separate(name, data_type):
    words = []
    current_word = name[0].lower()
    # BigBlueMuffin
    for char in name[1:]:
        if char.isupper():
            words.append(current_word.lower())
            current_word = char
        else:
            current_word += char
    words.append(current_word.lower())
    return " ".join(words)


def main():
    for line in sys.stdin:
        operation, dat_type, input_str = line.split(";")
        if operation == "S":
            result = separate((input_str), dat_type).replace('(', "").replace(')', "")
        else:
            words = input_str.split()
            result = combine(words, dat_type)
                
        print(result.strip())
        

        
if __name__ == "__main__":
    main()

