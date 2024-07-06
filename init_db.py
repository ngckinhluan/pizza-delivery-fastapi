from database import engine, Base

# Import your models here
from models import User, Order

# Create all tables in the database
Base.metadata.create_all(bind=engine)
