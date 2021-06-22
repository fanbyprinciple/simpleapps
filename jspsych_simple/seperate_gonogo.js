var timeline = [];

    /* preload images */
    var preload = {
      type: 'preload',
      images: [ 
        
               'img/ff001.jpg', 'img/ff002.jpg', 'img/ff003.jpg', 'img/ff005.jpg', 'img/ff006.jpg',
               'img/ff011.jpg', 'img/ff008.jpg', 'img/ff009.jpg', 'img/ff012.jpg', 'img/ff014.jpg',
               'img/ff015.jpg', 'img/ff016.jpg', 'img/ff017.jpg', 'img/ff019.jpg', 'img/ff020.jpg', 
               'img/ff022.jpg', 'img/ff023.jpg', 'img/ff024.jpg', 'img/ff029.jpg', 'img/ff030.jpg',
      
               'img/ss001.jpg', 'img/ss003.jpg', 'img/ss005.jpg', 'img/ss006.jpg', 'img/ss008.jpg', 
               'img/ss009.jpg', 'img/ss011.jpg', 'img/ss012.jpg', 'img/ss013.jpg', 'img/ss014.jpg', 
               'img/ss015.jpg', 'img/ss016.jpg', 'img/ss018.jpg', 'img/ss020.jpg', 'img/ss021.jpg', 
               'img/ss023.jpg', 'img/ss026.jpg', 'img/ss027.jpg', 'img/ss028.jpg', 'img/ss032.jpg',
               
               'img/sc002.jpg', 'img/sc003.jpg', 'img/sc004.jpg', 'img/sc008.jpg', 'img/fc009.jpg',
               'img/fc011.jpg', 'img/fc012.jpg', 'img/fc013.jpg', 'img/sc014.jpg', 'img/sc015.jpg',
               'img/sc017.jpg', 'img/fc018.jpg', 'img/fc019.jpg', 'img/sc020.jpg', 'img/fc022.jpg', 
               'img/fc023.jpg', 'img/fc025.jpg', 'img/sc003.jpg', 'img/fc027.jpg',
               
               'img/sh001.jpg', 'img/fh003.jpg', 'img/sh004.jpg', 'img/sh005.jpg', 'img/sh006.jpg', 
               'img/fh008.jpg', 'img/sh009.jpg', 'img/sh011.jpg', 'img/fh012.jpg', 'img/sh013.jpg',
               'img/sh015.jpg', 'img/fh017.jpg', 'img/fh020.jpg', 'img/fh021.jpg', 'img/fh022.jpg', 
               'img/fh023.jpg', 'img/fh025.jpg', 'img/fh026.jpg', 'img/fh028.jpg', 'img/sh030.jpg',
               'img/sh031.jpg', 'img/fh032.jpg', 'img/sh033.jpg', 'img/sh034.jpg', 'img/sh035.jpg', 
               'img/fh037.jpg', 'img/fh038.jpg',
               
               'img/fk001.jpg', 'img/fk002.jpg', 'img/fk008.jpg', 'img/fk010.jpg', 'img/fk013.jpg',
               'img/fk024.jpg', 'img/fk014.jpg', 'img/fk017.jpg', 'img/fk018.jpg', 'img/fk022.jpg',
               'img/fk026.jpg', 'img/fk027.jpg', 'img/fk033.jpg', 'img/fk035.jpg', 'img/fk037.jpg',               
               'img/fk038.jpg', 'img/fk040.jpg', 'img/fk041.jpg', 'img/fk042.jpg',
               
               'img/sk004.jpg', 'img/sk005.jpg', 'img/sk006.jpg', 'img/sk009.jpg', 'img/sk012.jpg',
               'img/sk015.jpg', 'img/sk016.jpg', 'img/sk020.jpg', 'img/sk021.jpg', 'img/sk023.jpg',
               'img/sk025.jpg', 'img/sk028.jpg', 'img/sk029.jpg', 'img/sk031.jpg', 'img/sk032.jpg', 
               'img/sk034.jpg', 'img/sk036.jpg', 'img/sk039.jpg', 'img/sk043.jpg', 'img/sk044.jpg', 
               'img/sk045.jpg',
               
               
               'img/ft002.jpg', 'img/ft004.jpg', 'img/ft006.jpg', 'img/ft007.jpg', 'img/st009.jpg',
               'img/st010.jpg', 'img/st011.jpg', 'img/st012.jpg',
               
               
               
      ]
    }
    timeline.push(preload);
    
    /* define welcome message trial */
    var welcome = {
      type: "html-keyboard-response",
      stimulus: "Welcome to the Experiment. Press any key to begin."
    };
    timeline.push(welcome);
    
    
    /* define instructions trial */
    
    // why do we have this here?
    var introduction = {
      type: "html-keyboard-response",
      stimulus: `
        <p>In this task, a fixation (+) will appear on the screen, you have to keep your gaze on the cross throughtout the experiment, which will be followed by various images.</p><p>Please keep the laptop screen <strong>45-55 cms</strong> away from your eyes.</p>
       
        <p>Press any key to continue. </p>
      `,
      // post_trial_gap: 2000
    };
    timeline.push(introduction);
    
    var subject_name = null
    
    var s_info = {
            type: 'survey-text',
            questions: [{prompt: 'Please enter your name', name: 'Name', required :0},
            {prompt: 'Age', name: 'Age', required :0},
            {prompt: 'Gender', name: 'Gender', required :0},
            {prompt: 'Phone number(optional)', name: 'Phone number', required :0}],
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
        <p>Items would appear in the center of the screen.</p><p>If the item is <strong>Househould objects</strong>, 
        press the <strong>SPACE key</strong> on the keyboard as fast and accurately as you can.</p>
        <p>If the item is <strong>Food (edible)</strong> or <strong>Stationary objects</strong>, do not press anything.</p>
       
        <p>Press any key to begin.</p>
      `,
      // post_trial_gap: 2000
    };
    timeline.push(instructions);
    
    
    var full = {
      type: 'fullscreen',
      fullscreen_mode: true
    };
    timeline.push(full);
    
    var practice_stimuli = [
     
      { stimulus: "img/fc009.jpg", correct_response: ' '},
      { stimulus: "img/ff001.jpg", correct_response: null},
     
    ]

    /* test trials */
    var test_stimuli_food = [

      { stimulus: "img/fc009.jpg", correct_response: ' '},
      { stimulus: "img/fc011.jpg", correct_response: ' '},
      { stimulus: "img/fc012.jpg", correct_response: ' '},
      { stimulus: "img/fc013.jpg", correct_response: ' '},
      { stimulus: "img/fc018.jpg", correct_response: ' '},
      { stimulus: "img/fc019.jpg", correct_response: ' '},
      { stimulus: "img/fc022.jpg", correct_response: ' '},
      { stimulus: "img/fc023.jpg", correct_response: ' '},
      { stimulus: "img/fc025.jpg", correct_response: ' '},
      { stimulus: "img/fc027.jpg", correct_response: ' '},
      
      { stimulus: "img/fh003.jpg", correct_response: ' '},
      { stimulus: "img/fh008.jpg", correct_response: ' '},
      { stimulus: "img/fh012.jpg", correct_response: ' '},
      { stimulus: "img/fh017.jpg", correct_response: ' '},
      { stimulus: "img/fh020.jpg", correct_response: ' '},
      { stimulus: "img/fh021.jpg", correct_response: ' '},
      { stimulus: "img/fh022.jpg", correct_response: ' '},
      { stimulus: "img/fh023.jpg", correct_response: ' '},
      { stimulus: "img/fh025.jpg", correct_response: ' '},
      { stimulus: "img/fh026.jpg", correct_response: ' '},
      
      { stimulus: "img/fh028.jpg", correct_response: ' '},
      { stimulus: "img/fh032.jpg", correct_response: ' '},
      { stimulus: "img/fh037.jpg", correct_response: ' '},
      { stimulus: "img/fh038.jpg", correct_response: ' '},
      
      
      { stimulus: "img/ss001.jpg", correct_response: null},
      { stimulus: "img/ss003.jpg", correct_response: null},
      { stimulus: "img/ss005.jpg", correct_response: null},
      { stimulus: "img/ss006.jpg", correct_response: null},
      { stimulus: "img/ss008.jpg", correct_response: null},
      { stimulus: "img/ss009.jpg", correct_response: null},
      { stimulus: "img/ss011.jpg", correct_response: null},
      { stimulus: "img/ss012.jpg", correct_response: null},
      { stimulus: "img/ss013.jpg", correct_response: null},
      { stimulus: "img/ss014.jpg", correct_response: null},
      
      { stimulus: "img/ss015.jpg", correct_response: null},
      { stimulus: "img/ss016.jpg", correct_response: null},
      { stimulus: "img/ss018.jpg", correct_response: null},
      { stimulus: "img/ss020.jpg", correct_response: null},
      { stimulus: "img/ss021.jpg", correct_response: null},
      { stimulus: "img/ss023.jpg", correct_response: null},
      { stimulus: "img/ss026.jpg", correct_response: null},
      { stimulus: "img/ss027.jpg", correct_response: null},
      { stimulus: "img/ss028.jpg", correct_response: null},
      { stimulus: "img/ss032.jpg", correct_response: null},
      
      
      { stimulus: "img/fk001.jpg", correct_response: ' '},
      { stimulus: "img/fk002.jpg", correct_response: ' '},
      { stimulus: "img/fk008.jpg", correct_response: ' '},
      { stimulus: "img/fk010.jpg", correct_response: ' '},
      { stimulus: "img/fk013.jpg", correct_response: ' '},
      { stimulus: "img/fk014.jpg", correct_response: ' '},
      { stimulus: "img/fk017.jpg", correct_response: ' '},
      { stimulus: "img/fk018.jpg", correct_response: ' '},
      { stimulus: "img/fk022.jpg", correct_response: ' '},
      { stimulus: "img/fk024.jpg", correct_response: ' '},
      
      { stimulus: "img/fk026.jpg", correct_response: ' '},
      { stimulus: "img/fk027.jpg", correct_response: ' '},
      { stimulus: "img/fk033.jpg", correct_response: ' '},
      { stimulus: "img/fk035.jpg", correct_response: ' '},
      { stimulus: "img/fk037.jpg", correct_response: ' '},
      { stimulus: "img/fk038.jpg", correct_response: ' '},
      { stimulus: "img/fk040.jpg", correct_response: ' '},
      { stimulus: "img/fk041.jpg", correct_response: ' '},
      { stimulus: "img/fk042.jpg", correct_response: ' '},
      
      { stimulus: "img/ff001.jpg", correct_response: null},     
      { stimulus: "img/ff002.jpg", correct_response: null},
      { stimulus: "img/ff003.jpg", correct_response: null},
      { stimulus: "img/ff005.jpg", correct_response: null},
      { stimulus: "img/ff006.jpg", correct_response: null},
      { stimulus: "img/ff008.jpg", correct_response: null},
      { stimulus: "img/ff009.jpg", correct_response: null},
      { stimulus: "img/ff011.jpg", correct_response: null},
      { stimulus: "img/ff012.jpg", correct_response: null},
      { stimulus: "img/ff014.jpg", correct_response: null},
      
      { stimulus: "img/ff015.jpg", correct_response: null},
      { stimulus: "img/ff016.jpg", correct_response: null},
      { stimulus: "img/ff017.jpg", correct_response: null},
      { stimulus: "img/ff019.jpg", correct_response: null},
      { stimulus: "img/ff020.jpg", correct_response: null},
      { stimulus: "img/ff022.jpg", correct_response: null},
      { stimulus: "img/ff023.jpg", correct_response: null},
      { stimulus: "img/ff024.jpg", correct_response: null},
      { stimulus: "img/ff029.jpg", correct_response: null},
      { stimulus: "img/ff030.jpg", correct_response: null},
    

    ];
    
    var test_stimuli_stationary = [
      { stimulus: "img/ss015.jpg", correct_response: null},
      { stimulus: "img/fk001.jpg", correct_response: ' '},
    ]
  

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

timeline.push(instructions_practice)


// Practice trial
var practice1 = { 
  type: "image-keyboard-response",
  stimulus: jsPsych.timelineVariable('stimulus'),
  choices: [' '],
  stimulus_duration: 750,
  trial_duration: 1250,
  response_ends_trial:false,
  timing_post_trial: 0,
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

var instructions_main_food= {
  type: "html-keyboard-response",
  stimulus: `
    <p> Now the main experiment starts!</p>
    
    <p> There will be no feedback. </p>
    <p> Remember </p>
    <p>If <strong>Househould objects</strong>, press the <strong>SPACE key</strong> on the keyboard as fast and accurately as you can.</p>
    <p>If <strong>Food (edible)</strong>, then <strong>DON'T</strong> press any KEY.</p>
   
    <p>Press any key to begin.</p>
  `,
};

timeline.push(instructions_main_food)

var test_1_food = { 
  type: "image-keyboard-response",
  stimulus: jsPsych.timelineVariable('stimulus'),
  choices: [' '],
  stimulus_duration: 750,
  trial_duration: 1250,
  response_ends_trial:false,
  timing_post_trial: 0,
  post_trial_gap:0,
  timing_response: 1250,//total trial duration needs to changed
  data: {
    task: 'response',
    correct_response: jsPsych.timelineVariable('correct_response')
  },
  on_finish: function(data){
    data.correct = jsPsych.pluginAPI.compareKeys(data.response, data.correct_response); 
  }
}

var break_block_food = {
  type: "html-keyboard-response",
  data: {
    trial_id: "moving to next phase"
  },
  stimulus: "<p>Take a break.</p>"+"<P>For Household products, press <STRONG>SPACE key </STRONG></p>"+"<p> For edible Food Items, <STRONG> DON'T PRESS </STRONG>any key",
  timing_post_trail: 0
}

var test_2_food = { 
  type: "image-keyboard-response",
  stimulus: jsPsych.timelineVariable('stimulus'),
  choices: [' '],
  stimulus_duration: 750,
  trial_duration: 1250,
  response_ends_trial:false,
  timing_post_trial: 0,
  post_trial_gap:0, 
  timing_response:1250,//total trial duration needs to changed
  data: {
    task: 'response',
    correct_response: jsPsych.timelineVariable('correct_response')
  },
  on_finish: function(data){
    data.correct = jsPsych.pluginAPI.compareKeys(data.response, data.correct_response);
  }
}

var test_3_food = { 
  type: "image-keyboard-response",
  stimulus: jsPsych.timelineVariable('stimulus'),
  choices: [' '],
  stimulus_duration: 750,
  trial_duration: 1250,
  response_ends_trial:false,
  timing_post_trial: 0,
  post_trial_gap:0, 
  timing_response:1250,//total trial duration needs to changed
  data: {
    task: 'response',
    correct_response: jsPsych.timelineVariable('correct_response')
  },
  on_finish: function(data){
    data.correct = jsPsych.pluginAPI.compareKeys(data.response, data.correct_response);
  }
}

var test_procedure_1_food = {
  timeline: [fixation, test_1_food],
  timeline_variables: test_stimuli_food,
  repetitions: 1,
  randomize_order: true,
}


timeline.push(test_procedure_1_food);

timeline.push(break_block_food)

var test_procedure_2_food = {
  timeline: [fixation, test_2_food],
  timeline_variables: test_stimuli_food,
  repetitions: 1,
  randomize_order: true,
}

timeline.push(test_procedure_2_food)

timeline.push(break_block_food)

var test_procedure_3_food = {
  timeline: [fixation, test_3_food],
  timeline_variables: test_stimuli_food,
  repetitions: 1,
  randomize_order: true,
}

timeline.push(test_procedure_3_food)


// Instructions for stationary experiment
var instructions_main_stationary= {
  type: "html-keyboard-response",
  stimulus: `
    <p> Now there is some variation in the experiment!</p>
    
    <p> There will be no feedback. </p>
    <p> Remember </p>
    <p>If <strong>Househould objects</strong>, press the <strong>SPACE key</strong> on the keyboard as fast and accurately as you can.</p>
    <p>If <strong>Stationary objects</strong>, you <strong>DON'T</strong> have to press any KEY.</p>
   
    <p>Press any key to begin.</p>
  `,
};

timeline.push(instructions_main_stationary)

var test_1_stationary = { 
  type: "image-keyboard-response",
  stimulus: jsPsych.timelineVariable('stimulus'),
  choices: [' '],
  stimulus_duration: 750,
  trial_duration: 1250,
  response_ends_trial:false,
  timing_post_trial: 0,
  post_trial_gap:0,
  timing_response: 1250,//total trial duration needs to changed
  data: {
    task: 'response',
    correct_response: jsPsych.timelineVariable('correct_response')
  },
  on_finish: function(data){
    data.correct = jsPsych.pluginAPI.compareKeys(data.response, data.correct_response); 
  }
}

var break_block_stationary = {
  type: "html-keyboard-response",
  data: {
    trial_id: "moving to next phase"
  },
  stimulus: "<p>Take a break.</p>"+"<P>For Household products, press <STRONG>SPACE key </STRONG></p>"+"<p> For stationery, <STRONG> DON'T PRESS </STRONG>any key",
  timing_post_trail: 0
}

var test_2_stationary = { 
  type: "image-keyboard-response",
  stimulus: jsPsych.timelineVariable('stimulus'),
  choices: [' '],
  stimulus_duration: 750,
  trial_duration: 1250,
  response_ends_trial:false,
  timing_post_trial: 0,
  post_trial_gap:0, 
  timing_response:1250,//total trial duration needs to changed
  data: {
    task: 'response',
    correct_response: jsPsych.timelineVariable('correct_response')
  },
  on_finish: function(data){
    data.correct = jsPsych.pluginAPI.compareKeys(data.response, data.correct_response);
  }
}

var test_3_stationary = { 
  type: "image-keyboard-response",
  stimulus: jsPsych.timelineVariable('stimulus'),
  choices: [' '],
  stimulus_duration: 750,
  trial_duration: 1250,
  response_ends_trial:false,
  timing_post_trial: 0,
  post_trial_gap:0, 
  timing_response:1250,//total trial duration needs to changed
  data: {
    task: 'response',
    correct_response: jsPsych.timelineVariable('correct_response')
  },
  on_finish: function(data){
    data.correct = jsPsych.pluginAPI.compareKeys(data.response, data.correct_response);
  }
}

var test_procedure_1_stationary = {
  timeline: [fixation, test_1_stationary],
  timeline_variables: test_stimuli_stationary,
  repetitions: 1,
  randomize_order: true,
}


timeline.push(test_procedure_1_stationary);

timeline.push(break_block_stationary)

var test_procedure_2_stationary= {
  timeline: [fixation, test_2_stationary],
  timeline_variables: test_stimuli_stationary,
  repetitions: 1,
  randomize_order: true,
}

timeline.push(test_procedure_2_stationary)

timeline.push(break_block_stationary)

var test_procedure_3_stationary = {
  timeline: [fixation, test_3_stationary],
  timeline_variables: test_stimuli_stationary,
  repetitions: 1,
  randomize_order: true,
}

timeline.push(test_procedure_3_stationary)

var debrief_block = {
  type: "html-keyboard-response",
  stimulus: function() {

    // var trials = jsPsych.data.get().filter({task: 'response'});
    // var correct_trials = trials.filter({correct: true});
    // var accuracy = Math.round(correct_trials.count() / trials.count() * 100);
    // var rt = Math.round(correct_trials.select('rt').mean());
    
    return `Thank you for participating in this Experiment. `
  }
}

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
    document.writeln("<div style=\"text-align: center; font-size: 24px;\">The experiment has ended. Thanks for participating!");
  }
});