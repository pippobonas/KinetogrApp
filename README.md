# KinetogrApp

A simple application to quickly consult which platforms a film is available on. KinetogrApp is built using React for the frontend and Flask for the backend.

## Feature
- View the list of movies
- Search of movies

## Installation 
1. Clone the repository
    
2. Install the dependencies
   - For React:
   ```bash
   cd React/kinetograpp-react
   npm install
   ```
   - For Flask:
   ```bash
   cd Flask
   pip install -r requirements.txt
   ```
   - - [Optional] Create python environment
    ```bash
    mkdir .venv
    python -m venv .venv
    ```
3. Start the backend server
   - -[Optional] Create Migration with flask-migrate
   ```bash
    flask db migrate -m "initial migration"
   ```
   - run
   ```bash
   flask run
   ```
4. Start the frontend server
   - run
   ```bash
   cd React/kinetograpp-react
   npm start
   ```
