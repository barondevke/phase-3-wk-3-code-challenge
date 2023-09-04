from models import Restaurant, Customer, Review
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///maindb.db')

# Create instances of Restaurant and Customer
res1 = Restaurant(restaurant_name='Res1', price=80)
res2 = Restaurant(restaurant_name='Res2', price=90)

cus1 = Customer(first_name='Jo', last_name='Mama')

Session = sessionmaker(bind=engine)
session = Session()

# Add the Restaurant and Customer instances to the session to persist them
session.add(res1)
session.add(res2)
session.add(cus1)
session.commit()  # Commit to get the IDs generated for res1, res2, and cus1

# Now you can access the IDs
print(f"Restaurant ID: {res1.restaurant_id}")
print(f"Customer ID: {cus1.customer_id}")

# Create a Review instance using the obtained IDs
rev1 = Review(rating=10, customer_id=cus1.customer_id, restaurant_id=res1.restaurant_id)

# Add and commit the Review instance
session.add(rev1)
session.commit()

# Now the Review instance is associated with the specific Customer and Restaurant.
