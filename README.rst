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


