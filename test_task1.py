import inspect
import unittest

import task1 as test_module


class TestTask1Methods(unittest.TestCase):

    def test_class_is_exists(self):
        self.assertTrue(
            hasattr(test_module, 'Student'),
            'Проверьте есть ли класс Student в модуле')
        self.assertTrue(
            inspect.isclass(test_module.Student),
            'Проверьте что Student является классом'
        )

    def test_class_has_foo_method(self):
        class_obj = test_module.Student
        self.assertTrue(
            hasattr(class_obj, 'foo'),
            'Проверьте есть ли у класса Student метод foo')
        self.assertTrue(
            isinstance(class_obj.foo, property),
            ('Проверьте что Student.foo является методом и при'
             ' его обьявлении используется декоратор @property')
        )

    def test_variable_is_instance_of_student(self):
        self.assertTrue(
            hasattr(test_module, 'student'),
            'Проверьте что создали переменную student')
        self.assertTrue(
            isinstance(test_module.student, test_module.Student),
            ('Проверьте, переменная student'
             ' является экземпляром класса Student'))

    def test_student_foo_returns_bar(self):
        student = test_module.student
        self.assertEqual(
            student.foo, 'bar',
            'Проверьте что экземпляр student класса Student возвращает "bar"')


if __name__ == '__main__':
    unittest.main()
