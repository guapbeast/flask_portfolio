{% include navigation.html %}

For my create task, I'm going create a series of word games that the user could play just for entertainment, or to help the explore new items to buy depending on their preference. The first game that I'm going to program is a Hangman game where I have a Tea version and a Tee version, with words being set in both games leaving the user to figure them out. I would also have an CSP page that would lead the user to page that could help them to discover key terms related to AP Computer Science Principles. In order to create the game, I would have to use a series of JavaScript functions and Python, in order to create the structure and inner workings of the game and use HTML and CSS to make the game more user friendly and improve the UI.


Some issues that I've encountered so far are getting the API to function properly and correctly load the assets. The API I used is extremely complicated and takes too many resources to figure out, so I think I should switch API's or try to make my own.




# Requirements
| Requirements| Implementation |
| ------------- | ------------- |
| Use of List/Collection Types  | A list was used for the initialization and establishment of sets of strings that would later be randomly picked for usage|
| Input  | Users input characters into the program via a prompt displayed by the code, which asks for keyboard input. |
| Procedure | A function that takes user input and provides a response to the input is present |
| Algorithm | There are algorithmic elements present in the coded program with the most prominent element being the conditional statements that are used throughout the code. In the program, the code calls on if and else statements in order to verify the inputs of the users and deliver a response to the inputs. Iteration in the code takes place when the algorithm is repeated multiple times until the user completes the input or runs out of tries to provide an input. The sequencing of the code takes place when the input is returned in a specific order to deliver a response. |
| Calls to Procedure | The interaction with buttons determines the calls to procedures as different buttons result in different calls to procedure, the inputs presented determine which procedure is run. |
| Instruction for Output | The output is determined by the inputs that are provided to the program by the user; if the user provides all of the correct required inputs, an output is returned in the form of strings, which congratulate the user, however, if not all of the correct required inputs are provided, then an output prompting the user to try again is displayed. |
| Commenting | Used in order to explain the code for new readers of the code. |


# Issues Faced
Some issues that I've encountered so far are getting the API to function properly and correctly load the assets. The functionality of my webpage also is something that i've faced issues with, as sometimes the layout of the page gets messed up and the style of the webpage gets skewed.
 

# Commits 
 

* [Creation of Page](https://github.com/NinjaBreadLord/super-duper-bassoons/commit/9eff7c9e806d17d13e8304cf06087ec5597c444d)
* [Routing of Page through Python as well as Integration into Webpage](https://github.com/NinjaBreadLord/super-duper-bassoons/commit/f294298b90f9d2fa95b90135278fbaffc4c51c0d)
* [SASS integration](https://github.com/NinjaBreadLord/super-duper-bassoons/commit/ce3fe9e61da38f890d0ded6c8c5acf1daedb7161)
* [Additional Edition added](https://github.com/NinjaBreadLord/super-duper-bassoons/commit/1c372192cc431ef04f9f311cfa9bdf369327c924)
* [SCSS CSS Generation](https://github.com/NinjaBreadLord/super-duper-bassoons/commit/53fcc9cfcd9846e9fbabf991ad02e66c1538d5cb)


# Writeup and Code (1 min Video link on Slack)

* [Code](https://github.com/NinjaBreadLord/super-duper-bassoons/commit/f294298b90f9d2fa95b90135278fbaffc4c51c0d)


3a




The written procedure contributes much to the program as it makes up a large part of the infrastructure of the program. Since the idea of the program is to create a guessing word game, the algorithm provides the code segment for the displaying of the letters as the user inputs characters into the program. The algorithm implemented in the procedure uses identifiers in order to identify elements of the program and then uses javascript algorithms in the form of conditional statements which provide actions that are carried out by the program in every situation. One example is when the code uses an if statement on whether the selected word includes the correct letter of the randomized word. If the selected word matches one or more of the correct letters in the randomized word, the letter is revealed, and if not, the else statement displays a notification that tells the user that the letter they chose is incorrect.



3d.
 
![Code](https://github.com/NinjaBreadLord/super-duper-bassoons/blob/main/static/assets/rithwikh/Screen%20Shot%202022-02-27%20at%209.11.31%20PM.png)


The first call to data takes place in the form of the buttons on the page, which have procedures that are called upon and allow for the button to carry out the actions and be interact-able to the user. In order to display an output result, the condition that has to be met is that the user must click on the button in order for the procedure to run. The end result of the procedure of the button is that the user is directed to 
a different page, or is able to interact with the program being able to do things such as restart the game and load a new word into the game.

The second call to data takes place in the for of the actual word game which prompts the user for input in the form of letters. The procedures that are called upon allow for the user to interact with the actual program. In order to display an output result, the condition that has to be met is that the user must provide input to the function by typing in a letter. The end result of the procedure of the input of letters is that the user gets prompted with whether or not their guess is correct, and the website outputs and displays the result of their guesses. If the user correctly guesses all of the letters, the procedure prompts them with a congratulatory notification and a popup to play again, and if the user doesn't, the correct word is displayed and the user is prompted with a popup to play again.




