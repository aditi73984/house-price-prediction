async function predict() {
    const quality = document.getElementById("quality").value;
    const area = document.getElementById("area").value;
    const garage = document.getElementById("garage").value;
    const basement = document.getElementById("basement").value;
    const resultDiv = document.getElementById("result");

    if (!quality || !area || !garage || !basement) {
        resultDiv.style.color = "red";
        resultDiv.innerText = "⚠️ Please fill all fields";
        return;
    }

    resultDiv.style.color = "#333";
    resultDiv.innerText = "Predicting price...";

    try {
        const response = await fetch("http://127.0.0.1:8000/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                OverallQual: Number(quality),
                GrLivArea: Number(area),
                GarageCars: Number(garage),
                TotalBsmtSF: Number(basement)
            })
        });

        const data = await response.json();

        resultDiv.style.color = "#1b4332";
        resultDiv.innerText =
            `Estimated Price: ₹ ${data.predicted_price.toLocaleString()}`;

    } catch (error) {
        resultDiv.style.color = "red";
        resultDiv.innerText = "❌ Server not reachable";
        console.error(error);
    }
}
