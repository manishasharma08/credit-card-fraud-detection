function testFraud() {
    alert("Button working"); // TEST

    let sample = new Array(29).fill(1);
    sample[28] = 900;

    document.getElementById("inputData").value = sample.join(",");
}

function predict() {
    alert("Predict clicked"); // TEST

    fetch('/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ data: new Array(29).fill(1) })
    })
    .then(res => res.json())
    .then(data => alert(JSON.stringify(data)))
    .catch(err => alert(err));
}