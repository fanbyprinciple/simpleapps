function setup() {
    createCanvas(255, 255);
    background(220);

    loadJSON('/airplane', gotAirplane)
  }

let x, y;
let airplane
let strokeIndex = 0
let index = 0

function gotAirplane(data){
    console.log("here")
    //console.log(data)
    let airplane = data.drawing
    //console.log(drawing)

    // for(let path of drawing){
    //     noFill()
    //     stroke(0)
    //     strokeWeight(3)
    //     beginShape()
    //     for (let i=0; i< path[0].length; ++i){
    //         let x = path[0][i]
    //         let y = path[1][i]
    //         vertex(x,y)            
    //     }
    //     endShape()
    // }
}
  
  function draw() {
    if (airplane) {
        x = airplane[strokeIndex][0][index]
        y = airplane[strokeIndex][1][index]
        stroke (0)
        strokeWeight(3)
        point(x,y)

        index++

        if(index >= airplane[strokeIndex][0].length) {
            strokeIndex ++
            index = 0

        }

    }

  }