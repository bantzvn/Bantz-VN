
label autistic_balt:
    scene bg eestiBG

    "You wake up in a frozen wasteland"

    "You don't know what the fuck is going on"
    
    show eesti normal
    
    e "Welcome to Estonia!"

    e "Haha now you are stuck in Estonia!!"
    
    "You want to die"
    
    e "Now, before we go any further, which is the most autistic balt?"
    
    menu:
        "Estonia":
            jump estonia_pissed
            
        "Latvia":
            jump latvia_correct
            
        "Lithuania":
            jump lithuania_gunshot
    
    label estonia_pissed:
        show eesti mad
        hide eesti
        hide bg
        "You are kill"
        return
    
    label latvia_correct:
        e "Right answer!"
        return
        
    label lithuania_gunshot:
        e "Oh no, now you've done it"
        "You hear a gunshot in the distance"
        
    return
