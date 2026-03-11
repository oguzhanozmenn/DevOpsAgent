class CICDAgent:
    def generate_github_actions(self, analysis_result: dict):
        project_type = analysis_result.get("project_type", "Unknown")

        if project_type == "Node.js":
            return self._node_actions()
        elif project_type == "Python":
            return self._python_actions()
        else:
            return "# CI/CD support for this project type is coming soon."

    def _node_actions(self):
        return """name: Node.js CI

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3
    - name: Use Node.js 18
      uses: actions/setup-node@v3
      with:
        node-version: 18
        cache: 'npm'
    - run: npm install
    - run: npm test --if-present
"""

    def _python_actions(self):
        return """name: Python CI

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python 3.11
      uses: actions/setup-python@v4
      with:
        python-version: "3.11"
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
    - name: Run tests
      run: |
        # pytest (varsa çalıştırır)
        python -m pytest
"""