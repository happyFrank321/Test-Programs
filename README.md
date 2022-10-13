# Test-Programs
--Decorator--
Напишите функцию-декоратор, которая сохранит (закеширует) значение декорируемой функции.
Если декорируемая функция будет вызвана повторно с теми же параметрами — декоратор должен вернуть сохранённый результат, не выполняя функцию.

--DecoratorV2--
Напишите декоратор, оптимизирующий работу декорируемой функции. 
Декоратор должен сохранять результат работы функции на ближайшие 3 запуска и вместо выполнения функции возвращать сохранённый результат.

--Test_example__ 
Напишите тесты для модуля, который переводит кириллический текст в сообщения на азбуке Морзе. Убедитесь, что библиотека умеет правильно обрабатывать множество потенциальных ситуаций:
1.Текст превращается в правильное сообщение
2.Если функция модуля получает текст не с кириллическими или латинскими символами, то они не преобразуются на выводе
3.Если функция модуля получает не текст, а какой-то другой объект, то она порождает правильно исключение
4.Проверка правильности указанного языка
