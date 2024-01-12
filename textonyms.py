def gen_textonyms(word):
    key_mapping = {'a': '2', 'b': '2', 'c': '2', 'd': '3', 'e': '3', 'f': '3',
                   'g': '4', 'h': '4', 'i': '4', 'j': '5', 'k': '5', 'l': '5',
                   'm': '6', 'n': '6', 'o': '6', 'p': '7', 'q': '7', 'r': '7',
                   's': '7', 't': '8', 'u': '8', 'v': '8',
                   'w': '9', 'x': '9', 'y': '9', 'z': '9'}

    num_representation = ' '.join(key_mapping[char] for char in word.lower())

    return num_representation


def find_textonyms(user_word, word_list):
    user_word_num = gen_textonyms(user_word)
    textonyms_find = [word for word in word_list if gen_textonyms(word) == user_word_num]
    return textonyms_find


if __name__ == "__main__":
    with open('word_list.txt', 'r') as file:
        word_list = [line.strip() for line in file]
        print(word_list)
    user_input = input("Enter a word:")

    textonyms = find_textonyms(user_input, word_list)
    if textonyms:
        print(f"Textonyms for '{user_input}':{' '.join(textonyms)}")
    else:
        print(f"no textonyms found for'{user_input}'.")
