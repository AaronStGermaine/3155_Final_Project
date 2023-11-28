from . import orders, promos, order_details, customers, ratings, recipes, resources, foods, payment_info


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(customers.router)
    app.include_router(ratings.router)
    app.include_router(recipes.router)
    app.include_router(resources.router)
    app.include_router(foods.router)
    app.include_router(promos.router)
    app.include_router(payment_info.router)