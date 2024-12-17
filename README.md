# GROCERY-FASTAPI-REACRJS

This project is a YouTube video downloader built with **FastAPI** for the backend and **ReactJS** for the frontend. Follow the steps below to set up and run the project.

## Project Repository

[GROCERY-FASTAPI-REACRJS](https://github.com/iamabhaypatel28/grocery-react.git)

---

## Steps to Set Up and Run the Project

### 1. Clone the Repository

First, clone the project repository to your local machine:

```bash
git clone https://github.com/iamabhaypatel28/grocery-react.git
```

---

### 2. Set Up the Backend (FastAPI)

1. Navigate to the backend folder:

   ```bash
   cd backend
   ```

2. Create a Python virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the FastAPI server:

   ```bash
   uvicorn main:app --reload
   ```

   The backend server will start running on **[http://127.0.0.1:8000](http://127.0.0.1:8000)**.
   Show all api in **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

---

### 3. Set Up the Frontend (ReactJS)

1. Navigate to the frontend folder:

   ```bash
   cd frontend
   ```

2. Install React dependencies:

   ```bash
   npm install
   ```

3. Start the React development server:

   ```bash
   npm start
   ```

   The frontend will start running on **[http://localhost:3000](http://localhost:3000)**.

---

### 4. Create a `.env` File for React

In the `frontend` folder, create a `.env` file with the following content:

```env
REACT_APP_API_URL=http://localhost:8000/
```

This environment variable sets the API URL for the ReactJS project.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.