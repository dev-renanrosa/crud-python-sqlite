# 📌 CRUD em Python com SQLite  

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Concluído-success)
![Contribuições](https://img.shields.io/badge/Contribuições-Bem--vindas-orange)

Este é um projeto simples de **CRUD (Create, Read, Update, Delete)** utilizando **Python** e **SQLite**, feito como parte de estudos em programação e banco de dados.

---

## ⚡ Funcionalidades
- ✅ Criar usuários  
- ✅ Listar usuários  
- ⚙️ Atualizar usuários  
- 🗑️ Excluir usuários  

---

## 🛠 Tecnologias utilizadas
- **Python 3**  
- **SQLite**  
- **VS Code**  

---

## ▶️ Como executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/dev-renanrosa/crud-python-sqlite.git
   cd crud-python-sqlite

## ▶️ Como executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/dev-renanrosa/crud-python-sqlite.git
   cd crud-python-sqlite

2. Certifique-se de ter o Python 3 instalado.
Para verificar:
python --version

3. Ative o ambiente virtual:
venv\Scripts\activate

4. Linux/Mac:
source venv/bin/activate

5.Execute o projeto:
python crud.py

---

## 📖 Exemplo de Uso

```python
from crud import adicionar_usuario, listar_usuarios

# Adicionar usuário
adicionar_usuario("Renan", "renan@email.com")

# Listar usuários
listar_usuarios()


