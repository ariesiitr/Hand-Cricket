# Project: Hand Cricket
Submitted in fulﬁllment of the requirement for

# ArIES 
# 2nd-year recruitment project


Mentored by:-	Maanas Verma (3rd Year EPH)
  		Pranjal Mangal (3rd Year EE)

Submitted by:- Akshat Gupta (ECE)
				Yatin Mittal (Mech)
                        Shrashtika Singh (EE)

# Brief Description: 
Playing Hand Cricket with a computer, with gesture detection.
  
# Ideation Process:
●	Rules of the Game- Detailed discussions regarding the rules of the game. 
1)	The game will offer the players up to six hand gestures (1 to 6) to play the game only with the right hand.
2)	The game will only be a single-player game in which the player plays against the computer. User will do the batting, and the computer will do the balling.
3)	The computer will generate gestures using random functions and whenever that value matches with the player gesture, then the game will be over.

# Hand Gesture Detection:
Requirement: The player should be play this game in a well-lighted area as proper finger detection requires sufficient light.

Studying various online examples and hand detection repositories to come up with the best hand detection method. 
Choices between - OpenCV, Yolo, and CNN. 

1)	OpenCV- Less error-prone and a lot faster, but difficult to configure.
2)	Yolo - Training of data requires a lot of time as it requires labeling of each image.
3)	CNN - Too slow, and the response time is way ahead of other methods. Not feasible for this project. 

# Algorothm used in finger detection and counting using OpenCV:
MediaPipe offers customizable Python solutions as a prebuilt Python package on PyPI, which can be installed simply with pip install mediapipe. It also provides tools for users to build their solutions.

Firstly for palm detection, we use a pre-built Palm detection model in MediaPipe. MediaPipe Hands utilizes an ML pipeline consisting of multiple models working together. A palm detection model that operates on the full image and returns an oriented hand bounding box. A hand landmark model operates on the cropped image region defined by the palm detector and returns high-fidelity 3D hand keypoints.

After the palm detection over the whole image, our subsequent Hand landmark model performs precise keypoint localization of 21 3D hand-knuckle coordinates inside the detected hand regions via regression, that is direct coordinate prediction. The model learns a consistent internal hand pose representation and is robust even to partially visible hands and self-occlusions.
Link for the reference: https://google.github.io/mediapipe/solutions/hands
To implement this algorithm first, we create a class “handDetector”.
We use this class in our actual model.
Using MediaPipe, the accuracy rate is high and better than the previous algorithm.
First, we write a code to simply count fingers 0 to 5 instead of detecting a particular hand pose.
For detecting particular six hand poses shown in the above snap to make our model more effective, we write unique code lines for each particular hand pose.

# Algorithm used:
To detect the particular hand pose of the right hand we write unique code for each hand pose, the algorithm used for 4 fingers is up-down. If the top point of any of the fingers is above the bottom point of finger that means the finger is open otherwise close. For thumb, we used the left-right algorithm. If the thumb of the right hand is the right side of the screen then it would be considered as open otherwise close.

# Time and Random module:
We used a timer to provide the player with sufficient time to be ready with his/her hand gesture using Timer module. We have set the timer for 2 seconds. Timer module is an inbuilt module in python.
We used random.randint() function of random module for generating the computer’s number. Random module is an inbuilt module in python. The random.randint() method returns a random integer between the specified integers.

We also add two more functions. First, for displaying the number shown by the player and generate by the computer in one round. And second, for displaying the final score of the player and who is the winner.
We are simply using numpy library in these functions.

After fulfilling all the requirements of the game we integrate all the above-discussed functions and modules on a single python file.

# How the game looks like and how it works:
In this hand cricket game, always user will do batting i.e. in every round user will always choose a number at first. After that computer will generate its number using random module. This will happen again and again until the user number and computer’s number are unequal. And display  
Internally, the code will add the user’s score and computer’s score in every round. When the values of user and computer will match then the game will over and the screen will display the final score of the user and display who is the winner.
If the user score greater than the computer score then the user will win and display “PLAYER WIN” and vice-versa. If the user and computer score is equal the then it will display the user score and “TIE”.

# How to play:
1)	Run the python file
2)	A window ‘a’ display, press ‘q’ to start timer of 2 seconds. User should ready with hand gestures. 
3)	After 2 seconds hand gesture is detected and display on the other window ‘Image’.
4)	Press close ‘x’ to close the ‘Image’ window. Press ‘esc’ to close the window ‘a’.
5)	After that computer number display on a new window ‘Image’. Press ‘x’ to close the window.
6)	A new window ‘Image’ pops up which displays the instant score of both computer and user in that round. Press ‘x’ to close the window.
7)	Again window ‘a’ pop up for the user’s gesture detection and the same process will repeat until the value of user and computer will match.
8)	When the values match, then after display the instant score, a new window pops up and displays the total score of the user and the winner. Press ‘x’ to close the open window and the program stops.
