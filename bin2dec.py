def bin2dec(bin):
    reversed_bin = [int(i) for i in bin][::-1]
    return sum([reversed_bin[i] * 2 ** i for i in range(len(reversed_bin))])


bin_number = input()
is_bin = set(bin_number).issubset({'0', '1'}) or set(bin_number[1::]).issubset({'0', '1'})
minus = bin_number[0] == '-'
if is_bin:
    print(bin2dec(bin_number))
elif is_bin and minus:
    print(f'-{bin2dec(bin_number[1::])}')
else:
    print('Введите двоичное число, состоящее из нулей и единиц')
