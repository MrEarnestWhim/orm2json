import json

from django.db.models import QuerySet


class Orm2JSON:
    """
    Серелизатор данных (ага, а тут докума на русском :3)
    """

    def __init__(self, data, allowed: (list, tuple), add_static=None, **kwargs):
        """
        :param data: Объект или кверисет объектов
        :param allowed: Что хотим получить из этого объекта
        :param add_static: Докинуть какие-то кастомные поля в объект
        Пример:
            Serializer(
                User.objects.filter(**filter),
                (
                    'username',
                    'guid',
                    'avatar',
                    {
                        'game': ['game_id', 'title'],
                        'category': [
                            'category',
                            'internal_name',
                        ],
                    },
                ),
                image_size={
                    'avatar': 'icon',
                },
                add_static={
                    'custom_field': 'какой то текст' (получается, это поле и содержимое будет у каждого пользователя)
                }
            )
         Тем самым на выходе мы получим от пользователей только имя, гуид и аватарку, при этом аватарка будет самой
         маленькой.
        """

        if add_static is None:
            add_static = {}

        self.add_static = add_static
        self.allowed = allowed
        self.data = data
        self.filters = kwargs

    def filter_data(self, item, name=''):
        """
        Обработка кастомных типов данных.
        :param item: Содержимое поля из модели
        :param name: Имя этого поля
        на выходе получаем то, что можно преобразовать в JSON
        """
        # Вот интересный пример для картинок от StdImageFieldFile

        # if isinstance(item, StdImageFieldFile):
        #     if item:
        #         try:
        #             image = getattr(item, self.image_size[name]) if self.image_size.get(name) else item
        #         except AttributeError:
        #             return ''
        #         return '/static/media/' + str(image)
        #     return ''

        if hasattr(item, '__dict__'):
            # Проверка на класс
            return item.__str__()

        return item

    def __getter(self, obj) -> dict:
        """
        Вытаскиваем из модели то что нам нужно
        :param obj: Объект модели
        :return: dict готовый на выход
        """
        result = {}
        for item in self.allowed:
            if isinstance(item, str):
                result.update({
                    item: self.filter_data(
                        getattr(obj, item, ''))
                })
            else:
                for key in item.keys():
                    try:
                        if 'ManyRelatedManager' in str(type(getattr(obj, key))) \
                                or 'RelatedManager' in str(type(getattr(obj, key))):
                            _many_result = []
                            for many_item in getattr(obj, key).all():
                                many_ser_object = Orm2JSON(many_item, item[key])
                                _many_result += many_ser_object.serialize()

                            result.update({
                                key: _many_result
                            })
                            continue
                    except Exception:
                        result.update({
                            key: []
                        })
                        continue

                    ser_object = Orm2JSON(getattr(obj, key), item[key])
                    try:
                        _data = ser_object.serialize()[0]
                    except IndexError:
                        _data = {}

                    result.update({
                        key: _data
                    })

        if self.add_static:
            result.update(self.add_static)

        return result

    def serialize(self) -> list:
        """
        Внешняий метод, запускающий серелизацию.
        :return:
        """
        # Если дата вдруг пришла пустая. Ибо тот же .first() при пустате вернет None
        if self.data is None:
            return []

        # Если нам придет список объектов
        if isinstance(self.data, QuerySet):
            result = []
            for item in self.data:
                result.append(self.__getter(item))

            return result

        # Ну или объект всего 1
        return [self.__getter(self.data)]

    def serialize_json(self) -> str:
        return json.dumps(self.serialize())
