# Pagan_Divination
Flask & Bootstrap Web App projekt

## Overview
Pohanská webová aplikace - Objev svého ochránce a patrona mezi vikingskými, slovanskými a keltskými bohy. Dynamické a plně responzivní stránky. 
Aplikaci lze on-line spustit zde:
https://pagan-divination.onrender.com/

### Použité technologie
- Flask pro backend
- Bootstrap pro frontend
- SQLAlchemy pro správu databáze SQLite
- HTML5 & CSS3 pro šablony stránek
- Python pro backend logiku

## Licence
Tento projekt je licencován pod licencí MIT. Použité knihovny mají své vlastní licence:

- Flask: BSD License
- SQLAlchemy: MIT License
- Bootstrap: MIT License
- SQLite: Public Domain
- Python: Python Software Foundation License

## Files

- `main.py`: main app
- `init_database.py`: creates a database with tables in "/instance" and populates it with gods
- `gods.py`: class that creates gods
  
- `index.html`: landing page, where you can choose the divination type
- `divination.html`: individual divination page, generated dynamically
- `contact.html`: contact information
- `base.html`: base page to be extended by children templates
- `navbar.html`: navbar element to be included in base.html
- `footer.html`: footer element to be included in base.html

## Setup
### Prerequisites:
Python 3.x
Virtual environment (optional but recommended)
Flask, SQLAlchemy, Bootstrap, and other packages listed in requirements.txt

### Usage - Step-by-Step:
1. Clone the repository 
- First, clone the repository:
bash: git clone https://github.com/your-username/pagan-divination.git
bash: cd pagan-divination

2. Create a virtual environment and install dependencies
- It’s recommended to create a virtual environment and install dependencies from the requirements.txt file:
bash: python -m venv venv
bash: source venv/bin/activate  # On Windows: venv\Scripts\activate
bash: pip install -r requirements.txt

3. Run the application
- Start the application:
bash: python main.py
The app will be accessible at http://127.0.0.1:5000/, using Flask’s default configuration.

4. Configuration and logging
- The application uses specific configuration and logging settings.
- You can modify configuration parameters in the config/app_config.py file to suit your needs.
- Logs are saved based on the settings defined in config/logging_config.py.

### Web Pages View

- https://pagan-divination.onrender.com/

## Project Highlights

- **Idea**: Showcase of passion & knowledge turned into a functional and enjoyable web app
- **Layout**: Demonstrates the use of friendly and engaging UX
- **Bootstrap use**: Shows the ability in using Bootstrap, HTML & CSS
- **Responsive web design**: Shows proficiency in creating a modern web that works on a variety of different size displays
- **Database**: Use of SQLAlchemy to work with SQLite database
- **API**: Use of Rest API endpoint to share data
