def introspection_info(obj):
    # Тип объекта
    type_obj = type(obj).__name__

    # Атрибуты объекта
    attributes_obj = [attrib for attrib in dir(obj) if not callable(getattr(obj, attrib))]
    # dir(obj)

    # Методы объекта
    methods_obj = [method for method in dir(obj) if callable(getattr(obj, method))]

    # К какому модулю принадлежит объект
    module_obj = getattr(obj, '__module__', None)
    # obj.__module__

    info = {'type': type_obj,
            'attributes': attributes_obj,
            'methods': methods_obj,
            'module': module_obj
            }

    return info


# Пример собственного класса
class MyClass:
    def __init__(self, value):
        self.value = value

    def display(self):
        return f"Value: {self.value}"

    def increment(self):
        self.value += 1


number_info = introspection_info(42)
print(number_info)

# Примеры с другими объектами
my_obj = MyClass(42)
class_info = introspection_info(my_obj)
print(class_info)

list_info = introspection_info([1, 2, 3])
print(list_info)

dict_info = introspection_info({'key': 'value'})
print(dict_info)

string_info = introspection_info("Hello, World!")
print(string_info)