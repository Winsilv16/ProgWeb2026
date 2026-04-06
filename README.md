# 🛒 Projeto Django - Sistema de Loja

Este repositório contém um sistema web desenvolvido com **Django**, com funcionalidades básicas de uma loja virtual, incluindo cadastro de produtos, categorias e fabricantes.

---

## 🚀 Funcionalidades

* 📦 Cadastro de Produtos
* 🏭 Cadastro de Fabricantes
* 🗂️ Cadastro de Categorias
* 🔗 Relacionamento entre tabelas (ForeignKey)
* 🖼️ Upload de imagens para produtos
* 🔐 Painel administrativo (Django Admin)
* 🌐 Página inicial simples

---

## 🧱 Tecnologias utilizadas

* Python 3
* Django 4.2.7
* SQLite3
* Pillow (upload de imagens)

---

## ⚙️ Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

---

### 2. Criar e ativar o ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux / Codespaces
# venv\Scripts\activate  # Windows
```

---

### 3. Instalar dependências

```bash
pip install django==4.2.7
pip install pillow
```

---

### 4. Rodar migrações

```bash
python manage.py migrate
```

---

### 5. Criar superusuário

```bash
python manage.py createsuperuser
```

---

### 6. Executar o servidor

```bash
python manage.py runserver 0.0.0.0:8000
```

---

## 🌐 Acessos

* 🏠 Página inicial:
  `http://localhost:8000/`

* 🔐 Painel administrativo:
  `http://localhost:8000/admin/`

---

## 📁 Estrutura do projeto

```
lojaAdmin/
├── loja/
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   ├── urls.py
│
├── media/
├── manage.py
```

---

## 🧠 Aprendizados

Durante o desenvolvimento deste projeto foram praticados:

* Criação de projetos com Django
* Modelagem de banco de dados
* Uso de migrations
* Relacionamentos entre tabelas
* Uso do Django Admin
* Upload de arquivos/imagens
* Configuração de rotas (URLs)

---

## 📌 Observações

* O arquivo `.gitignore` foi configurado para evitar envio de arquivos desnecessários como:

  * `venv/`
  * `db.sqlite3`
  * `media/`

---

## 👨‍💻 Autor

Desenvolvido por **Winnicius da Silva Faustino de Alcântara**

---

## ⭐ Status do Projeto

✅ Finalizado (versão inicial)
🚧 Possíveis melhorias futuras:

* Interface frontend
* API REST
* Sistema de autenticação para usuários

---
