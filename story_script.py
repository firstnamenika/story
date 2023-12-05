import os 
import time
import sys




class Shadow:
    def __init__(self):

      pass

    def appears(self):
       print_with_some_delay("\nYou hear something.")
       one_sec_delay()
       print_with_delay("""A shadow manifests as an inky silhouette, 
             dense and formless, hovering ominously.""")
       print_with_delay("\nDoes it want to hurt you?")
       two_sec_delay()
       print_with_delay("""\nAmbiguous, the shadow leaves you unsure whether 
             it harbors benevolence or malevolence.""")
    
    def scares(self):
       #for when you enter the room and you maybe can choose to run away
       #but the shadow doesnt actually fight, it only scares
       print_with_delay("""The shadow twists into ominous shapes, 
             whispering chilling echoes that play on your deepest fears,
                 paralyzing everything within.""")

    def closeShadowSounds(self):
       #something for when you see the shadow
       print_with_delay("""--------redo--------.""")
       print_with_much_delay("{name}".format(name=name))
       one_sec_delay()
       print_with_much_delay("{name}".format(name=name))
    
    def distantShadowSounds(self):
       #something for when youre in the camera scene, but still feel the shadow
       print_with_delay("""Suddenly, a guttural whisper, 
             as if emanating from the very darkness itself, reached your ears.""")
       one_sec_delay()
       print_with_delay("Are those sounds of the Shadow?")
   
      
class Skeleton:
   
    def __init__(self):
       pass
    
    def appears(self):
      print_with_delay("""Amidst the shadows, two skeletal figures emerge, 
                       their hollow sockets fixating on you. With a sudden lurch, 
                       they close in, unleashing a cascade of ghostly whispers, 
                       chilling the air around them.""")
   

    def makes_sound(self):
      print_with_delay("""The air is pierced by chilling echoes of bone-rustling 
                       and chilling, sinister laughter.""")
    
    def distant_sounds(self):
      print_with_delay("\nSuddenly you hear a haunting wail, echoing through the desolate night..")
    

class StrangeCreature:
    def __init__(self):
       pass
    
    def appears(self):
      print_with_delay("Abruptly, a bizarre creature materializes, its hostile stance suggesting an imminent confrontation.")
   
    def makes_sound(self):
      print_with_delay("\nYou hear Strange Creature explode with visceral roars!")
   
    def fights(self):
      print_with_some_delay("\nIt makes a leap toward you, exuding a formidable presence.")
   
    def distant_groans(self):
      print_with_delay("""Dreadful moans echo from distant Creature, 
                       haunting the surroundings with ghoulish wails.""")

shadow1 = Shadow()
skeleton1 = Skeleton()
skeleton2 = Skeleton()
strange_creature = StrangeCreature()


# ----printing and delay functions------
def print_with_delay(text, delay=0.05):
   for char in text:
      print(char, end='', flush=True)
      time.sleep(delay)
   print(end='\n')  

def print_with_some_delay(text, delay=0.1):
   for char in text:
      print(char, end='', flush=True)
      time.sleep(delay)
   print(end='\n\n')  

def print_with_some_delay_no_br(text, delay=0.1):
   for char in text:
      print(char, end='', flush=True)
      time.sleep(delay)

def print_with_much_delay(text, delay=0.3):
   for char in text:
      print(char, end='', flush=True)
      time.sleep(delay)
   print(end='\n\n')   

def print_two_parts(text1, text2):
   #you still need to add new lines manually
   print_with_some_delay_no_br(text1)
   one_sec_delay()
   print_with_some_delay(text2)

def one_sec_delay():
   time.sleep(1)

def two_sec_delay():
   time.sleep(2)
#------------------------------------------

#---intro----------------------------------
def intro():

    print('\n\n\n\n\n\n')
    print_with_some_delay("What is happening?")
    one_sec_delay()
    print_with_much_delay("It is so dark here..")
    two_sec_delay()
    #------get name-------------------------------
    get_name()
    #----------------------------------------------
    one_sec_delay()
    print_with_delay("What is this place?\n")
    print_with_delay("You can choose to walk in multiple directions to find a way out.")
    #------intro scene--------------------------------
    introScene()

#---get name-------------------------------
def get_name():
    print_with_some_delay("Can you remember your name?")
    print("Enter your name: ", end="")
    one_sec_delay()
    name = input().title()
    print_with_some_delay("\nHello, {}".format(name))
 

#---introscene-----------------------------
def introScene():

    def intro_deadwall():
        print_with_delay("\nOh no, it is a dead end!")
        shadow1.closeShadowSounds() 
        print("\nTry again")
        one_sec_delay()
        introScene()
    
    def choice():
        print("\nleft, right, backward, forward\n\nEnter your choice: ", end="")
        user_input = input().lower().strip()
        valid_choices = ['left','l', 'right', 'r', 'b', 'backward', 'f', 'forward']
        other_choices = ['help', 'help me','sos']
        if user_input in valid_choices:
           
           if user_input == 'left' or user_input == 'l':
            show_shadow_figure()
   
           elif user_input == 'right' or user_input == 'r':
            show_skeletons()
   
           elif user_input == 'backward' or user_input == 'b':
            haunted_room()
            
   
           elif user_input == 'forward' or user_input == 'f':
            intro_deadwall()

        elif user_input in other_choices:
          print_with_delay("\nNo one will come for help. Where would you go?\n")
          skeleton2.distant_sounds()
          one_sec_delay()
          choice()

        else:
          print_with_delay("\nIt is too dark to see. Where would you go?")
          one_sec_delay()
          choice()
    
    one_sec_delay()
    skeleton1.distant_sounds()
    print_two_parts("\nTake a look around, ", "have you been here before?")
    strange_creature.distant_groans()
    one_sec_delay()
    print_with_delay("\n\nWhere should you go now?")   
    choice()

#---shadow figure--------------------------
def show_shadow_figure():
   
   def shadow_deadwall():
        print_with_delay("\nOh no, its a dead end!")
        one_sec_delay()
        shadow1.distantShadowSounds() 
        print("\nTry again before the Shadow consumes you.")    
        choice()   
   
   def runaway():
      print_with_delay("\nTry to run away?")
      one_sec_delay()
      print("\nyes, no\n\nEnter your choice: ", end="")
      user_input = input().lower().strip()
      valid_choices = ['yes','y','no', 'n']
      if user_input in valid_choices:
         if user_input == 'no' or user_input == 'n':
            print_with_delay("\nThe shadow pierces you with its empty stare.") 
            print_with_delay("\nBetter get going before it is too late.")           
            
         if user_input == 'yes' or user_input == 'y':
            print("Run!")
            one_sec_delay()
            print_with_some_delay("Run!")
            introScene()
      else:
         print_with_delay("No time for this!")
         shadow1.closeShadowSounds()
         one_sec_delay()
         runaway()  
   
   def choice():
      print("\nleft, back, right\n\nEnter your choice: ", end="")
      user_input = input().lower().strip()
      valid_choices = ['right', 'r', 'left', 'l', 'back', 'b']
      if user_input in valid_choices:
         if user_input == 'right' or user_input == 'r':
            cameraScene()

         if user_input == 'left' or user_input == 'l':
            shadow_deadwall()
            
         if user_input == 'back' or user_input == 'b':
            introScene()
      else:
         print("It is too dark too see. Where should you go next?")
         shadow1.closeShadowSounds()
         one_sec_delay()
         choice()   
      
   shadow1.appears()
   two_sec_delay()
   shadow1.scares()
   runaway()
   print_with_delay("\nRun! Where to next?")
   choice()

#---cameraScene----------------------------
def cameraScene():
   
   def choice():
      print("\nback, forward\n\nEnter your choice: ", end="")
      user_input = input().lower().strip()
      valid_choices = ['forward', 'f', 'b', 'back']
      if user_input in valid_choices:
         if user_input == 'forward' or user_input == 'f':
            print_with_delay("You follow the light, its gentle glow guiding you towards a sanctuary where shadows dissipate, and a new beginning awaits.")
            exit_game() 
            
         if user_input == 'back' or user_input == 'b':
            print_with_delay("You decide to go back..")
            shadow1.closeShadowSounds()
            show_shadow_figure()
      else:
         print("Maybe another time. Where should you go next?")
         one_sec_delay()
         choice()   
   
   print_with_delay("""
         You see light in the next room, a glimmer of hope piercing through 
         the menacing darkness, promising safety and solace in its warm embrace.
         """)
   shadow1.distantShadowSounds()
   print("\nRun! Where to next?")
   choice()

#---skeletons------------------------------
def show_skeletons():
   
   def skeleton_room_deadwall():
      
      def collect_weapon(): 
            print_with_delay("\n\nWould you like to collect the weapon?")
            print("\nEnter yes or no: ", end="")
            answer = input().lower().strip()
            if answer == 'yes' or answer == 'y':
               print_with_delay('\nYou have collected the weapon.\n')
               global weapon_count
               weapon_count += 1
            
            elif answer == 'no' or answer == 'n':
               print_with_delay("\nLet's leave this place!")
               return True
            
            else:
               collect_weapon()
   
      print_with_delay("\nOh no, it is a dead end!")
      one_sec_delay()  
      print_with_delay("\nAmidst the dust, a concealed weapon emerges, its significance elusive..")
      collect_weapon()
      skeleton2.distant_sounds() 
      print_with_delay("\nIt's the skeletons again.")  
      show_skeletons()            

   def choice():
      print("\nleft, back, forward\n\nEnter your choice: ", end="")
      user_input = input().lower().strip()
      valid_choices = ['forward', 'f', 'left', 'l', 'b', 'back']
      if user_input in valid_choices:
         if user_input == 'forward' or user_input == 'f':
            strange_creature.makes_sound()
            strange_creature_scene()
            
         if user_input == 'left' or user_input == 'l':
            skeleton_room_deadwall()
            
         if user_input == 'back' or user_input == 'b':
            print_with_some_delay("\nRun!")
            introScene()
      else:
         print_with_delay("\nIt is too dark too see. Where should you go next?")
         one_sec_delay()
         choice()
   
   skeleton1.appears()
   print_with_delay("\nRun! Where to next?")
   choice()

#---strange creature-----------------------
def strange_creature_scene():

    def check_weapon():
       if weapon_count == 0:
          print_with_delay("\nI do not think we've seen any weapons. What is going to happen?")

       else:
          print_with_some_delay("\nI have a weapon!")
          print_with_some_delay("I have a chance!")
    
    def fight_or_flee():
      print_with_delay("\nStart the fight or flee?")
      print("\nEnter fight or flee: ", end="")
      user_input = input().lower().strip()
      valid_choices = ['fight', 'fi', 'flee', 'fl']
      if user_input in valid_choices:
         if user_input == 'fight' or user_input == 'fi':
            fight()
         elif user_input == 'flee' or user_input == 'fl':
            print_with_delay("\nYou decide to flee the Creature.")
            show_skeletons()

      else:
         print_with_delay("Not sure what to do.")
         strange_creature.makes_sound()
         fight_or_flee()

    def fight():
           
           def fight_with_weapon():
              print_with_delay("\nYou get the weapon.")
              print_with_much_delay("\n \n \n y\n o\n\nu  \n\n a\n \nr\n e\n")
              print_with_much_delay("  \n    f \n      i\n      g    \n        h\n         t     \n          i\n           n\n               g")
              print_with_some_delay("\n\nYou won!")
              exit_game()
           
           if weapon_count == 0:
              print("\nsucks to be you")
              dead()
           
           else:
              fight_with_weapon()
              
    print_with_delay("\nSlowly you move forward.")
    print_with_some_delay("\nIn the moonlight-lit room, you encounter a bizarre creature, sending a shiver that chills to the core.")
    strange_creature.appears()
    print("\nWas there any weapon along the way?")
    #check if we found a weapon
    check_weapon()
    strange_creature.makes_sound()
    strange_creature.fights()
    fight_or_flee()
    
#---haunted room---------------------------
def haunted_room():

   def choice():
      print_with_delay("\nright, left, back\n")
      print("Enter your choice: ", end="")
      user_input = input().lower().strip()
      valid_choices = ['right', 'r', 'l', 'left', 'b', 'back']
      if user_input in valid_choices:
         if user_input == 'right' or user_input == 'r':
            print_with_delay("\nFinally, a way out!")
            print_two_parts("\nYou found a hole in the crumbling wall ", "and escaped quietly.\n")
            exit_game()
            
         elif user_input == 'left' or user_input == 'l':
            print_with_some_delay("\nErrant turn.")
            print_with_delay("\nYou are swarmed by hungry snakes.")
            dead()
            
         elif user_input == 'back' or user_input == 'b':
            introScene()
      else:
         print("Snakes are everywhere! Where should you go next?")
         one_sec_delay()
         choice()   

   print_with_some_delay("\nYou walk into a desolate, shattered room, snakes slither in the gloom.")
   one_sec_delay()
   print_with_some_delay("Snakes start crawling in your direction.")
   print_with_delay("\nBetter get out of here!")
   choice()


#---exits----------------------------------
def dead():
   print("\nyou're dead")
   exit_game()

def exit_alive():
   print("youve found the exit")
   print_with_some_delay("Congratulations!")  
   exit_game()

def exit_game():
   print_with_much_delay("\nGame over") 
   print_two_parts("\nWould you ", "like to restart?\n")

   return True
#------------------------------------------
   

   

if __name__ == "__main__":
  while True:
   try:
      weapon_count = 0
      intro()



    
       