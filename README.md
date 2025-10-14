# System Monitoring with AI Agents

A multi-agent system for monitoring system resources, detecting anomalies, and generating AI-powered reports.

## 🚀 Features

- Real-time system monitoring (CPU, Memory, Disk, Network)
- AI-powered anomaly detection
- Automated report generation with natural language summaries
- Web-based dashboard for visualization
- Configurable alerting system

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/multi_agent_system_monitoring.git
   cd multi_agent_system_monitoring
   ```

2. **Create and activate a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   - Copy `.env.example` to `.env`
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```

## ⚙️ Configuration

Edit the `.env` file to configure:
- `OPENAI_API_KEY`: Your OpenAI API key for AI-powered reports
- (Add other configuration options here as needed)

## 🚀 Usage

### Command Line Interface
```bash
python main.py
```

### Web Dashboard
Start the web interface:
```bash
python web/app.py
```
Then open `http://localhost:5000` in your browser.

## 📊 System Requirements

- Python 3.8+
- OpenAI API key
- (List any other system requirements here)

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
