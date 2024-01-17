from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv
import os

load_dotenv()

url = os.getenv("DB_URI")

engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()
class DatabaseConnector:
    def __init__(self) -> None:
        self.connection = None


    def connect(self):
        self.connection = engine.connect()

    def close(self):
        self.connection.close()


    def save(self, model):
        session.add(model)
        session.commit()  

    def update(self, model, filter, update, commit=True):
        query = self.query(model).filter(filter)
        affected_rows = query.update(update)    
        if commit:
            session.commit()  
        return query.first(), affected_rows
    

    def delete(self, model, filter, commit=True):
        query = self.query(model).filter(filter)
        data = query.first()
        affected_rows = query.delete()
        if commit:
            session.commit()  
        return data, affected_rows

    def query(self, model):  
        return session.query(model)
    
    def get(self, model, pk):
        return session.get(model, pk)
    

db = DatabaseConnector()
db.connect()