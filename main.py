def read_book(filename: str) -> str:
    return open(filename).read()

def main() -> None:
    filename: str = "books/frankenstein.txt"
    file_contents: str = read_book(filename)
    num_words: int = count_words(file_contents)
    characters: dict = count_characters(file_contents)
    freq_char: list = order_char_count(characters)
    print(f"There are {num_words} in {filename.split('/')[-1]}.")
    print()
    print("# of characters:")
    for c in freq_char:
        if not c[0].isalpha():
            continue
        print(f"  {c[0]}: {c[1]}")
    print('-'*20)
    return

def count_words(text) -> int:
    return len(text.split())

def count_characters(text: str) -> dict:
    count = {}
    for c in text.lower().replace(' ', '').replace('\n', ''):
        if c in count.keys():
            count[c] += 1
        else:
            count[c] = 1
    return count

def order_char_count(count: dict) -> list:
    ordered_count = []
    for c in count.keys():
        ordered_count.append((c, count[c]))
    ordered_count.sort(reverse=True, key=lambda x: x[1])
    return ordered_count

main()

