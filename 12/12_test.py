def generate_combinations(s):
    # Find the index of the first '?'
    index = s.find('?')

    # Base case: if no '?' found, print the string
    if index == -1:
        print(s)
        return

    # Replace '?' with '.' and continue recursion
    generate_combinations(s[:index] + '.' + s[index + 1:])

    # Replace '?' with '#' and continue recursion
    generate_combinations(s[:index] + '#' + s[index + 1:])

# Example usage
string_to_replace = '???.###'
generate_combinations(string_to_replace)