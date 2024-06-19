FROM python:3.9  # or any other Python base image

# Install Tkinter and other necessary packages
RUN apt-get update && apt-get install -y \
    python3-tk \
    x11-apps

# Copy your application code
COPY . /app
WORKDIR /app

# Install any Python dependencies
RUN pip install -r requirements.txt

CMD ["python", "your_script.py"]
