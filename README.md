# Snow-It-All

My Zackathon 2025 project: a chatbot that transforms negative energy into motivation.

## [Presentation](https://docs.google.com/presentation/d/1keW7NyoTF-HZtHlXJzlhkUlBpfOyG7t9466k-EC8AHA/edit?usp=sharing)

## Environment Setup

### Mac-Specific Instructions

1. Pre-requisites: `Brew` and `pip`
2. Clone the repository
3. Set up virtual environment

```shell
python3 -m venv path/to/venv
```

4. Start virtual environment

```shell
source path/to/venv/bin/activate
```

5. From the repository, install requirements

```shell
pip install requirements
```

### System-Agnostic Instructions

1. Sign up and create an API key for [Together AI](https://api.together.ai/signin).
2. Create a `.env` file that contains your `TOGETHER_API_KEY` and `SYSTEM_PROMPT` to instruct the AI agent.
3. Run `python app.py` and let the snowstorm begin!
