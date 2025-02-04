def get_file_contents(file_to_read):
    file_contents = ""
    with open(file_to_read) as f:
        file_contents = f.read()
    return file_contents

def count_words(file_to_count):
    return len(file_to_count.split())

def count_characters(word_to_count):
    count_dict = {}
    for character in word_to_count:
        character_lowered = character.lower()
        if character_lowered in count_dict:
            count_dict[character_lowered] += 1
        else:
            count_dict[character_lowered] = 1
    return count_dict

def print_report(path_to_file, words_count, character_count):
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{words_count} words found in the document\n")
    for character in character_count:
        if character.isalpha():
            print(f"The '{character}' character was found {character_count[character]} times")
    print("--- End report ---")

def main():
    path_to_file = "books/frankenstein.txt"
    file_contents = get_file_contents(path_to_file)
    words_count = count_words(file_contents)
    character_count = count_characters(file_contents)
    print_report(path_to_file, words_count, character_count)

main()