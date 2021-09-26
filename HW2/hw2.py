"""
Версия с изменением отчётов "inplace" в функциях make_report, print_report и save_report 
"""

import csv


def read_from_file(file_path_name: str):
    """"Из файла записываю в словарь только нужные данные для выполнения ДЗ"""
    with open(file_path_name, newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        next(reader)  # header

        data_dict = {}
        for row in reader:
            parts = data_dict.setdefault(row[1], {})  # 'Департамент' header[1]
            salaries = parts.setdefault(row[2], [])  # 'Отдел' header[2]
            salaries.append(int(row[-1]))
        return data_dict


def menu() -> str:
    print("Выберите вариант:")
    print("1 - Вывести иерархию команд")
    print("2 - Вывести сводный отчёт")
    print("3 - Сохранить сводный отчёт")
    print("4 - Выход")
    return input()


def make_report(data: dict, salary_report: list):
    """Создаю отчёт, который буду потом использовать для печати или записи в файл
       Записываю в полученную переменную salary_report
       make_report  вызывается только, когда salary_report пустой"""
    for dep in data:
        sum_salary = 0
        count_empl = 0
        max_salary = 0
        min_salary = float("inf")
        for part in data[dep]:
            sum_salary += sum(data[dep][part])
            count_empl += len(data[dep][part])
            max_salary = max(max_salary, max(data[dep][part]))
            min_salary = min(min_salary, min(data[dep][part]))
        avg_salary = round(sum_salary / count_empl)
        salary_report.append([dep, count_empl, min_salary, max_salary, avg_salary])


def print_report(data: dict, report: list):
    """Печатаю полученный в report отчёт. 
        Если он пустой, создаю его из data"""
    if not report:
        make_report(data, report)
    for dep, count_empl, min_salary, max_salary, avg_salary in report:
        print(f"{dep}:    Число сотрудников  {count_empl}")
        print(f"    Зарплата:  мин {min_salary}, макс {max_salary}, средн {avg_salary}")


def print_hierarchy(data: dict, *args):
    """Не использую данные из args. 
        Переменная args нужна, так как при вызове print_hierarchy набор параметров может быть неизвестен"""
    for dep in data:
        print(f"{dep}:")
        print("    ", end="")
        print(*data[dep], sep=", ")


def save_report(data: dict, report: list):
    """Сохраняю в файл 'salary_report.csv' полученный в report отчёт. 
        Если он пустой, создаю его из data"""
    HEADER = ["Департамент", "Число сотрудников", "Мин", "Макс", "Средн"]
    if not report:
        make_report(data, report)
    with open("salary_report.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(HEADER)
        for row in report:
            writer.writerow(row)


def main():
    """Читаю данные из 'Corp Summary.csv'
       В зависимости от пункта меню  вызываю функцию из словаря choices или выхожу из цикла ('4')"""
    data_dict = read_from_file("Corp Summary.csv")
    salary_report = []
    choices = {
        "1": print_hierarchy,
        "2": print_report,
        "3": save_report,
    }  # словарь функций
    choice = menu()
    while choice != "4":
        if choice in choices:
            print()
            choices[choice](data_dict, salary_report)
            print()
        choice = menu()


if __name__ == "__main__":
    main()
