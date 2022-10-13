from math import sqrt
from typing import TextIO

from matplotlib import pyplot as plt


def task1(movies_views: list[int], file: TextIO) -> None:
    row_format = "{:>4} {:>9}"
    file.write("Таблиця частот:\n")
    file.write("Фільм   Перегляди\n")
    for index, movie_views in enumerate(movies_views, 1):
        file.write(f"{row_format.format(index, movie_views)}\n")
    checked = []
    file.write("Таблиця сукупних частот:\n")
    file.write("Частота   Перегляди\n")
    for movie_views in movies_views:
        if movie_views in checked:
            continue
        frequency = movies_views.count(movie_views)
        checked.append(movie_views)
        file.write(f"{row_format.format(frequency, movie_views)}\n")
    max_views = max(movies_views)
    file.write(f"Фільми, переглянуті найчастіше:\n")
    for index, movie_views in enumerate(movies_views, 1):
        if max_views == movie_views:
            file.write(f"{index} - {max_views}\n")


def task2(movies_views: list[int], file: TextIO) -> None:
    maxFrequency = 0
    checked = []
    for movie_views in movies_views:
        if movie_views in checked:
            continue
        frequency = movies_views.count(movie_views)
        checked.append(movie_views)
        if frequency > maxFrequency:
            maxFrequency = frequency
            mode = movie_views

    file.write(f"Мода: {mode}\n")

    movies_views = sorted(movies_views)
    n = len(movies_views) - 1
    median = (movies_views[int(n / 2)] + movies_views[int(n / 2 + 0.5)]) / 2
    file.write(f"Медіана: {median}\n")


def task3(movies_views: list[int], file: TextIO) -> None:
    n = len(movies_views)
    S = 0
    for movie_views in movies_views:
        S += movie_views
    mean = S / n
    result = 0
    for movie_views in movies_views:
        result += (movie_views - mean) ** 2
    file.write(f"Дисперсія: {result / (n - 1)}\n")

    file.write(f"Середнє квадратичне відхилення розподілу: {sqrt(result / (n - 1))}\n")


def task4(movies_views: list[int]) -> None:
    plt.figure(figsize=(15, 6), dpi=80)
    plt.xlabel("Movies")
    plt.ylabel("Views")
    n = len(movies_views)
    plt.bar([f"{'M' + str(i) if (i % (n / 20) == 0 or i == n - 1) else i * ' '}" for i in range(len(movies_views))],
            movies_views)
    plt.savefig("result.png")


def main() -> None:
    while True:
        file_name = input("Назва файла: ")
        try:
            with open(file_name + ".txt") as file:
                movies_views = list(map(int, file.read().splitlines()[1:]))
            break
        except FileNotFoundError:
            print("Файл не знайдено")

    with open("result.txt", "w", encoding="utf-8-sig") as file:
        file.write("Завдання №1:\n")
        task1(movies_views, file)

        file.write("\n")
        file.write("Завдання №2:\n")
        task2(movies_views, file)

        file.write("\n")
        file.write("Завдання №3:\n")
        task3(movies_views, file)

        task4(movies_views)


if __name__ == "__main__":
    main()
