# Snow-It-All

My Zackathon 2025 project: a chatbot that transforms negative energy into motivation.

## [Presentation](https://docs.google.com/presentation/d/1keW7NyoTF-HZtHlXJzlhkUlBpfOyG7t9466k-EC8AHA/edit?usp=sharing)

## Environment Setup

### Mac-Specific Setup Instructions

1. Pre-requisites:

- Git
- Homebrew
- pip
- Python

2. Clone the repository.

```shell
git clone https://github.com/Ho1yShif/Snow-It-All.git
```

3. Set up virtual environment.

```shell
python3 -m venv path/to/venv
```

4. Start virtual environment.

```shell
source path/to/venv/bin/activate
```

5. From the repository directory, install requirements.

```shell
pip install -r requirements
```

### Windows-Specific Setup Instructions

1. Pre-requisites:

- Git
- Pip
- Python

2. Clone the repository.

```shell
git clone https://github.com/Ho1yShif/Snow-It-All.git
```

3. Set up virtual environment.

```shell
python -m venv path\to\venv
```

4. Start virtual environment.

```shell
path\to\venv\Scripts\activate
```

5. From the repository directory, install requirements.

```shell
pip install -r requirements.txt
```

### Additional System-Agnostic Setup Instructions

1. Sign up and create an API key for [Together AI](https://api.together.ai/signin).
2. Create a `.env` file in the main project directory that contains your `TOGETHER_API_KEY` and `SYSTEM_PROMPT` to instruct the AI agent.

```text
TOGETHER_API_KEY="123"
SYSTEM_PROMPT="Just return 'Hello World'"
```

3. Run `python app.py` and let the snowstorm begin!
