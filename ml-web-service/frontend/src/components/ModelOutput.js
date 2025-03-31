import React from 'react';

const ModelOutput = ({ prediction }) => {
    return (
        <div>
            <h2>Model Prediction</h2>
            {prediction ? (
                <p>{`The predicted output is: ${prediction}`}</p>
            ) : (
                <p>No prediction available.</p>
            )}
        </div>
    );
};

export default ModelOutput;