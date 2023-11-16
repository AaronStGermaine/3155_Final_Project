from . import orders, order_details, customers, ratings, recipes, resources, foods


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(customers)
    app.include_router(ratings)
    app.include_router(recipes)
    app.include_router(resources)
    app.include_router(sandwiches)
