## Characters
define sa = Character("Sanjana")
define sh = Character("Shivani")
define v = Character("Vaibhavi")
define r = Character("Riya")
# Define User character after username is input
define User = Character("", dynamic=True)

# Character Images
image sanjana = im.Scale("images/characters/sanjana.png", 500, 800)
image shivani = im.Scale("images/characters/shivani.png", 500, 800)
image vaibhavi = im.Scale("images/characters/vaibhavi.png", 500, 800)
image riya = im.Scale("images/characters/riya.png", 500, 800)

# Background Images
image title_screen = "images/bg/titlescreenbg.png"
image black_bg = "images/bg/blackbg.png"
image outside_bg = "images/bg/outsidebg.png"
image python_bg = "images/bg/pythonbg.png"
image c_bg = "images/bg/cbg.png"
image hallway_bg = "images/bg/hallwaybg.png"

# Fonts
define gui.text_font = "fonts/Poppins/Poppins-Regular.ttf"
define gui.name_text_font = "fonts/Poppins/Poppins-Bold.ttf"
define gui.interface_text_font = "fonts/Poppins/Poppins-SemiBold.ttf"
define gui.bold_font = "fonts/Poppins/Poppins-Bold.ttf"
define gui.text_size = 30

#### Start Screens ####
label start:
    scene title_screen
    # Language Selection
    menu:
        "English":
            $ _preferences.language = None
        "Hindi":
            $ _preferences.language = "hi"

    # Ask user to enter their name, ensure it's not empty
    $ username = ""
    while not username:
        $ username = renpy.input("Please enter your name:")
        $ username = username.strip()  # Remove trailing whitespace
    # Define User character with entered username
    $ User = Character(username)

    jump script_ch1

#### Part 1 ####

label script_ch1:

    scene outside_bg with dissolve

    User "It is my first day at CodeVortex Academy."

    User "I feel excited I walk closer and closer to the entrance."

    User "I came here for a reason - to learn about computers, their working, and coding - an activity that has been a part of my bucket list for a long time."

    scene hallway_bg with dissolve

    show shivani with dissolve

    User "A girl with long black hair tied back in a ponytail approaches me. I make eye contact with her, smiling, trying to be as friendly as possible."

    sh "Oh hello there, you must be [username]. I'm Shivani. Welcome to CodeVortex. We are delighted about having you here."

    User "Ah yes, that's me. [username]. Thank you, Shivani. It's nice to meet you. I'm eager to start learning here."

    sh "So you've signed up to learn here at CodeVortex in the evening shift. You will need to be here every evening, from 5 p.m. to 8.m."

    User "I understand."

    sh "Now let me walk you through your responsibilities as a student here."

    sh "Your duties will include being punctual for all classes, submitting all assignments, and also...making friends!"

    sh "You must also start with the basics of concepts and progress through all the modules we have to offer."

    sh "Is all this clear, [username]?"

    User "Yes, absolutely. Thank you, Shivani. I'm eager to start learning here."

    sh "You already said that, aha."

    sh "Now...without wasting any time, let me guide you through our first course...Basic Computer Architecture."

    sh "In this course, you will learn about the achitecture of a computer system, the components, and the processes which take place within a computer."

    User "That sounds great! Now where do we have to -"

    scene black_bg with fade

    jump script_ch2

return
