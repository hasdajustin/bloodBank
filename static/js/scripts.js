const quotes = [
    "A single drop of blood can save a life.",
    "Donate blood, save a soul.",
    "You are somebody’s type donate blood."
];

function changeQuote() {
    const randomIndex = Math.floor(Math.random() * quotes.length);
    document.getElementById("quote").innerText = quotes[randomIndex];
}
changeQuote();
setInterval(changeQuote, 2000);