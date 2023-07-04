letters_english = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'D', 'G', 'B', 'C', 'M', 'P', 'F', 'H', 'V', 'W', 'Y', 'K', 'J', 'X', 'Q', 'Z']
points_english  = [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   2,   2,   3,   3,   3,   3,   4,   4,   4,   4,   4,   5,   8,   8,   10,  10]
letters_russian = ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т', 'Д', 'К', 'Л', 'М', 'П', 'У', 'Б', 'Г', 'Ё', 'Ь', 'Я', 'Й', 'Ы', 'Ж', 'З', 'Х', 'Ц', 'Ч', 'Ш', 'Э', 'Ю', 'Ф', 'Щ', 'Ъ']
points_russian  = [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   2,   2,   2,   2,   2,   2,   3,   3,   3,   3,   3,   4,   4,   5,   5,   5,   5,   5,   8,   8,   8,   10,  10,  10]
letters = letters_english + letters_russian
points  = points_english  + points_russian
index = 0
sum = 0
word = input("Введите слово : ").upper()
output_word = list(word)
for char in letters:
    index += 1
    for i in range(len(output_word)):
        if output_word[i] == char:
            point_index = points[index-1]
            sum = sum + point_index
print(sum)