from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL_FONTE = "postgresql://usuario:senha@localhost/fonte"
DATABASE_URL_ALVO = "postgresql://usuario:senha@localhost/alvo"

engine_fonte = create_engine(DATABASE_URL_FONTE)
SessionLocalFonte = sessionmaker(autocommit=False, autoflush=False, bind=engine_fonte)
BaseFonte = declarative_base()

engine_alvo = create_engine(DATABASE_URL_ALVO)
SessionLocalAlvo = sessionmaker(autocommit=False, autoflush=False, bind=engine_alvo)
BaseAlvo = declarative_base()

def testar_conexao():
    try:
        with engine_fonte.connect() as conn:
            conn.execute("SELECT 1")
        print("Conexão com o banco de dados Fonte bem-sucedida!")
        
        with engine_alvo.connect() as conn:
            conn.execute("SELECT 1")
        print("Conexão com o banco de dados Alvo bem-sucedida!")
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")

if __name__ == "__main__":
    testar_conexao()
