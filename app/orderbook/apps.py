from django.apps import AppConfig

class OrderbookConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orderbook'

    def ready(self):
        print("starting orderbook scheduler")
        from orderbook import utils
        # import importlib
        # importlib.reload(utils)
        utils.solidScheduler()
        # python manage.py runserver --noreload