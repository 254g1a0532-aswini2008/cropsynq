function getRecommendation() {

    let commodity = document.getElementById("commodity").value;
    let storage = document.getElementById("storage").value;
    let days = document.getElementById("days").value;

    if (days === "") {

        document.getElementById("result").innerHTML =
            "<p>Please enter the storage duration.</p>";

        return;
    }


    let packaging = "";
    let reason = "";


    if (commodity === "Tomato") {

        packaging = "Perforated Food-Grade Film";

        reason =
            "Allows controlled gas exchange and helps reduce moisture accumulation.";
    }

    else if (commodity === "Potato") {

        packaging = "Breathable Mesh Packaging";

        reason =
            "Provides ventilation and helps reduce moisture-related spoilage.";
    }

    else if (commodity === "Onion") {

        packaging = "Breathable Mesh Bag";

        reason =
            "Allows air circulation and helps prevent moisture buildup.";
    }

    else if (commodity === "Apple") {

        packaging = "Controlled-Atmosphere Packaging";

        reason =
            "Helps control oxygen and carbon dioxide levels and maintain freshness.";
    }

    else if (commodity === "Banana") {

        packaging = "Ventilated Food-Grade Packaging";

        reason =
            "Provides ventilation and helps maintain fruit quality.";
    }

    else {

        packaging = "Breathable Food-Grade Packaging";

        reason =
            "Helps maintain suitable airflow and reduce moisture accumulation.";
    }


    document.getElementById("result").innerHTML = `

        <div class="result-box">

            <h2>📦 Recommendation Result</h2>

            <p>
                <b>Commodity:</b> ${commodity}
            </p>

            <p>
                <b>Storage Condition:</b> ${storage}
            </p>

            <p>
                <b>Storage Duration:</b> ${days} days
            </p>

            <hr>

            <h3>🌱 Suggested Packaging</h3>

            <div class="packaging">
                ${packaging}
            </div>

            <h3>💡 Why this packaging?</h3>

            <p>
                ${reason}
            </p>

            <div class="result-benefits">

                <p>✅ Helps maintain freshness</p>

                <p>✅ Helps reduce spoilage</p>

                <p>✅ Supports better storage</p>

                <p>👨‍🌾 Useful for farmers and sellers</p>

            </div>

        </div>
    `;
}