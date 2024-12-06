# module_1_7

# Исходные данные
grades = [[5, 3, 3, 5, 4], [2, 4, 3, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5],[5, 5, 5, 4, 5]]
students = {"Иванов","Сидоров", "Кузнецова", "Антохин", "Смирнова", "Желнова"}

# Преобразуем множество в отсортированный список для корректного сопоставления
sorted_students = sorted(students)

# Создаем пустой словарь для хранения результатов
average_grades = {}

# Проходимся по списку оценок и вычисляем средние баллы
for i in range(len(grades)):
    student_name = sorted_students[i]
    student_grades = grades[i]

    # Вычисление среднего балла
    average_grade = sum(student_grades) / len(student_grades)

    # Добавляем запись в словарь
    average_grades[student_name] = round(average_grade, 2)

print(average_grades)

