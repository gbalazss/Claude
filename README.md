## UV Python Guide

`uv` is an extremely fast Python package installer and resolver, designed as a drop-in replacement for `pip` and `pip-tools`.

### 1. Installation
Install `uv` using the standalone installer:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Project Initialization
To start a new project, use `uv init`. This creates a `pyproject.toml` and a basic project structure:
```bash
uv init my-python-app
cd my-python-app
```

### 3. Managing Dependencies
Add packages to your project. This automatically updates your `pyproject.toml` and locks the dependencies:
```bash
uv add requests
```

### 4. Synchronizing the Environment
To ensure your local virtual environment (`.venv`) exactly matches the lockfile:
```bash
uv sync
```

### 5. Running Your Project
You can run Python scripts or project entry points within the managed environment without activating it manually:
```bash
uv run hello.py
```

---

## Step-by-Step User Guide for This Project

Follow these steps to get the project up and running on your local machine:

1.  **Install uv**: If you haven't already, install the `uv` CLI tool using the command in the Installation section above.
2.  **Clone the Repository**:
    ```bash
    git clone <repository-url>
    cd <project-folder>
    ```
3.  **Setup the Environment**: Run the sync command to create a virtual environment and install all necessary dependencies:
    ```bash
    uv sync
    ```
4.  **Activate the Environment (Optional)**: While `uv run` is preferred, you can manually activate the environment:
    ```bash
    source .venv/bin/activate  # On macOS/Linux
    .venv\Scripts\activate     # On Windows
    ```
5.  **Execute the Main Function**: Run the main entry point of the application:
    ```bash
    uv run python main.py
    ```
6.  **Adding New Tools**: If you need to add more libraries during development:
    ```bash
    uv add <package-name>
   