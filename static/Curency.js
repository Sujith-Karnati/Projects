function convertCurrency() {
    let amount = document.getElementById("amount").value;
    let fromCurrency = document.getElementById("from_currency").value;
    let toCurrency = document.getElementById("to_currency").value;

    if (amount === "" || isNaN(amount)) {
        alert("Please enter a valid amount");
        return;
    }

    fetch("/convert", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            from: fromCurrency,
            to: toCurrency,
            amount: amount
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById("result").innerHTML = "Invalid currency!";
        } else {
            document.getElementById("result").innerHTML = 
                `Converted Amount: ${data.converted} ${toCurrency}`;
        }
    })
    .catch(error => console.error("Error:", error));
}

/* Dark Mode Toggle */
document.getElementById("theme-toggle").addEventListener("change", function() {
    document.body.classList.toggle("dark-mode");
});
