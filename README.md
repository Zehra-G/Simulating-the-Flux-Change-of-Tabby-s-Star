# Simulating the Flux Change of Tabby's Star

## Abstract

KIC 8462852 in the star constellation called Cygnus, or shortly Tabby’s Star since it was discovered by Tabetha Boyajian of Yale, is a star that has been baffling scientists ever since its discovery. This star that is 1480 light years away from our Earth was observed to change its flux in an unexpected way. Occasionally, it gets much dimmer than usual, even to the point of getting 22% dimmer at a relatively short timescale. Several theories were proposed to explain this inconsistent behavior of the star, however, none turned out to predict its behavior accurately. Some people even think that the aliens are extracting energy from it, causing it to fluctuate in brightness unexpectedly (Strickland, 2018).

![Star KIC 8462852 in infrared (2MASS survey) and ultraviolet (GALEX)](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/KIC_8462852_in_IR_and_UV.png/640px-KIC_8462852_in_IR_and_UV.png)

*Star KIC 8462852 in infrared (2MASS survey) and ultraviolet (GALEX)*

In this project, I used a data file from NASA to simulate the change of Tabby’s Star’s flux. I imported random, time and GraphicsPlus to be able to use their modules. To make my simulation look more aesthetically pleasing, I created a Celestial object class, and Shooting Star and Galaxy classes that inherited from it. These objects are displayed and moved in the background of the simulation. To create my Tabby’s Star simulation, I used various lists, functions and conditionals to analyze my data and display different sizes of the Tabby’s Star image with the appropriate time difference between each changing image.

## Project Description

I defined the common parameters like the position and type of the objects in my Celestial class and wrote getter and setter methods like getType, getPosition, setScale. In my shooting star class that inherited from the Celestial class, I used an image object in my refresh method to make the simulation look more aesthetically pleasing. I also created a move method there that moves the shooting star to random locations using a for loop.

To simulate the flux change of the Tabby’s Star, first I created lists that held data in the csv file from NASA that I was working with. I read from that csv file and appended the time and flux data to my lists (tabbytime, tabbyflux). I also created another list (tabbytimedifferances) that held the difference between each consecutive time value in the tabbytime list, because I needed these values to create the real ratios of time between Tabby’s Star’s flux changes in my simulation. 
 
I used 10 resized versions of the same star image (smallest to largest) to create 10 image objects in my main function. After sorting the flux data, I used for loops and divided the flux data into ten categories by magnitude. For example, flux values that were higher than 1.5 were category 1, for which I used my biggest star image, and the ones that were between 1.5 and 1 were category 2, for which I used my second biggest star image, and so on (the values in this sentence are just for the example and are not the real limits). I determined the lower & upper magnitude limits for each category and appended them to a separate list. 

I repeated the same steps for the time values using the time differences list that I created. I sorted the time difference between each flux data entry into ten categories from smallest to largest in terms of how much time has passed since, to determine for how long I’m going to display the image for that entry. Using various conditionals, I displayed the appropriate sized image object for the appropriate amount of time for each entry in data. I also displayed the time and the flux values using text objects on my simulation window.

Additionally, I had two other functions in this project calculating the mean flux value and the maximum flux value. These values were also displayed on the simulation window for a better understanding of the displayed flux value of the star as it was changing. To write the function that calculated the mean, I used recursion. This function took in a list of values as the parameter. The base case was to return the element if there was only one element in the list, since then it would be the mean. Then I used the formula for the mean value of given values to write the recursive case.

## Results


https://user-images.githubusercontent.com/113384943/199319162-4241a11a-fb84-4c33-9630-8b7ae5a035c2.mov



When we run the tabbysimulation.py, it iterates over Tabby’s flux and time lists and displays the image in the appropriate size category for an amount of time depending how long it took for the second flux data to be taken between consecutive flux data entries. This created a Tabby’s Star simulation using real flux and time ratios. The flux value for every data entry and the time is displayed on the side of the window, as well as the maximum and the mean flux values. In the background of the simulation window, shooting stars are moving to random locations. 

## Critical Evaluation of the Design:

In terms of making the simulation more aesthetically pleasing, I think it would look better if I had more celestial objects in the background. I have defined a Galaxy class that inherited from the Celestial class for future use, which I haven’t used in this project yet. Galaxy class has some of the methods for rotation ready. There could be spinning galaxy image objects that are randomly positioned in the background of the simulation, which would make it much more visually appealing. More classes of celestial objects can be added.
 As for my code design, I think I could think of more efficient ways to display the right image for every flux value for the right amount of time. There are a lot of lines of similar code in the part that I use conditionals in the for loop that I used for that task. That part of the code takes up a lot of space in my main function and is not the most efficient way to execute this task. 

## Potential Biases or Limitations:

First of all, the data file that was used in this project was uploaded five years ago, meaning that the simulation of Tabby’s Star’s flux change might not reflect the current state of the star’s fluctuations in flux. Data that was taken in the near past would be better to reflect the state of Tabby’s Star today. This data set was uploaded to data.world website by Dave Griffith, and it was taken by NASA’s Kepler Telescope showing time, flux, standard deviation and the orientation. I used only time and the flux for this project. This data set was not a relatively big one, so I am assuming that the uploader to data.world created the csv file with a certain section of the complete data. This limits the scope of my simulation. 



## References:

Strickland, Ashley Cnn. “Tabby’s Star: Why Does the ‘most Mysterious Star in the Universe’ Act This Way?” CNN, 3 Jan. 2018, edition.cnn.com/2018/01/03/us/tabbys-star-mystery-dimming-brightening/index.html.
“Tabby’s Star Dimming - Dataset by Dave.” Data.World, 13 Nov. 2021, data.world/dave/tabbys-star-dimming.
Image 1 Credits:
“Tabby’s Star Dimming - Dataset by Dave.” Data.World, 13 Nov. 2021, data.world/dave/tabbys-star-dimming.
Acknowledgements: 
Prof. Stacy Doore
Harsha Somaya (CS152 A Student)
Chandrachud Gowda ‘25 (CS 231 student)

