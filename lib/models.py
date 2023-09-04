from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.schema import Table

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'
    restaurant_id = Column(Integer, primary_key=True, autoincrement=True)
    restaurant_name = Column(String)
    price = Column(Integer)

    reviews = relationship('Review', backref='restaurant')

    def __repr__(self):
        return f"{self.restaurant_name} {self.price}"
    
    def customers(self):
        return [review.customer for review in self.reviews]

class Customer(Base):
    __tablename__ = 'customers'
    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)

    reviews = relationship('Review', backref='customer')

    def __repr__(self):
        return f"{self.customer_id} {self.first_name} {self.last_name}"

class Review(Base):
    __tablename__ = 'reviews'
    review_id = Column(Integer, primary_key=True, autoincrement=True)
    rating = Column(Integer, nullable=False)

    customer = relationship('Customer', back_populates='reviews')
    restaurant = relationship('Restaurant', back_populates='reviews')

    customer_id = Column(Integer, ForeignKey('customers.customer_id'))
    restaurant_id = Column(Integer, ForeignKey('restaurants.restaurant_id'))

    def __repr__(self):
        return f"{self.review_id} {self.rating}"

customer_restaurant_association = Table(
    'customer_restaurant',
    Base.metadata,
    Column('customer_id', Integer, ForeignKey('customers.customer_id'), primary_key=True),
    Column('restaurant_id', Integer, ForeignKey('restaurants.restaurant_id'), primary_key=True),
)
