# Insightfy 🧠

**Insightfy** é uma API de análise de texto inteligente, construída com **FastAPI** e **OpenAI GPT**.  
Ela permite classificar, resumir e atribuir rótulos criativos a qualquer texto enviado, sendo útil para aplicações educacionais, criativas ou corporativas.

---

## 🔍 Funcionalidades

- **POST `/analyze`**  
  Analisa um texto e retorna:
  - ✅ Um **resumo** curto
  - 🧩 A **classificação do tipo de texto** (ex: técnico, poético)
  - 🏷️ Um **código ou label criativo**

- **GET `/history`**  
  Lista os textos analisados anteriormente e seus respectivos resultados.

- **Swagger UI `/docs`**  
  Interface interativa para testes rápidos da API.

---

## 🚀 Tecnologias Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [OpenAI GPT API](https://platform.openai.com/)
- [SQLite](https://www.sqlite.org/index.html)
- [Uvicorn](https://www.uvicorn.org/)
- [Render](https://render.com/)

---

## 🛠 Como Executar Localmente

```bash
# 1. Clone o repositório
git clone https://github.com/EricDias8/Insightfy3.git
cd Insightfy3

# 2. Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Configure o arquivo .env com sua chave da OpenAI
touch .env
```

### `.env` (exemplo)
```env
OPENAI_API_KEY=sk-xxxxxx
DATABASE_URL=sqlite:///./requests.db
```

```bash
# 5. Execute o servidor local
uvicorn main:app --reload
```

Acesse: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🌐 Deploy em Produção

A API está publicada gratuitamente no Render:

🔗 **[https://insightfy3-api.onrender.com/docs](https://insightfy3-api.onrender.com/docs)**

---

## ✅ Checklist de Boas Práticas

- [x] `.env` incluído no `.gitignore`
- [x] API documentada com Swagger
- [x] Chave secreta protegida no deploy
- [x] Banco leve e funcional (SQLite)
- [x] Estrutura modular em FastAPI

---

## 📄 Licença

Distribuído sob a licença MIT.

---

Desenvolvido com 💻 por [Eric Dias](https://github.com/EricDias8)
