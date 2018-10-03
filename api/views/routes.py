"""
Routes module to handle request urls
"""
from api.controllers.login_controllers import LoginControl
from api.controllers.menu_controllers import MenusController
from api.controllers.orders_controllers import OrdersController
from api.controllers.signup_controllers import SignupControl


class Urls:
    """
        Class to generate the urls
    """

    @staticmethod
    def generate(app):
        """
        Generate urls
        :param app:
        :return:
        """
        app.add_url_rule('/api/v2/auth/signup/', view_func=SignupControl.as_view('register_user'),
                         methods=['POST'], strict_slashes=False)
        app.add_url_rule('/api/v2/auth/login/', view_func=LoginControl.as_view('login_user'),
                         methods=['POST'], strict_slashes=False)
        app.add_url_rule('/api/v2/users/orders/', view_func=OrdersController.as_view('make_order'),
                         methods=['POST'], strict_slashes=False)
        app.add_url_rule('/api/v2/users/orders/', view_func=LoginControl.as_view('order_history'),
                         methods=['GET'], strict_slashes=False)
        app.add_url_rule('/api/v2/orders/', view_func=OrdersController.as_view('get_orders'),
                         methods=['GET'], strict_slashes=False)
        app.add_url_rule('/api/v2/orders/<int:order_id>/', view_func=OrdersController.as_view('get_single_order'),
                         methods=['GET'], strict_slashes=False)
        app.add_url_rule('/api/v2/orders/<int:order_id>/', view_func=OrdersController.as_view('update_order_status'),
                         methods=['PUT'], strict_slashes=False)
        app.add_url_rule('/api/v2/menu/', view_func=MenusController.as_view('get_menu'),
                         methods=['GET'], strict_slashes=False)
        app.add_url_rule('/api/v2/menu/', view_func=MenusController.as_view('add_food_item'),
                         methods=['POST'], strict_slashes=False)

