
# Задачка 1

В первом задании студенту нужно написать класс Student с инициализатором и методом foo(), который возвращает “bar” затем создать student – экземпляр этого класса. 


Проверьте в тестах, что

- класс существует
- у класса есть метод foo
- student - экземпляр класса student
- student.foo возвращает “bar”


# Задачка 2

Во очередном задании студенту нужно написать приложение на Flask, которое при обращении к /foo возвращает {“ready”: “ok} со статус-кодом 200, а при обращении к /404 –  {“ready”: “not”} со статус кодом 200.

Проверьте в тестах, что

- маршрут /foo обрабатывается
- маршрут /404 обрабатывается
- при обращении  к /foo возвращается  {“ready”: “ok”}
- при обращении  к /404 возвращается  {“ready”: “not”}


Тесты пишите с помощью unittest. Если тест падает, студент всегда должен понимать, что он сделал не так и что ему нужно сделать теперь!
