**Documentação: Gerador de PDF do Currículo**

Esta ferramenta automatiza a geração de um PDF a partir de uma página web usando Pyppeteer e Chromium. Abaixo você encontrará instruções para instalar dependências, configurar e executar o aplicativo.
---

## 1. Pré‑requisitos

Antes de começar, certifique‑se de ter:

* **Python 3.7+** instalado no sistema.
* **Chromium** (pacote Debian/Ubuntu: `chromium` ou `chromium-browser`).
* Uma **virtualenv** (recomendado) ou ambiente global configurado.

---

## 2. Instalação

1. Clone ou acesse a pasta do projeto:

   ```bash
   git clone https://github.com/luisfelipefr/curriculo
   cd curriculo
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Instale as dependências do Python:

   ```bash
   pip install pyppeteer
   ```

---
