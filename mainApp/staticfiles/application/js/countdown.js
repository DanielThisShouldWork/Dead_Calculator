function startCountdown(targetDate) {
    function updateCountdown() {
        const now = new Date().getTime();
        const countdownDate = new Date(targetDate).getTime();
        console.log("Countdown Date: ", countdownDate);  // Debugging

        if (isNaN(countdownDate)) {
            console.error("Invalid countdown date");
            clearInterval(interval);
            return;
        }

        const distance = countdownDate - now;
        
        if (distance < 0) {
            clearInterval(interval);
            document.getElementById("countdown").innerHTML = "Tempo scaduto!";
            return;
        }

        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        document.getElementById("days").innerText = days;
        document.getElementById("hours").innerText = hours;
        document.getElementById("minutes").innerText = minutes;
        document.getElementById("seconds").innerText = seconds; 
    }

    const interval = setInterval(updateCountdown, 1000);
}
