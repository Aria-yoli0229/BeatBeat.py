### BeatBeat - A Rhythm Game with Pygame

BeatBeat is a simple rhythm game made with Python and Pygame. Players could try to achieve the highest comboo by pressing the correct arrow keys as the notes fall down to the hit line!

__features__
- multiple game states: Start -> Select Speed Level -> Play -> End
- Diffirent speed level could be chosen
- Sound effects with .wav file when you hit the note successfully
- Fonts with .ttf files for UI styling
- Judgement System: Perfect, Good, Miss
- Score system and Combo system
- Game ends after a fixed numeber(default 20 and if you want to play for longer time, you could change the value of max_note_num in the programme) of notes are generated

__Make sure the following 3 resource files are in the same directory:__
- duang.wav
- WDXLLubrifontTC-Regular.ttf
- DelaGothicOne-Regular.ttf

__controls__
| Key / Action       | Function / 描述                   |
|--------------------|------------------------------------|
| `← ↑ → ↓`          | Hit notes in the corresponding lane |
| `Enter`            | Start / Confirm / Proceed  |
| `↑ / ↓`            | Change note falling speed  |
| `Esc`       | Return to speed selection screen |
| Mouse Left Click   | Click buttons on screen |
