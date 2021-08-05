class FalseNumber:
    pass
class CalcTest:

    @staticmethod
    def addition(n, m):
        """Шукає суму двох чисел

        >>> CalcTest.addition(4, 2)
        6

        :param n: Перше ч
        :param m: Друге ч
        :return: Результат
        """
    @staticmethod
    def subtraction(n, m):
        """Шукає різницю двох чисел

        >>> CalcTest.subtraction(9, 2)
        7


        :param n: Перше ч
        :param m: Друге ч
        :return: Результат
        """

    @staticmethod
    def multiplication(n, m):
        """ Шукає добуток чисел
        >>> CalcTest.multiplication(12, 2)
        24

        :param n: Перше число
        :param m: Друге число
        :return: Результат
        """

    @staticmethod
    def division(n, m):
        """ Шукає частку чисел
        >>> CalcTest.division(12, 2)
        6

        :param n: Перше число
        :param m: Друге число
        :return: Результат
        """

    @staticmethod
    def degree(n, m):
        """ Шукає степінь числа
        >>> CalcTest.degree(12, 2)
        144

        :param n: Перше число
        :param m: Друге число
        :return: Результат
        """

    @staticmethod
    def root(n, m):
        """ Шукає корінь числа
        >>> CalcTest.root(169, 2)
        13

        :param n: Перше число
        :param m: Степінь
        :return: Результат
        """

        if n <= 0:
         raise FalseNumber
        else:
            return n ** (1 / b)

    @staticmethod
    def percentage(n, m):
        """ Шукає проценти числа
        >>> CalcTest.root(100, 10)
        10

        :param n: Перше число
        :param m: Друге число
        :return: Результат
        """

        if n <= m:
            raise FalseNumber
        else:
            return m * 100 / n
