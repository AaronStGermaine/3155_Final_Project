from . import orders, order_details, recipes, foods, resources, customers, ratings, promos

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    recipes.Base.metadata.create_all(engine)
    foods.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    customers.Base.metadata.create_all(engine)
    ratings.Base.metadata.create_all(engine)
    promos.Base.metadata.create_all(engine)