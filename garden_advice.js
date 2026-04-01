// Function to determine gardening advice based on season and plant type
function getGardeningAdvice(season, plantType) {
    let advice = "";

    // Determine advice based on the season
    if (season.toLowerCase() === "summer") {
        advice += "Water your plants regularly and provide some shade.\n";
    } else if (season.toLowerCase() === "winter") {
        advice += "Protect your plants from frost with covers.\n";
    } else {
        advice += "No specific advice for this season.\n";
    }

    // Determine advice based on the plant type
    if (plantType.toLowerCase() === "flower") {
        advice += "Use fertilizer to encourage blooms.";
    } else if (plantType.toLowerCase() === "vegetable") {
        advice += "Keep an eye out for pests!";
    } else {
        advice += "No advice for this type of plant.";
    }

    return advice;
}

// Get user input using prompt()
let currentSeason = prompt("Enter the current season (e.g., summer, winter):");
let currentPlant = prompt("Enter the plant type (e.g., flower, vegetable):");

// Generate and log the advice to the console
const finalAdvice = getGardeningAdvice(currentSeason, currentPlant);
console.log(finalAdvice);
