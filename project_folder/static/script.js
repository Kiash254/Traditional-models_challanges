function submitQuiz() {
    const form = document.getElementById('predictionForm');
    const formData = new FormData(form);
    const responses = {};

    formData.forEach((value, key) => {
        responses[key] = value;
    });

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(responses)
    }).then(response => {
        if (response.ok) {
            response.json().then(data => {
                const prediction = data.prediction;
                console.log('Prediction:', prediction);
                alert('Prediction: ' + prediction);
            });
        } else {
            alert('Error submitting survey.');
        }
    }).catch(error => {
        console.error('Error:', error);
        alert('Error submitting survey.');
    });
}