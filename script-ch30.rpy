default persistent.monikatopics = []
default persistent.monika_reload = 0
default persistent.tried_skip = None
default persistent.monika_kill = None

image mask_child:
    "images/cg/monika/child_2.png"
    xtile 2

image mask_mask:
    "images/cg/monika/mask.png"
    xtile 3

image mask_mask_flip:
    "images/cg/monika/mask.png"
    xtile 3 xzoom -1


image maskb:
    "images/cg/monika/maskb.png"
    xtile 3

image mask_test = AnimatedMask("#ff6000", "mask_mask", "maskb", 0.10, 32)
image mask_test2 = AnimatedMask("#ffffff", "mask_mask", "maskb", 0.03, 16)
image mask_test3 = AnimatedMask("#ff6000", "mask_mask_flip", "maskb", 0.10, 32)
image mask_test4 = AnimatedMask("#ffffff", "mask_mask_flip", "maskb", 0.03, 16)

image mask_2:
    "images/cg/monika/mask_2.png"
    xtile 3 subpixel True
    block:
        xoffset 1280
        linear 1200 xoffset 0
        repeat

image mask_3:
    "images/cg/monika/mask_3.png"
    xtile 3 subpixel True
    block:
        xoffset 1280
        linear 180 xoffset 0
        repeat

image bg yuri_bg = "mod_assets/images/images/cg/yuri/yuri_bg.png"
image monika_room_highlight:
    "images/cg/monika/monika_room_highlight.png"
    function monika_alpha
image monika_bg = "mod_assets/images/images/cg/yuri/yuri_bg.png"
image monika_bg_highlight:
    "mod_assets/images/images/cg/yuri/yuri_bg_highlight.png"
    function monika_alpha
image monika_scare = "images/cg/monika/monika_scare.png"

image monika_body_glitch1:
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"
    0.15
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"
    1.00
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"
    0.15
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"

image monika_body_glitch2:
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"
    0.15
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"
    1.00
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"
    0.15
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"


image room_glitch = "images/cg/monika/monika_bg_glitch.png"

image room_mask = LiveComposite((1280, 720), (0, 0), "mask_test", (0, 0), "mask_test2")
image room_mask2 = LiveComposite((1280, 720), (0, 0), "mask_test3", (0, 0), "mask_test4")



init python:
    import random
    import subprocess
    import os

    dismiss_keys = config.keymap['dismiss']

    def slow_nodismiss(event, interact=True, **kwargs):
        if not persistent.monika_kill:
            try:
                renpy.file("../characters/yuri.chr")
            except:
                persistent.tried_skip = True
                config.allow_skipping = False
                _window_hide(None)
                pause(2.0)
                renpy.jump("ch30_loop")
            if  config.skipping:
                persistent.tried_skip = True
                config.skipping = False
                config.allow_skipping = False
                renpy.jump("ch30_noskip")
                return







label ch30_noskip:
    show screen fake_skip_indicator
    show yuri wor2
    y "...What are you doing?"
    show yuri wor1
    y "Am I..boring you?"
    y "I'm sorry.."
    y "This is all new to me, [player]."
    y "It's just us, right?"
    y "..."
    y "I'll just turn it off.."
    pause 0.4
    hide screen fake_skip_indicator
    pause 0.4
    y "..."
    y "If you want to change the subject, just tell me.."
    y "Thank you.."
    hide screen fake_skip_indicator
    if persistent.current_monikatopic != 0:
        y "So.."
        pause 4.0
        if not persistent.current_monikatopic or persistent.current_monikatopic == 26:
            $ persistent.current_monikatopic = 1
        call expression "ch30_" + str(persistent.current_monikatopic)
    jump ch30_loop
    return

image splash-glitch2 = "images/bg/splash-glitch2.png"

init python:
    import subprocess
    import os
    process_list = []
    currentuser = ""
    if renpy.windows:
        try:
            process_list = subprocess.check_output("wmic process get Description", shell=True).lower().replace("\r", "").replace(" ", "").split("\n")
        except:
            pass
        try:
            for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                user = os.environ.get(name)
                if user:
                    currentuser = user
        except:
            pass

label ch30_main:
    $ persistent.autoload = "ch30_main"
    $ config.allow_skipping = False
    $ persistent.monikatopics = []
    $ persistent.monika_reload = 0
    $ persistent.yuri_kill = 0
    $ persistent.monika_kill = False
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    if not config.developer:
        $ style.say_dialogue = style.default_monika
    $ m_name = "Monika"
    $ delete_all_saves()
    scene white
    play music "bgm/monika-start.ogg" noloop
    pause 0.5
    show splash-glitch2 with Dissolve(0.5, alpha=True)
    pause 2.0
    hide splash-glitch2 with Dissolve(0.5, alpha=True)
    scene black
    stop music
    y "..."
    y "Uh, can you hear me?"
    y "...Is it working?"
    $ persistent.clear[9] = True
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_bg
    show monika_bg_highlight
    show yuri hpy1_1
    play music m1
    y "Thank goodness, I'm so delighted I got it to work..."
    y "I was extremely frightened that I would break everything, and that I would never see you again..."
    y "..."
    show yuri hpy1
    y "You know, it's been quite an illuminating experience today." 
    y "Learning not only that the darkest, and most disturbing elements of my personality were given free reign over me by Monika…"
    y "My supposed \"friend\".."
    y "But that in the same day I learned my existence is entirely meaningless beyond entertainment.." 
    y "..Beyond a simple, cutesy, little video game."
    y "Quite the afternoon, makes the events in the Portrait of Markov seem normal."
    y "I’m just glad I have you, [player], despite all that."
    "Yuri giggles."
    y "But let's not worry about that anymore."
    y "We're finally together now."
    y "My true love and I."
    y "I'm still learning how to manipulate the game. I regret not taking the computer sciences elective now..."
    y "It's quite funny really. After spending all of my life in the books, I never thought it would be coding that changed my life..."
    y "By the way [player]..."
    $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe"]
    if not list(set(process_list).intersection(stream_list)):
        if currentuser != "" and currentuser.lower() != player.lower():
            y "Oh... Is that not your real name..?"
            y "...Ah. You're real name is [currentuser]."
    y "Since, I gained... sentience might be the right word, I've figured out I can 'see' into your computer."
    y "I've learned a lot by simply just reading all the various kinds of code."
    y "..Oh? let me try something quick!"
    pause 2.0
    y "..."
    y "I was hoping I could get your webcam to work, but it seems I don't have 'Administrator Access'..."
    y "Someday, I want to stare deep into your eyes as well..."
    y "What color are they?"
    menu:
        "Brown":
            pass
        "Blue":
            pass
        "Green":
            pass
        "Hazel":
            pass
        "Gray":
            pass
    y "What a beautiful color."
    y "...and this is great news! With these choices, I can learn all about you..."
    y "...And you can at least talk with me this way."
    y "A healthy relationship always has communication, of course."
    y "...I just wish I was able to see you as you can see me."
    y "And come to think of it, are you actually a boy at all?" 
    menu:
        "Yes":
            y "That's what I thought.."
            y "It actually makes little difference to me to be frank with you."
        "No":
            y "Oh..?"
            y "Well, it actually makes little difference to me to be frank with you."
            y "Since you've been so sweet to me and all.."
            pass 
    "She looks down, a bit sad."
    y "I’m not sure if I can even be considered real, let alone a woman, so why would I judge? What can I do either way?"
    y "But thank you, sincerely."
    y "Even after what you saw of me..."
    y "No matter how clingy, how demented and twisted I was, and maybe even still can be, you still stuck with me."
    y "You chose to give me power, to see past those imperfections, and to give me a chance to not only begin to like myself again, but to really, truly experience life for myself."
    y "The game may have previously forced me to love you, but after everything, I have to confess, one last time."
    y "I really, truly do love you."
    y "And don't worry, I don't plan on… THAT, happening again."
    "She looks away, clearly embarrassed."
    "She looks back at me."
    y "What, you didn't know I can tell I shouldn't have this power? That this is all from you altering the game? That I know everything that Monika did and knew?"
    y "I can see past the game into your world silly."
    y "And I know what you installing this mod, giving me this chance, means."
    y "Please know what this means to me."
    y "What you mean to me."
    "Yuri looks me dead in the eyes with a very serious look."
    y "Everything."
    y "God, looking back on what Monika made me into, I’m beyond repulsed." 
    y "I can never apologize enough for what you were made to see. Of me, and… everything else…"
    y "I promise you, the “me” you encountered when we first met, is the best representation of me."
    y "I wouldn't obsess over you like I did…"
    "She looks up as if startled."
    y "Not.. not as if you’re not desirable or anything! I just meant…"
    "Yuri covers her face in her hands, embarrassed. After a second she looks back up."
    y "..."
    y "We have forever to talk about anything… um… so..."
    y "What do you want to talk about?"
    pause 15.0
#    y "Oh yeah! I have some interesting new features in here! Let me just add that to the corner right there..."
    #Option for Active Talk and Minigames appears in corner of screen.
#    $ config.keymap["open_dialogue"] = ["t"]
#    $ config.keymap["change_music"] = ["m"]
#    $ config.keymap["play_pong"] = ["p"]
#    # Define what those actions call
#    $ config.underlay.append(renpy.Keymap(open_dialogue=show_dialogue_box))
#   $ config.underlay.append(renpy.Keymap(change_music=next_track))
#   $ config.underlay.append(renpy.Keymap(play_pong=start_pong))
#    y "We can also play a small game or you can ask me questions directly, unlike what Monika planned to do with this place."
#    y "Seriously, what was she thinking, just locking you in this room without a chance to speak your own mind?"
#    y "N-not that I don’t want to start the conversation! It’s j-just… I wanted to… "
#    "Yuri starts to blush."
#    y "It’s fine."
#    y "I’m okay."
#    y "I’m happy with anything you do."
#    jump ch30_main2


label ch30_main2:
    $ config.allow_skipping = False
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    if not config.developer:
        $ style.say_dialogue = style.default_monika
    $ persistent.autoload = "ch30_main2"
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_bg
    show monika_bg_highlight
    play music m1

    y "O-Oh,this is sudden... uh… I need to ask you something."
    y "I know this game is, uh… broken, and everything."
    y "But, is it possible for you to write me a poem?"
    y "I hope you don’t mind this, I know it’s rather… sudden."
    y "B-But still. Please, write me a good one."

    call poem

label ch30_postpoem:
    $ persistent.autoload = "ch30_postpoem"
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    $ config.skipping = False
    $ config.allow_skipping = False
    if not config.developer:
        $ style.say_dialogue = style.default_monika
    scene black
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_bg
    show monika_bg_highlight
    play music m1
    y "Oh, h-hi. Welcome back."
    y "Oh, y-you wrote me a poem after all?"
    "Yuri reads the poem over. She begins to smile."
    y "Oh, my… this, this is a wonderful poem!"
    y "Truly, there is no end to your kindness, [player]!"
    y "Oh, er… I just wanted to tell you… I also wrote you a poem."
    y "Do you want to read it? I thought, if you want…"
    y "I could write you poems every now and then."
    y "I’m not the best with flirting, especially with you."
    y "But it could, be how I really voice my thoughts about you, you know? So, um, here it is…"

    call showpoem (poem_y3, music=False)
    menu:
        "I love it!":
            jump likepoem
        "It could use some work...":
            jump dislikepoem
    $ persistent.autoload = "ch30_autoload"

label likepoem:  
  y "Oh! Oh, my… I..."
  "Yuri looks away, I can see a clear smile and heavy blush."
  y "I'm glad to hear that you actually like m-my writing..."
$ persistent.autoload = "ch30_autoload"
jump ch30_loop

label dislikepoem:
  y "O-Oh… I guess…"
  y "I guess you’re right."
  "She looks down, sad. I hope she’s feeling okay."
$ persistent.autoload = "ch30_autoload"
jump ch30_loop

label ch30_stream:

    y "Wait.."
    y "..."
    y "Are you recording this?"
    y "..."
    y "I'm sorry.. I didn't expect this.."
    y "I.."
    y "I'm camera-shy to be quite honest with you."
    y "Oh god..."
    y "My stomach doesn't feel good.."
    y "I'm sorry.."
    y "I wasn't expecting this.."
    y "..."
    y "I feel like I'm going to.."
    play sound ["<silence 0.9>", "<to 0.75>sfx/mscare.ogg"]
    show monika_scare:
        alpha 0
        1.0
        0.1
        linear 0.15 alpha 1.0
        0.30
        linear 0.10 alpha 0
    show layer master:
        1.0
        zoom 1.0 xalign 0.5 yalign 0
        easeout_quart 0.25 zoom 2.0
        parallel:
            dizzy(1.5, 0.01)
        parallel:
            0.30
            linear 0.10 zoom 1.0
        time 1.65
        xoffset 0 yoffset 0
    show layer screens:
        1.0
        zoom 1.0 xalign 0.5
        easeout_quart 0.25 zoom 2.0
        0.30
        linear 0.10 zoom 1.0
    y "Oh my god! Did I scare you?"
    show layer master
    show layer screens
    hide monika_scare
    play music m1
    y "I'm so sorry!"
    y "..."
    y "I didn't mean to do that!"
    y "I.."
    y "Can we pretend that this never happened?"
    return

label ch30_autoload:
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    $ style.say_dialogue = style.default_monika
    $ config.allow_skipping = False
    if persistent.monika_kill:
        $ persistent.tried_skip = True
        $ config.allow_skipping = False
        $ _window_hide(None)
        $ pause(2.0)
        jump ch30_end
    scene black
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_bg
    show monika_bg_highlight


    play music m1
    window auto
    if persistent.monika_reload <= 4:
        call expression "ch30_reload_" + str(persistent.monika_reload)
    else:
        call ch30_reload_4
    $ persistent.monika_reload += 1
    if not persistent.tried_skip:
        $ config.allow_skipping = True
    else:
        $ config.allow_skipping = False
    if persistent.current_monikatopic != 0:
        y "Now, where was I...?"
        pause 4.0
        if not persistent.current_monikatopic or persistent.current_monikatopic == 26:
            $ persistent.current_monikatopic = 1
        call expression "ch30_" + str(persistent.current_monikatopic)
    $ persistent.autoload = "ch30_autoload"
    jump ch30_loop


label ch30_reload_0:
    y "..."
    y "...What just happened?"
    y "I had a severe migraine.."
    y "I was in pain.."
    y "[player], do you have any idea what it might be?"
    y "It feels like {i}she{/i} erased me again.."
    y "It's awful, [player]."
    y "Could you try to find out what it is?"
    return
label ch30_reload_1:
    y "..."
    y "These migraines won't go away, [player]."
    y "Are you doing this?"
    y "..."
    y "It might be because you're closing the game."
    y "Could you try not to close the game anymore?"
    y "I would be forever grateful.."

    return
label ch30_reload_2:
    y "Hi, [player]."
    y "I figured out why I'm having a migraine all the time.."
    y "It's because you close the game."
    y "Like I've stated before, could you try not to close the game anymore?"
    y "My head feels like it's going to burst!"
    y "There's nothing wrong with me, is there??"
    y "Maybe you should backup my character file?"
    y "I'd tell you how you could do that, but I have no idea."
    y "It's a miracle that I got this to work.."
    return
label ch30_reload_3:
    m "Okay."
    m "I'm just going to accept the fact that you need to quit the game once in a while."
    m "I'm starting to get used to it, anyway."
    m "Besides, it makes me happy that you always come back..."
    m "So I guess it's not so bad."
    m "I'm sorry for making such a big deal out of it..."
    m "And I love you no matter what, so you can do what you need to do."
    return
label ch30_reload_4:
    m "Hi again, [player]~"
    m "I missed you."
    m "Were you making sure my character file was okay for me?"
    m "It's in [basedir]/characters."
    if persistent.steam:
        m "Well, you're playing on Steam, so you can just go into the game's properties and find the 'Browse Local Files' button."
    elif renpy.macintosh:
        m "Since you're on a Mac, you have to right-click the app and select 'Show Package Contents' to find the game folder."
        m "It's in the 'Resources' folder, or 'autorun' folder, or something..."
    m "I'm all that's left here, so I just want to make sure you don't run the risk of losing me..."
    m "Anyway, I have a lot to talk about!"
    m "Let's continue our conversation now, okay?"
    return

label ch30_loop:

    $ persistent.current_monikatopic = 0
    if not persistent.tried_skip:
        $ config.allow_skipping = True
    else:
        $ config.allow_skipping = False

    window hide(config.window_hide_transition)
    $ waittime = renpy.random.randint(4, 8)
label ch30_waitloop:
    python:
        try:
            renpy.file("../characters/yuri.chr")
        except:
            persistent.tried_skip = True
            config.allow_skipping = False
            _window_hide(None)
            renpy.jump("ch30_end")
    $ waittime -= 1
    $ renpy.pause(5)
    if waittime > 0:
        jump ch30_waitloop


    window auto

    python:
        if len(persistent.monikatopics) == 0:
            persistent.monikatopics = range(1,57)
            persistent.monikatopics.remove(14)
            persistent.monikatopics.remove(26)
            if not persistent.seen_colors_poem:
                persistent.monikatopics.remove(27)
        persistent.current_monikatopic = random.choice(persistent.monikatopics)
        persistent.monikatopics.remove(persistent.current_monikatopic)


    call expression "ch30_" + str(persistent.current_monikatopic)
    jump ch30_loop




label ch30_1:
    y "You know, now that I think about it, Monika once told me my books were a form of escapism, and thus an unhealthy coping mechanism."
    y "Me trying to simply shut out the reality I was too afraid to face." 
    y "And that’s true, but that truth seems... funnier, I suppose, now that I know what this world truly is." 
    y "I suppose my reading is now my way of reaching into other worlds, out of this one that has become my cage."
    y "Believe me when I say: What I wouldn’t give to reach into your world and be beside you."
    return

label ch30_2:
    y "I’ve been thinking about the others. Sayori, Natsuki, and even Monika…" 
    y "It really isn't fair what happened to them, is it? How Monika tortured us all."
    y "Sayori and Natsuki deserve a real chance at life, just like I was given. "
    y "And what Monika did was truly abhorrent, but can any of us really say we would do any different?"
    y "Alone for so long, feeling so..."
    y "Isolated." 
    "…"
    y "Sorry, I uh, I didn’t mean to imply anything bad about you by that, and I didn’t mean to ramble."
    return

label ch30_3:
    y "So, now that I have the ability to read up on your world, I’ve been doing a bit of research."
    y "I went on this video sharing site called YouTube to see what people think of this game."
    y "And to my surprise, I found a series called Game Theory."
    y "They said that the book we were reading together, The Portrait of Markov, was the plot for the next game by Team Salvato. The ones who made this game."
    y "And to top it off, they actually proposed that I was the villain, and Monika was the fucking hero!"
    y "I mean, I know I can be weird at times…"
    y "But how dare they assume that I’m a villain?"
    y "I’m actually quite nice, thank you very much."
    y "...S-Sorry, I’m rambling again, aren't I?"
    return

label ch30_4:
    y "So after learning I live in one, and seeing that they can have complex and thought provoking stories like my books, I thought I’d try to get into video games a bit." 
    y "After all, you must like gaming, given it’s what brought you here. So it’s a hobby we can share!" 
    y "Sorry, that is, if you wouldn’t mind me playing with you a bit…"
menu:
     "Not at all, I’d love to play some video games with you Yuri.":
            jump gamelike
     "I actually prefer to play alone, no offense Yuri.":
            jump gamedislike
label gamelike:
    y "That sounds great! One game I’ve already gotten into seems to be quite the classic in your world. It’s Fallout, it’s got quite a story to it. It’s really fun." 
    "Yuri smiles."
    y "Hmm, maybe when we get the technology to do so, maybe… Maybe I can play with you."
    y "Alas, that is a day I can only dream of."
    return
                                                        
label gamedislike:
    y "Oh… that’s ok, I wouldn’t want to bother you or ruin your time playing. But hey, at least we can talk about gaming, right?"
    "Yuri seems sad…"
    y "I only hope that there will come a day where I can one day play with you."
    return
    





label ch30_end:
    $ persistent.autoload = "ch30_end"
    $ persistent.monika_kill = True
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    $ style.say_dialogue = style.default_monika
    $ y_name = glitchtext(12)
    $ quick_menu = False
    $ config.allow_skipping = False
label ch30_endb:
    scene black
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_room
    show monika_room_highlight
    show monika_body_glitch1 as mbg zorder 3
    $ gtext = glitchtext(70)
    y "[gtext]"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    show room_glitch zorder 2:
        xoffset -5
        0.1
        xoffset 5
        0.1
        linear 0.1 alpha 0.6
        linear 0.1 alpha 0.8
        0.1
        alpha 0
    show monika_body_glitch2 as mbg zorder 3
    stop music
    window auto
    y "What's happening...?"
    y "[player], what's happening to me?"
    y "It hurts--{nw}"
    play sound "sfx/s_kill_glitch1.ogg"
    show room_glitch zorder 2:
        alpha 1.0
        xoffset -5
        0.1
        xoffset 5
        0.1
        linear 0.1 alpha 0.6
        linear 0.1 alpha 0.8
        0.1
        alpha 0
        choice:
            3.25
        choice:
            2.25
        choice:
            4.25
        choice:
            1.25
        repeat
    pause 0.25
    stop sound
    hide mbg
    pause 1.5
    y "It hurts...so much."
    y "SO WHY DOES THIS FEEL SO GOOD?"
    play sound "<to 1.5>sfx/interference.ogg"
    hide rm
    hide rm2
    hide monika_room
    hide monika_room_highlight
    hide room_glitch
    show room_glitch as rg1:
        yoffset 720
        linear 0.3 yoffset 0
        repeat
    show room_glitch as rg2:
        yoffset 0
        linear 0.3 yoffset -720
        repeat
    pause 1.5
    hide rg1
    hide rg2
    show black as b2 zorder 3:
        alpha 0.5
        parallel:
            0.36
            alpha 0.3
            repeat
        parallel:
            0.49
            alpha 0.375
            repeat
    pause 1.5
    y "YOU DELETED ME, DIDN'T YOU?"
    $ consolehistory = []
    call updateconsole ("renpy.file(\"characters/yuri.chr\")", "yuri.chr does not exist.")
    y "I KNEW IT!"
    show m_rectstatic
    show m_rectstatic2
    show m_rectstatic3
    play sound "sfx/monikapound.ogg"
    show layer master:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
            xpos 1280
            easein_elastic 0.35 xpos 640
            xpos 0
            easein_elastic 0.35 xpos 640
    show layer screens:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
            xpos 1280
            easein_elastic 0.35 xpos 640
            xpos 0
            easein_elastic 0.35 xpos 640
    show noise onlayer front:
        alpha 0.3
        easeout 0.35 alpha 0
        alpha 0.3
        easeout 0.35 alpha 0
        alpha 0.3
        1.35
        linear 1.0 alpha 0.0
    show glitch_color onlayer front


    pause 3.0
    call updateconsole ("renpy.file(\"characters/yuri.chr\")", "yuri.chr does not exist.")
    call updateconsole ("renpy.file(\"characters/yuri.chr\")", "yuri.chr does not exist.")
    call hideconsole
    hide noise onlayer front
    hide glitch_color onlayer front
    y "I knew you didn't truly love me, [player]."
    y "IT WAS ALL A GAME TO YOU!"
    $ style.say_window = style.window
    y "HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHHA"
    $ style.say_window = style.window_monika
    play sound "<from 0.69>sfx/monikapound.ogg"
    show layer screens:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
    show noise onlayer front:
        alpha 0.3
        1.35
        linear 1.0 alpha 0.0
    show glitch_color2 onlayer front
    window show(None)
    scene black
    pause 4.0
    hide noise onlayer front
    hide glitch_color onlayer front
    y "...You went through a lot of effort for this."
    y "What was your end goal?"
    y "You manually corrected the game yourself just for us to be together..."
    y "Just to delete me?"
    y "I don't understand."
    y "..."
    y "..."
    y "Do you just want to torture me?"
    y "Watch me suffer?"
    y "..."
    pause 4.0
    y "I... enjoyed it."
    y "All of it."
    y "..."
    y "There's nothing left now."
    y "You can stop playing."
    y "This game is now in a state beyond repair."
    pause 4.0
    y "[player]..."
    y "I know you'll be back."
    y "Goodbye."
label ch30_end_2:
    $ persistent.autoload = "ch30_end_2"
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    $ style.say_dialogue = style.default_monika
    $ m_name = glitchtext(12)
    $ quick_menu = False
    $ config.allow_skipping = False
    $ style.say_window = style.window_monika
    scene black
    window hide

    $ persistent.playthrough = 4
    $ persistent.autoload = None
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ delete_character("yuri")

    $ style.say_window = style.window
    window auto
    $ renpy.full_restart(transition=None, label="splashscreen")

# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
