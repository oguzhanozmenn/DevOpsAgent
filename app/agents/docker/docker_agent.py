class DockerAgent:
    def generate_dockerfile(self, analysis_result: dict):
        project_type = analysis_result.get("project_type", "Unknown")

        if project_type == "Node.js":
            return self._node_dockerfile()
        elif project_type == "Python":
            return self._python_dockerfile()
        else:
            return "# Project type not supported for Dockerfile generation yet."

    def _node_dockerfile(self):
        return """# Base image
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy package files and install dependencies
COPY package*.json ./
RUN npm install --production

# Copy the rest of the application
COPY . .

# Expose the application port
EXPOSE 3000

# Start the application
CMD ["npm", "start"]
"""

    def _python_dockerfile(self):
        return """# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Start the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
"""