FROM python:3.9-slim

# Install dependencies
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY transformers_inference.py .

# Expose the application port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "transformers_inference:app", "--host", "0.0.0.0", "--port", "8000"]