Which Code Witch Machine Learning Lesson: 
Teachable Machine LESSON : Hat / No Hat
https://teachablemachine.withgoogle.com/

Teachable Machine is a Machine Learning framework which uses AI models that differentiate sound, images, and poses, which can be used to build applications.

Teachable Machine is a Google funded project made in partnership with Tensorflow.JS, ml5.JS, P5.JS, Coral, Framer, Node.JS, Glitch, and Arduino



This is a start-up lesson, showing how to make a web application using Teachable Machine. 
We will use this framework to check if the user is wearing a hat or not wearing a hat.

Getting Started

Go to the Teachable Machine Learning page at https://teachablemachine.withgoogle.com/
Click the GET STARTED button
Select an IMAGE PROJECT, using the STANDARD IMAGE MODEL

STANDARD IMAGE MODEL

The STANDARD IMAGE MODEL is set up in three columns: the CLASS column, the TRAINING column, and the PREVIEW column. 

In this workflow, we assign a CLASS for each state that needs to be discerned by Teachable Machine, and create a series of image samples. 

Then, we TEACH these classes to the ml5.JS framework online, and PREVIEW the results using the Tensorflow.JS framework in the same window. 

Finally we EXPORT the MODEL, which can be viewed as a HTML page provided by Teachable Machine.

WALKTHROUGH

BUILDING CLASSES

Decide on a series of states which are binary, or clearly discernible. 
In this case, we will decide on a HAT Class and a NO HAT Class. 
Change the name of the first class to HAT, by clicking on the pencil icon next to Class 1.
Change Class 2 to NO HAT, using the same step process.
Click on Webcam for HAT to turn on the camera and take selfies of yourself wearing a hat. 
The longer you hold the button the more pictures you will take. 
It’s ok to only have less than 50 images of yourself. 
If you find you took too many pictures, click on the 3 dots next to the Class header, and select Remove All Samples, to start over.
Repeat this series of steps for NO HAT Class.



TRAINING THE MODEL

Click on the TRAIN MODEL button in the center column to teach the classes to this model.
IMPORTANT: do not click away from the webpage tab while the model is being trained.



PREVIEW THE MODEL

Test to see if the model works. Under the PREVIEW there will be a window showing the webcam results.
Make sure that the webcam is selected as ON, and that the correct camera is selected.
The OUTPUT should show correctly a percentage of 100% of HAT or NO HAT, if you sampled images for each CLASS correctly.

EXPORT THE MODEL

To view and share this project click on the EXPORT MODEL button in the PREVIEW header.
Within the preset Tensorflow.js tab, select ☁️Upload my model
Your samples aren’t sent to any servers, unless you save your project to Google Drive — and even then, it’s in your Google Drive, so that sample data is still yours. When you train the model, it trains in your browser tab without sending anything to any servers.
Copy and save the shareable link. Open a new tab and you will see a unique page using your model, designated by a unique URL extension, from https://teachablemachine.withgoogle.com/models/  

Hat / No Hat
YOUTUBE Tutorial : https://www.youtube.com/watch?v=CcdamNqyl-I
