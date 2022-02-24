<h1 align="center" style="font-size: 250%;"><b>
Battleships Terminal Game
</b></h1>

[Check the live project here!](https://jfrdrkssn.github.io/second-project-ci/)


---
## How to play
---

This game is based on the classic [Battleships game](https://en.wikipedia.org/wiki/Battleship_(game)).

When the game starts an info area is displayed at the top, containing info about the game. The player is then prompted to enter a name. The boards are drawn up and the player can now enter co-ordinates.

The player can see their ships, marked with an **__S__**, on their board. The computer ships are hidden.
Hits are marked with **__*__** and misses with **__M__*.

---
## **Features**
---

- Info
    - At the top of the game there's info on how the game is set up.
    
    add image

- Random ship generation on the game board
    - Ships are placed randomly on both the player and computer board.
    - The computer ships are invisible to the player.

    ADD IMAGE

- Turn based
    - The game is turn based.
    - There's 16 rounds in total.
    - Rounds are updated and displayed after each turn.

    ADd image

- Input validation
    - Player can choose any name. It's capitalized when referenced.
    - When entering co-ordinates for the board, only __whole numbers__ within the board size are valid.
    - The player is informed of any input errors, like entering the same co-ordinates (numbers) twice.

    add image

### **Unimplemented features**

- Player and computer scores
    - When all ships on either board has been sunk, declare a winner.
    - If either the player or computer has a higher score when all rounds are over, declare a winner.

---
## **Data Model**
---

The data chosen for this project is a class. The class is called Board and holds everything for the application to run.

---
## **Testing**
---


    - [PEP 8 linter](http://pep8online.com/)


### **Bugs**

No known bugs.

---
## **Deployment**
---

### **Heroku**

The project was deployed to Heroku using the following steps...

1. Log in to Heroku and create a new application.
2. Go to the "Settings" tab.
3. Add the following buildpacks in this order.
    1. heroku/python
    2. heroku/nodejs
4. Link [this repository](https://github.com/JFrdrkssn/third-project-ci) with the Heroku application.
5. Choose "Automatic Deployment" or "Manual Deployment".


## **Credits**

### **Code**
- The code is based on [Code Institute's](https://codeinstitute.net/) school curriculum. It's from a video where a tutor shows an example of a simple Battleships game in Python.

## Acknoledgments

- My Mentor, Gerard McBride, for continuous helpful feedback and support.
- Fellow student Patrik Österljung, for peer review of code and insightful tips. [GitHub](https://github.com/oljung)