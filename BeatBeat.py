'''
Dear tutor:
I have used the pygame package to achieve my project.
And during the project, I have used a '.wav' file to let my game has sound effect.
In addition, I used 2 '.ttf' files to let my game could show beautiful font.
So, to run my programme correctly, don't forget to download above 3 files. *^-^*
'''

import pygame
import sys
import random


clock = pygame.time.Clock()


color0 = (0, 0, 0) # Black
color1 = (255, 250, 205) # LemonChiffon
color2 = (255, 250, 250) # Snow
color3 = (255, 215, 0) # Gold
color4 = (142, 229, 238) # CadetBlue2
color5 = (255, 193, 193) # 	RosyBrown1

max_note_num = 10 # The game will over after max_note_num notes be created

# Set some initial value
hit_line = 500
speed = 1
judge_image = None
judge_rect = None
stay_time = 0 # to help perfect/good/miss stay on screen for longer time
break_time = 120 # to help 'playing' screen go to 'end' screen more slowly
num_perfect = 0
num_good = 0
num_miss = 0
score = 0
combo = 0
max_combo = 0
last_note_num = max_note_num

game_status = 'start'


# draw the game screen
pygame.init()
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption('BeatBeat')


class note:
    def __init__(self, x, speed):
        self.x = x # center_x
        self.y = -7.5 # center_y
        self.speed = speed

    def move(self):
        self.y += self.speed

    def draw(self):
        pygame.draw.rect(screen, color2, (self.x - 20, self.y - 7.5, 40, 15))

# the sound effect
pygame.mixer.init()
sound = pygame.mixer.Sound('duang.wav')

# set the format and so on of the text that will be shown on the screen
title_font = pygame.font.Font('WDXLLubrifontTC-Regular.ttf', 60)
title_image = title_font.render('BeatBeat', True, color3)
title_rect = title_image.get_rect()
title_rect.centerx = 200
title_rect.centery = 250
enter_font = pygame.font.Font('WDXLLubrifontTC-Regular.ttf', 30)
enter_image = enter_font.render('PLAY', True, color0, color2)
enter_rect = enter_image.get_rect()
enter_rect.centerx = 200
enter_rect.centery = 330

select_font = pygame.font.Font('WDXLLubrifontTC-Regular.ttf', 30)
select_image = select_font.render('SELECT YOUR SPEED LEVEL', True, color2)
select_rect = select_image.get_rect()
select_rect.centerx = 200
select_rect.centery = 200
speed_font = pygame.font.Font('WDXLLubrifontTC-Regular.ttf', 60)
speed_image = speed_font.render(f'{speed:02d}', True, color2)
speed_rect = speed_image.get_rect()
speed_rect.centerx = 200
speed_rect.centery = 300
play_image = select_font.render('GO!', True, color0, color2)
play_rect = play_image.get_rect()
play_rect.centerx = 200
play_rect.centery = 400

arrow_font = pygame.font.Font('DelaGothicOne-Regular.ttf', 40)
arrow_image1 = arrow_font.render('←', True, color1)
arrow_rect1 = arrow_image1.get_rect()
arrow_rect1.centerx = 50
arrow_rect1.centery = 560
arrow_image2 = arrow_font.render('↑', True, color1)
arrow_rect2 = arrow_image2.get_rect()
arrow_rect2.centerx = 150
arrow_rect2.centery = 560
arrow_image3 = arrow_font.render('→', True, color1)
arrow_rect3 = arrow_image3.get_rect()
arrow_rect3.centerx = 250
arrow_rect3.centery = 560
arrow_image4 = arrow_font.render('↓', True, color1)
arrow_rect4 = arrow_image4.get_rect()
arrow_rect4.centerx = 350
arrow_rect4.centery = 560
back_image = arrow_font.render('⏎', True, color1)
back_rect = back_image.get_rect()
back_rect.centerx = 20
back_rect.centery = 20

judge_font = pygame.font.Font('WDXLLubrifontTC-Regular.ttf', 40)
judge_image1 = judge_font.render('PERFECT', True, color3)
judge_rect1 = judge_image1.get_rect()
judge_rect1.centerx = 200
judge_rect1.centery = 300
judge_image2 = judge_font.render('GOOD', True, color4)
judge_rect2 = judge_image2.get_rect()
judge_rect2.centerx = 200
judge_rect2.centery = 300
judge_image3 = judge_font.render('MISS', True, color5)
judge_rect3 = judge_image3.get_rect()
judge_rect3.centerx = 200
judge_rect3.centery = 300

score_font = pygame.font.Font('WDXLLubrifontTC-Regular.ttf', 30)
combo_image = score_font.render(f'{combo:03d}', True, color2)
combo_rect = combo_image.get_rect()
combo_rect.centerx = 200
combo_rect.centery = 50
score_image = score_font.render(f'{score:05d}', True, color2)
score_rect = score_image.get_rect()
score_rect.centerx = 200
score_rect.centery = 20

end_font = pygame.font.Font('WDXLLubrifontTC-Regular.ttf', 30)
perfect_end_image = end_font.render(f'PERFECT: {num_perfect:03d}', True, color3)
perfect_end_rect = perfect_end_image.get_rect()
perfect_end_rect.centerx = 200
perfect_end_rect.centery = 150
good_end_image = end_font.render(f'GOOD: {num_good:03d}', True, color4)
good_end_rect = good_end_image.get_rect()
good_end_rect.centerx = 200
good_end_rect.centery = 200
miss_end_image = end_font.render(f'MISS: {num_miss:03d}', True, color5)
miss_end_rect = miss_end_image.get_rect()
miss_end_rect.centerx = 200
miss_end_rect.centery = 250
max_combo_image = end_font.render(f'MAX_COMBO: {max_combo:03d}', True, color2)
max_combo_rect = max_combo_image.get_rect()
max_combo_rect.centerx = 200
max_combo_rect.centery = 300
score_end_image = end_font.render(f'SCORE: {score:05d}', True, color2)
score_end_rect = score_end_image.get_rect()
score_end_rect.centerx = 200
score_end_rect.centery = 350


# build a dictionary notes to save all note
column_x = [50, 150, 250, 350] # to limit where the note will appear randomly
notes_left = []
notes_right = []
notes_up = []
notes_down = []
notes = {0: notes_left, 1: notes_right, 2: notes_up, 3: notes_down}


# to let the screen appear consistently so we use loop
while True:
    screen.fill(color0)

    # start screen
    if game_status == 'start':
        # draw
        screen.blit(title_image, title_rect)
        screen.blit(enter_image, enter_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_status = 'level' # player could go to 'level' screen by using the 'Enter' key
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and enter_rect.collidepoint(event.pos):
                    game_status = 'level' # player could also go to 'level' screen by clicking the 'PLAY'

    # level screen
    # player could choose speed level from 1 to 10
    elif game_status == 'level':
        # draw
        screen.blit(select_image, select_rect)
        speed_image = speed_font.render(f'{speed:02d}', True, color2)
        screen.blit(speed_image, speed_rect)
        screen.blit(play_image, play_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    speed = speed % 10 + 1 # player could increase the speed by using up key
                elif event.key == pygame.K_DOWN:
                    speed = speed - 1 # player could decrease the speed by using down key
                    if speed == 0:
                        speed = 10
                elif event.key == pygame.K_RETURN:
                    game_status = 'playing' # player could start the game by using Enter key
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and speed_rect.collidepoint(event.pos):
                    speed = speed % 10 + 1 # player could also change the speed by clicking the num
                if event.button == 1 and play_rect.collidepoint(event.pos):
                    game_status = 'playing' # player could also start the game by clicking GO!


    # playing screen
    elif game_status == 'playing':
        if random.random() < 0.02 and last_note_num > 0: # each loop has 2% chance to create a note
            last_note_num -= 1
            column_id = random.choice([0, 1, 2, 3])
            notes[column_id].append(note(column_x[column_id], speed))

        # draw
        screen.blit(arrow_image1, arrow_rect1)
        screen.blit(arrow_image2, arrow_rect2)
        screen.blit(arrow_image3, arrow_rect3)
        screen.blit(arrow_image4, arrow_rect4)
        pygame.draw.line(screen, color2, (10, hit_line), (390, hit_line), 1)
        screen.blit(back_image, back_rect)

        combo_image = score_font.render(f'{combo:03d}', True, color2)
        screen.blit(combo_image, combo_rect)
        score_image = score_font.render(f'{score:05d}', True, color2)
        screen.blit(score_image, score_rect)

        for note_list in notes.values():
            for n in note_list:
                n.move()
                n.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # to judge if player press the correct key immediately
                if event.key == pygame.K_LEFT and notes[0]:
                    for i, n in enumerate(notes[0]):
                        if abs(n.y - hit_line) < 10:
                            judge_image = judge_image1
                            judge_rect = judge_rect1
                            stay_time = 20 # to let 'PERFECT' stay longer on the screen
                            notes[0].pop(i) # let the note disappear
                            num_perfect += 1
                            pygame.draw.rect(screen, color3, (n.x - 40, n.y - 20, 80, 40), 2)
                            score += 100
                            combo += 1
                            sound.play()
                            break
                        elif abs(n.y - hit_line) < 20:
                            judge_image = judge_image2
                            judge_rect = judge_rect2
                            stay_time = 20
                            notes[0].pop(i)
                            num_good += 1
                            pygame.draw.rect(screen, color4, (n.x - 40, n.y - 20, 80, 40), 2)
                            score += 50
                            combo += 1
                            sound.play()
                            break
                elif event.key == pygame.K_UP and notes[1]:
                    for i, n in enumerate(notes[1]):
                        if abs(n.y - hit_line) < 10:
                            judge_image = judge_image1
                            judge_rect = judge_rect1
                            stay_time = 20
                            notes[1].pop(i)
                            num_perfect += 1
                            pygame.draw.rect(screen, color3, (n.x - 40, n.y - 20, 80, 40), 2)
                            score += 100
                            combo += 1
                            sound.play()
                            break
                        elif abs(n.y - hit_line) < 20:
                            judge_image = judge_image2
                            judge_rect = judge_rect2
                            stay_time = 20
                            notes[1].pop(i)
                            num_good += 1
                            pygame.draw.rect(screen, color4, (n.x - 40, n.y - 20, 80, 40), 2)
                            score += 50
                            combo += 1
                            sound.play()
                            break
                elif event.key == pygame.K_RIGHT and notes[2]:
                    for i, n in enumerate(notes[2]):
                        if abs(n.y - hit_line) < 10:
                            judge_image = judge_image1
                            judge_rect = judge_rect1
                            stay_time = 20
                            notes[2].pop(i)
                            num_perfect += 1
                            pygame.draw.rect(screen, color3, (n.x - 40, n.y - 20, 80, 40), 2)
                            score += 100
                            combo += 1
                            sound.play()
                            break
                        elif abs(n.y - hit_line) < 20:
                            judge_image = judge_image2
                            judge_rect = judge_rect2
                            stay_time = 20
                            notes[2].pop(i)
                            num_good += 1
                            pygame.draw.rect(screen, color4, (n.x - 40, n.y - 20, 80, 40), 2)
                            score += 50
                            combo += 1
                            sound.play()
                            break
                elif event.key == pygame.K_DOWN and notes[3]:
                    for i, n in enumerate(notes[3]):
                        if abs(n.y - hit_line) < 10:
                            judge_image = judge_image1
                            judge_rect = judge_rect1
                            stay_time = 20
                            notes[3].pop(i)
                            num_perfect += 1
                            pygame.draw.rect(screen, color3, (n.x - 40, n.y - 20, 80, 40), 2)
                            score += 100
                            combo += 1
                            sound.play()
                            break
                        elif abs(n.y - hit_line) < 20:
                            judge_image = judge_image2
                            judge_rect = judge_rect2
                            stay_time = 20
                            notes[3].pop(i)
                            num_good += 1
                            pygame.draw.rect(screen, color4, (n.x - 40, n.y - 20, 80, 40), 2)
                            score += 50
                            combo += 1
                            sound.play()
                            break
                elif event.key == pygame.K_ESCAPE:
                    game_status = 'level' # player could back to level by using Esc key
                    # let all game statue back to initial value
                    combo = 0
                    score = 0
                    num_perfect = 0
                    num_good = 0
                    num_miss = 0
                    for n in notes.values():
                        n.clear()
                    last_note_num = max_note_num
            elif event.type == pygame.MOUSEBUTTONDOWN: # player could also back to level screen by clicking the back arrow
                if event.button == 1 and back_rect.collidepoint(event.pos):
                    game_status = 'level'
                    combo = 0
                    score = 0
                    num_perfect = 0
                    num_good = 0
                    num_miss = 0
                    for n in notes.values():
                        n.clear()
                    last_note_num = max_note_num

        # let the miss note disappear
        for note_list in notes.values():
            for n in note_list:
                if n.y > hit_line + 30:
                    judge_image = judge_image3
                    judge_rect = judge_rect3
                    stay_time = 20
                    note_list.remove(n)
                    num_miss += 1
                    if combo > max_combo:
                        max_combo = combo
                    combo = 0
                    break

        # let PERFECT/GOOD/MISS judge text stay longer on the screen
        if stay_time > 0:
            screen.blit(judge_image, judge_rect)
            stay_time -= 1

        # when all max_note_num notes was created and disappeared the game over
        if last_note_num == 0 and not(notes[0] or notes[1] or notes[2] or notes[3]):
            if break_time > 0:
                break_time -= 1
            else:
                game_status = 'end'

    # end screen
    elif game_status == 'end':
        # draw
        perfect_end_image = end_font.render(f'PERFECT: {num_perfect:03d}', True, color3)
        screen.blit(perfect_end_image, perfect_end_rect)
        good_end_image = end_font.render(f'GOOD: {num_good:03d}', True, color4)
        screen.blit(good_end_image, good_end_rect)
        miss_end_image = end_font.render(f'MISS: {num_miss:03d}', True, color5)
        screen.blit(miss_end_image, miss_end_rect)
        max_combo_image = end_font.render(f'MAX_COMBO: {max_combo:03d}', True, color2)
        screen.blit(max_combo_image, max_combo_rect)
        score_end_image = end_font.render(f'SCORE: {score:05d}', True, color2)
        screen.blit(score_end_image, score_end_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    pygame.display.flip()
    clock.tick(60)