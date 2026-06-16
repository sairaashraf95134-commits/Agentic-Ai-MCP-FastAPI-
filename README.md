# 🚀 Agentic AI System using MCP + LangGraph + FastAPI

## 🧠 Overview

This project demonstrates a **real-world Agentic AI system** that goes beyond traditional chatbots.

Instead of only generating text responses, this system can:

> 🧠 Reason → 🧰 Choose tools → ⚙️ Execute actions → 📡 Return real-world results

It integrates **MCP (Model Context Protocol)** for tool standardization, **LangGraph** for intelligent agent orchestration, and **FastAPI** for deployment.


## 🎯 Why This Project?

Traditional AI models:

> ❌ Only respond with text

This system:

> ✅ Understands user intent
> ✅ Selects the right tool automatically
> ✅ Executes real-world tasks (email, search, etc.)
> ✅ Works like an autonomous assistant

---

## ⚙️ Key Features

### 🧠 Intelligent Agent

* Dynamically decides which tool to use
* Multi-step reasoning with LangGraph

### 🌐 Web Search Capability

* Real-time Google search using SERPAPI
* Returns structured results

### 📧 Email Automation

* Sends emails using Yagmail SMTP
* Fully automated response system

### 🔗 MCP Tool Integration

* Standardized tool calling architecture
* Easily extendable system

### ⚡ FastAPI Backend

* REST API endpoint for AI agent
* Production-ready structure

---

## 🏗 System Architecture

```
User Request
      ↓
FastAPI (main.py)
      ↓
Assistant Layer (assistant.py)
      ↓
LangGraph Agent (agent.py)
      ↓
MCP Tool Server (mcp_tool_server.py)
      ↓
External Tools
   ├── 🌐 SERPAPI (Search)
   ├── 📧 Yagmail (Email)
   └── ⚙️ Math

## 🧰 Tech Stack

* 🐍 Python 3.10+
* 🧠 LangGraph (Agent orchestration)
* 🔗 MCP (Model Context Protocol)
* ⚡ FastAPI (Backend API)
* 📧 Yagmail (Email automation)
* 🌐 SERPAPI (Search API)
* 🔐 Python-dotenv (Environment management)




## 💡 What I Learned

This project helped me understand:

* How **real AI agents** are structured in production
* How tools are integrated into LLM-based systems
* How MCP standardizes tool communication
* How LangGraph manages decision-making workflows
* How backend APIs expose AI capabilities


## 🚀 Future Improvements

* 🧠 Add long-term memory to the agent
* 💬 Add chat history persistence
* 📱 Integrate WhatsApp / Telegram bots
* 📄 Add PDF / file reading tools
* ☁️ Deploy on cloud (Render / AWS)
* 🖥 Build frontend UI chatbot


## 📌 Why This Project Matters

This project represents a shift from:

> 💬 “Chatbots that talk”
> to
> 🤖 “AI Agents that act”

It is a step toward **autonomous AI systems capable of real-world actions.**


## 🏷️ Tags

`#AI` `#AgenticAI` `#LangGraph` `#MCP` `#FastAPI` `#Python` `#Automation` `#MachineLearning`

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to fork and improve it!

