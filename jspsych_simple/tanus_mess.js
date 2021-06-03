/* create timeline */

    
var timeline = [];

/* preload images */
var preload = {
  type: 'preload',
  images: ['img/s001.jpg', 'img/s003.jpg', 'img/s005.jpg', 'img/s008.jpg', 'img/s009.jpg',
           'img/s012.jpg', 'img/s013.jpg', 'img/s014.jpg', 'img/s015.jpg', 'img/s016.jpg',
           'img/s018.jpg', 'img/s021.jpg', 'img/s023.jpg', 'img/s026.jpg', 'img/s029.jpg',
           
           'img/f002.jpg', 'img/f003.jpg', 'img/f005.jpg', 'img/f006.jpg', 'img/f011.jpg', 
           'img/f012.jpg', 'img/f015.jpg', 'img/f016.jpg', 'img/f020.jpg', 'img/f022.jpg',
           'img/f023.jpg', 'img/f024.jpg', 'img/f025.jpg', 'img/f029.jpg', 'img/f030.jpg',
           
           
           'img/c002.jpg', 'img/c004.jpg', 'img/c006.jpg', 'img/c008.jpg', 'img/c009.jpg',
           'img/c011.jpg', 'img/c012.jpg', 'img/c013.jpg', 'img/c014.jpg', 'img/c015.jpg',
           'img/c016.jpg', 'img/c018.jpg', 'img/c020.jpg', 'img/c022.jpg', 'img/c023.jpg',
           'img/c025.jpg', 'img/c027.jpg',
           
           'img/h001.jpg', 'img/h004.jpg', 'img/h005.jpg', 'img/h008.jpg', 'img/h009.jpg',
           'img/h011.jpg', 'img/h012.jpg', 'img/h013.jpg', 'img/h015.jpg', 'img/h016.jpg',
           'img/h017.jpg', 'img/h018.jpg', 'img/h020.jpg', 'img/h022.jpg', 'img/h023.jpg',
           'img/h026.jpg', 'img/h030.jpg', 'img/h031.jpg', 'img/h032.jpg', 'img/h033.jpg',
           'img/h034.jpg', 'img/h037.jpg', 'img/h038.jpg',
           
           
           'img/k001.jpg', 'img/k004.jpg', 'img/k005.jpg', 'img/k006.jpg', 'img/k009.jpg',
           'img/k012.jpg', 'img/k014.jpg', 'img/k015.jpg', 'img/k018.jpg', 'img/k021.jpg',
           'img/k022.jpg', 'img/k023.jpg', 'img/k024.jpg', 'img/k025.jpg', 'img/k026.jpg',
           'img/k028.jpg', 'img/k029.jpg', 'img/k031.jpg', 'img/k032.jpg', 'img/k036.jpg',
           'img/k037.jpg', 'img/k039.jpg', 'img/k040.jpg', 'img/k044.jpg', 'img/k045.jpg',
           
           'img/t004.jpg', 'img/t005.jpg', 'img/t006.jpg', 'img/t007.jpg', 'img/t012.jpg',

  ]
}
timeline.push(preload);

/* define welcome message trial */
var welcome = {
  type: "html-keyboard-response",
  stimulus: "Welcome to the Experiment. Press any key to begin."
};
timeline.push(welcome);

var subject_name = null

var s_info = {
        type: 'survey-text',
        questions: [{prompt: 'Please enter your name', name: 'Name', required :1},
        {prompt: 'Age', name: 'Age', required :1},
        {prompt: 'Gender', name: 'Gender', required :1},
        {prompt: 'Phone number', name: 'Phone number (optional)', required :0}],
        on_finish: function() {
          //Important for for getting subject's name that's how the script knows what's the name of the participant, in order to save it.
          subject_name = jsPsych.data.get(s_info).values();
          //if in case there's an error regarding subject's name, change the 3 below to 2
          // subject_name = subject_name[3].response.Name;
    }
}
    
timeline.push(s_info)

/* define instructions trial */
var instructions = {
  type: "html-keyboard-response",
  stimulus: `
    <p>In this experiment,items would appear in the center 
    of the screen.</p><p>If the item is <strong>Househould objects</strong>, 
    press the <strong>SPACE key</strong> on the keyboard as fast and accurately as you can.</p>
    <p>If the item is <strong>Food (edible)</strong> or <strong>Stationary objects</strong>, do not press anything.</p>
   
    <p>Press any key to begin.</p>
  `,
  // post_trial_gap: 2000
};
timeline.push(instructions);

// let deg_resize = { 
//   type: 'virtual-chinrest', blindspot_reps: 5, resize_units: 'deg', pixels_per_unit: 224.7, item_path: 'jspsych-6.3.0/examples/img/card.png', }; 
// timeline.push(deg_resize);

// let deg_resize = {
//   type: "virtual-chinrest",
//   blindspot_reps: 1,
//   resize_units: "deg",
//   pixels_per_unit: 50,
//   viewing_distance_report: "none",
// };

// timeline.push(deg_resize)

var full = {
  type: 'fullscreen',
  fullscreen_mode: true
};
timeline.push(full);

var practice_stimuli = [
  { stimulus: "img/c002.jpg", correct_response: null},
  { stimulus: "img/c004.jpg", correct_response: null},
  { stimulus: "img/c006.jpg", correct_response: null},
  { stimulus: "img/c008.jpg", correct_response: null},
  { stimulus: "img/c009.jpg", correct_response: null},
  { stimulus: "img/f002.jpg", correct_response: ' '},
  { stimulus: "img/f003.jpg", correct_response: ' '},
  { stimulus: "img/f005.jpg", correct_response: ' '},
  { stimulus: "img/f006.jpg", correct_response: ' '},
  { stimulus: "img/f011.jpg", correct_response: ' '},
]

/* test trials */
var test_stimuli = [

  { stimulus: "img/c002.jpg", correct_response: null},
  { stimulus: "img/c004.jpg", correct_response: null},
  { stimulus: "img/c006.jpg", correct_response: null},
  { stimulus: "img/c008.jpg", correct_response: null},
  { stimulus: "img/c009.jpg", correct_response: null},
  { stimulus: "img/c011.jpg", correct_response: null},
  { stimulus: "img/c012.jpg", correct_response: null},
  { stimulus: "img/c013.jpg", correct_response: null},
  { stimulus: "img/c014.jpg", correct_response: null},
  { stimulus: "img/c015.jpg", correct_response: null},
  
  { stimulus: "img/c016.jpg", correct_response: null},
  { stimulus: "img/c018.jpg", correct_response: null},
  { stimulus: "img/c020.jpg", correct_response: null},
  { stimulus: "img/c022.jpg", correct_response: null},
  { stimulus: "img/c023.jpg", correct_response: null},
  { stimulus: "img/c025.jpg", correct_response: null},
  { stimulus: "img/c027.jpg", correct_response: null},
  
  { stimulus: "img/h001.jpg", correct_response: null},
  { stimulus: "img/h004.jpg", correct_response: null},
  { stimulus: "img/h005.jpg", correct_response: null},
  { stimulus: "img/h008.jpg", correct_response: null},
  { stimulus: "img/h009.jpg", correct_response: null},
  { stimulus: "img/h011.jpg", correct_response: null},
  { stimulus: "img/h012.jpg", correct_response: null},
  { stimulus: "img/h013.jpg", correct_response: null},
  { stimulus: "img/h015.jpg", correct_response: null},
  { stimulus: "img/h016.jpg", correct_response: null},
  
  { stimulus: "img/h017.jpg", correct_response: null},
  { stimulus: "img/h018.jpg", correct_response: null},
  { stimulus: "img/h020.jpg", correct_response: null},
  { stimulus: "img/h022.jpg", correct_response: null},
  { stimulus: "img/h023.jpg", correct_response: null},
  { stimulus: "img/h026.jpg", correct_response: null},
  { stimulus: "img/h030.jpg", correct_response: null},
  { stimulus: "img/h031.jpg", correct_response: null},
  { stimulus: "img/h032.jpg", correct_response: null},
  { stimulus: "img/h033.jpg", correct_response: null},
  
  { stimulus: "img/h034.jpg", correct_response: null},
  { stimulus: "img/h037.jpg", correct_response: null},
  { stimulus: "img/h038.jpg", correct_response: null},
  
  { stimulus: "img/k001.jpg", correct_response: null},
  { stimulus: "img/k004.jpg", correct_response: null},
  { stimulus: "img/k005.jpg", correct_response: null},
  { stimulus: "img/k006.jpg", correct_response: null},
  { stimulus: "img/k009.jpg", correct_response: null},
  { stimulus: "img/k012.jpg", correct_response: null},
  { stimulus: "img/k014.jpg", correct_response: null},
  { stimulus: "img/k015.jpg", correct_response: null},
  { stimulus: "img/k018.jpg", correct_response: null},
  { stimulus: "img/k021.jpg", correct_response: null},
  
  { stimulus: "img/k022.jpg", correct_response: null},
  { stimulus: "img/k023.jpg", correct_response: null},
  { stimulus: "img/k024.jpg", correct_response: null},
  { stimulus: "img/k025.jpg", correct_response: null},
  { stimulus: "img/k026.jpg", correct_response: null},
  { stimulus: "img/k028.jpg", correct_response: null},
  { stimulus: "img/k029.jpg", correct_response: null},
  { stimulus: "img/k031.jpg", correct_response: null},
  { stimulus: "img/k032.jpg", correct_response: null},
  { stimulus: "img/k036.jpg", correct_response: null},
  
  { stimulus: "img/k037.jpg", correct_response: null},
  { stimulus: "img/k039.jpg", correct_response: null},
  { stimulus: "img/k040.jpg", correct_response: null},
  { stimulus: "img/k044.jpg", correct_response: null},
  { stimulus: "img/k045.jpg", correct_response: null},
  
  { stimulus: "img/t004.jpg", correct_response: null},
  { stimulus: "img/t005.jpg", correct_response: null},
  { stimulus: "img/t006.jpg", correct_response: null},
  { stimulus: "img/t007.jpg", correct_response: null},
  { stimulus: "img/t012.jpg", correct_response: null},
  
  
  { stimulus: "img/s001.jpg", correct_response: null},
  { stimulus: "img/s003.jpg", correct_response: null},
  { stimulus: "img/s005.jpg", correct_response: null},
  { stimulus: "img/s008.jpg", correct_response: null},
  { stimulus: "img/s009.jpg", correct_response: null},
  { stimulus: "img/s012.jpg", correct_response: null},
  { stimulus: "img/s013.jpg", correct_response: null},
  { stimulus: "img/s014.jpg", correct_response: null},
  { stimulus: "img/s015.jpg", correct_response: null},
  { stimulus: "img/s016.jpg", correct_response: null},
  
  { stimulus: "img/s018.jpg", correct_response: null},
  { stimulus: "img/s021.jpg", correct_response: null},
  { stimulus: "img/s023.jpg", correct_response: null},
  { stimulus: "img/s026.jpg", correct_response: null},
  { stimulus: "img/s029.jpg", correct_response: null},
  
  { stimulus: "img/f002.jpg", correct_response: ' '},
  { stimulus: "img/f003.jpg", correct_response: ' '},
  { stimulus: "img/f005.jpg", correct_response: ' '},
  { stimulus: "img/f006.jpg", correct_response: ' '},
  { stimulus: "img/f011.jpg", correct_response: ' '},
  { stimulus: "img/f012.jpg", correct_response: ' '},
  { stimulus: "img/f015.jpg", correct_response: ' '},
  { stimulus: "img/f016.jpg", correct_response: ' '},
  { stimulus: "img/f020.jpg", correct_response: ' '},
  { stimulus: "img/f022.jpg", correct_response: ' '},
  
  { stimulus: "img/f023.jpg", correct_response: ' '},
  { stimulus: "img/f024.jpg", correct_response: ' '},
  { stimulus: "img/f025.jpg", correct_response: ' '},
  { stimulus: "img/f029.jpg", correct_response: ' '},
  { stimulus: "img/f030.jpg", correct_response: ' '},


];


//instructions for practice
var instructions_practice = {
type: "html-keyboard-response",
stimulus: `
<p> Lets get a bit of practice in. </p>

<p> This is practice, but read this carefully. </p>
<p>If the item is <strong>Househould objects</strong>, 
press the <strong>SPACE key</strong> on the keyboard as fast and accurately as you can.</p>
<p>If the item is <strong>Food (edible)</strong> or <strong>Stationary objects</strong>, <STRONG>DON'T</STRONG> press any key.</p>

<p>Press any key to begin.</p>
`,
// post_trial_gap: 2000
};
// timeline.push(instructions_practice)


// Practice trial
var practice1 = { 
type: "image-keyboard-response",
stimulus: jsPsych.timelineVariable('stimulus'),
choices: [' '],
stimulus_duration: 750,
trial_duration: 500,
response_ends_trial:false,
timing_post_trial: 500,
post_trial_gap:0,
timing_response: 1250,//total trial duration needs to changed

data: {
task: 'response',
correct_response: jsPsych.timelineVariable('correct_response')
},
on_finish: function(data){
data.correct = jsPsych.pluginAPI.compareKeys(data.response, data.correct_response); 

console.log("response: " , data.response," correct: ", data.correct_response)
if (data.correct){
  trl_correct = 1
} else {
  trl_correct = 0
}

}
}

//Feedback Trial
var feedback_trial = {
type: 'html-keyboard-response',
stimulus: function(){
  if (trl_correct == 1){
    html = '<div style="font-size: 30px;color: green;">Correct!</div>';
  } else{
    html = '<div style="font-size: 30px;color: red;">Wrong!</div>';
  }
  return html
},
trial_duration: 500,
};

var fixation = {
type: 'html-keyboard-response',
stimulus: '<div style="font-size:60px;">+</div>',
choices: null,
trial_duration: 500,
// trial_duration: function(){
//   return jsPsych.randomization.sampleWithoutReplacement([500], 1)[0];
// },
data: {
task: 'fixation'
}
}

var practice_procedure = {
timeline: [fixation, practice1, feedback_trial],
timeline_variables: practice_stimuli,
repetitions: 1,
randomize_order: true,
}

timeline.push(practice_procedure)

var instructions_main= {
type: "html-keyboard-response",
stimulus: `
<p> Now the main experiment starts!</p>

<p> There will be no feedback. </p>
<p> Remember </p>
<p>If the item is <strong>Househould objects</strong>, 
press the <strong>SPACE key</strong> on the keyboard as fast and accurately as you can.</p>
<p>If the item is <strong>Food (edible)</strong> or <strong>Stationary objects</strong>, do not press anything.</p>

<p>Press any key to begin.</p>
`,
// post_trial_gap: 2000
};
timeline.push(instructions_main)

var test1 = { 
type: "image-keyboard-response",
stimulus: jsPsych.timelineVariable('stimulus'),
choices: [' '],
stimulus_duration: 750,
trial_duration: 500,
response_ends_trial:false,
timing_post_trial: 0,
post_trial_gap:500,
timing_response: 1250,//total trial duration needs to changed
data: {
task: 'response',
correct_response: jsPsych.timelineVariable('correct_response')
},
on_finish: function(data){
data.correct = jsPsych.pluginAPI.compareKeys(data.response, data.correct_response); 
}
}

var break_block = {
type: "html-keyboard-response",
data: {
trial_id: "moving to next phase"
},
stimulus: "<p>Take a break.</p>"+"<P>For Household products, press <STRONG>SPACE key </STRONG></p>"+"<p> For edible Food Items or Stationery, <STRONG> DON'T PRESS </STRONG>any key",
timing_post_trail: 0
}

var test2 = { 
type: "image-keyboard-response",
stimulus: jsPsych.timelineVariable('stimulus'),
choices: [' '],
stimulus_duration: 750,
trial_duration: 500,
response_ends_trial:false,
timing_post_trial: 0,
post_trial_gap:500, 
timing_response:1250,//total trial duration needs to changed
data: {
task: 'response',
correct_response: jsPsych.timelineVariable('correct_response')
},
on_finish: function(data){
data.correct = jsPsych.pluginAPI.compareKeys(data.response, data.correct_response);
}
}

var test3 = { 
type: "image-keyboard-response",
stimulus: jsPsych.timelineVariable('stimulus'),
choices: [' '],
stimulus_duration: 750,
trial_duration: 500,
response_ends_trial:false,
timing_post_trial: 0,
post_trial_gap:500, 
timing_response:1250,//total trial duration needs to changed
data: {
task: 'response',
correct_response: jsPsych.timelineVariable('correct_response')
},
on_finish: function(data){
data.correct = jsPsych.pluginAPI.compareKeys(data.response, data.correct_response);
}
}

var test_procedure = {
timeline: [fixation, test1],
timeline_variables: test_stimuli,
repetitions: 3,
randomize_order: true,
}


timeline.push(test_procedure);

timeline.push(break_block)

var test_procedure_2 = {
timeline: [fixation, test2],
timeline_variables: test_stimuli,
repetitions: 3,
randomize_order: true,
}

timeline.push(test_procedure_2)

timeline.push(break_block)

var test_procedure_3 = {
timeline: [fixation, test3],
timeline_variables: test_stimuli,
repetitions: 3,
randomize_order: true,
}

timeline.push(test_procedure_3)



var debrief_block = {
type: "html-keyboard-response",
stimulus: function() {

// var trials = jsPsych.data.get().filter({task: 'response'});
// var correct_trials = trials.filter({correct: true});
// var accuracy = Math.round(correct_trials.count() / trials.count() * 100);
// var rt = Math.round(correct_trials.select('rt').mean());

return `Thank you for participating in this Experiment. `
// return `<p>You responded correctly on ${accuracy}% of the trials.</p>
//   <p>Your average response time was ${rt}ms.</p>
//   <p>Press any key to complete the experiment. Thank you!</p>`;

}
};
timeline.push(debrief_block);

function saveData(name, data){
var xhr = new XMLHttpRequest();
xhr.open('POST', 'write_data.php'); // 'write_data.php' is the path to the php file described above.
xhr.setRequestHeader('Content-Type', 'application/json');
xhr.send(JSON.stringify({filename: subject_name, filedata: data}));
}

/* start the experiment */
jsPsych.init({
timeline: timeline,
fullscreen: true,
on_finish: function() {
data = jsPsych.data.get().localSave('csv','mydata_N.csv');
saveData("AX-CPT_", data);
document.writeln("<div style=\"text-align: center; font-size: 24px;\">The experiment has ended. Thanks for participating!"+ "</p>Now an excel sheet will get generated on your computer, Please download that file and mail me at <strong>tanu@cbcs.ac.in</strong>" +"</p>You may close the window now.</div>");
}
});