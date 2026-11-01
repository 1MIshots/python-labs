def main():
    word = input()
    # По условию слово непустое.
    result = word[1:] + word[0]
    print(repr(result))

if __name__ == '__main__':
    main()
