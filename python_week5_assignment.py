# Assignment 1: Design Your Own Class!
class Smartphone:
   def __init__(self, ringtone, screen_size, battery_life):
      self.ringtone = ringtone
      self.screen_size = screen_size
      self.__battery_life = battery_life # private attribute
      
   screen = "touchable"
   
   def scroll(self):
      print("Scrolling...")
   def tap(self):
      print("Tapping...")
   def swipe(self):
      print("Swiping...")
      
   def play_ringtone(self):
      print(f"Playing ringtone: {self.ringtone}")
   def display_screen_size(self):
      print(f"Screen size: {self.screen_size} inches")

   def set_battery_life(self, hours):
       self.__battery_life = hours
   def display_battery_life(self):
      print(f"Battery life: {self.__battery_life} hours")
   
class Basic_phone(Smartphone):
   def __init__(self, ringtone, screen_size, battery_life, call_duration):
      super().__init__(ringtone, screen_size, battery_life)
      self.call_duration = call_duration
   
my_phone = Basic_phone("default ringtone", 6, 24, 2)
my_phone.__battery_life = 16 # This will not change the private attribute
my_phone.display_battery_life()
print(my_phone.screen)
my_phone.play_ringtone()
my_phone.display_screen_size()
my_phone.scroll()
my_phone.tap()
my_phone.swipe()
my_phone.set_battery_life(16) # This will change the private attribute
my_phone.display_battery_life()
my_phone.call_duration = 3 # This will change the public attribute
print(my_phone.call_duration)

# Activity 2: Polymorphism Challenge!
class Animal:
   def __init__(self, sound, movement):
      self.sound = sound
      self.movement = movement
      
   def speak(self):
      print(f" sound: {self.sound}")
   def move(self):
      print(f" movement: {self.movement}")

bird = Animal("chirp", "fly")
lion = Animal("roar", "walk")
fish = Animal("blub", "swim")

bird.speak()
lion.speak()
fish.speak()
bird.move()
lion.move()
fish.move()
