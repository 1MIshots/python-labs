def main():
    text = input()
    n_position = text.find('н')
    k_position = text.find('к')
    # По условию обе строчные кириллические буквы присутствуют.
    if n_position < k_position:
        print('Раньше н')
    else:
        print('Раньше к')

if __name__ == '__main__':
    main()
