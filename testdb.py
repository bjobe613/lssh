from lssh.models import *
import resetDB

prod = Product(name = "TEST", price=100, category_id = 1, condition_id = 1, payment_method_id = 1)

db.session.add(prod)
db.session.commit()

print(Category.query.get(1).products)
print(prod.category.name)