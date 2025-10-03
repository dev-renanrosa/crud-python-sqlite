import sqlite3

# Conexão com banco SQLite
conn = sqlite3.connect("cadastro.db")
cursor = conn.cursor()

# Criar tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT
)
""")

# Funções CRUD
def adicionar_usuario(nome, email):
    cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
    conn.commit()

def listar_usuarios():
    cursor.execute("SELECT * FROM usuarios")
    for usuario in cursor.fetchall():
        print(usuario)

# Testando
adicionar_usuario("Renan", "renan@email.com")
listar_usuarios()
