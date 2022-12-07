dictionary = {'Россия': 'Москва',
              'Франция': 'Париж',
              'Германия': 'Берлин',
              'Нидерланды': 'Амстердам',
              'Испания': 'Мадрид',
              'Турция': 'Анкара',
              'Италия': 'Рим',
              'Китай': 'Пекин',
              'Бразилия': 'Бразилиа',
              'ЮАР': 'Кейптаун',
              'США': 'Вашингтон',
              'Япония': 'Токио'}
inverted_dictionary = {value: key for key, value in dictionary.items()}
if __name__ == '__main__':
    while True:
        print('Что вы хотите сделать? (1 - узнать столицу по названию страны, 2 - узнать страну по столице): ')
        choice = input()
        if choice == '1':
            print('Введите название страны: ')
            country = input()
            if dictionary.get(country) is not None:
                print('Столицей государства ' + country + ' является город ' + dictionary.get(country))
            else:
                print('Такой страны в списке нет!')
        elif choice == '2':
            print('Введите название столицы: ')
            capital = input()
            if inverted_dictionary.get(capital) is not None:
                print('Страной со столицей ' + capital + ' является ' + inverted_dictionary.get(capital))
            else:
                print('Такой столицы в списке нет!')
        else:
            print('Некорректный ввод действия, попробуйте еще раз!')
