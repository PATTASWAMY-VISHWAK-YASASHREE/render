import React, { useState } from 'react';
import ModelOutput from './components/ModelOutput';

function App() {
    const [inputData, setInputData] = useState('');
    const [prediction, setPrediction] = useState(null);

    const handleInputChange = (event) => {
        setInputData(event.target.value);
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        const response = await fetch('/api/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ data: inputData }),
        });
        const result = await response.json();
        setPrediction(result.prediction);
    };

    return (
        <div>
            <h1>Machine Learning Model Prediction</h1>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    value={inputData}
                    onChange={handleInputChange}
                    placeholder="Enter input data"
                />
                <button type="submit">Predict</button>
            </form>
            {prediction && <ModelOutput prediction={prediction} />}
        </div>
    );
}

export default App;