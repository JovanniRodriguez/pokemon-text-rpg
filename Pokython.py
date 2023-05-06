'''Pokemon Red for Python
By Jovanni Rodriguez'''


'''Sources used:
https://www.reddit.com/r/ASCII_Archive/comments/d09jhz/pokemon_ascii_textart_collection_over_500_pokemon/
https://stackoverflow.com/questions/20302331/typing-effect-in-python
GameFreak, Nintendo, Pokemon franchise 
'''
#Add "try again"/reload function when user types in wrong values
#Add text boxes around all text prompts
#indent all images/logo to middle of screen, not left
#space out everything so it looks cleaner, like a screen refresh. Don't want to see old output above new scenes
#change text size / font 
#add sounds when selecting things, background sound etc. if possible 
#make gamemenu for text speed etc.
#actually make text speed system

#make starter descriptions with ascii art

import pyfiglet
from rich import print
import sys
import time
from time import sleep
import pygame

pygame.init()




#============== S O U N D S =====================

#use pygame.mixer.find_channel().play(sound1) 





#pygame.mixer.Channel(1).play(title_music)   <-------------- uncomment this line for opening theme
    





print('===============================================================================')

print('''








''')




potion = 'Potion'

global pokemon_team
pokemon_team = []

global pc_storage
pc_storage = ['Potion']
global bag
bag = []




def print_typing_medium(text):                             #modified version of borrowed stackoverflow code, more generalized for use with all in-game text.
    '''Takes text and types it at medium speed.''' 

    for char in text:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()



def print_typing_fast(text):
    '''takes text and types it at fast speed. '''
    for char in text:
        sleep(0.02)
        sys.stdout.write(char)
        sys.stdout.flush()



def print_typing_slow(text):
    '''takes text and types it at slow speed. '''
    for char in text:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()

def print_typing_extreme(text):
    '''takes text and types it super fast, really only for the title and any images/ art printed.'''
    for char in text:
        sleep(0.001)
        sys.stdout.write(char)
        sys.stdout.flush()







        

#title = pyfiglet.figlet_format('Pokemon Red', font='basic')
#print(f'[yellow]{title}[/yellow]')





print_typing_extreme('''                                .;:**'                           
                                `                                
    .:XHHHHk.              db.   .;;.     dH  MX                 
  oMMMMMMMMMMM       ~MM  dMMP :MMMMMR   MMM  MR      ~MRMN     
  QMMMMMb  "MMX       MMMMMMP !MX' :M~   MMM MMM  .oo. XMMM 'MMM
    `MMMM.  )M> :X!Hk. MMMM   XMM.o"  .  MMMMMMM X?XMMM MMM>!MMP
     'MMMb.dM! XM M'?M MMMMMX.`MMMMMMMM~ MM MMM XM `" MX MMXXMM 
      ~MMMMM~ XMM. .XM XM`"MMMb.~*?**~ .MMX M t MMbooMM XMMMMMP 
       ?MMM>  YMMMMMM! MM   `?MMRb.    `"""   !L"MMMMM XM IMMM  
        MMMX   "MMMM"  MM       ~%:           !Mh.""" dMI IMMP  
        'MMM.                                             IMX   
         ~M!M                                             IMP   ''')


print_typing_extreme('''                                                                    
                    ###                              ##                 
    #####            ##   ###  ##                    ##                 
     ## ##           ##    ##  #                                        
     ## ##   ###   ####    ##  #   ###  ### #  #### ###   ####  #####   
     ####   ## ## ## ##     ###   ## ##  #### ###    ##  ## ###  ## ##  
     ## ##  ##### ## ##     ###   #####  ##    ###   ##  ##  ##  ## ##  
     ## ##  ##    ## ##     ###   ##     ##     ###  ##  ### ##  ## ##  
    #### ##  ####  #####     #     #### ####  ####  ####  ####  ### ### 
                                                                    
                                                                    
''')



def intro_oak():
    '''Prints the intro portion with prof. oak.'''
    print('''                                                            

                              ▓▒▒░▒▓▓▓▒▒▓▓▓▓▓▓▒▒
                             ▒▓▒░░░░░░░░░░░░░░░▓▓▓▒▒
                          ▒▓▓▒░░░░░▒▒░░░░░░░░░░░░░░▒▓▒░
                           ▒▒▓▒▒▒▒▓▓▓▓▒░░░▓▒▒▒▓▓▒▒░░▒▓▒
                           ▒▒▒▒▒▓▒▒▒░░▒▓▒▒▓▒░░░░▒▓▒░▒█▒
                            ▓▓▓█▒░░░░░░▒▒░░░░░░░░█▓▒█▒
                            ░▒▓██▓▓░░▒░░▒░░░░░▓▓▓██▓▒░
                            ░▒░░▒▓██▓▓▓▒▒▓▒▓█▓▓██▓▓▒▒▓▒
                            ▒█▒▒█▒░▒▒▓█░░░▒▓█▓▒▒░░▒▒░█▒
                            ▒▓▓█▓▒░░▒▓▓▒░░░▒░░░░░▓▓▓▒░
                             ▒▓█▓░░▒▒▓▒▒▒░░░▒░░░▓▒░
                                 ▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒
                                 ▓▓█▓▓▒░░░░▒▓▓███▓
                            ▒▒▓▓▓▒░░▒▓███▓▓▓▓▒░█▓░▓▒▒▒
                          ▓███▓▒▒░░░▓████▓▓▒▒▒▒▒▒░░▒▓▓▒▒▒
                         ▒█▓▒▒▒▒▓▓▒░▓██▒▒▒▒▒▒▒▒▓▒░░▒▒░░░░▒▒
                        ▓██▓▓▒▒▒▒▓█▒▒▒▒▒▓▓▓▓▓██▓▒▒▒▒░░░░▒▓
                        ▓█▓▓▓▓█████▓▓▓██▓▒▒▒▒▒▓█▓▒▒▒░░░░░░▒▓▒
                       ▒▒▒░▓█▓▓▓▓▓▒░▒▓▓▓▒▒▒▒▒▒▓█▒░░░▒▒░░▒▒▒█▒
                      ▒▓▒░░▓██▒▒▓░▒▓██▓█▓▓▓▒▒▒▓█▒░░░▒░░░▓▒░▓▒
                     ▒▓▓▓▓▓▓██▓▒░░░░▒▒▒▓▓▓▓▒▒▒▓█▒░░▒▒░░░█▒░░▒▒
                    ▒▒▒░░░░░▒█▒░░░░░▒▓█▓▓▓▓▓▓▓██▒░▒▒░░░░█▒░░▓▓
                   ▒▓▒░░░░░░▒███▓▒░░░▒█▓▓▓▒░▒▓█▒▒▒░░░░░░█▒░░▒▓
                    ▓▒░░░░░░░░▓███▓▓█▓░░░░░░░▓█▒▒▒░░░░░░█▒░░░▒▓▒
                     ▒▒▓▓▓▓▓▓▓▓▓▓███▓▒░░░░░░░▓█▒░░░░░░░░█▓░░░▒█▒
                         ▒█▒░▒▓▓▓▒▓██▓▓▒░▒▓▓▓██░░░░░░░░░█▓▒▒▓▓▒
                         ▒█▒░░░░░░▒█▓██▓▓▓██▓██░░░░░░░░▒█▓▒▒▓▒
                         ▒▒▒▒▒░░░░▒█▓▓▓▓▓▓▓▓▓██▓▒░░░▒░░░▒▓▓▒
                        ▓▓░░░░▒▒░░▒█▓▒▓██▓▓▒▓▓▓█▒░░▒▒░░░░▓▓
                        ▓▓░░░░▒▒░░▒█▓▓▓█▓▓▒▒▒▒▓█▒░░▒▒░░░░▓▓
                        ▓▓░░░░▒▒░░▒█▓▓▓▓▓▓▓▓▒▒▓█▒░░▒▒░░░░▓▓
                        ▓▓░░░░▒▒░░▒█▓▒▓█▓▒▓▓▒▒▓█▒░░▒▒░░░░▓▓
                        ▓▓▒░░▒▒▒░░▒█▓▒▓█▓░█▓▒▒▓█▒░░▒▒▒░░▒▓▓
                        ▓▓░░░░░░░▒▓▓▓▒▒█▓░█▓▒▒▓█▒░░░░░░░░▓▓
                         ▒▓█▓░░░▒█▓▒▒▒▒▓▒░▓▓▓▓▓█▓░░░░░▓█▓▒
                          ▓█▓▓▓▓▓▓▒▒▓█░░░░▒█▓▓▓▓▓▓▓▓▓██
                          ▓█▓▒▒▒▒▒▒▒▓█░░░░▒█▓▒▒▒▒▒▒▒▒▓█
                         ▒▓▓▓▓▓▓▒▒▒▒▓▓▒░░░▒█▓▒▒▒▒▓█▓▓▓▓▒
                         ▒███████▓▓▓▓▓▓█▓░▒▓▓▒▒▓▓▓▓▓▓▓▓▓▓▒
                         ▒█▓▒▒▒▒▒█▓▒▒▓▓▒░░▒▒▓▓██▓▒▒▒▒▒▓██▒
                         ▒▓▓▒▒▒▒▒▒▓▓▓▒      ▓█▓▒▒▒▒▒░░▒▓▒
                           ▓▓▓▓▓▓▓▒          ▓▓▓▓▓▓▓▓▓▓▓                   ''')
    print()
    print('---------------------------------------------------------------------')

    print_typing_medium('Hello there! Welcome to the world of Pokemon!')
    enter = input()
    print_typing_medium('My name is Oak! People call me the Pokemon Prof!')
    enter = input()
    print_typing_medium('This world is inhabited by creatures called Pokemon!')
    enter = input()
    print_typing_medium('For some people, Pokemon are pets.')
    enter = input()
    print_typing_medium('Others use them for fights.')
    enter = input()
    print_typing_medium('Myself... I study Pokemon as a profession.')
    enter = input()
    sleep(0.5)
    print()
    print('''
                                        ▒▒▓▓▓▓▒▒
                                   ▒▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▒
                               ▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▓▓▒
                           ░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒
                         ░▒▓▓▓▓▒▓▓▓▓▒░░▒▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▒
                         ▒█▓▓▒▒▒▓█▒░▒▒▒▒░▓█▒▒▒▒▒▒▒▒▒▒▒▒▓▓
                         ░▒▓▒▒▒▒▓▓▓▒▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒▒▒▓█
                           ▒▓▓▒▒▒▓▓▓▓▓▓▓▒▒░░░░▒▒▒▒▒▒▒▒▓██
                            ▒▒▓▒▒▒▒░▒▒▒░░░░░░░░░▒▒▓▓▓▓▓██
                             ▓▓░░░░░░░░░░░░░░▒▒▒▓███████▓
                           ▒▓▒░░░░░░░░▒▒▒▒▒▒▓▓▓▓▓▓▒▓▓▒░░░▒▒
                           ▒▓▓▓▓▓▓▓▓▓▓████▓▓▒▒▒░▓█░░░░▒░░█▓
                             ▒▓▓███▓▓▓▒▒▒▒▒▒▒▒░░▒▓░░▒▒▒▒▒▓▒
                                ▒█▓▒▒▒▒▒▒▒▒░░▒▒▒░░░▒█▓▒▒▒
                                 ▒▓▓▓▒▒▒▒▒▒▓▓▒░░░░▓▓▒▒▒
                                   ▒▓█▓▓▒▒▒▒▒▒▓▓▓▓█▓▒
                               ░▒▒▓█▓▓▓▓████▓▒▓█▓▓▒▓▓▒
                            ▒▒▓▓▓▒▓█▓▓▓▓▓▓▓▒▒▒░░▓█▓▒▒▒▓▒
                          ▒▓▓▒▒▒▒▒▓▓▓▓▓██▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▒▒
                        ▒▒▓▒░▒▒▒▒▒░░░▒▓████████▓▓▓▓▓▓▒░▒▒▓▒▒
                      ▒▒▒▒░░░░▒▓▒░░░░░▒▓████████▓▒▒▒░░░▓█░▒▓▒
                     ▒▒░░░░░░░▒█▓░░░░▒▓█████████▒░░░░░▒▒▒░░▒▒▒
                    ▒▓▒▒▒░░░▒▒▒▒░░░░░▒██████████▒░░░░▒▒░░░░░▒▓▒
                   ▒▒▒▒▒▒▓▓▓▓█▓░░░░░▒▓████████▓▒░░░░░▒█▒░░░░▒▓▒
                  ▒▓▓▒▓▒░░░░▒█▓░░░░░▓█████████▓░░░░░░▒█▒░░░░░░▒▒
                    ▒▓█▓░░▒▒▒█▓▒▒░░▒▓█████████▓░░░░░░▒█▓▒░░░░░▓▓
                      ▒▓▓▓▒▒▓▓▓▒▒▒▒▒██████████▓▒░░░░░▒▓▒▒▒▒░░▒▓█
                        ▒▒▒▓█▓▓▓▓▓▓▓█▓▒▓▓█████▓▒▒▒▒▒▒▒▓▒▒▒▒▒▒▓██
                            ▒▓▓▓▓▓████▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓████▓▓██
                             ▓▓▓▓█▓▓▓▓▓▓█▓▒▒▒▒▓▓▓▓▓▓██▓████▓▒▓██
                              ▒▓██▓▓▒▒▒▓█▓▓▒▒▒▒▒▒▒▒▓█▓░░▒▓▓█████
                                ▒█▓▓▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▓█▓▒▓██▓▓▓▓██
                               ▒▓▓▓▓▒▒▒▒▓▓██▓▓▒▒▒▒▒▓███▓▒▓▓▓████
                              ▒▓▓▓▒▒▒▒▒▓▓▓▓▓▓▓▒▒▒▒▒▓█▓▓▓▓▒▒▒▒▒▒▒
                              ▒██▓▒▒▒▒▒▓█▒░▓▓▓▒▒▒▒▒▓█▒░▒▒▓▓▓▒
                              ▒█▓▒▒▒▒▒▒▓█▒░▓▓▓▒▒▒▒▒▓█▒
                              ▒█▓▒▒▒▒▒▒▓▓▒░▓▓▒▒▒▒▒▒▒▓▓▒
                              ▒▒▒▒▒▒▒▓▓▓▒░░░▒█▓▒▒▒▒▒▒▓█▒
                             ▓▓▒▒▒▒▒▒▓█▓░░░░▒█▓▒▒▒▒▒▒▓█▒
                             ▓█▓▒▒▒▒▒▓█▓░░░░▒█▓▒▒▒▒▒▒▓█▒
                             ▓█▓▒▒▒▒▒▓█▓░░░░░▒▓▓▓▒▒▓▓▓▒
                              ▓▓▓▓▓▓▓▓▒░░░░░░░▒██▓▓██▓
                              ▒██████▓░░░░░░░░▒█▓▒░▒██▓▒
                            ▒▓▓▓▒▒▒▓▓▓█▒░░░░▒█▓▓▓▓▓▓▓▓▓▒
                          ▒▒▓▓▓█▓▓▓█▓▓█▓░░░░▒██▓▓▓▓▓▓▓▓██
                         ▒█▒░░▒▒▓█▓▓▓▓▓▒░░░░▒▓██▓▒░░░▒▓█
                          ▒▓▓▓▓▓▓▓▓▓▓▒░░░░░░░░▒▓▓▓▓▓▓▓▓▓▒
                           ░▒▒▒▒▒▒░░░░░░░░░░░░░░▒▒▒▒▒▒▒                    ''')
    print()
    print('---------------------------------------------------------------------')

    print_typing_medium('First, What is your name? ')
    print()
    sleep(0.5)
    
    
    print('''
 __________________
| 1). [NEW NAME]   |
| 2). [RED]        |
| 3). [ASH]        |
| 4). [JACK]       |
|__________________| ''')
    global player_name
    player_name = input('')
    
    if player_name == '1':
        player_name = input('Your name? : ')
        
    elif player_name == '2':
        player_name = 'Red'

    elif player_name == '3':
        player_name = 'Ash'

    elif player_name == '4':
        player_name = 'Jack'


    
    
    print_typing_medium('Right! So your name is ' + player_name + '!')
    enter = input()
    print()
    sleep(0.5)



    print('''
                        ▒▓▓▓▒
                         ▒▓▓▓▓▓▒▒
                           ▒▓▓▓▓▓▓▒
                      ▒▒▓▓▓▓▓▓▓▒▓▓▓▓▓▒▒▓▒▒
                  ▒▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▒▒▒▒▓▒
               ▒▓▓▓▓▓█▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
              ▒▒░▓▓▓▒▓▓▓▒▒▒▒▓▓▓▒▒▒▓▒▒▒▒▒▒▒▒▒▓▓▒
                  ▒▓▓▓▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▒▓▓▓▓▓▓▓▒
                 ▒▓▓▒▒▒▓▓▓██▓▓▒▓█▒▒▒▒███░▒▓░▒▓▓▓▓▓▓▒
                ▒▓▓▒▒▒▒▓██▓▓▓▓▓▓█▒▒▒▓▓▓▓▒▒▒░▒▓▓▓▓▓▓▓▒
               ▒███▓▓▓▓▓▒▒▒▓██▓▒▒▒▓▒▒▓▓▒█▓▒▓▓▓██▓▒▒
                  ▓█▓██▓▒▒▒░▒█▒▒▒▒░░░█▒░▒▓▓░░░░▒▓▒
                  ▒▓▓▓▒░▓▓▒░▒▓▒▒▒▒░░░▒▒▓▓▓▓▓▒░░░░█▒
                        ▓▓▒▒▒▒▒▒▒▒▓▓░░░▒▓▓▓█▓▒░░▒▓▒
                         ▒▓▒▒▒▒▓▓▓▒▒▒░▒▓░░░░▓█▓▓▓░▒▓
                             ▒▒▒▓▓▒▓█▒░░▒▒▒▒▒▓▓▒░░░░▓
                          ▒▓▓▓▓▓▓▒▒▒▒▓▓▓▒░░░▒▓█▓▒▒░░░▒
                       ▒▒▓▓▒▒▓▒▓▓▓▓▒▒▒▒░░░░░░░▒▓█▒░░░▒▒
                      ▒▓▓▒▒▒▒▒▒▒▒▒▒░▒▓▓▓░░░░░░▒▒▒▒▒▒▒▒▓▓
                        ▓▓▒▓▓░░░░░░▒▓▒░▒▓▒▒▒▒▓▓▒▒█▓▒▒▓▓▓
                       ▒▒▒░▒▒░░░░░▓▒░▒▒▒░▓█▓      ▒▒▒▒▒
                      ▒▓░░▒░░░░░░░░▒▓▒░▒▓██
                      ▒▓░▒█░░░░░░░░░░▓▓▓▓▓▓
                     ▓▒░░▒█▒░░░▒▓▓▓▓▓▓▓▓▒
                     ▓▓▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▒
                   ▒▓▓▒▒▒▓█▓▒▓▓▒░░▒▒▒▒▒▒█▒
                     ▓▓▓█▓▓▓▓▓██▓▒▒▓▒▒▒▓█▒
                     ▓▓░▓▓▓▒▒▓▓▓▓▓▓██████▒
                     ▒▒▒█▓▓▒▒▓▓█▓▓▒▒▒▒▒▓▓▒▒
                      ▒▓▓▓▒▒▒▓▓▓██▓▒▒▒▒▒▒▓▓
                      ▒█▓▒▒▒▒▓▓▓▓░▒▓▒▒▒▒▒▓█
                      ▒█▓▒▒▒▒▓█▓░░▓▓▒▒▒▒▒▓█
                      ▒▓▒▒▒▒▒▓█▒   ▒▒▒▒▒▒▒▓▓▒
                    ░▒▒▒▒▒▒▒▓▓▒    ▒█▒▒▒▒▒▓█▒
                     ▓▓▒▒▒▒▒▓▓     ▒▓▒▒▒▒▒▓█▒
                     ▓▓▓▓▓▓▓▓▓       ▓▓▓▓▓▓█▒
                   ▒▓▒▒▒▓▓▒▒▓█       █▓▒▓▓▒▒▒▓
                   ▒▓▒░▒▓▓░░▒▓       █▓▒▓▓░░▓▓▒
                  ▓█▓▓▓▓▒▒▓█▓        ▒▓█▒▓▓▓▓▓█▒
                 ▒▒▒░░░▒▓▓▓▒           ▒▓▒░░░▒█▒
                  ▒▓▓▓▓▓▒                ▒▓▓▓▓             ''')
    print()
    print('---------------------------------------------------------------------')
    print_typing_medium('This is my grandson.')
    enter = input()
    print_typing_medium('He\'s been your rival since you were a baby.')
    enter = input()
    print_typing_medium('...Erm, what is his name again?')
    print()
    sleep(0.5)


  
    print('''
 __________________
| 1). [NEW NAME]   |
| 2). [BLUE]       |
| 3). [GARY]       |
| 4). [JOHN]       |
|__________________|  ''')
    global rival_name
    rival_name = input('')
    
    if rival_name == '1':
        rival_name = input('Rival\'s name? : ')
        
    elif rival_name == '2':
        rival_name = 'Blue'

    elif rival_name == '3':
        rival_name = 'Gary'

    elif rival_name == '4':
        rival_name = 'John'
        
    print_typing_medium('That\'s right! I remember now! His name is ' + rival_name + '!')
    enter = input()
    sleep(0.5)
    print('---------------------------------------------------------------------')
    print_typing_medium(player_name + '!')
    enter = input()
    print_typing_medium('Your very own Pokemon legend is about to unfold!')
    enter = input()
    print_typing_medium('A world of dreams and adventures with Pokemon awaits!')
    enter = input()
    print_typing_medium('Let\'s go!')
    enter = input()
    sleep(0.5)
    house_upstairs()





    
def house_upstairs():
    '''prints house upstairs sequence and gets it running.'''
    print_typing_extreme('---------------------------------------------------------------------')
    print()
    print('You are in your bedroom.')
    enter = input()
    print('''
░▓▀▀▀▀▀▀▌░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓█▓▓▓▓▓▓▓░░░░░░░░░░░▓█▓▓▓▓▓▓▌
░█▄▄▄▄▄@▌░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▓▓▓▓▓██░░░░░░░░░░j██▓▓▓▓██▌
▌▓█████╬▌█@##################░░░░░░░░░░░░░░░░░░░░░██▓▓▓▓▓██░░░░░░░░░░j██▓▓▓▓██▌
▌█░░░▀▀▒▌█▌░░░░░░░░░░░░░░░░░░▌░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀▀▀▀▀░░░░░░░░░░░▀▀▀▀▀▀▀▀▀
 ▐▓▓▓▓▓▓░█▌░░░░░░░░░░░░░░░░░░▌░░░░▒░░░░▒░░░░▒░░░░▒░░░░░░░░░░░░░░░░░░░▄▄░░░░░░░░
▌▌░░░'░j▌█▌░░░░░░░░░░░░░░░░░░▌                                       ██U,,╓▄▓▒█
▓█▓▓▓▓▓█▌█▌░░░░░░░░░░░░░░░░░▄▌                                       ███▀▓▓█▓▀█
▌░░░█▌░░░█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓█▀                                       ▓▓█▀█▌░█░▐
█╬╬╬█▓╬╬╬█▓▄▄▌▀▀▀▀▀▀▀▀▀▀▀▀▌▄█                                        ▓░█░▐@▄███
                                                                     

   
                                ░╓▄▄▄╖
                                ▓▄░░░▒█
                               ▓▀`▓"▓`▀▓
                               ▓▀██▄██▀▓
                                ▓▓▓▓▓▓▌
 
                               ▄▓▓▓▓▓▓▓▄                    
                              ▐▒░░░░░░░j▌
                              ▐▓▌░░░░░▐╣▌
                              ▐▓▌░░░░░▐╣▌
                              ╙▓▓█▓▓▓█▓Ñ▀                                ░
                               ▓▒▀▀▀▓
                               █ ~~ █    
                               ╙▓Ñ▀▓▓@╜Ñ╖
                                 ▀▀▐▄░▓▀
 ▌ÑÑÑ▀ÑÑÑ╨▓                          `                       ▄▄╖, ,▄@▄      
 ▌▀▓▓▓▓▓▀▀█                                                 ║▓░╙▐▓░▄╫▓
 █╜'`````▀█                                                 ╟█▓▀▀▀▌▀▓▌
 ▌        ▓ ░    ░    ░         ░                           ╫▌░░▓█w▄░▓U
 ▌        ▓                                                  ▀▀╙▐██╝▓▌
 ▌        ▓                                                   ,▄▌░▌▄
 ▌        ▓                                                  ╔╬█▄░▓█▄         
 ▌▀▀▀▀▀▀▀▀█                                                  ╙▓░▀▀▀░▓
 ▌░░░░░░░░▓                                                   ▀╣▄▄▄▓            ''')

    sleep(0.5)
    bedroom_choices()


 
def bedroom_choices():
    '''Creates bedroom prompts'''
    print()
    print('What would you like to do?')
    sleep(0.5)
    print('''
 ______________________
| 1). [Check PC]       |
| 2). [Check SNES]     |
| 3). [Go downstairs]  |
| 4). [Menu]           |
|______________________|    ''')
    choice = input('')

    if choice == '1':
        pc_options()





        
        
        
    elif choice == '2':
        print_typing_medium(player_name + ' is playing the SNES!')
        enter = input()
        print_typing_medium('...Okay!')
        enter = input()
        print_typing_medium('It\'s time to go!')
        enter = input()
        bedroom_choices()
        
        
    elif choice == '3':
        print('Going downstairs...')
        sleep(1.0)
        house_downstairs()

    elif choice == '4':
        player_menu()
        bedroom_choices()
        
        
    

    
    

def pc_options():
    '''Creates pc prompts'''
    print_typing_medium(player_name + ' turned on the PC.') #Create storage system and bag/item management !! ****************
    enter = input()
    print()
    print('''
 ______________________
| 1). [Witdhraw item]  |
| 2). [Deposit item]   |
| 3). [Log off]        |
|______________________|    ''')
    print('What do you want to do?')
    pc_choice = input('')
    print()
    if pc_choice == '1':
        pc_withdraw()

    
    if pc_choice == '2':
        if bag[0] == '':
            print('There is nothing to deposit!')
            print()
            sleep(0.5)
        else:
            pc_deposit()

    if pc_choice == '3':
        sleep(0.5)
        print('Logging off...')
        sleep(0.3)
        bedroom_choices()
        





def start_menu():
    '''Start menu after title screen for selecting new game, options'''
    #print_typing_medium('Select one')
    print()
    sleep(0.5)
    print('''
 _________________
| 1). [New Game]  |
| 2). [Option]    |
|_________________|
''')
    user_input = input('')
    
    if user_input == '1':
        intro_oak()
        

    elif user_input == '2':
        print()
        option_menu()
    





def start_game():
    '''Initiates after title screen.'''
    
    press_enter = input('|========================[Press enter to begin]=========================| ')
    if press_enter == '':
     
        sleep(0.1)
      
        sleep(1.0)
        
   
        
        
        sleep(0.3)
        start_menu()
        #put next game phase here and call it as a function ex: character_info()
    else:
        print()
        print_typing_medium('Nope try again')
        print()
        print()
        
        start_game()




def option_menu():
    '''Options menu for text speed adjustment.'''
    print('''
 ________________________________________
|               TEXT SPEED               |
|                                        |
|  1). FAST    2). MEDIUM    3). SLOW    |
|________________________________________| ''')
    
    
    user_input = input('')
    if user_input == '1':
        type_speed = 0.02
        print('Text speed changed to FAST')
        enter = input()
        
    elif user_input == '2':
        type_speed = 0.05
        print('Text speed changed to MEDIUM')
        enter = input()
        
    elif user_input == '3':
        type_speed = 0.1
        print('Text speed changed to SLOW')
        enter = input()
    







def pc_withdraw():
    '''Withdraws items from the pc.'''
    if pc_storage == []:
        print()
        print('There is nothing stored.')
        enter = input()
        
        
        pc_options()
    x = 0
    y = 1
    print('--------------------')
    print()
    print('What do you want to withdraw?')
    while x < len(pc_storage):
        print(str(y) + '). ' + '['+ pc_storage[x] + ']')
        x = x + 1
        y = y + 1
    print()
    print('--------------------')
    withdraw_choice = input('')
    if withdraw_choice == '1':
            global item1
            item1 = pc_storage[0]
            bag.append(item1)
            pc_storage.pop(0)
            print()
            print('Withdrew ' + bag[0] + '.')
            enter = input()
            bedroom_choices()






def pc_deposit():
    '''Deposits items into the pc.'''
    if bag == []:
        print()
        print('Your bag is empty!')
        enter = input()
        
        pc_options()
    x = 0
    y = 1
    print('--------------------')
    print()
    print('What do you want to deposit?')
    while x < len(bag):
        print(str(y) + '). ' + '['+ bag[x] + ']')
        x = x + 1
        y = y + 1
    print()
    print('--------------------')
    deposit_choice = input('')
    if deposit_choice == '1':
        item1 = bag[0]
        pc_storage.append(item1)
        bag.pop(0)
        print()
        print('Deposited ' + pc_storage[0] + '.')
        enter = input()
        bedroom_choices()















def menu_pokemon():  #expand on this to view pkmn summaries/details
    '''Prints all pokemon currently in user party.'''
    if pokemon_team == []:
        print('You have no POKEMON in your team.')
        enter = input()
    print()
    print('Pokemon: ')
    print('--------------------')
    x = 0
    y = 1
    while x < len(pokemon_team):
        print(str(y) + '). ' + '['+ pokemon_team[x] + ']')
        x = x + 1
        y = y + 1
    print()
    print('--------------------')
    print()
    enter = input()






def menu_item():
    '''prints items in bag.'''
    print()
    x = 0
    y = 1
    while x < len(bag):
        print(str(y) + '). ' + '['+ bag[x] + ']')
        x = x + 1
        y = y + 1
    print()
    print('--------------------')
    enter = input()






    

def player_menu():  # gets stuck in a loop for some reason. Also loops this menu when going back upstairs.
    print('''
 _______________
| 1). [Pokemon] |
| 2). [Item]    |
| 3). [Save]    |
| 4). [Option]  |
| 5). [Exit]    |
|_______________|    ''')

    menu_input = input('')
    if menu_input == '1':
        menu_pokemon()  #expand on this to view pkmn summaries 
        player_menu()

    if menu_input == '2':
        menu_item()
        player_menu()

    if menu_input == '3':
        save_game()
        player_menu()

    if menu_input == '4':
        option_menu()
        player_menu()  # <----- this could be the issue

    
        
        
    
        




def save_game():
    print()
    print('''
__________________________________''')
    print('PLAYER   ' + player_name)
    print()
    print('BADGES    0')
    print()
    print('POKEDEX   0')
    print('''__________________________________''')
    sleep(0.5)
    print_typing_medium('Would you like to SAVE the game?')
    print('''
 _________
| 1). YES |   
| 2). NO  |
|_________|   ''')
    save_choice = input('')
    if save_choice == '1':
        sleep(0.3)
        print_typing_medium('Now Saving...')
        sleep(1.0)
        print_typing_medium(player_name + ' saved the game!')
        enter = input()
        player_menu()
        
        

def house_downstairs():
    print_typing_extreme('---------------------------------------------------------------------')
    print()
    print('You are downstairs.')
    enter = input()
    print('''
░░░░░░░░▓▌░░░░░░░░▓░░░░░░░░░░▐██▓▓▓▓██▌░░░░░░░░░░▐██▓▓▓▓▓█▌░░░░░░░░░░▐██▓▓▓▓▓█▌
░░░░░░░░█▌░░░░░░░░█░░░░░░░░░░▐██▓╬╬╬█▓▌░░░░░░░░░░▐██▓╬╬╬▓█▌░░░░░░░░░░▐██▓╬╬╬▓█▌
▄▄▄▄▄▄▄▄█▌▄▄▄▄▄▄▄▄█░░░░░░░░░░▐██▓▓▓▓██▌░░░░░░░░░░▐██▓▓▓▓██▌░░░░░░░░░░▐██▓▓▓▓▓█▌
██▐▌▌▐▌▓█▌█▐▓▌▌▐▌▓█░░░░░░░░░░░▀▀▀▀▀▀▀▀░░░░░░░░░░░░▀▀▀▀▀▀▀▀▀░░░░░░░░░░░▀▀▀▀▀▀▀▀▀
▓█▓▓███▌█▌▓█▓▓███▌█░    ░    ░╥▄▄▄▄▄▄▄░░    ░    ░    ░    ░    ░           ░▄▄
 ▒▓▓ █ ▓█▌▓░▓█ ▓ ▓█          ▓▀▀▀▀▀▀▀▀▓                                 ╓▄▓▌█▀▓
▓██████▌█▌▓██████▌█          █▓▀▀▀▀▀▀▓╟                              ░▒██▓▌ █▄▓
░░░█▌░░░█▌░░░█▌░░░█          ██░░░░░░█╟                              █▀█╓▐▓▌█▀▓
▓▓▓██▓▓▓██▓▓▓██▓▓▓█          ▓▓█▓▓▓▓█▓▓                              ▓░███▌▒░▄▐
 
   
                                ┌▄▄▄▄┌
                               ╓█░░░░▓▄                                     
                              ▐▓▌└▌▐▌▐▓▌
                              ▐▓██████▀╗
                               ╙▌▓▓▓▓▓▀

                                                    ▄████╗╖
                              ▄▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀╟ ▓▌║▀████
                     ╓▄▄▄▄▄▄  ▌░░░░░░░░░╓▄░░░░░░░╟ ░█▒╔████▀
                     ▓ ░░░░ █ ▌░░░░░░▄╦▄▄░▄▓░░░░░╟ █ █▌█▀╙█
                     ▓╓▄▄▄▄╖█ ▌░░░░░▀▄▀╚▀▀█▓░░░░░╟ █╖▓███▓▓
                     ▓▓░▒░░██ ▌░░░░░░░╙▄▄▓░░░░░░░╟ ▀▓╜▒░░██
                              ▌░░░░░░░░░░░░░░░░░░╟
                     ▄▀▀▀▀▀▀▓ █░░░░░░░░░░░░░░░░░░█─▄▀▀▀▀▀▀▓
                     ▓ ░░░░ █ ▓███████████████████ █  ░░░ ▓
                     ▓▐▀▀▀▀▌█ ▐▌▄█▀▀▀▀▀▀▀▀▀▀▀▀█▄▄▌ █▐▀▀▀▀█▓
                     ╙▀  ░ ▀╙                       ▀  ░ ▀▀

 
                                                                        

                    ░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
                    ░░░░░░░░░░░░░░░░░░░░
                    ░░░░░░░░░░░░░░░░░░░░
                    ░░░░░░░░░░░░░░░░░░░░                                                    ''')

    downstairs_choices()
    

def downstairs_choices():
    print()
    print('What would you like to do?')
    sleep(0.5)
    print('''
 ______________________
| 1). [Check TV]       |
| 2). [Check books]    |
| 3). [Talk to Mom]    |
| 4). [Go upstairs]    |
| 5). [Go outside]     |
| 6). [Menu]           |
|______________________|    ''')
    
    choice = input('')

    if choice == '1':
       print_typing_medium('There\'s a movie on TV.')
       enter = input()
       print_typing_medium('Four boys are walking on railroad tracks.')
       enter = input()
       print_typing_medium('I better go too.')
       enter = input()
       downstairs_choices()
       





        
        
        
    elif choice == '2':
        print_typing_medium('Crammed full of POKEMON books!')
        enter = input()
        downstairs_choices()
        
        
        
    elif choice == '3':
        print_typing_medium('MOM: ')
        sleep(0.3)
        print_typing_medium('All boys leave home some day.')
        enter = input()
        print_typing_medium('it said so on TV.')
        enter = input()
        sleep(0.4)
        print_typing_medium('PROF. OAK, next door, is looking for you.')
        enter = input()
        downstairs_choices()
        
        

    elif choice == '4':
        print('Going upstairs...')  
        sleep(1.0)
        house_upstairs()


    elif choice == '5':
        print('Going outside...')
        pallet_town()


    elif choice == '6':
        player_menu()
        downstairs_choices()
        








        
        
        
    






def pallet_town():   #not printing town out right for some reason, fix later 
    print_typing_extreme('---------------------------------------------------------------------')
    print()
    print('You are downstairs.')
    enter = input()
    print('''
























 

   ▄▒▀░░░░░░░░░░░░░░░░░░▀▄▄                                        ▄▄▒▀░░░░░░░░
▄░▀ ░░ ░░░░░░░░░░░░░░░░░░  ░ ▀▒▄                                ▄▄▀░░ ░░░░░░░░░░
 ░░ ░░ ░░░░░░░░░░░░░░░░░░  ░  ░▐                                ▓░ ░░ ░░░░░░░░░░
 ░░ ▄▓▓▓▓▓▓▀▀▀▀▀▓▓▓▀▓▓▓▓▓▓▄▄░ ░▐                                ▓░ ░▄▄▓▓▀▓▓▓▀▀▀▀
▌▓▓▀░░ ▐▌ ░▓   ▐▌ ░█▌ ░▓  ░▀▀▓▓█                                ▓▓▓▓▀░░ ▓ ░▐
 █▌ ▒  ░▀▀▀░   ░▀▀▀░░▀▀░▒  ░ ▐▌                                  ▐▌ ░   ░▀▀▀░
 █▌▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▌                                  ▐█▄▄▄▄▄▄▄▄▄▄▄▄▄
░░█     ░▓▓▓▓▓▓░▓▀▀▓▓▀▀▓     ▌░                         ▐▓▓▀▀▓▓▓ ░▐     ░▓▓▓▓▓▓░
░░█      ▓▌  ▓▓▐▌▄░█▌▄░▓     ▌░                         ▌░   ░ █░░▐     ░█▓  ▐▓
░░█ ░░░░ ▌░░░▀█░░░░░░░░░░░░░ ▌░                         ▌▄▄▄▄▄▄█░░▐░░░░░░█░░░▀▓
░░▀▀▀▀▀▒▄▀▀▀▀▀▀▄▀▀▀▀▀▀▀▀▀▀▀▀▀░░                             ░░▓▐░░░▀▀▀▀▀▄▀░▀▀▀▀▄


                                  ▄▄▄▄
                                 █▄▄▄▄█
                                ▐█▄▌▐▄█
                                 ▓▓███▌
                                                     ▄▄▒▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
                                                 ▄▄▀░  ░░░░░▒░░░░░░░▒░░░░░░░▒░░░
                                                ▌░  ░  ░░░░░▒░░░▒░░░▒░░░▒░░░▒░░░
                                                ▌░  ░  ░░░░░░░░░░░░░░░░░░░░░░░░░
▄██ ▄██ ▄██ ▄██ ▄██ ▄██▄▓█▓▓▓▓▓█                ▌░  ░  ░▒░░▒░░░▒▒░░░░░ ▒░░ ░░░ ░
▓░▐ ▓░▐▌▓░▐▌▓░░▌▓░░▌▓░░▌▌      █                ▌░  ░  ░░▒▒░░░▒░░▒░░░░░░░░░░░░░░
▓ ▐ ▓ ▐▌▓ ▐ ▓ ░▌▓ ░▌▓ ░▌▀▀▀▀▒▒▌█                ▌░  ░  ░▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
                           ░  ▀▀                ▌░ ░▄▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▀▀▀▀▀▀▀▀▀▓▓▓
░░ ░░░ ░░░ ░ ░ ░░░ ░ ░ ░ ░ ░ ░ ░                █▓▓▀░░  ▌ ░▐▌ ░▐▌ ░▐░       ▓ ░▐        
░ ░░    ░ ░░      ░░      ░░                     ░▓      ▀▀  ▀▀ ░░░░ ░░  ░░ ░░░░
░░ ░ ░░░░░ ░ ░░░ ░ ░░░░░ ░ ░░▒░░                 ░▐
      ░░      ░░      ░░    ░ ░░                 ░▐ ▄▀▀▐▄▀▀▐▄▀▀▐░▓▒▓▓▒▐░▄▀▀▒▄▀▀▐
░░░  ░ ░░░░  ░ ░ ░▒  ░ ░ ░▒  ░ ░                 ░▐ ▌▄▄▓▌▄▄▐▌▄▄▐ ▓▌  ▐▓░▓▄▄▐█▄▄▐
░ ░░░ ░ ░ ░░░ ░ ░ ░░░ ░ ░ ░   ░░                 ░▐ ░░░░░░░░░░░░░▓░░░░▓░░░░░░░░░
                                                  ▒ ▀▀▀▀▀▀▀▀▀▀▀▀▀ ▀▀▀▀▀▀ ▀▀▀▀    
                                                                                                 ''')
    pallet_town_choices()



def pallet_town_choices():
    print()
    print('What would you like to do?')
    sleep(0.5)
    print('''
 _________________________ ''')
    print('|1). [Your house]         |')
    print('|2). [' + rival_name + '\'s house]       |')
    print('|3). [Oak\'s lab]          |')
    print('|4). [Route 1]            |')
    print('|5). [Talk to girl]       |')
    print('|6). [Talk to man]        | ')
    print('|7). [Menu]               |')
    print('''|_________________________|    ''')
    choice = input('')

    if choice == '1':
        print('Going to ' + player_name + '\'s home...')
        sleep(0.5)
        house_downstairs()


    elif choice == '2':
        print('Going to ' + rival_name +'\'s home...')
        #rival_home()   <---- make rival's home, upstairs and downstairs

    elif choice == '3':
        print('Going to Oak\'s lab...')
        #oak_lab() <------- make oak's lab 

    elif choice == '4':
        print('Going to Route 1...')
        #route_1() <---- Make route 1 

    elif choice == '5':
        print()
        print('GIRL:')
        
        print_typing_medium('I\'m raising POKEMON too!')
        enter = input()
        print_typing_medium('When they get strong, they can protect me!')
        enter = input()
        pallet_town()

    elif choice == '6':
        print()
        print('MAN: ')
        
        print_typing_medium('Technology is incredible!')
        enter = input()
        print_typing_medium('You can now store and recall items')
        enter = input()
        print_typing_medium('and POKEMON as data via PC!')
        enter = input()
        pallet_town()

    elif choice == '7':
        player_menu()
        pallet_town()

    else:
        print('Try again')
        enter = input()
        pallet_town()
    







def rival_home():
    print('---------------------------------------------------------------------')
    print()
    print('You are in ' + rival_name + '\'s home. ')
    enter = input()
    print('''
▓▓█▓█▓▓▓▓█▓▓█▓█▓▓▓▓▒                                                 ▐▌██▓▓▓▓▓▌█
█▄█▄█▄▄█▓██▄█▄█▄▄█▐░                                                 ▐▌▌███▌▐█▌█
▒▒▒██▒▒▒▓█▒▒▒▓█▒▒▒▐▒                                                 ▐▌▓▓▓█▓▓▓▒█
░▄▄██▄▄░██░▄▄▓█░▄░▓                                                  ▐▌░▄░█▌▄▄░█
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀                                                  ░▀▀▀▀▀▀▀▀▀▀
                                                                               
                                                                               
                                                                               
                     ▄▒▀▀█▄░                                                   
                    ▐░░▐█▀░▓ ▄▌  ▀▀▀░ ▐▌▀▀▀▀▀▀▀▀▀▄                             
                    ▐░░▒  ▄▌ █▌   ░   ▐▌░░░░░░░░░▌ ▄▄▄▄▄▄▄                     
                    ▐░▄▓██ █ █▌▄▄▄░▄▄▄▐▌░░░░░░░░░▌▐▌ ░░░ ▐▌                    
                    ▐▒████▄█ ▓░░░░░░░░░░░░░░░░░░░▌▐▌▄▄▄▄▄▐▌                    
                    ▐▓▌░░░██ ▓░░░░░░░░░░░░░░░░░░░▌▐▓▌░░░▓▓▌                    
                             ▓░░░░░░░░░░░░░░░░░░░▌                             
                    ▄▀▀▀▀▀▀▓ ▓░░░░░░░░░░░░░░░░░░░▌ ▓▀▀▀▀▀▓                      
                    ▐  ░░░ █ ▀▓█▓████████████▓▓█▓▌▐▌ ░░░ ▐▌                     
                    ▐▓▌▀▀▀██  ▌░▓▀▀▀▓▀▀▀▀▀▀▀▀▓▌░█ ▐▌█▀▀▀█▐▌                     
                     ▀  ░ ▀▀  ▐█░░░░▄█             ▀▀  ░▀▀                      
                              ▓▓▀████▄▀                                         
                             ░▓██▀▀▓█▌▓                                         
                               ▀▓▓▀▓▓▀                                          
                                                                                

▓▀▄▄▄▄▀▓▄                                                             ▓▓▓▄ ▄▄▀▓▄
▓░▄▓▓░▒▓▓                                                             ▓▌░▄▓▄▒▒▓▓
▀▌░░▒░▐▓▓                                                            ▐█▓▒░░▓░▓▓▓
▒▄▒██░▄▒█                                                            ▐▓░▄▐██▒▄▒█
▀  ▓▓▀ ▀▀                                                              ▀  ▓█▀ ▀▒
 ▄▄▌▐█▄            ░░░░░░░░░░░░░░░░░░░░                                 ▄▓░▓▄▄  
▓▐█▄░█▌▓           ░░░░░░░░░░░░░░░░░░░░░                               ▌██░▄█▒▌ 
▀▌▄▄▄▄▐▀           ░░░░░░░░░░░░░░░░░░░░                                ▓▒▄▄▄░▓▀ 
 ▀▄▄▄▄▀            ░░░░░░░░░░░░░░░░░░░░░                                ▀▄▄▄▓▀         ''')
    
























    
start_game()

