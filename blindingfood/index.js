function getRandomColor() {
				
    var letters = "0123456789ABCDEF".split('');
    var color = "#";
    for (var i = 0; i < 6; i++) {
        color += letters[Math.round(Math.random() * 15)];
    } //ends for loop 
    return color; 


} // ends getRandomColor Function


var clickedTime; var createdTime; var reactionTime; 

function makeBox() {
        var time=Math.random();
        time=time*3000;
    
    setTimeout(function() {
    
        if (Math.random()>0.5) {
        
            document.getElementById("box").style.borderRadius="100px";
            
            } else {
            
                document.getElementById("box").style.borderRadius="0";
            }
            
        var top= Math.random();
            top= top*300;
        var left= Math.random();
            left= left*500; 
            
        document.getElementById("box").style.top = top + "px";
        document.getElementById("box").style.left = left + "px"; 
    
        document.getElementById("box").style.backgroundColor=getRandomColor();
    
        document.getElementById("box").style.display="block";
        
        select_images = ["burger.png", "kitty.png", "pizza.png"]
        document.getElementById("boximage").src= select_images[Math.floor(Math.random() * select_images.length)]

        createdTime=Date.now();
        
    }, time); 

}

document.getElementById("box").onclick=function() {

    clickedTime=Date.now();
    
    reactionTime=(clickedTime-createdTime)/1000;
    
    document.getElementById("printReactionTime").innerHTML="Your Reaction Time is: " + reactionTime + "seconds";
    
    this.style.display="none";
    
    makeBox();
    
    
}

makeBox(); 





