from django.apps import AppConfig


class NotesConfig(AppConfig):
    """
    Configuration class for the 'notes' application.

    This class inherits from Django's AppConfig and provides
    the configuration details for the 'notes' application,
    such as the name of the app and the default field type
    for primary key auto-generation.

    :ivar default_auto_field: Specifies the default type for
    auto-created primary key fields.
    :type default_auto_field: str
    :ivar name: Defines the full Python path to the application.
    :type name: str
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notes'
