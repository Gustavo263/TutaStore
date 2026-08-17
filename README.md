# 🛒 TuttaStore

E-commerce full stack desenvolvido em **Django**, simulando uma loja virtual de livros — do catálogo de produtos ao checkout com pagamento integrado.

Projeto pessoal criado para aplicar na prática conceitos de desenvolvimento back-end, modelagem de dados relacionais, autenticação customizada e integração com APIs de pagamento.

---

## 📋 Sobre o projeto

O TuttaStore é uma aplicação de e-commerce que cobre o fluxo completo de uma loja online:

- Catálogo de produtos organizado por categorias hierárquicas
- Carrinho de compras persistente por sessão
- Fluxo de checkout com seleção de endereço, opções de entrega e pagamento
- Sistema de contas de usuário com autenticação customizada
- Histórico de pedidos e lista de desejos
- Painel administrativo customizado para gestão de produtos e pedidos

---

## ✨ Funcionalidades

### Loja
- Listagem de produtos com filtro por categoria (categorias em árvore, via MPTT)
- Página de detalhe do produto com imagens, especificações e preço com desconto
- Sistema de lista de desejos (wishlist) por usuário

### Carrinho
- Adição, atualização e remoção de itens via requisições assíncronas (AJAX/jQuery)
- Cálculo automático de subtotal, frete e total

### Checkout
- Seleção de opções de entrega
- Seleção de endereço de entrega cadastrado
- Integração com **PayPal** (PayPal Checkout SDK) e **Stripe** para processamento de pagamento
- Confirmação e registro automático do pedido após pagamento aprovado

### Contas de usuário
- Modelo de usuário customizado (`Customer`), autenticado por e-mail
- Cadastro com ativação de conta via link enviado por e-mail
- Recuperação e redefinição de senha
- Gerenciamento de múltiplos endereços de entrega, com endereço padrão
- Edição de dados pessoais e exclusão de conta

### Pedidos
- Histórico de pedidos do usuário
- Registro de itens, valores e status de pagamento de cada pedido

### Administração
- Painel administrativo customizado com **Jazzmin**
- Gestão de produtos, categorias, tipos de produto, especificações e imagens
- Gestão de opções de entrega e formas de pagamento

---

## 🛠️ Tecnologias utilizadas

**Back-end**
- Python
- Django 4.0
- Django ORM
- django-mptt (categorias em árvore)
- django-jazzmin (painel admin)
- django-debug-toolbar (ambiente de desenvolvimento)

**Pagamento**
- PayPal Checkout SDK
- Stripe

**Front-end**
- HTML5 / CSS3
- Bootstrap
- JavaScript / jQuery

**Banco de dados**
- SQLite (desenvolvimento)

**Outros**
- Git / GitHub
- Testes automatizados com Django `TestCase`

---

## 📁 Estrutura do projeto

```
core/                 # Configurações do projeto (settings, urls, wsgi/asgi)
store/                # Catálogo de produtos e categorias
basket/                # Carrinho de compras
checkout/              # Fluxo de checkout, entrega e pagamento
account/               # Autenticação, cadastro e endereços de usuário
orders/                # Pedidos e itens de pedido
book/                  # Listagem de livros
templates/             # Templates HTML organizados por app
static/                # Arquivos estáticos (CSS, JS)
```

---

## 🚀 Como executar o projeto localmente

### Pré-requisitos
- Python 3.10+
- pip

### Passo a passo

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/tuttastore.git
cd tuttastore

# Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

# Instale as dependências
pip install -r requirements.txt

# Aplique as migrações
python manage.py migrate

# Crie um super usuário (para acessar o admin)
python manage.py createsuperuser

# Rode o servidor de desenvolvimento
python manage.py runserver
```

Acesse `http://127.0.0.1:8000/` no navegador.
O painel administrativo fica disponível em `http://127.0.0.1:8000/admin/`.

### Variáveis de ambiente

Configure suas próprias chaves de API do Stripe e PayPal antes de testar o fluxo de pagamento (não utilize as chaves de exemplo do repositório em produção).

---

## ✅ Testes

O projeto conta com testes automatizados para as principais views e modelos das apps `store` e `basket`.

```bash
python manage.py test
```

---

## 🗺️ Possíveis melhorias futuras

- Migrar variáveis sensíveis (chaves de API, secret key) para variáveis de ambiente
- Adicionar paginação e busca de produtos
- Adicionar avaliações e comentários de produtos
- Implementar testes para as apps `checkout`, `account` e `orders`
- Deploy em ambiente de produção (Heroku, Railway ou similar)

---

## 👤 Autor

**Gustavo Lemes**
Estudante de Engenharia de Software | Python & Django

- LinkedIn: [linkedin.com/in/lemesgustavo](https://www.linkedin.com/in/lemesgustavo)
- E-mail: gustavo.2006lemes@gmail.com

---

## 📄 Licença

Este projeto foi desenvolvido para fins de estudo e portfólio pessoal.
