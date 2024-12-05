# Импорт необходимых библиотек
import rt_with_exceptions as runner
import unittest
import logging

# Настройка логирования
logging.basicConfig(
    level=logging.INFO, 
    filemode='w', 
    filename='runner_tests.log',
    encoding='UTF-8', 
    format='%(asctime)s | %(levelname)s | %(message)s'
)

# Тестовый класс для проверки функциональности Runner
class RunnerTest(unittest.TestCase):
    # Тест метода walk
    def test_walk(self):
        try:
            run = runner.Runner("Вася", -5)  # Создание экземпляра с отрицательной скоростью
            for _ in range(10):
                run.walk()  # Эмуляция 10 шагов
            self.assertEqual(run.distance, 50)  # Проверка пройденной дистанции
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning("Неверная скорость для Runner", exc_info=True)
            return f'Error! {e}'

    # Тест метода run
    def test_run(self):
        try:
            run = runner.Runner(2)  # Создание экземпляра с корректным параметром
            for _ in range(10):
                run.run()  # Эмуляция 10 забегов
            self.assertEqual(run.distance, 100)  # Проверка пройденной дистанции
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)
            return f'Error! {e}'

    # Тест сравнения двух объектов Runner
    def test_challenge(self):
        run1 = runner.Runner('Name3.1')
        run2 = runner.Runner('Name3.2')
        for _ in range(10):
            run1.walk()
            run2.run()
        self.assertNotEqual(run1.distance, run2.distance)  # Проверка различий в дистанциях

# Запуск тестов
if __name__ == '__main__':
    unittest.main()
