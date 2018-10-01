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
        app.add_url_rule('/api/v2/auth/signup/', view_func=OrdersController.as_view('register_user'),
                         methods=['POST'], strict_slashes=False)
        app.add_url_rule('/api/v2/auth/login/', view_func=OrdersController.as_view('login_user'),
                         methods=['POST'], strict_slashes=False)
        app.add_url_rule('/api/v2/users/orders/', view_func=OrdersController.as_view('make_order'),
                         methods=['POST'], strict_slashes=False)
        app.add_url_rule('/api/v2/users/orders/', view_func=OrdersController.as_view('get_history'),
                         methods=['GET'], strict_slashes=False)
        app.add_url_rule('/api/v2/orders/', view_func=OrdersController.as_view('get_orders'),
                         methods=['GET'], strict_slashes=False)
        app.add_url_rule('/api/v2/orders/<int:order_id>/', view_func=OrdersController.as_view('get_single_order'),
                         methods=['GET'], strict_slashes=False)
        app.add_url_rule('/api/v2/orders/<int:order_id>/', view_func=OrdersController.as_view('update_order_status'),
                         methods=['PUT'], strict_slashes=False)
        app.add_url_rule('/api/v2/menu/', view_func=OrdersController.as_view('get_menu'),
                         methods=['GET'], strict_slashes=False)
        app.add_url_rule('/api/v2/menu/', view_func=OrdersController.as_view('add_meal'),
                         methods=['POST'], strict_slashes=False)

