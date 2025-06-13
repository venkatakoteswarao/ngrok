# 🚀 Flask Ngrok Tunnel Manager

This is a simple yet powerful **Flask-based web application** that allows users to **create, view, and stop public ngrok tunnels** through a browser interface. It's ideal for developers who want to **instantly expose local applications** (e.g., Flask, Streamlit, or any local server) to the internet without using the terminal.

---

## 📝 Description

Ngrok is a tool that creates secure tunnels to your local server. This Flask app provides a **web-based frontend** that:
- Accepts a local URL input
- Creates a public `https://...ngrok.io` tunnel using **Pyngrok**
- Displays the public URL
- Allows stopping the active tunnel with a single click

No need to manually use the ngrok CLI. It’s all automated through the Flask backend.

---

## 🌟 Features

- 🔗 Deploy a public ngrok tunnel for any local URL
- 🛑 Stop active tunnels from the UI
- 📡 Automatically shows the active public link
- ✅ One-click tunnel control
- ⚙️ Clean Flask + Pyngrok integration
- 🖼️ HTML interface powered by Jinja2

---

## 🧰 Tech Stack

- 🐍 Python 3
- 🔥 Flask
- 🌐 Pyngrok
- 🖼 HTML (Jinja2 templates)

---

