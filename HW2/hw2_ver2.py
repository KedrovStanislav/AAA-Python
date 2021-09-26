"""
Версия без изменения отчётов "inplace" в функциях make_report, print_report и save_report 
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


def make_report(data: dict):
    """Создаю отчёт, который буду потом использовать для печати или записи в файл"""

    salary_report = []
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
    return salary_report


def print_hierarchy(data: dict):
    """Печатаю иерархию"""

    for dep in data:
        print(f"{dep}:")
        print("    ", end="")
        print(*data[dep], sep=", ")


def print_report(report: list):
    """Печатаю полученный в report отчёт."""

    for dep, count_empl, min_salary, max_salary, avg_salary in report:
        print(f"{dep}:    Число сотрудников  {count_empl}")
        print(f"    Зарплата:  мин {min_salary}, макс {max_salary}, средн {avg_salary}")


def save_report(report: list):
    """Сохраняю в файл 'salary_report.csv' полученный в report отчёт"""

    HEADER = ["Департамент", "Число сотрудников", "Мин", "Макс", "Средн"]
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
    choice = menu()
    while choice != "4":
        if choice == "1":
            print_hierarchy(data_dict)
        elif choice == "2":
            if not salary_report:
                salary_report = make_report(data_dict)
            print_report(salary_report)
        elif choice == "3":
            if not salary_report:
                salary_report = make_report(data_dict)
            save_report(salary_report)
        print()
        choice = menu()


if __name__ == "__main__":
    main()
