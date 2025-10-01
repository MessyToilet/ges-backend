from db.base import Base 
from db.session import engine


def init_db():
    print("[-] Initializing database...")
    Base.metadata.create_all(bind=engine)
    print("[+] Database initialized!")

def clear_db():
    print("[!] Clearing database...")
    Base.metadata.drop_all(bind=engine)
    print("[+] Database cleared.")
