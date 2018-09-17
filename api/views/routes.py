"""
Routes module to handle request urls
"""
from api.controllers.orders_controllers import OrdersController


class Urls:
    """
        Class to generate urls
    """

    @staticmethod
    def generate(app):
        """
        Generate urls
        :param app:
        :return:
        """
        app.add_url_rule('/api/v1/orders/', view_func=OrdersController.as_view('make_order'),
                         methods=['POST'], strict_slashes=False)
