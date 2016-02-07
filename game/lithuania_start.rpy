label lithuania_start:
    scene bg lithuaniaBG
    
    "You wake up in a comfy autumn field"
    
    "There's a rustle in the bushes behind you"
    
    show lithuania normal
    
    l "Oh... Oh! Hello!"
    l "S-sorry, did I startle you?"
    "You shake your head"
    l "Okay, good, haha.."
    l "You're foreigner, yes?"
    "You nod, not sure why this person is talking to you"
    l "I'm Lithuania, pleasure to meet you..."
    "You try to give her your best smile, but she's really weirding you out so it turns into a sort of confused grimace"
    l "Or maybe it's not pleasure, maybe I'm a bother..."
    l "I'm bother aren't I?"
    l "Should just kill self right? Haha...ha..."
    menu:
        "Might as well":
            jump lithuania_yes
            
        "What?":
            jump lithuania_what
            
        "No, stop":
            jump lithuania_stop
            
    label lithuania_yes:
        l "O-okay! H-here I go!"
        hide lithuania
        "She pulls out a gun and shoots herself before you have time to react."
        "Good job, jerk"
        return
    label lithuania_what:
        l "Kill myself, you know? If I'm a bother I should just kill myself, right?"
        p "No, stop this nonsense about killing yourself!"
        jump lithuania_stop
    label lithuania_stop:
        l "Oh, sorry, I'm not used to foreigners"
        l "So I should not kill self, yes?"
        p "Yes, not kill self. I'd rather have you alive."
        l "You are very strange."
        l "What is your name?"
        menu:
            "ur mum x-DD":
                $ playername = "ur mum x-DD"
            "Anon":
                $ playername = "Anon"
            ":DDDDDDDDDDDDD":
                $ playername = ":DDDDDDDDDDDDD"
        l "Nice to meet you, [playername]"
   
    p "Nice to meet you too, Latvia."
    l "Nice hehe... nice to meet me..."
    p "What?"
    l "Nothing! Just very weird..."
    l "Just wondering...do you like krepšinis?"
    menu:
        "Krepšinis?":
            jump krepsinis
        "I love crepes!":
            jump crepes
        "\"kill self\" doesn't sound that bad to be honest...":
            l "Y-yes, you're right, sorry"
            jump lithania_yes
    
    label krepsinis:
        l "Oh sorry! Basketball! Like basketball?"
    label crepes:
        l "No! Krepšinis! Basketball!!"
        
    l "Do you want to play?"
    p "Yeah sure, I'll play some basketball."
    
    scene bg basketballBG
    show lithuania normal
    "You go to a nearby krepšinis court"
    
    "You played basketball with Lithuania for a while."
    "Turns out she was much better than you, but you don't really mind since she seems so happy"
    l "Triple! I've never had so much fun! Especially not with foreigner..."
    "You check 'em"
    p "Can you make a half-court shot?"
    l "Yes, yes! Look!"
    "Lithuania makes a perfect shot from half-court"
    p "Wow, I never knew Lithuanians were that good at basketball..."
    l "Please don't...don't call me good, I am not good..."
    p "That was pretty impressive, I'm pretty sure you're great."
    l "I don't...I don't think..."
    p "You're really wonderful."
    l "I... I... You're just saying that because you're refugee! No way you like Lithuania!"
    p "Sorry, I think you're wonderful...."
    l "Prove It!"
    l "G-Give kiss..."
    l "Just one..."
    "Lithuania offs herself out of nowhere :DD"
return