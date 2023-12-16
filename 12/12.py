import sys
D = open(sys.argv[1]).read().strip()
lines = D.split('\n')


def test_match(field, hint):
    a = [x for x in field.split('.') if '#' in x]
    a = [len(x) for x in a]
    if a == hint:
        return True
    else:
        return False

def generate_combinations(s, hint):
    # Find the index of the first '?'
    index = s.find('?')

    # Base case: if no '?' found, print the string
    if index == -1:
        # print(s)
        if test_match(s,hint):
            return 1
        else:
            return 0

    ans = 0
    # Replace '?' with '.' and continue recursion
    ans += generate_combinations(s[:index] + '.' + s[index + 1:], hint)

    # Replace '?' with '#' and continue recursion
    ans += generate_combinations(s[:index] + '#' + s[index + 1:], hint)

    return ans

ans = 0
part2 = True
for line in lines:
    field, hint = line.split()
    hint = [int(x) for x in hint.split(',')]
    if part2:
        field = '?'.join([field]*5)
        hint = hint*5
    score = generate_combinations(field, hint)
    print(score)
    ans += score

print(ans)
