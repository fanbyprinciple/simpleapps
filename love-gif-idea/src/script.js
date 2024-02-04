let scale = 1; // Initial scale for the "Yes" button

  document.getElementById('noButton').addEventListener('click', function() {
    scale += 0.1; // Increase scale by 10%
    document.getElementById('yesButton').style.transform = 'scale(' + scale + ')';
    
    console.log(scale)
    
    if (scale > 3) {
      document.getElementById('noButton').innerText = "seriously?"
    }
    
    if (scale > 5) {
      document.getElementById('noButton').innerText = "Click yes already please"
    }
    
    if (scale > 10) {
      document.getElementById('noButton').innerText = "No more games!"
    }
    
    
const sadTexts = [
    "Devu you forgot our walks by hauz khas?",
    "I wil not accept no for an answer.",
    "Aww... why not devu????",
    "Are you really really really sure?",
    "That hurts. but say, is that green button expanding?",
    "Yhi dosti, yhi pyaar?",
    "Ill complain to asha amma!",
    "Mein nhi khel rha",
    "chummade kallikaade",
    "Issok, I have enough chechi maar",
    "It too late for bakchodi now, you have no choice.",
    "Long distance valentine ban jao!",
    "Mukka marunga",
    "I still love you Devu",
    "Hai mera ek tarfa pyaar",
    "Bhagwaan thodi akal dede isse",
    "Pyaar kam h toh aise hi toh bologe"
  ];

  // Randomly select a sad text
  const randomIndex = Math.floor(Math.random() * sadTexts.length);
  const selectedText = sadTexts[randomIndex];

  // Display the selected sad text
  document.getElementById('q').innerText = selectedText;
    document.getElementById('panda').src="https://media.tenor.com/0Xr-5-SbieQAAAAi/bubududu-panda.gif"
  });



document.getElementById('yesButton').addEventListener('click', function() {
 
 document.getElementById('q').innerText = "Yay! I love you Devu!"; 
  document.getElementById('panda').src="https://media.tenor.com/tRF59TL7c28AAAAM/bear.gif"
  
document.getElementById('yesButton').remove()
document.getElementById('noButton').remove()
  

});

