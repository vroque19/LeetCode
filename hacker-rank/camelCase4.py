# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def combine(words):
    return "".join(word.capitalize() for word in words)

def separate(name):
    words = []
    current_word = name[0]
    
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
        operation, var_type, input_str = line.split(";")
        if operation == "S":
            if var_type == "M":
                result = separate(input_str[:-2])
            else:
                result = separate(input_str)
        else:
            words = input_str.split()
            if var_type == "M":
                result = input_str[:1] + combine(words)[1:]
                result += "()"
            else:
                result = combine(words)
                
        print(result.strip())

        
if __name__ == "__main__":
    main()
