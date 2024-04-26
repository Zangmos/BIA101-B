input_str = "((())))(()(())())(()())))))((()())()))()()())())(())(()(())(())()(((()()(((((()(((()))()(()(())()))(((("
floor_index= 0

for i in input_str:
    if i== "(":
        floor_index= floor_index+1
    if i ==")":
        floor_index= floor_index-1
print('the final floor is', floor_index)


def is_valid_brackets(input_str):
    stack = []
    brackets = {'(': ')', ')': '('}
    for char in input_str:
        if char in brackets:
            if stack and brackets[char] == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
    return not stack


print(is_valid_brackets("()"))  
print(is_valid_brackets("(())"))  
print(is_valid_brackets("(()))")) 
print(is_valid_brackets("((()))")) 
print(is_valid_brackets(")("))

# Example usage
input_str = "()(()"
print(is_valid_brackets(input_str))
 
input_str = "((())))(()(())())(()())))))((()())()))()()())())(())(()(())(())()(((()()(((((()(((()))()(()(())()))(((("
stack = []
for char in input_str:
    if char == "(":
        stack.push(char)
    if char == ")":
        stack.pop(char)
print ("length of stack:", stack)


input_str = "((())))(()(())())(()())))))((()())()))()()())())(())(()(())(())()(((()()(((((()(((()))()(()(())()))(((("
stack = []
for char in input_str:
    if char == "(":
        stack.append(char)
    if char == ")":
        stack.pop(char)
print ("length of stack:", stack)
if length != 0:
    print(True)
else:
    print(False)
