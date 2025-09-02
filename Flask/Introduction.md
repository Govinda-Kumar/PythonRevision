# Flask Overview

Flask is a **lightweight and flexible web framework for Python**. It allows you to quickly build web applications while keeping things simple. Flask provides just enough features to get started, and you can add more functionality with extensions as needed.  

In short:  
> Flask lets you build web apps quickly, stay in control, and add features only when you need them.  

---

## Key Features

- **Lightweight:** Minimal core, easy to learn and start using.  
- **Flexible:** Use only the tools you need and add more via extensions.  
- **Extensible:** Customize your app exactly the way you want.  

---

## Why Flask is Simple and Developer-Friendly

- Start with a small app and scale up as your project grows.  
- Minimal setup required—no unnecessary boilerplate.  
- Lots of tutorials, documentation, and community support.  
- Doesn’t get in your way—easy to understand and use.  
- Perfect for developers who want full control without complexity.  

---

## Sample Code

Here’s a basic example to get started with Flask:  

```python
from flask import Flask

# Create a Flask app instance
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def hello_world():
    return "Hello World!"

# Run the app
if __name__ == "__main__":
    app.run()
