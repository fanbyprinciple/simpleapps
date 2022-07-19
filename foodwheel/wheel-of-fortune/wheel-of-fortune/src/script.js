function main() {
    //== variabels ===================================
    var _wheel = document.querySelector("#wheel");
    var _arrow = document.querySelector("#arrow");
    var _jackpotDisp = document.querySelector("#jackpot");
    var _jackpot = 0;
    var _scoreDisp = document.querySelector("#score");
    var _score = 0;
    var _deg = 7.5;
    var _position = _deg%360;
    
    //== functions ===================================
    //random number function
     function random(min, max) {
        return Math.round(Math.random() * (max - min) + min);
    }
    
    //spin teh wheel
    _arrow.addEventListener("click", spin);
    function spin(evt){
        //remove click event
        _arrow.removeEventListener("click", spin);
        
        //aniamtion arrow
        _arrow.classList.add("arrowanimation");
        
        //new position wheel
        _deg = _deg + 180 + (15 * random(0,24));
        
        //give wheel position
        _wheel.style.transform = "rotate(" + _deg + "deg)";
        
        //chec position
        var _position = _deg%360;
        console.log(_position + " position");
        
        if(_position == 7.5){
           _score = _score + 800;
           _jackpot = _jackpot + 800;
           }
        if(_position == 22.5){
           _score = _score + 700;
           _jackpot = _jackpot + 700;
           }
        if(_position == 37.5){
           _score = _score + 500;
           _jackpot = _jackpot + 500;
           }
        if(_position == 52.5){
           _score = _score + 200;
           _jackpot = _jackpot + 200;
           }
        if(_position == 67.5){
           _score = _score + 100;
           _jackpot = _jackpot + 100;
           }
        if(_position == 82.5){
           _score = _score + 200;
           _jackpot = _jackpot + 200;
           }
        if(_position == 97.5){
           _score = _score + 300;
           _jackpot = _jackpot + 300;
           }
        if(_position == 112.5){
           _score = _score + 400;
           _jackpot = _jackpot + 400;
           }
        if(_position == 127.5){
           _score = _score + 100;
           _jackpot = _jackpot + 100;
           }
        if(_position == 142.5){
           _score = _score + 600;
           _jackpot = _jackpot + 600;
           }
        if(_position == 157.5){
           _score = _score + 700;
           _jackpot = _jackpot + 700;
           }
        if(_position == 172.5){
           _score = _score + 800;
           _jackpot = _jackpot + 800;
           }
        if(_position == 187.5){
            //bank
           _jackpot = _jackpot + _score;
            _score = 0;
           }
        if(_position == 202.5){
           _score = _score + 800;
           _jackpot = _jackpot + 800;
           }
        if(_position == 217.5){
           _score = _score + 700;
           _jackpot = _jackpot + 700;
           }
        if(_position == 232.5){
           _score = _score + 600;
           _jackpot = _jackpot + 600;
           }
        if(_position == 247.5){
           _score = _score + 500;
           _jackpot = _jackpot + 500;
           }
        if(_position == 262.5){
           _score = _score + 400;
           _jackpot = _jackpot + 400;
           }
        if(_position == 277.5){
           _score = _score + 300;
           _jackpot = _jackpot + 300;
           }
        if(_position == 292.5){
           _score = _score + 200;
           _jackpot = _jackpot + 200;
           }
        if(_position == 307.5){
           _score = _score + 100;
           _jackpot = _jackpot + 100;
           }
        if(_position == 322.5){
            //bank
           _jackpot = _jackpot + _score;
            _score = 0;
           }
        if(_position == 337.5){
            //jackpot
           _score = _score + _jackpot;
           _jackpot = 0;
            _jackpotSound.play();
           }
        if(_position == 352.5){
            //bank
           _jackpot = _jackpot + _score;
            _score = 0;
           }
        
        //after spin
        setTimeout(function() {
            //make clickebel again
            _arrow.addEventListener("click", spin);
            //remove arrow animation
            _arrow.classList.remove("arrowanimation");
            //update score and jackpot
            // _scoreDisp.innerHTML = "You definitely are drolling for " ;
            _jackpotDisp.innerHTML = "Nah! you need mummy's home cooked food."
        }, 5000);
    }
}


window.onload = function() {
    main();
}