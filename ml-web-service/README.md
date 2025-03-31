# Machine Learning Web Service

This project is a machine learning web service that serves predictions through a Flask API and a React frontend. The service is designed to be easily deployable on Render.

## Project Structure

```
ml-web-service
├── api
│   ├── app.py                # Main entry point for the API
│   ├── model
│   │   └── model.pkl         # Serialized machine learning model
│   ├── requirements.txt       # Python dependencies for the API
│   └── Dockerfile             # Dockerfile for building the API image
├── frontend
│   ├── public
│   │   └── index.html        # Main HTML file for the frontend
│   ├── src
│   │   ├── App.js            # Main component of the React application
│   │   └── components
│   │       └── ModelOutput.js # Component for displaying model output
│   ├── package.json           # npm configuration for the frontend
│   ├── webpack.config.js      # Webpack configuration for bundling the frontend
│   └── README.md              # Documentation for the frontend
├── README.md                  # Overview of the entire project
└── render.yaml                # Deployment configuration for Render
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd ml-web-service
   ```

2. **API Setup:**
   - Navigate to the `api` directory.
   - Install the required Python packages:
     ```
     pip install -r requirements.txt
     ```
   - Run the API:
     ```
     python app.py
     ```

3. **Frontend Setup:**
   - Navigate to the `frontend` directory.
   - Install the required npm packages:
     ```
     npm install
     ```
   - Start the frontend application:
     ```
     npm start
     ```

## Deployment

To deploy the application on Render, ensure that you have a Render account and follow these steps:

1. Create a new web service for the API using the `Dockerfile` in the `api` directory.
2. Create a new static site for the frontend using the `frontend` directory.
3. Configure the `render.yaml` file to specify the services and their build/start commands.

## Usage

Once the application is running, you can access the frontend at `http://localhost:3000` (or the URL provided by Render after deployment). Use the interface to input data and receive predictions from the machine learning model.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.