import unittest

import task2


class TestFooMethods(unittest.TestCase):

    def setUp(self):
        self.app = task2.app.test_client()
        self.foo = self.app.get('/foo')

    def test_foo_page_is_available(self):
        self.assertEqual(
            self.foo.status_code, 200,
            'Проверьте, что адрес "/foo" доступен')

    def test_foo_page_returns_json(self):
        self.assertTrue(
            self.foo.is_json,
            ('Проверьте что при запросе на страницу "/foo"'
             ' данные возвращаются в формате json'))

    def test_foo_page_result_is_dict(self):
        self.assertTrue(
            isinstance(self.foo.json, dict),
            ('Проверьте что при запросе на страницу "/foo"'
             'возвращаемые данные являются словарем'))

    def test_foo_page_returns_correct_key(self):
        self.assertTrue(
            "ready" in self.foo.json.keys(),
            ('Проверьте что при обращении на страницу "/foo"'
             'в возращаемом словаре указан правильный ключ'))

    def test_foo_page_returns_correct_value(self):
        self.assertEqual(
            self.foo.json.get('ready'), "ok",
            ('Проверьте что при запросе на страницу "/foo"'
             ' приходят правильные данные'))


class Test404Methods(unittest.TestCase):

    def setUp(self):
        self.app = task2.app.test_client()
        self.bar_404 = self.app.get('/404')

    def test_404_page_is_available(self):
        self.assertEqual(
            self.bar_404.status_code, 200,
            'Проверьте, что адрес "/404" доступен')

    def test_404_page_returns_json(self):
        self.assertTrue(
            self.bar_404.is_json,
            ('Проверьте что при запросе на страницу "/404"'
             ' данные возвращаются в формате json'))

    def test_404_page_result_is_dict(self):
        self.assertTrue(
            isinstance(self.bar_404.json, dict),
            ('Проверьте что при запросе на страницу "/404"'
             'возвращаемые данные являются словарем'))

    def test_404_page_returns_correct_key(self):
        self.assertTrue(
            "ready" in self.bar_404.json.keys(),
            ('Проверьте что при обращении на страницу "/404"'
             'в возращаемом словаре указан правильный ключ'))

    def test_404_page_returns_correct_value(self):
        self.assertEqual(
            self.bar_404.json.get('ready'), "not",
            ('Проверьте что при запросе на страницу "/404"'
             ' приходят правильные данные'))


if __name__ == '__main__':
    unittest.main()
