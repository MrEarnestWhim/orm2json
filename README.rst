==========
ORM 2 JSON
==========

A library for converting ORM Django models to JSON format. You can easily work with a simple request, as well as nested Many To Many.

Quick start
-----------
0. Install packages::

    pip install django-orm2json

1. Add "orm2json" to your INSTALLED_APPS setting like this (Optional. Under future functionality)::

    INSTALLED_APPS = [
        ...
        'orm2json',
    ]

2. Example code::

    from orm2json import Orm2JSON

    serialize_object = Orm2JSON(
        User.objects.filter(**filter),
        (
            'username',
            'email',
            'avatar',
            {
                'game': ['game_id', 'title'],
                'category': [
                    'category',
                    'internal_name',
                    {
                        'title': [
                            'name',
                            'date'
                        ]
                    }
                ],
            },
        ),
        image_size={
            'avatar': 'icon',
        },
        add_static={
            'custom_field': 'text'
        }
    )
    type(serialize_object.serialize())
    >> <class 'list'>
    type(serialize_object.serialize_json())
    >> <class 'str'>

3. Supported fields:

+---------------------------+-----------+
| Field                     | Supported |
+===========================+===========+
| AutoField                 | ?         |
+---------------------------+-----------+
| BigAutoField              | ?         |
+---------------------------+-----------+
| BigIntegerField           | YES       |
+---------------------------+-----------+
| BinaryField               | ?         |
+---------------------------+-----------+
| BooleanField              | YES       |
+---------------------------+-----------+
| CharField                 | YES       |
+---------------------------+-----------+
| DateField                 | ?         |
+---------------------------+-----------+
| DateTimeField             | ?         |
+---------------------------+-----------+
| DecimalField              | ?         |
+---------------------------+-----------+
| DurationField             | ?         |
+---------------------------+-----------+
| EmailField                | ?         |
+---------------------------+-----------+
| FileField                 | ?         |
+---------------------------+-----------+
| FilePathField             | ?         |
+---------------------------+-----------+
| FloatField                | YES       |
+---------------------------+-----------+
| ImageField                | ?         |
+---------------------------+-----------+
| IntegerField              | YES       |
+---------------------------+-----------+
| GenericIPAddressField     | ?         |
+---------------------------+-----------+
| NullBooleanField          | ?         |
+---------------------------+-----------+
| PositiveIntegerField      | YES       |
+---------------------------+-----------+
| PositiveSmallIntegerField | YES       |
+---------------------------+-----------+
| SlugField                 | ?         |
+---------------------------+-----------+
| SmallIntegerField         | ?         |
+---------------------------+-----------+
| TextField                 | YES       |
+---------------------------+-----------+
| TimeField                 | ?         |
+---------------------------+-----------+
| URLField                  | ?         |
+---------------------------+-----------+
| UUIDField                 | ?         |
+---------------------------+-----------+
| ForeignKey                | YES       |
+---------------------------+-----------+
| ManyToManyField           | YES       |
+---------------------------+-----------+
| OneToOneField             | ?         |
+---------------------------+-----------+

? - Not tested
