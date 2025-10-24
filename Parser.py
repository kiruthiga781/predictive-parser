# Predictive Parser for Arithmetic Expressions

# Grammar:
# E  -> T E'
# E' -> + T E' | ε
# T  -> F T'
# T' -> * F T' | ε
# F  -> (E) | id

parsing_table = {
    'E': {'id': ['T', "E'"], '(': ['T', "E'"]},
    "E'": {'+': ['+', 'T', "E'"], ')': ['ε'], '$': ['ε']},
    'T': {'id': ['F', "T'"], '(': ['F', "T'"]},
    "T'": {'+': ['ε'], '*': ['*', 'F', "T'"], ')': ['ε'], '$': ['ε']},
    'F': {'id': ['id'], '(': ['(', 'E', ')']}
}

terminals = ['id', '+', '*', '(', ')', '$']
non_terminals = ['E', "E'", 'T', "T'", 'F']

def predictive_parse(input_tokens):
    stack = ['$', 'E']
    index = 0
    print(f"{'Stack':<20}{'Input':<20}{'Action'}")

    while len(stack) > 0:
        top = stack[-1]
        current_input = input_tokens[index]

        print(f"{' '.join(stack):<20}{' '.join(input_tokens[index:]):<20}", end='')

        if top in terminals:
            if top == current_input:
                stack.pop()
                index += 1
                print(f"Match {current_input}")
            else:
                print("Error: Unexpected symbol")
                return False
        elif top in non_terminals:
            if current_input in parsing_table[top]:
                production = parsing_table[top][current_input]
                stack.pop()
                if production != ['ε']:
                    stack.extend(production[::-1])
                print(f"{top} -> {' '.join(production)}")
            else:
                print("Error: No rule for this symbol")
                return False
        elif top == '$':
            if top == current_input:
                print("Accepted ✅")
                return True
            else:
                print("Error: Stack end reached")
                return False
    return False


def tokenize(expression):
    tokens = []
    i = 0
    while i < len(expression):
        if expression[i].isalpha():
            tokens.append('id')
            while i < len(expression) and expression[i].isalnum():
                i += 1
        elif expression[i] in ['+', '*', '(', ')']:
            tokens.append(expression[i])
            i += 1
        elif expression[i] == ' ':
            i += 1
        else:
            print(f"Invalid character: {expression[i]}")
            return []
    tokens.append('$')
    return tokens


if __name__ == "__main__":
    expression = input("Enter an arithmetic expression: ")
    tokens = tokenize(expression)
    if tokens:
        print("\nTokens:", tokens)
        print("\n--- Parsing Process ---")
        result = predictive_parse(tokens)
        print("\nResult:", "Valid Expression ✅" if result else "Invalid Expression ❌")
          
