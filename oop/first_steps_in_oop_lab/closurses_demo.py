def get_print_list_func(separator_char):
    def internal_print(ll):
        # separator_char makes a closure with parent
        print(separator_char.join(str(x) for x in ll))

    return internal_print

print_list = get_print_list_func('; ')
print_list([1, 2, 3, 4])
print_list = get_print_list_func(' * ')
print_list([5, 6, 7, 8])