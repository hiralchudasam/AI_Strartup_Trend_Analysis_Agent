# AI Startup Trend Analysis Agent

## Overview

The AI Startup Trend Analysis Agent is a Streamlit-based web application that leverages the Grok AI model (via the free Groq API) to provide real-time insights into emerging trends in the AI startup ecosystem. Powered by the Agno agent framework, it integrates free tools such as DuckDuckGo for web searches and Newspaper for article extraction and summarization. This tool is designed for entrepreneurs, analysts, and tech enthusiasts to query and receive actionable intelligence on key players, funding rounds, market opportunities, and challenges in AI, technology, and innovation sectors—all without relying on paid services.

## Features

- **Interactive Query Interface**: Enter natural language queries (e.g., "Latest AI startup funding trends") to get AI-generated summaries and insights.
- **Free Resource Focus**: Utilizes only free-tier APIs and tools for accessibility and cost-efficiency.
- **Real-Time Analysis**: Searches recent news and extracts content from articles to deliver up-to-date trend reports in markdown format.
- **Customizable Agent**: Pre-configured with instructions for focused, insightful responses on startup trends.
- **User-Friendly UI**: Simple Streamlit dashboard for seamless interaction.

## Technologies & Dependencies

- **Frontend**: Streamlit (for the web interface)
- **AI Model**: Grok (Llama 3.3 70B Versatile) via Groq API
- **Agent Framework**: Agno (for agent creation and tool integration)
- **Tools**:
  - DuckDuckGoTools: Web search capabilities
  - NewspaperTools: Article parsing and content extraction
- **Environment**: Python 3.8+, dotenv for API key management

See [requirements.txt](requirements.txt) for full dependencies.

## Prerequisites

- Python 3.8 or higher
- A free Grok API key from xAI (obtain at [console.groq.com](https://console.groq.com) or x.ai)
- Git (for cloning the repository)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/hiralchudasam/AI_Strartup_Trend_Analysis_Agent.git
   cd AI_Strartup_Trend_Analysis_Agent
   ```

2. Create a `.env` file in the root directory and add your API key:
   ```
   GROK_API_KEY=your_grok_api_key_here
   ```
   *Note: Never commit `.env` to version control (it's in `.gitignore`)*

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit application:
   ```
   streamlit run startup_trends_agent.py
   ```

2. Open your web browser to `http://localhost:8501`.

3. In the app:
   - Enter a query in the text input field (default: "What are the latest trends in AI startups?").
   - Click **Analyze Trends** to generate insights.
   - View the markdown-formatted response with trend summaries, opportunities, and challenges.

### Example Queries
- "What are the top AI startups to watch in 2024?"
- "Recent funding in generative AI companies"
- "Challenges facing AI startups in healthcare"

## Project Structure

- `startup_trends_agent.py`: Core application file containing Streamlit UI, agent setup, and query handling.
- `requirements.txt`: List of Python dependencies.
- `.env`: Environment variables (API key; not tracked).
- `.gitignore`: Excludes sensitive files.
- `README.md`: This file.

## Contributing

Contributions are welcome! To get started:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

Please ensure code adheres to PEP 8 standards and includes tests where applicable. For major changes, open an issue first to discuss.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. (Create one if needed.)

## Support & Issues

If you encounter issues or have suggestions:
- Check the [Issues](https://github.com/hiralchudasam/AI_Strartup_Trend_Analysis_Agent/issues) tab on GitHub.
- For API-related problems, verify your Grok key and rate limits.

---

*Built with ❤️ for the AI community. Track startup trends effortlessly!*
