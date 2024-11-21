
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

#  Flappy Face 
## CS110 Final Project   Fall Semester, 2024 

## Team Members

Samuel Yu

***

## Project Description

 I want to make flappy bird but instead of a flappy bird, I want it to be a face. First, the gamer will prompt the user to take a picture of his face before the game and then his face will appear on the screen. The face will then act like a regular flappy bird where it will automatically fall and it will fly up when you press the space bar. I want the game to save the face and score the user gets. 

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. Start Menu 
2. Moving Background and Tubes 
3. Score Tracker 
4. Obstacle Collision 
5. Game Over Screen

### Classes

- Cloud - Makes the cloud image and puts it on the screen. It moves the clouds as the screen is moving 
- Controller- Controls the entire program. It controls the movement of the screen and all the actions of the user. 
- Player- Controls the user and makes the player up, and down and checks whether it makes contact with any of the pipes.
- Floor- Makes the floor and as the background is moving, the floor is moving 
- Pipes- Makes the Pipes and generates the height for the top tip and the bottom. Also has a hitbox and checks whether the player hits the tubes 


## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Run Counter Program  |GUI window appears with count = 0  |
|  2                   | click count button   | display changes to count = 1      |
etc...
