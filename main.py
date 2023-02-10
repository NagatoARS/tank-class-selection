from db import *


def main():

    total = 0
    for key in questions:
        print(f'{key} - {questions[key]}')
        this_answers = answers[key]
        count = 1
        # {'count': 'ключ_конкретного_ответа'}
        dict_count = {}
        for ans in this_answers:
            for add_key in ans:
                print(f'- {count} - {ans[add_key]}')
                dict_count[count] = add_key
                count += 1

        result = input('Введите номер ответ: \n')
        if result.isdecimal() == False:
            print("Error")
            exit()
        result = int(result)
        while result > len(dict_count):
            result = input('Некорректный ввод! Введите номер ответ: \n')
            result = int(result)
        id_answer = dict_count[result]
        current_value = indicator.get(id_answer)
        if current_value is not None:
            # total=total+indicator[id_answer]
            print("Hello world")

        try:
            total = total+indicator[id_answer]
            print(100/0)
        except KeyError:
            print("Except,KeyError!")
        except ZeroDivisionError:
            print("Except, ZeroDivisionError!")

    print('-----')
    print(total)


if __name__ == "__main__":
    main()
