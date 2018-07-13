/* Buzzfeed Quiz
Create a Buzzfeed Quiz with 5 questions. Create a method for determining what
the results will be. Combine our knowledge of HTML, JS, and CSS to get hired at
Buzzfeed.
1. Finish the function 'creatQuestions'
  a. Make sure you have a list of dictionary of questions
  b. Create the questions and options (aka the radio buttons) DYNAMICALLY
  in JavaScript. In other words, don't hard code the questions; we want to use
  code to access our list of dictionary of questions.
      (HINT 1: HTML is just a bunch of STRINGS. Create HTML code with JS by
      creating strings with tags i.e. ('<input type="radio" name="group" value ="asdf"'))
      (HINT 2: Group the radio button inputs for each question using the SAME name
       or class)
  c. Make sure our changes are reflected in the HTML
      (HINT: getElementById and change its innerHTML)
  d. Call this function WHEN THE PAGE LOADS!!!!
      (HINT: wrap the function in paranthesis like in Overwatch Hero workshop)
2. Define the function 'submitAnswer'
  a. We want to iterate through each group of questions to see what the user
  selected.
  (HINT: a selected answer is "checked"; look up checked radio button)
  b. Determine how your Buzzfeed personality is predicted
      ideas (easy): Assign points to each of your option. If an option makes the
      user a Broccoli, assign a low point (0,1). If an option makes the user a Carrot,
      assign medium high points (4,5). If an option makes the user a Celery,
      assign high points (10). All numbers selected are arbitrary; you decide.
          0-10 points = Snow White
          11-20 points = Belle
          21-30 points = Star-Lord
          31-40 points = Loki
      ideas (medium):
          Determine which value was selected the MAXIMUM times
          Need to handle TIES.
3. Make more questions, add CSS, add images, use BootStrap
*/
(function createQuestions(){

  /*TODO: ADD MORE QUESTIONS. Create a field for images*/

  var questions = [
    {
      "question": "What is your favorite weekend hobby?",
      "name": "weekend",
      "answers" : {
        "Sitting back with a good book.": "Belle",
        "Blowing out some thermo's": "Star-Lord",
        "Causing small problems as a bit of fun.": "Loki",
        "Cleaning out the house": "Snow White"
      }
    },
    {
      "question": "What is one of your favorite colors?",
      "name": "colors",
      "answers" : {
        "Green": "Loki",
        "Yellow": "Belle",
        "Red": "Star-Lord",
        "Blue": "Snow White"
      }
    },
    {
      "question": "Do you purposely push people in front of street trolleys to heroically save them afterwards?",
      "name": "trolley",
      "answers" : {
        "No...": "Belle",
        "What horrible person would do that?": "Snow White",
        "Of Course ;)": "Loki",
        "Maybe, if I wanted to impress them": "Star-Lord"
      }
    }
  ];

  var html = "";
  for (var i = 0; i < questions.length; i++){
    html += questions[i]["question"] + "<br>" ;
    for (var key in questions[i]["answers"]){
      html += '<input type="radio" name="' + questions[i]["name"] + '" value="';
      html += questions[i]["answers"][key] + '">' + key + "<br>";
    }
  }

  /* TODO: set the element "survey" 's innerHTML to html'*/
  document.getElementById("quiz").innerHTML = html
})();

function submitAnswer(){
  var total = 0;
  var categories = ["weekend", "trolley", "colors"];

  /* TODO:  Determine your winning "personality" */
  var score = {
    "Snow White": 0,
    "Belle": 0,
    "Star-Lord": 0,
    "Loki": 0
  }

  for (var j = 0; j < categories.length; j++){
    var cat = document.getElementsByName(categories[j]);
    for (var i = 0; i< cat.length; i++){
      if (cat[i].checked){
        score[cat[i].value] = score[cat[i].value] + 1;
      }
    }
  }

  var win_char;
  var win_score = 0;

  for (var key in score){
    if (score[key] > win_score){
      win_score = score[key];
      win_char = key;
    }
  }

  /*TODO: Replace the empty quotes with the result of the quiz*/
  document.getElementById("results").innerHTML = "You most relate to "  + win_char;
}
