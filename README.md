# 🛡️ Cyber-AI Intelligence Agent

An autonomous research agent designed to track and report on emerging cyber threats using the **ReAct (Reason + Act)** framework.

## 🚀 Features
- **Real-time Research**: Uses DuckDuckGo to find breaches from the last 30 days.
- **Structured Reporting**: Automatically maps findings to MITRE ATT&CK and STRIDE frameworks.
- **Cloud-Native**: Configured for Ollama Cloud API with secure header authentication.
- **Parsing Resilience**: Built-in handling for LLM formatting errors.

## 🛠️ Installation
1. Clone the repo: `git clone https://github.com/yourusername/cyber-ai-agent.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Ensure you have an **Ollama Cloud API Key**.

## 🖥️ Usage
Run the main script:
```bash
python security_bot.py
