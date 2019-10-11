==========
ORM 2 JSON
==========

A library for converting ORM Django models to JSON format. You can easily work with a simple request, as well as nested Many To Many.

Quick start
-----------

1. Add "orm2json" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'orm2json',
    ]

2. Example code::

    import Orm2JSON

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
