import re

def main():
    with open('input.txt') as file:
        regex = re.compile(f'^({file.readline().strip().replace(', ', '|')})+$', flags=re.MULTILINE)
        print(len(regex.findall(file.read())))


if __name__ == '__main__':
    main()
