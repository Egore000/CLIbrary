from dataclasses import dataclass
from domain.exceptions.base import ApplicationException
from domain.values.base import BaseValue


@dataclass
class Inputter:
    """
        Менеджер ввода значения нужного типа
        
        :param BaseValue value_type: Тип входного значения
        :param str msg: Сообщение при вводе в терминале
        :param *exceptions: Возможные исключения
        :type *exceptions: ApplicationException   
    """

    value_type: BaseValue 
    msg: str
    exceptions: ApplicationException | tuple[ApplicationException]

    @classmethod
    def input(cls) -> BaseValue | None:
        """
        Ввод значения нужного типа
        
        :return: Значение нужного типа
        :rtype: BaseValue or None

        :raises ApplicationException:   
        """
        value = None
        while True:
            try:
                value = cls.value_type(input(cls.msg).strip())
                return value    
            except cls.exceptions as e:
                print(e.message)
