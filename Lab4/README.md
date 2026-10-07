## Changes Made

### Task 1 – Fixed Hit Detection

* Fixed the target hit-detection bug.
* Changed hit detection from rectangular collision detection to **circular distance-based detection**.
* The click is now considered a hit only when it falls within the target's actual radius.
* This makes the hit detection more accurate and matches the circular shape of the targets.

### Task 2 – Added Moving Targets

* Added movement to the targets.
* Each target now has its own horizontal and vertical velocity (`vx` and `vy`).
* Targets move continuously while the game is running.
* Added boundary checking so targets **bounce off the edges of the game window** instead of leaving the screen.
* Added different movement speeds/directions to make targets move in different patterns.
* The circular hit detection from Task 1 continues to work correctly with moving targets.

### Task 3 – Added Combo Scoring

* Added a scoring system to the game.
* Each successful hit increases the score.
* Added a **combo system** where consecutive successful hits increase the score multiplier.
* The score is calculated using the points-per-hit and current combo multiplier.
* A missed shot resets the combo and multiplier back to `1x`.
* Added on-screen display for:

  * Current score
  * Current combo multiplier
  * Number of hits
  * Number of misses

### Task 4 – Added Timed Game Rounds

* Added a **30-second countdown timer** for each game round.
* The remaining time is displayed on the game screen.
* When the timer reaches zero:

  * The game ends.
  * No additional shots are accepted.
  * The final score is displayed clearly.
* Added the ability to start a new round using the **R key**.
* Restarting a round resets:

  * Score
  * Hits
  * Misses
  * Combo
  * Combo multiplier
  * Timer
  * Targets
* Targets resume moving when a new round starts.
 
 Repository Link - https://github.com/sameerdeshpande17/04_target_shooting
