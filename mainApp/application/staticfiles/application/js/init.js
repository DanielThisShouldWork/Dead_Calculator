//Hook up the tweet display

$(document).ready(function() {
                           
    $(".countdown").countdown({
                date: "24 October 2024 23:30:00",
                format: "on"
            },
            
            function() {
                // callback function
            });

}); 