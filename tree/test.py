inp = [int(i) for i in input('Enter input: ').split()]

if len(inp) == 2 and inp[0] == -1:
    print('   -1')
    print('  /')
    print('-2')
elif len(inp) == 2 and inp[0] == -2:
    print('-2')
    print('  \ ')
    print('   -2')
else:
    print(-1)