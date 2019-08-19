$(document).ready(function() {
    function count_down(Inminutes) {
        var countdown = Inminutes * 60 * 1000;
        var timerId = setInterval(function() {
            countdown -= 1000;
            var min = Math.floor(countdown / (60 * 1000));
            var sec = Math.floor((countdown - (min * 60 * 1000)) / 1000);

            if (min < "10") { min = "0" + min; }
            if (sec < "10") { sec = "0" + sec; }

            if (countdown <= 0) {
                clearInterval(timerId);
                // var audio = new Audio('https://interactive-examples.mdn.mozilla.net/media/examples/t-rex-roar.mp3');
                var audio = new Audio('http://localhost:5000/static/media/service-bell_daniel_simion.mp3')
                audio.play();
                alert("End of pomodoro session")
                $('.minutes').html(min);
                $('.seconds').html(sec)
            } else {
                $('.minutes').html(min);
                $('.seconds').html(sec);
            }

        }, 1000);
    }

    function stop() {
        console.log("Stop button pressed...")
    }

    $("#startButton").click(function() {
        var Inminutes = $("#duration").val()
        console.log(Inminutes);
        count_down(Inminutes);
    });

    $("#stopButton").click(function() {
        stop();
    });
});