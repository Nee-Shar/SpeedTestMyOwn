from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL
from models.speedtest import Base

# Create DB engine
engine=create_engine(DATABASE_URL)

#Create Seesion
SessionLocal=sessionmaker(autocommit=False, autoflush=False , bind=engine)


#Dependacny to get DB Session
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()    

def create_tables():
    Base.metadata.create_all(bind=engine)
    print("Tables Created Successfully")
    
if __name__ == "__main__":
    try:
        with engine.connect() as conn:
            print("✅ Database connected successfully!")
    except Exception as e:
        print(f"❌ Database connection failed: {e}")   

    create_tables()    