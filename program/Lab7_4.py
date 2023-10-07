def replace_words(sentence, forbidden_words):
    words = sentence.lower().split()
    for forbidden_word in forbidden_words:
        lower_forbidden_word = forbidden_word.lower()
        sentence = sentence.replace(forbidden_word, '*' * len(lower_forbidden_word))
    return sentence

with open('input1.txt', 'r') as file:
    forbidden_words = file.read().split()

input_sentence = input('Введите предложение: ')
result = replace_words(input_sentence, forbidden_words)
print('Результат:', result)