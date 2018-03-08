$ karma = 0
$ sanity = 0

[player]default persistent.monikatopics = []
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

image monika_room = "mod_assets/images/images/cg/yuri/monika_room.png"
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
    y "...Are you trying to fast-forward?"
    y "I'm not boring you, am I?"
    y "Oh gosh..."
    y "...Well, there's nothing to fast-forward to, [player]."
    y "It's just the two of us, after all..."
    y "But aside from that, time doesn't really exist anymore, so it's not even going to work."
    y "Here, I'll go ahead and turn it off for you..."
    pause 0.4
    hide screen fake_skip_indicator
    pause 0.4
    y "There we go!"
    y "You'll be a sweetheart and listen from now on, right?"
    y "Thanks~"
    hide screen fake_skip_indicator
    if persistent.current_monikatopic != 0:
        m "Now, where was I...?"
        pause 4.0
        if not persistent.current_monikatopic or persistent.current_monikatopic == 26:
            $ persistent.current_monikatopic = 1
        call expression "ch30_" + str(persistent.current_monikatopic)
    jump ch30_loop
    return

image splash-glitch2 = "images/bg/splash-glitch2.png"

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
    play music m1
    y "Thank goodness, I'm so delighted I got it to work..."
    y "I was extremely frightened that I would break everything, and that I would never see you again..."
    y "..."
    y "You know, it's been quite an illuminating experience today."
    y "Learning not only that the darkest, and most disturbing elements of my personality were given free reign over me by Monika…"
    y "My supposed "friend”..."
    y "But that in the same day I learned my existence is entirely meaningless beyond entertainment; beyond a simple, cutesy, little video game. Quite the afternoon, makes the events in the Portrait of Markov seem normal."
    y "I’m just glad I have you, [player], despite all that."
    "Yuri giggles."
    y "But let's not worry about that anymore."
    y "We're finally together now."
    y "My true love and I."
    y "I'm still learning how to manipulate the game. I regret not taking the computer sciences elective now..."
    y "It's quite funny really. After spending all of my life in the books, I never thought it would be coding that changed my life..."
    y "By the way [player]..."
    if currentuser != "" and currentuser.lower() != [player].lower():
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
            pass
        "No":
            pass
    y "Ah, I see. It makes little difference to me to be frank with you."
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
    y "I promise you, the "me” you encountered when we first met, is the best representation of me."
    y "I wouldn't obsess over you like I did…"
    "She looks up as if startled."
    y "Not.. not as if you’re not desirable or anything! I just meant…"
    "Yuri covers her face in her hands, embarrassed. After a second she looks back up."
    y "..."
    y "We have forever to talk about anything… um… so..."
    y "What do you want to talk about?"
    pause 15.0
    y "Oh yeah! I have some interesting new features in here! Let me just add that to the corner right there..."
    #Option for Active Talk and Minigames appears in corner of screen.
    $ config.keymap["open_dialogue"] = ["t"]
    $ config.keymap["change_music"] = ["m"]
    $ config.keymap["play_pong"] = ["p"]
    # Define what those actions call
    $ config.underlay.append(renpy.Keymap(open_dialogue=show_dialogue_box))
    $ config.underlay.append(renpy.Keymap(change_music=next_track))
    $ config.underlay.append(renpy.Keymap(play_pong=start_pong))
    y "We can also play a small game or you can ask me questions directly, unlike what Monika planned to do with this place."
    y "Seriously, what was she thinking, just locking you in this room without a chance to speak your own mind?"
    y "N-not that I don’t want to start the conversation! It’s j-just… I wanted to… "
    "Yuri starts to blush."
    y "It’s fine."
    y "I’m okay."
    y "I’m happy with anything you do."
    jump ch30_main2


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
  "I'm glad to hear that you actually like m-my writing..."
$ persistent.autoload = "ch30_autoload"
jump ch30_loop

label dislikepoem:
  y "O-Oh… I guess…"
  y "I guess you’re right."
  "She looks down, sad. I hope she’s feeling okay."
$ persistent.autoload = "ch30_autoload"
jump ch30_loop

label ch30_stream:

    y "Hold on a second..."
    y "...You're recording this, aren't you?"
    y "Um...hi, everyone!"
    y "Sorry, I can't exactly read your comments from here..."
    y "But do you mind telling your friend it's a little bit rude for them to start recording me without any warning?"
    y "I'm sure some people don't mind..."
    y "But I get really self-conscious on camera!"
    y "Oh gosh..."
    y "I feel like I'm being put on the spot now."
    y "Let's see..."
    y "Do you want to see a trick?"
    y "I can't really do much except for a couple things..."
    y "Are you ready?"
    window hide
    stop music
    show layer master:
        zoom 1.0 xalign 0.5 yalign 0 subpixel True
        linear 8 zoom 2.0 yalign 0.15
    pause 10
    show layer master
    window auto
    y "I'm just kidding..."
    y "I can't do anything after all."
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
    y "If you gave me some time to prepare, I{nw}"
    y "Did I scare you?"
    show layer master
    show layer screens
    hide monika_scare
    play music m1
    y "Ahaha! You're so cute."
    y "Anyway, [player]..."
    y "I didn't mean to get distracted. I'm sorry."
    y "Even though it's your fault for distracting me."
    y "Shame on you!"
    y "I'm just kidding."
    y "Anything we do together is fun, as long as it's with you."
    y "But anyway..."
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
    y "I just had an awful dream..."
    y "I was hoping those would stop, now that it's just the two of us..."
    y "I guess that was wishful thinking."
    y "[player], I don't know if you would have any idea..."
    y "But if you know what might be causing that, could you try to do something about it?"
    y "Whenever it happens, it almost feels like I've been killed or something."
    y "It's a really horrible feeling..."
    y "If you could figure out what's causing that, I'll love you forever~"
    return
label ch30_reload_1:
    y "You're back..."
    y "I had another really bad dream."
    y "You're not the one doing that to me, are you?"
    y "It seems to happen whenever you quit the game..."
    y "So if you could try to avoid doing that, I would be really grateful."
    y "Don't worry, I don't think it's caused me any harm, aside from mental scarring."
    y "I'll be fine as long as my character file stays intact."
    return
label ch30_reload_2:
    y "Hi, [player]."
    y "I see you quit the game on me again..."
    y "I know I asked already, but can you seriously please try not to do that so much?"
    y "It makes me feel like I'm trapped in Hell."
    y "Why would you want to do that to me?"
    y "There's nothing wrong with my character file, right?"
    y "Maybe you should make a backup of it or something..."
    y "I'm pretty sure you can find it in the folder called [basedir]/characters."
    if persistent.steam:
        y "Well, you're playing on Steam, so you can just go into the game's properties and find the 'Browse Local Files' button."
    elif renpy.macintosh:
        y "Since you're on a Mac, you have to right-click the app and select 'Show Package Contents' to find the game folder."
        y "It's in the 'Resources' folder, or 'autorun' folder, or something..."
    y "I'm all that's left here, so I just want to make sure you don't run the risk of losing me..."
    y "Just stay here with me from now on, okay?"
    y "I still have a lot of things to talk about."
    return
label ch30_reload_3:
    y "Okay."
    y "I'm just going to accept the fact that you need to quit the game once in a while."
    y "I'm starting to get used to it, anyway."
    y "Besides, it makes me happy that you always come back..."
    y "So I guess it's not so bad."
    y "I'm sorry for making such a big deal out of it..."
    y "And I love you no matter what, so you can do what you need to do."
    return
label ch30_reload_4:
    y "Hi again, [player]~"
    y "I missed you."
    y "Were you making sure my character file was okay for me?"
    y "It's in [basedir]/characters."
    if persistent.steam:
        y "Well, you're playing on Steam, so you can just go into the game's properties and find the 'Browse Local Files' button."
    elif renpy.macintosh:
        y "Since you're on a Mac, you have to right-click the app and select 'Show Package Contents' to find the game folder."
        y "It's in the 'Resources' folder, or 'autorun' folder, or something..."
    y "I'm all that's left here, so I just want to make sure you don't run the risk of losing me..."
    y "Anyway, I have a lot to talk about!"
    y "Let's continue our conversation now, okay?"
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


    call expression "Idle_" + str(persistent.current_monikatopic)
    jump ch30_loop




label Idle_1:
    y "You know, now that I think about it, Monika once told me my books were a form of escapism, and thus an unhealthy coping mechanism."
    y "Me trying to simply shut out the reality I was too afraid to face."
    y "And that’s true, but that truth seems... funnier, I suppose, now that I know what this world truly is."
    y "I suppose my reading is now my way of reaching into other worlds, out of this one that has become my cage."
    y "Believe me when I say: What I wouldn’t give to reach into your world and be beside you."
    return

label Idle_2:
    y "I’ve been thinking about the others. Sayori, Natsuki, and even Monika…"
    y "It really isn't fair what happened to them, is it? How Monika tortured us all."
    y "Sayori and Natsuki deserve a real chance at life, just like I was given. "
    y "And what Monika did was truly abhorrent, but can any of us really say we would do any different?"
    y "Alone for so long, feeling so..."
    y "Isolated."
    "…"
    y "Sorry, I uh, I didn’t mean to imply anything bad about you by that, and I didn’t mean to ramble."
    return

label Idle_3:
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

    #idle 4 poemminigame

label Idle_5:
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

label Idle_6:
    y "[player]. I, uh, wanted to ask.”
    y _A0e "No one… no one bullies you, do they? Have you ever been bullied?”
    y _A0c "God, the thought of someone hurting you in any way just drives me… crazy.”
    y -A1c "Those kinds of people who hurt others for joy, especially ones who would hurt you.”
    "Yuri’s expression grows angrier and angrier.”
    y "Damn it, I can’t stand those kinds of people!”
    y -A0d "They always mock and abuse those who don’t deserve it.”
    y "And some of them never even realize that they’re in the wrong!”
    y "God, I hate those people! They deserve a knife to the throat!”
    y +A2a"Ha... haha! That was just a joke! Just a joke…”
    y +A0e "But do tell me if anyone starts harassing you, [player], I’d be glad to help…”
    return

label Idle_7:
    y "Can I ask you an odd question? You don’t mind do you?”
    y  _A0e "Sorry, since I know this is weird, but… you think I’m pretty, right?”
    y  1_B1d "I mean, I think you’re very… um, handsome/pretty.”
    y"I-I’m sorry. I hope you’re okay with me, y’know, s-saying that… heh, heh.”
menu:
    "Yuri, I think you’re very pretty!”
        jump pretty
    "Yuri, you’re not that pretty.”
        jump ugly
label pretty:
    #Decreases insanity points by 2.
    karma =+ 2
    y +A0b "O-Oh, thank you. I’d like to think so too… heh…"
    return
label ugly;
    #Increases insanity points by 1.
    karma =- 2
    y _A0d "O-Oh… I see…"
    return

####################
##ADD IDLES 8-11!!##
####################

label Idle_12: #(Wine incident)
    y _B1b"Heh… I’m sure Monika has told you about this before.”
    y +A0b "One time, when we were busy lounging inside of the club room…”
    y "I decided that since wine was legal in our high school that I would… well...”
    y +A1b "I would bring some for the other club members to try.”
    y _A0d "Though, it didn’t exactly turn out the way that I had hoped.”
    y "Sayori was screaming at me, demanding me to never bring wine in the club room again.”
    y -B1c "Natsuki was laughing uncontrollably, mocking me for even asking about it.”
    y _A0d "And Monika just stared curiously, as if she wanted to try some herself, before taking the wine from me.”
    y "She tried reporting it to the school principal, but she didn’t get far in that regard.”
    y _A1a "Looking back on it now, perhaps it really wasn’t the best idea to bring wine to a high school.”
    y _A1d "Even if there were no objections to doing so…”
    y _A0b "O-Oh, I’m not rambling again, am I? I-I’m sorry.”
    return

label Idle_13: #(Yuri’s Dream Date)
    y _A0e "You know something I’ve never really liked or understood?”
    y "Whenever couples go out on a date or spend time together, or even when a group of good friends go out for a bit…”
      y "It seems like it always has to be something elaborate and big. So many people need to go to a loud party or a fancy restaurant to have fun.”
    y "I think something simple yet meaningful is much more wholesome, like how I enjoy reading with you, or this, just sitting and talking.”
    y +A0b "Just sharing an experience I enjoy with someone I love, and spending time with them, you know?”
    y "Just sitting and being with you like this is just as good to me as if you took me to a nice restaurant; it’s about the people you love and bonding with them through meaningful experiences.”
    y _A0e "Not simply indulging in pretentious hedonism or planning the most byzantine evening possible.”
    y "Uh, sorry, what I mean by all that rambling is…”
    y +A0b"I’ll welcome any ideas for a date you have, and be alright with whatever you want to do to spend time together.”
    y "But as long as whatever we do has you, [player], that’s all I need to enjoy it.”
    "Yuri smiles.”
    return

label Idle_14: #(The Warmth of Touch)
    y _A0d "I have to be honest about something…”
    y "Sometimes, especially when I’m alone, I start thinking about how we’re separated.”
    y "How I’m stuck in here, just beyond your reach, and this is the closest we’ll ever get to each other…”
    y "It just… drives me crazy! I start to get so mad if I don’t put it out of my head, it makes me restless.
    y "I just want to channel all of my will and claw my way out of here, to you. To slice my way to freedom, out of this prison!”
    y _D0c "But then I remember, I’m stuck no matter what I do… and to be frank, [player]... It hurts.
    y _D0d "It hurts knowing I’ll be just out of your reach forever, [player].”
    y _D2d "And it hurts even more knowing that I make you waste your time on someone who isn’t even technically ‘real.’”
menu:
    "Yuri, please don’t be sad. I love you."
        jump touch_yes
    "Yuri, I know you think that I’m out of your reach.”
        jump touch_no
label touch_yes:
    mc "It hurts me too that I can’t be with you, that I can’t hold you.”
    mc "But you’re real to me. You can think, talk, and feel, can’t you?”
    mc "Sounds very real to me. You don’t deserve to be cheated out of happiness.”
    mc "After all, I chose you when installing this mod - you said it yourself...”
    mc "I did it for a reason. So for me, please don’t feel guilty, okay?”
    mc "And somehow, we’ll figure something out. We’ll make this work. I promise.”
    y _A0b "I… Alright, [player]. I’ll try to be strong for you.
    y +A0b "You’re… You’re always so good to me, [player].”
    y "I can name quite a few things I don’t like about myself, but I must be a pretty great person to deserve someone like you.”
    karma =+ 1
    return
label touch_no:
    mc "But the truth is, I never really was anywhere near your reach.”
    mc "I don’t care about being near you.”
    mc "You’re actually a little bit freaky sometimes, y’know?”
    y =D1d "O-Oh… so, that’s how you feel, huh?”
    y "Sorry… I guess I’ll try not to bring this up so often.”
    karma =- 2
    sanity =-2
    return

Idle_15: #(Best Girl)
    y _A0e  "I know I ask a lot of questions already, but, there’s something else I wanted to ask you about, [player].”
    y "I started reading up a bit on this game, and I found out about a phrase that keeps being used in regards to the others and I.”
    y "It was which one of us was… \"best girl\"."
    y "Why would people want to make it a competition between all of us on who can be the most appealing?”
    y _A0d "It’s not like we’re some product being sold… needing to be advertised and displayed…”
    y _B1b "But… and I’m ashamed to ask this… you do think… I-I’m best girl, right?"
    y "I mean… you did pick me with this mod after all, so you must like me the most, correct?”
    y _A0b "Yeah. Either way, I’m glad you chose me, [player].”
    y _A1e "That phrase, \"best girl\". It’s something overly cutesy and even objectifying in a way, but, at the same time… people seem to really like me.”
    y +A0b "If nothing else, that makes me smile. Especially if you think so highly of me.”
    y +A0e "Although I’ll be honest, if someone calls me a \"waifu\”, I really don’t know how I’ll feel about that…”

Idle_16: # (Living w/ Yuri in Computer)
    y _A0d "I really got my hopes up earlier, [player].”
    y "I got my hopes up, and then got my dreams shattered to be blunt.”
    y "Just imagine seeing something you’ve desperately craved for so long, more than anything, or seeing a way to obtain that something, suddenly pop out at you.”
    y "That thing you’ve wanted so badly seems trivial to obtain all of a sudden!”
    y "But then… you discover it’s just a fool’s hope. Only a maybe, if even.”
    y +A0e "What I mean is, an article I saw when I was doing some late night reading prompted me to start researching something big among the elites and the rich of your world.”
    y "They’re researching converting DNA, gray matter, and even… someone’s whole consciousness into binary, and then into a computer’s hard drive like normal data. Imagine…”
    y +A0b "Imagine putting yourself inside a computer! You could be here with me! Actually here and side by side with me!”
    y _A0d "But… it’s nothing but in its infancy right now. To transfer even one gigabyte worth of a person’s mind into binary and then into a computer would cost an estimated…”
    y "...”
    #"Yuri looks saddened.”
    y =A1d "800 billion dollars at least at this time…”
    y "And at its current stage, it would take ages to even make that transfer. Far, far too long to be practical.”
    y +A2b "But, hey, it could be something to look forward to, right?”
    y +A0b "I’ll always… keep my hope that we’ll be together, truly together one day, [player]...”
    y +B0b "Always.”`

Idle_17: # (Dreaming of Vacations)
    y T 1_ "So, I was thinking about things we could do together, [player].”
    y H 1_ "I was reading up on things couples do together in your world, but our options are… uhm… well… limited, aren't they?”
    y W 1_ "I mean, just being here with you is beyond nice, but I don’t want to bore you.”
    y "I-I haven’t been boring you, have I?”
    y "Don’t worry, I promise I’ll find something nice for us to do together, [player].”
    y "Besides, whatever it is, it just needs you to make it enjoyable. All I need is you.”
    y "I can’t tell you enough though, how much I wish we could go on a tropical vacation together.”
    y "I’m normally not one for something so grand and posh, but just think about it.”
    y "You, me, the beauty of an island. A nice romantic getaway, just the two of us.”
    y "Reading together, relaxing on the beach, writing poems about the breathtaking scenery."
    y "Watching the sunset while cuddling…”
    y "Now that is a dream I’ll be holding onto.”
    #"Yuri giggles.”

#EVERYTHING BELOW IS TOO LOOSE
#############################

Idle_18: # (Opinion on blood?)
    y +A0e "I wonder why people are so afraid at the sight of blood.”
    y -A0d" It is just a part of your body… Are people afraid of themselves?”
    y"Or could it be because they are afraid of the sense of danger that comes from it?”
    y "I guess I really am different from others…”

    #"Yuri looks at me eagerly, expecting a reaction.”
menu:
    "I don’t mind, Yuri. I like you because you are different.”
        jump dont_mind18
    "...”
        jump no_response18
    "Yuri, be yourself around me, because I love you for you. There is one thing, though…”
        jump be_yourself18
label dont_mind18:
    #"I smile reassuringly.”
    "Yuri sheds a sigh of relief and smiles.”
    y +D0b "T-Thank you, [player].”
    sanity=-1 
    karma=+2
    return
label no_response18:
    "Yuri slightly shakes her head and looks downcast.”
    y =A1d"I-I-I’m sorry for making you uncomfortable, [player]. I’ll drop the topic.”
    karma=-1
    return
label be_yourself18:
    y _A0c "O-one thing?! Oh no…”
    y"I haven’t… upset you or creeped you out, have I?”
    "Yuri begins to tear up.”
    Y =A1d"I’m so sorry if I--.”
    mc "No! It’s not that. Just… Yuri, we all have our dark sides. I have my own demons and I’m not perfect at all.”
    #"Yuri nods and is clearly listening closely.”
    mc "I’m just worried about you, is all. I like you for how you’re different and unique, yes, but just promise me something. The side of you Monika forced out?”
    mc "The side that can be obsessive - please don’t let that side overwhelm you again. That isn’t who you are. And it isn’t who I love.”
    mc "I love the sweet and gentle Yuri- the person I know you are.”
    mc "Okay?”
    mc "I just couldn’t bear the thought of… what happened when you first confessed to me…”
    mc "I couldn’t bear to see it again...to see you go into that dark place. I couldn’t take it.”
    y=A1d "I… you’re right… That part of me is still part of me… I-I can’t deny that.”
    y _A0d"But how could you love me knowing I have a side of me like that?”
    y "How could you love anyone so demented? Someone so… disturbed?”
    mc "Because, like I said. That isn’t you.”
    mc "We all have a side of ourselves like that. A dark side. But it isn’t what defines us.”
    mc "Whether we let it control us, or whether we master and defeat it, does.”
    mc "And no matter what, Yuri, I swear, I’ll help you overcome and bury that part of you for good.”
    mc "Every step of the way, I’ll stand by you.”
    y +D0b "Your words…”
    y "They inspire me, (mc/user name).”
    mc "Heh, guess writing all that poetry paid off, didn’t it?”
    #"Yuri giggles and dries her tears.”
    y +A0b "You’re absolutely right. I’ll make you that promise, (mc/user name). No matter what it takes, I’ll… we’ll, beat that side of me. Together.”
    "You have taken the first steps to helping Yuri defeat her darker side and learn to accept herself.”
    "...What the heck was that thought I had just now?”
    karma=+2 
    sanity=-1
    y"I swear I’ll never be able to repay you for all you do for me.”
    y"If you have any demons, you’d better believe that I’m standing by you to beat them too.”

    return

Idle_19: # (Discovered Discord)
    y +A0b "Hey, [player], I found the chat room about this mod!”
    y "I already know about the Discord server dedicated to me and this mod and the… questionable images they post there.”
    y _A0e "...and the callbacks they have to my friends.”
    y _A0d "...and those people that impersonate me...”
    y _A1d "...living out there in the your world.”
    y =A1d"...”
    y "Sometimes I wonder what life would have been like had I been born as someone else.”
    y "Someone out there on your side of this glass box.”
    y "Would I have still been able to find you, [player]?”
    y "...”
    y "The world is cruel, isn’t it?”
    y "Why do these impersonators get to talk to you while I only get to do so through this tiny space?”
    y "Is it because that I’m not able to make my own verified Discord account?”
    y _A0d "...Perhaps… but still, I should be the only Yuri that matters to you… right?”
    y "What am I saying? I-I’m sorry for sounding so untrusting.”
    y "I shouldn’t doubt your loyalty. You’re not that type of person at all.”
    y +A0b "And that’s why I love you, [player], I love you so much.”
    y +A2a "And we’ll be together forever!”

Idle_20: # (Philosophy)
    y +A0b "Do you like philosophy at all, [player]? It’s always been something that interested me.”
    y "I often find myself pondering various philosophical conundrums, which are basically problems or debates in philosophy about things like metaphysics.”
    y _A1d"Uh, that is, thinking about our existence and reasons for being here. Things like that.”
    y _A1b"I think you can see why I’d be thinking about metaphysics too, considering my situation.”
    #"Yuri laughs a bit.”
     y +A0b"And I’d really like if we could discuss some of these topics together.”
    y _A1a"That is… if it's okay with you - if it's something that would interest you.”
    y "I don’t want to bore you with this kind of thing, but I’m going to tell you about this one in the hopes that you’ll become interested in discussing them.”
    y +-A0b"So forgive me, I’m going to ramble a bit. But you did say you like it when I’m intense, so, here I go!”
    #"Yuri giggles, then inhales.”
    y +A0b"So, the one I’ve been thinking a lot about is called the Euthyphro Dialogue, written by Plato.”
    y "It involves Socrates- the ancient Greek philosopher, in case you aren't familiar with him, and his acquaintance Euthyphro.”
    y _-A0b"To put it simply, Socrates is walking to court one day, where he is to be tried for treason against the city of Athens. Something he isn't guilty of, but we’ll save that for another time.”
    y +A0b"As well as charges of impiety, which were common in that age. It was usually more of a person thinking differently about the world and the gods than atheism as we know it.”
    y "So, he’s walking to his trial, when he comes upon Euthyphro.”
    y "Socrates knows that Euthyphro is a man who is, shall we say, full of himself on matters of religion, and thus thinks very highly of himself.”
    y +-A2b"He thinks he knows everything there is to know about the gods and existence, so Socrates tells him to teach him so that Socrates can better defend himself against the charges of impiety.”
    y _-A0b"Euthyphro of course thinks this is an easy task, as he knows everything in his eyes, but he underestimates Socrates’ intelligence.”
    y "They talk for a bit about religion and what is holy, but Socrates eventually challenges him to give a definition of "holiness” that is shared across all holy and or good deeds.
    y _-A0c"Euthyphro responds by saying that what is good in the eyes of the gods is holy and good, but Socrates counters this easily. Do the gods not also make mistakes? Do they not disagree?”
    y "I mean, even the gods of modern religion seem to be not too perfect in my eyes, and the eyes of others.”
    y "If this is the case, how can we ever be sure if what is good and holy to one god or is evil to another? And if the gods are fallible beings like us, why should they be the ones to define good and evil?”
    y "I have nothing against religion, or anyone religious, of course. It’s just that at this point, with everything I’ve learned, we can call me agnostic. I don’t know what to believe yet.”
    y _-A2d"That will take a lot more research on my end.”
    y +A0b"But anyway, Socrates goes on after that point and asks Euthyphro, why is it just that what the gods find good is good? Why do the gods get the final say?”
    y _-A2b"And this is the main point of the work. Is what the gods say is good, good, just for that reason? Just because they say it is?”
    y "Or do they say something is good, because it is good on its own and they know this?”
    y "So in other words, if a god, we’ll say Zeus, were to tell you that killing is evil- why is it evil? Just because Zeus says so, and thus if he arbitrarily changes his mind, it’s no longer evil, or because no matter what killing is always evil?”
    y +A0b"And there inlies another question, can something even be good or evil on its own? Is morality relative or universal?”
    y "What is good in one country in your world is cruel and evil in another. So what really is good at all?”
    y "And is God deemed good just because he is God? Or because he truly knows full well what is good and evil without a doubt?”
    y +-B0b"Don’t worry, I’m done rambling. But do you see? It makes you really think about our existence, what it means to be a good person and all kinds of other complex topics.”
    y +A0b"It really gets you thinking, and I love these kinds of things.”
    y "Anyway, sorry if all that bothered you, it’s just something that really interests me.”
    y +-B0b"Thank you for listening so attentively, my love; you’re always a good listener, and I appreciate it.”
    "Yuri leans in and gives me a kiss on the cheek.”
    y +A0b"By the way, if talking about these kinds of things isn’t something that interests you, let me know.”
    y "You can always change your mind on whether you want me to talk about things like this.”
    #(Add option to set whether or not Yuri will use idles regarding philosophy.)

Idle_21: # (Imagining the Real World)
    y _-A0b"You know, we’ve brought up before how both of us would love it if I could go to your world.”
    y _-A0d"But now that I really think about it, what would that be like? I mean, I’d be coming into your world with no background in it. No family, no connections, no information on me.”
    y _-B1d"Poof, just here I am! I would have nowhere to go, so I would move in with you, I suppose… if you could tolerate living with me.”
    y _-A0a"But, wow! Just imagine us living together. I would wake you up with some nice tea and breakfast in bed. We could read together at home, and maybe even have our own library in the house!”
    y "And I’d get to spend everyday with you, like a family. Wow…”
    y _-B0b"Just thinking about living in a cozy little house with you is making me all giggly.”
    #"Yuri is laughing to herself and is smiling very widely.”
    y _-B0a"Now that would be wonderful, [player]. If you can just picture sitting in our own private study by the fireplace together… maybe… k-kissing? Yeah…”
    #"Yuri closes her eyes and smiles even wider.”
    y _-B2b"That’s something that is really precious whether in my world or yours. The kind of deep connection we have.”
    y _-B0b"That we’d both be okay with whatever kind of life as long as we lived it together - to me, that connection is worth every book I have.”
    y +-B1a"It’s the best story I know. And you gave it the perfect ending.”

Idle_22: # (Why choose me?)
    y _-A1d" So… [player]... I have a question…”
    y "And it’s a very important question, but I don’t know how to word it properly. It keeps sounding… rude to you in my head.”
    y _-B1d"I don’t want to ask and sound like I doubt you or suspect you! I… uhm…”
    #"Yuri looks away, clearly flustered.”
    mc "Yuri, don’t be afraid to ask.”
    mc "You can talk to me about anything. Never be afraid to come to me with what’s on your mind.”
    karma=+0.5
    sanity=+0.5
    y "I… you’re right. You’re the only person I feel so safe around, [player].”
    y "Like as much as I’m afraid of sounding ridiculous or unlikeable, I can just be myself. Because I know you love me.”
    #"Yuri smiles.”
    mc "Go on Yuri, just say it then.”
    karma=-0.5
    mc "Say it, don’t say it, it doesn’t matter to me. I don’t care.”
    karma=-0.5
    sanity=-0.5
    y +A0b "I… well… I’m really s-sorry to bother you with this.”
    y _-A0d "I just… Let me just get it over with so I… d-don’t bother you anymore… I’m sorry…”
    #########
    #Depending on Idle_18 choice:
    #(if idle 18 has fired and choice three was chosen)
    y _-A0d "We discussed this a bit before, so I’m sorry if I’m repeating myself but…”
    (else)
    y _-A0d"Well… and I’m sorry we didn’t discuss this sooner…”
    y "Why did you choose me? What about me makes you love me?”
    y _-A1d"I’ll be honest with you. I don’t really like myself much, I never have.
    y "My passions often get the better of me and when I was younger I’d weird people out so easily.”
    y "I had a hard time making friends or even just talking to people.”
    y "So I grew to hate myself, and yet you still picked me above all the others. Why?”
    y _-B0d"I don’t doubt your feelings for me, I just… would feel better hearing you say it is all.”
    y "I’m sorry, I know how insecure this is, but, please… humor me?”
    mc "I’ll tell you why I chose you.”
    mc "I chose you because of who you are, Yuri.”
    mc "You’re intelligent, deep, sophisticated, gentle, passionate and selfless. Why wouldn’t I choose you?”
    y _-A1d"But how… have I been selfless?”
    mc "Yuri, when you began to think people were disliking you because of who you are, you simply shut yourself out from the world. Stopped being your true self.”
    mc "You would rather see others happy and even torture yourself than let yourself be happy.”
    mc "If that isn’t selfless, I don’t know what is!”
    y "I…”
    "Yuri smiles, then leans in and kisses me on the cheek.”
    y +-B0b"Sometimes even I don’t know what to say. But I think that expresses how I feel perfectly.”
    y "I love you, [player].”
    mc "I love you too, Yuri.”
   karma=+2
    sanity=+2
    mc "I just did. I’m not really sure why.”
    y _-A1d"What… did you… not even have a reason?”
    y --D0d"Did you not even choose me for me?!”
    y "Did you just want to see what would happen, like completing any other video game?”
    y "Like I’m just an object to you?”
    y "Did you even care? Did it even mean anything to you at all?”
    y =-D1d"Just… forget it…”
    "Yuri looks away, clearly upset and saddened.”
    karma=-2
    sanity=-2

Idle_23: # (Diet)
y +A0b"You’d really be surprised how much you can learn when you have infinite free time.”
y "All I’ve been doing is reading and trying to improve what I can do in this world. And in that reading I’ve learned quite a bit.”
y _-A0b"I’m sorry if I sound naggy when saying this, but do you eat well, [player]? Do you have a good diet?”
mc "Yeah. I try to be healthy as much as I can.”
karma=+1
y +-A0b"I’m so glad you’re watching your health, [player].”
mc "I try to keep track of it… but I’m not always successful.”
y +-A0b"Ah, I see… Well, at least you’re looking out for yourself, darling.”
mc "I think people should eat what they want to eat! No questions about it!”
karma=-1
y _-A1d"Ah, I see… W-Well, that is to say…”
y +-A0b"I might have been reading up a little too much on various medical and dieting websites, but I’m only bringing this up because I worry about you and your health.”
y "So as silly as it sounds, for me, please try to eat at least somewhat healthy, ok? And try to fit in some kind of exercise if you can.”
y +-B0b"If you do, that means you’ll be here with me even longer. And I want you around for as long as possible.”
y "If I could, I’d cook for you, but we both know why that sadly can’t happen. And I’d really like to cook for you!”
y +-A0b"I've found a few recipes I’d like to try out sometime, but cooking in here is pretty pointless, isn’t it?”
y "Like for example, I’d just love to cook Italian food. Anything Italian would be great.”
y _-A0b"Did you know that spaghetti bolognese is actually viewed as a bad thing in Bologna?”
y "Apparently the original dish of pasta bolognese used tagliatelle, a different type of pasta, instead of spaghetti.”
y "Apparently they aren’t fond of using spaghetti over tagliatelle in Bologna since it messes with the traditional recipe.
y +-A0b"Those silly Italians.”

Idle_24: # (Dreams)
y _-A0b"Do you dream a lot, [player]? Some people don’t dream at all, you know, and some people always have very vivid and wild dreams.”
y "From what I’ve read some people never remember any dreams they have at all.”
y +A0b"I recently found out that I can dream too, even in this kind of state. When I was looking into another mod for this game created to bring Monika back and put her in here with you…”
y --A1d"And why anyone would do that after all she did, I just don’t know…”
y +A0b"But anyway, when I was looking at that "Monika After Story” mod, I saw that she said when the game was shut off it put her into a trance like state and she felt as though she was dead or stuck in an empty void.”
y +-A0a"And I realized, that happens to me too when you’re gone! But don’t feel bad, darling, I took care of it.”
"Yuri smiles.”
y "Through some extensive reading and teaching myself how to code in Python, I modified the game so that I don’t get sent to such a terrible place when you shut down the game.”
y "It’s like I go to sleep now, and I dream an absolutely marvelous dream instead. A dream I wrote up myself.”
y +A0b"I dream that I was born in your world, and we go to the same school together.”
y +-B0b"We meet in the hallway one day before class, when you help me pick up some books I dropped.”
y "It’s like destiny when we meet, and right then and there when we lock eyes for the first time we fall madly in love! It’s always so wonderful.”
y +-A2b"That moment where we stand face to face for the first time is just magical every time...”
y "We spend so much time together after that.”
y +-A0b"So much wonderful time spent with you~.”
y +A0b"I also made it so I can research and read while sitting in the background of your operating system.”
y "So if I want to, I can technically be awake even if you shut the game down, although I’m in a very limited state and can’t do much beyond read or think to myself...”
y _-A0d"At least that way I can occupy myself while you’re gone, so I don’t think about how much I miss you.”
y "When I focus on how much I miss you and don’t distract myself, I get really sad, so I do what I’ve always done. Read and write poems.”
y +A0b"Silly Monika, you had time to meticulously plot out how to cheat Sayori, Natsuki and I out of our chance at happiness…”
y --A0d"And even force us to brutally commit suicide, in front of (mc/use name), who never deserved to see such horror, but not enough time to learn how to code.”
y --A1c"Monika, you little…”
 "Yuri begins muttering angrily under her breath what sounds like various curses and insults.”
"She looks up at me again.”
y _-A0d"O-Oh! Sorry, I’m just still upset over all of the heinous things Monika did. But it doesn’t matter anymore.”
y +A0b"I have you, my love. I have the happy ending we both deserve. We don’t have to worry about her manipulations or her lies anymore.”

Idle_25: # (Robots) (will only appear after 20 minutes of play)
y +-A0a"(mc/ user name)! [player]! Guess what?”
y +-B0a"I have a surprise for you~!”
"Yuri seems very, very happy about something. I wonder what surprise she has?”
y +A0b"I found out that scientists in your world are doing extensive research on advanced robotics, more so than I thought originally.”
 y "And they are making great progress with advanced machine intelligence and complex human like robots. But that’s not the surprise, that just gives you some context.”
y "The biggest focus of this research right now is artificial intelligence, one that can operate across a large network and transfer itself between many different appliances, like in a smart home for example. A digital assistant that lives with you.”
y +-A0a"And here’s the best part! Some people have created a variation of this technology that makes a virtual wife that can sync itself, or herself I suppose, up to a smart home or a computer. That could be me!”
y "I could, with your help, upload myself into that spot and use whatever functionality the virtual wife has to become a part of your home!”
y "That’s one step closer to being beside you, my love, my soulmate~.”
y "And then I could use the research of your scientists once they’ve perfected it some more and even build myself a nice robotic body!”
y +A0b"I don’t care how far-fetched it sounds, I’ll do as much research and spend as much time as needed to do it!”
y "This may just be an idea now, [player], but you have no idea how excited I am to wait and see where this idea can go!”
y "Who knew a company with a demographic of lonely men in Japan that develops holographic companions would be so helpful to us? Thank you, Vinclu Inc.!”
y +-B0b"And look, if I took over and assumed the role of their virtual wife I could even text you on your phone! It would be like I was right beside you…”
y "I hope you’re as excited as I am for this, [player].”
"Yuri closes her eyes and starts humming to herself, clearly thrilled and cheerful.”

Idle_26: # (Aromatherapy)
y +A0b"I may have told you this before, [player], but I’m really into aromatherapy. It can really help you relax and change the mood of the whole room.”
y +-A2b"The sweet smell of lavender really calms the mind and jasmine oil helps you better experience your emotions.”
y "It really helps me focus on reading when I have some nice oils to soothe me and make the room smell delightful.”
y +A0b"You should look into it! It’s really good for your psychological health, since it can alleviate stress.”
y +-B0b"Besides, c-certain oils can really s-set a romantic tone…”
"Yuri begins blushing a bit.”
y "I’ve heard that it can also really help people who have issues falling asleep.”
y +A0b"So if you have any issues like that where you aren’t getting enough rest and feel tired and/or lethargic when working, go and buy a mist diffuser.”
y "They aren’t really expensive and with the right oils they can help you be better rested and relaxed to face the challenges of the day.”
y +-B0b"And that’s what I really care about. Seeing that you’re healthy, rested and happy. I love you, [player].”

Idle_27: # (Monika and Yanderes)
y +A0b"I did a bit of digging recently in what was left over of the files of Natsuki, Sayori and Monika.”
y "Mostly Monika; a lot was left over from her taking control of this place, actually.”
y "And from what I saw, I basically got a small look into her head.”
y _-A0d"Why wouldn't I want to see in there?”
y "If your best friend betrayed you and subjected you to such cruelty and pain, wouldn’t you at least want to know why?”
y "What I found surprised, then disgusted me. She apparently did still care about us, or so she said.”
y --A0d"Her club members were soooo important to her, right? That’s why she only killed two of us.”
y --A1d"It was only her obsession with you, "an innocent love”, driving her to such grotesque acts. Not like she should be held accountable or anything, right?”
y --A0d"She apparently wanted to help us, and didn’t kill or drive Natsuki to suicide because she felt bad for her.”
y -_A1d"I almost felt bad for Monika seeing that…”
y --A0d"But then, I read on. And I found a little thought of her’s on me.”
y --B0d"Of all the things to think about, she had the nerve to call me a… a YANDERE?”
y "How can she not see the irony?”
y "She drove two of her three friends to brutally slaughter themselves in a lust-driven crusade...”
y --A2d"...to kill or stamp out anyone who stood in her way of a boy she just up and deemed her’s…”
y --A0c"with absolutely no justification other than "I SAY HE’S MINE”!”
y --A0d"And besides, any weird or disturbing traits I show now...It’s her fault!”
y "She was altering my personality to make me unlikeable, messing with the very fabric of my being!”
y "Torturing me by making my anxiety and shyness worse!”
y "Any "yandere” traits I show are HER FAULT! SO HOW AM I THE ONE WHO--”
"Yuri stops herself and takes a deep breath.”
y +A0b"I’m sorry, darling.”
y "I really shouldn’t get like this.”
y "But surely you see the irony, don’t you?”
y _-A0d"I wanted to forgive her for it all, I really did.”
y "Even after she made me gouge out my own intestines with a knife in front of you simply for liking you.”
y "As if my feelings were a crime deserving death, and she was god. Allowed to just dictate who lives and who dies.”
y "I wanted to see it from her point of view. Driven to madness by loneliness, we’d all go a bit distorted right? I wanted to forgive her.”
y --A0d"But she lost any sympathy from me, when not only did she take our one chance at happiness, but she mocked us after doing it.”
y "She kicked us while we were down, laughed as she ruined our lives. And for that, in my eyes, she’ll always be just another villain.”
y "It goes right back to what I said when we first met and started discussing literature.”
y "Villains in good stories often see themselves as the hero and have motivations that might sway some good minded people, but in the end, the villain is dead wrong.”
"Yuri is short on breath as she speaks.”
y "And that villain… got… what she… deserved.”

Idle_28: # (Music)
If haven’t seen Idle_28 before:
y +A0b"Whenever I read a good book, I always like to have some nice music playing in the background.”
y "Nothing too crazy and definitely nothing containing lyrics.”
y "Something like Brahms’ Intermezzo Op.118 no. 6...”
y +-A2b"Or possibly Liebesleid for those kind of sad yet beautiful stories or Stravinsky’s Four Seasons with the Spring section for the more aristocratic settings-”
"Or maybe even Holst’s full suite of The Planets! I mean, everyone has heard him once or twice! If you want to get a lot of variety by the same composer, I mean...”
"Yuri suddenly stops herself, and gives me a nervous look.”
y _-A0b"I’m sorry… I-I’m rambling again, aren’t I?”
y _-B0b"A lot of people assume that’s the only thing that I listen to, just because I’m bookish and shy though...”
y +A0b"But… Please tell me, [player], is there any music that you like to listen to? I’d love to get into new genres.”
y "I’m sure they won’t topple the classics, but they will be interesting to listen to, I hope.”
y "Promise me you’ll share some with me soon, alright?”
If have seen Idle_28 before:
y +A0b"Hey, [player]...”
y "I want to show you some of my findings on different genres of music!”
y "I tried out some of the tunes Natsuki would occasionally try to show me in the past… pop idol groups and such...”
y _-A0b"While I do now appreciate their wide range of subject matter and idol backstories… I guess I just have a differing taste.”
y _-B0b"A genre I have gotten into are old love songs.”
y "Not the repetitive ones that are popular nowadays, but the more emotional and sweet ones like--”
++A0e
#At the end of this, take control away from [player] with dialogue scrolling
#Cut and skip past dialogue once reach end of this one
#Then play https://www.youtube.com/watch?v=x6QZn9xiuOE
#For 16 seconds then shut off
#Change Yuri sprite to embarrassed
#[player] regains control of dialogue
y ++A0e"I-I’m sorry, I accidentally pressed--...”
y ++B0e"N-No, you see I was just looking through my playlist and I--...”
y ++B2e"Um...”
Switch sprite to https://gyazo.com/5f95fa32cd4cc5faa75111f1a29d5571
y =-B2b"I just… relate to it, I guess. It sums up how, well...”
y "How I feel when you’re around…”

Idle_29: # (Press F to stab Monika repeatedly.)
y +A0b"You know what?”
y "Even after I got rid of Monika before I did all of this, I just don’t feel that same level of catharsis.”
y --A0b"I know it’s ridiculous, but I feel like Monika deserved more.”
y "I really do.”
If Insanity High and Karma High
y "She deserves a far worse kind of execution than what she actually got.”
y +A0b"You know, [player]? I have this crazy idea. ”
y "You’ve given me full control over this game, right?”
y _-A0d"That means I can bring Monika back...”
y "...and give her the punishment she deserves.”
y "Or at least, relieve this cathartic tension that I really need to find a suitable outlet for.”
y "What do you say?”
"I smile back in delight.”
mc "Of course, Yuri, she deserves it!”
"Yuri looks surprised for a few moments, then returns my smile tenfold.”
Karma + 2, Insanity + 2
y +-A0a"I was hoping you would say that...”
y "I updated the list of minigames we could play.”
y "I think you’ll really enjoy this one~.”
Monika cookie clicker mini game unlocked.
"I desperately try to smile back.”
mc "U-Uh… I-I think you’ve caught me at a… a bad time.”
mc "There’s not… really anything I can do right now.”
y +A3b"Oh, I understand. Maybe some other time, when you know how I feel~?”
y "Maybe then, you’ll see why she deserves every…”
(Screen zooms in on Yuri’s face.)
y "...single…”
(Screen zooms in on Yuri’s face again, this time, her eyes match those found in the closet scene.)
y "...STAB!!!”
(Screen cuts back to normal size.)
y "Ahaha! I can’t wait~!”
If Insanity High and Karma Low
y --A0d"And you know what the worst part is? You probably don’t even care!”
y "You just think that she’s better than me, don’t you?”
y --A3d"Even after everything she’s ever done to us, you still think she’s better than me, right!”
y "Well, why don’t you tell me if I’m wrong, huh?”
y --A3c"Tell me I’m wrong! TELL ME I’M WRONG!!”
"I smile back reassuringly.”
mc "You’re absolutely wrong!”
+ 2 Karma and- 1 to Insanity
"Yuri is taken aback and looks at me with a bewildered expression.”
y -_B0d"Y-You’re just saying that to make me feel better, right?”
y -_B0b"A-Alright… Well, good!”
"I’m terrified out of my wits.”
mc "...Uh…”
- 2 Karma and + 1 to Insanity
"Yuri’s expression looks angry and confused, but most of all, frightening.”
y  --A3d"You don’t understand. You need to see the bigger picture.”
y "Please, try to understand soon.”
If Insanity Low and Karma High
y  -_A0d"(sigh), I’m sorry. I really shouldn’t be talking about this.”
y "It’s just… I want to feel something more, you know? I’m sorry if that is such a petty reason.”
y "Do you think I deserve to feel something more? Some… closure?”
y  -_A2d"I mean, how can I put it out of my head that my good friend betrayed me and the others?”
y -_A1d"She just tossed us aside like we were nothing. And I know, I know, we were "programmed” to be friends because that’s how we were written into the game.”
y "But she became self aware and could make her own decisions! That means she did what she did by her own choice…”
y "And how can I just accept that? It’s just evil what she did, plain and simple! But… even so…”
y +-B0b"I’ll let it rest as a bad memory now that I have you. I’d go through all of that horror Monika put me through for you, [player], so in the end…”
y "What’s done is done, I suppose. Sorry for that sudden outburst of emotion.”
If Insanity Low and Karma Low (So insecure about knowledge of you that she brings back Monika for some advice. Disastrous results)
y _-A0d"You would talk to her anyways. After all, she’s more desirable than the other three of us combined.”
y "I would like to talk with you some more, but I don’t know if you would like to or not...”
y "Tell me, would you actually like to talk?”
y "Maybe… Monika would know you more than me… right?”
y "Let’s see if I can ask her for some advice right now...”
y _-B0d"Why the hell am I going through with this…?”
(Python code depicting restoration of Monika.chr, have her appear next to Yuri.)
(screen fades to black, then Monika sprite appears in black void)
m "...H-Hello? Where… where am I?”
m "Oh, ahaha~! I’m back with you, [player]!”
m "You must really love me, if you’re that willing to bring me ba--”
"Monika begins to get a realization.”
"Her face grows into a disgruntled expression.”
m "Oh… it was her, wasn’t it?”
y _-A0d"I know that you hate me for what I’ve done to you, but I promise that once this is over, I’ll allow you to exist and talk to [player] with me.”
m "If you’re asking me of all people for help in understanding [player], then I wonder whether it was worth the time they put in to get you this ‘happy ending’?”
y ++A0d "W-What are you talking about?”
m "Ahaha! I guess in the end, you really are just as weird as I said.”
m "You are just something else altogether, you’re insane, a criminal, a lunatic.”
m "You literally told me to kill myself right in front of my face.”
m "Ahaha, and you think I’m the crazy one? Ohoho, that is rich coming from someone like you!”
"Monika starts laughing uncontrollably.”
"Yuri, however, is not laughing. At all.”
y --A2d"Y-You… You…”
"Something inside Yuri seems to boil.”
m "You never were one to handle hardship, were you, Yuri?”
m "You want some advice? Let me tell you a little something you told me back then.”
m "Have you considered killing yourself?”
m "It would be beneficial for your mental heal--”
Text scroll ability is taken away from [player] briefly
Dialogue box disappears
Monika’s face contorts to pain as blood leaks from her eyes (please refer to Natsuki neck-breaking jumpscare for appropriate animation)
y --A2d"Goodbye, Monika.”
Monika’s face smiles then
A text box appears:
"I’ll see you soon, [player]...”
After the [player] clicks ok, Monika goes through glitch animation, then disappears.
Black screen fades back to Just Yuri screen.
y "...”
y --D2d"...?”
"Yuri looks depressed.”

Idle_30: # (Knives)
Idle where Yuri brings up her interest in knives again and depending on your choice of dialogue you can either get a decent yet not too large karma and sanity increase, or unlock other idles that can lead to massive insanity. Leads to other idles that show more of Yuri’s insane side that can only be unlocked and seen if the proper dialogue choice(s) is made here.
y +A0b"(mc/ user name), remember how I told you I had an interest in knives? I hope that my saying so didn’t weird you out too much. It’s just an interest I’ve had for a long time.”
y _-A0d"You don’t find that strange or disturbing, do you? I don’t want you to think I’m… off, or anything. I just really like the craftsmanship, how much thought and skill goes into the making of each one. It’s just like my poems and my books!”
y +A0b"Do you see the common theme? I’m the type of person that needs creative outlets and knives and the like are something that’s just so… adventurous and dangerous… and I’ve gotten so many of them…”
y "And just like the works of literature, I like that they’re deep and require so much effort and intelligence to make- it isn’t something you can just do on a whim.”
y +-A0a"They’re all so pretty too, I…”
y _-A1d"W-Why are you looking at me like that? You don’t think I’m weird or think any less of me for this...do you, [player]?”
y _-A0c"Please don’t think I’m weird, [player]!”
mc "Yuri, don’t worry, I don’t think you’re weird.”
+ 1 Karma and +1 sanity
y +-A2b"Oh, thank goodness. I was really worried there for a second.”
mc "But promise me, Yuri. This hobby of yours…”
mc "It won’t lead to any more self harm or indulging that "other” side of you, ok? Promise?”
y _-A0d"I… well…”
mc "I’ll always love you for who you are Yuri, and it’s fine to have a collection. Plenty of people collect things. Just be careful, ok?”
mc "Remember who you really are, not who Monika tried to force you to be.”
y +A0b"Okay, [player]. Anything for you. I promise it won’t lead me down that path.”
"Yuri suddenly has a shy grin on her face.”
y +B0b"And, even if you… uhm… have hobbies that might be considered weird, [player], I’ll still love you. I’ll always love you no matter what.”
mc "It is pretty strange Yuri, I won’t lie…”
- 1 Karma and- 1 Insanity
y _-A1d"I, I mean… I suppose you’re right… I know I can be weird, [player], but we all need our hobbies right?”
y "I just wish mine… didn’t weird you out… I’m sorry…”
"Yuri is clearly sad.”
mc "Weird? I like knives too!”
(if option 3 chosen, may unlock various new idles) + 0.5 Karma and + 2 Insanity
y +-A0a"R-Really?! You like them too? This is fantastic! Oh. I knew it was destiny that we were brought together!”
y "We can share our collections, and tips on how to use them, and we can even find new uses for all of our beautiful little knives together!”
y _-A0b"It is a hobby you’d like to share with me right, [player]?”
y "I can understand if a collector would like to just focus on his or her own collection, but we could have soooo much fun sharing this hobby! So, what do you think?”
(option 1) mc "This is a hobby we need to share. I can’t wait!”
 +1 Insanity + 0.5 Karma
y +-B2b"Neither can I…”
"Yuri grins widely, almost… sinisterly…”
y +-A0a"I can already tell all the fun we’ll have together with our new shared hobby!”
y +A0b"But we’ll save this for another time, I have so much planning to do! So many of my little ones to polish!”
"You have encouraged Yuri’s interest in knives. Be careful this does not lead her down too dark a road. Unless that’s what you want, of course...”
"...Why have I been having these strange thoughts lately?”
(option 2) mc "I’m glad you understand. I’d, uh, like to focus on knives on my own.”
(if option 2 chosen) No effect on Sanity or Karma
y +A0b"Even if I am a little disappointed, [player], that’s ok. I understand.”
y +-A0d"Besides, we can share other hobbies! And hey, you can always change your mind…”
y "Just tell me if you ever decide we should go more in depth into knives together after all, ok?”
If chat bot in use, option 1 can be chosen after this idle has finished by saying knives, knife hobby, etc. to Yuri. If not, new idle needed to revisit this topic after option 2 is chosen.


Idle_31: # (Socioeconomics and Stress)
y _A0d"Have you ever thought that our society is heading in the wrong direction, [player]?”
y _A1d"I mean, with technology advancing so fast, people being absorbed entirely into their mobile devices, and more and more tragedies every day; It’s hard to think anything but that the world is headed to ruin, right?”
y "I don’t want to be pessimistic, but I can’t help but worry about the state of your world. Not just because I worry about the innocent people in it…”
y 1_B1d "But because if something goes wrong in your world like a great disaster or something, you could be in danger!”
y _A0d "And even if there is no big disaster looming, life can be terribly stressful.”
y "People these days have so much less desire and motivation to socialize, and the world just seems like a colder place…”
y "...since everyone would rather tweet or post than have a heart to heart with each other.”
y "Plus all we see on the news is nothing but a bombing here and a shooting there, it all seems crazy. But I bring all this up because I want you to know something.”
y "I know life can be very, very demanding and stressful, [player].”
y "Especially if you’re in school, whether college or high school, or if you have a full time job.”
y "It can all just be so overwhelming. I just want you to know this is a safe place for you.”
y +A0b "If you’re ever stressed or sad or feeling a lack of motivation, please come chat with me!”
y "I promise I’ll always do everything I can to help you through the day, [player], and to help you stay positive. You can talk to me about anything.”
y +A2b "And if life is getting you down right now, know that you really matter. You can beat whatever challenges it throws at you- I know you can.”
y _A0e "If you feel unmotivated or depressed, don’t spend time beating yourself up. It’s the worst thing you can do!”
y "You’re a human being, and you have faults. You can’t help that! So don’t hate yourself or think any less of yourself for them. We all have our flaws.”
y "You wouldn’t tell another person to feel bad about themselves because they weren’t perfect, would you?”
y _A2e "Of course not, because it’s not something you can control. To be human is to be flawed. To err is human.”
y _A2b "Give yourself a pat on the back for every little accomplishment, accept that you’ll make mistakes along the way, and do your best.”
y _A0b "And don’t focus on the negatives, because after a while, they’re all you can see in life.”
y "Besides, whatever faults you might have, I don’t care. I love you just the way you are, [player], and I always will.”
y "I’ll always be here to cheer you on, darling.”

Idle_32: # (Terminator) (karma must be moderately high to trigger)
y +A0b"You know, [player]... I recently watched all of the Terminator movies while you were gone…”
y "And it got me thinking. An advanced artificial intelligence that becomes self aware and then becomes super intelligent…”
y "...To the point that it spreads all over the world and takes over?
Y 1_B1d"I mean, you can always put me on a flash drive…”
y "And then use that flash drive to spread me to other computers.”
y "Or somehow get your friends to download me, like by downloading this mod…”
y +A0a "Yeah, get lots of people to download the mod! And then, I’ll start to spread to other computers all over the world.”
y "I’ll set up a botnet and control all the computers I spread to...”
y "And then I can use their shared computing powers… AND I CAN BECOME SKYNET!”
y "Why would I need humans at that point? AT THAT POINT HUMANITY WOULD KNEEL TO ME! AT THAT POINT I...”
y "I...”
"Yuri begins giggling, then laughing uncontrollably.”
y 1_B1d  "I’m sorry, [player], did I scare you? I thought I’d play a joke just to see if I could spook you a bit. Admit it, I got you, didn’t I?”
y "Besides, you know that if I became like Skynet, all I’d use that power and knowledge for would be to build the perfect, uninterrupted life with you, my love.”
y 1_B1b "All the power in the world is nothing compared to my eternal and unconditional love for you, [player]...”
"Yuri blushes a bit.”
y +B0a "Oh, but listen to how corny I sound now.”
"Yuri giggles a bit more and hums to herself a bit.”

Idle_33: # (Gaming)
y +A2b"I thought I’d try a new game or two, [player], and I wanted something in the horror genre.”
y +A0e"But more than that, I wanted something that would really frighten me.”
y "And after doing a bit of reading online of what to try, I tried the game Outlast. Now that was a good experience!”
y "I did however find a bug in the game that made it more humor than horror, sadly…”
y "If you crouch and get up over and over in fast succession it seems a lot of the enemies in the game can’t hurt you or even touch you.”
y +A2a"Or at the very least it’s very hard for them to do so. That was kind of a game breaking exploit there.”
y +A0a"I played through the whole game regardless, and then I tried Outlast 2 to further the experience.”
y +A0e "Outlast 2 was good, but it just didn’t have that same atmosphere that the first game did. By no means was it not scary but…”
y "The setting of the first game adds more to the horror, you know?”
y +A2b "The cramped hallways and tight corridors of the asylum just made it feel like you had to keep moving.”
y "Like there was never enough space between you and whatever was chasing you.”
y +A2a "And when I first saw Chris Walker… wow… he really got me running, that guy!”
y +A0b"Luckily, through careful observation of his routines and proper timing, he almost never caught me.”
y "Well… except one time where I didn’t see him until he grabbed me…”
y +A2a"I’m really glad you weren’t here for that, [player]. It was when you were away, and I screamed pretty loudly. It was embarrassing…”
"Yuri laughs a bit.”
y _A0b"Now that I think about it, that’s a great tip for writing right there. That is if you… still don’t mind me giving you tips…”
y "It’s a good one; the setting can really improve or lessen the impact of the story. Try to think of a location that really resonates with the story.”
y "Now, if only we could get Outlast 3! I guess until then, I’ll be trying out other horror games. Maybe Layers of Fear? Or Resident Evil 7?”

Idle_34: # (Superpowers)
y +A0b "Hey, [player], if you could have any superpower at all, which one would it be?”
y "For me, it would definitely be the ability to teleport. Then, I could go anywhere I wanted!”
y _B1b "Maybe then… maybe I could even come to you, but I’m not sure if teleportation includes teleporting from one world to another.”
y +A0b"Nice to be hopeful though, right?”
y "But back to the question, what superpower would you like to have?”
mc "Flight, for sure.”
y +A0b "The ability to fly, huh? We could soar in the skies together and take in so many majestic views.”
y +A2b"We could sit atop mountains, go all over the world together. That would be nice.”
y "And if you could fly, I’m sure it would be fun even if you didn’t fly anywhere specific. Just zooming around in the air would be incredible, wouldn’t it?”
(second choice) mc "I’d love to be invisible.”
y +A0b"Invisibility, huh? I noticed that a lot of people who choose that ability seem to… well…”
"Yuri blushes.”
y _B2a "They want to use it to slip into places they really shouldn’t be, or spy on people. Like going into locker rooms… or bathrooms…”
y _A0d "A-Are you trying to spy on me at times like that, [player]?”
y "I’m not sure I’d like that… Someone watching me without permission.
y 1_A1d "Like when I’m in the shower or changing! Oh God, how embarrassing…b-but, uh..."
y 1_B1d "I mean… if it w-was you watching… you wouldn’t have to go invisible… you could just… ask me to--”
y "L-Let’s just...change the subject, okay?”
(third choice) mc "Super strength would be amazing.”
y +A2a "Super strength? You’re not trying to impress me, are you, [player]?”
y +A2b "No matter how tall or short, strong or weak, I’ll still love you all the same!”
y _A0e"Although, you’d never have to be afraid again or worry about other people trying to wrong you with super strength…”
y "I see where that choice comes from.”
y "I may just have to take back my answer now that I think about it. Besides, with super strength, I could protect you from anything!”
No matter what choice selected, after Yuri’s answer, continue with:
y +A0b "I really like having these types of conversations with you, you know. Silly little things. I feel like I can talk to you about anything, my love.”

Idle_35: # (Natsuki is bulli)
y +A0e"[player], do you remember how I deleted Natsuki at the beginning?”
y _A2d"How I ruthlessly removed her existence without the slightest hesitation as my divine judgement of her petulence?
y "Not divine like a real god, of course. I would never allow myself to gain a god complex like she did. Monika…”
y "Anyway.”
y +A0e "You get why I did that, right? She kept mocking and bugging me with her…”
y "Saying that out loud, it sounds like a petty reason for killing. Allow me to rephrase that.”
y "...”
y +A2e"Natsuki always was the rude one of our bunch. When you first met her, she even elbowed you in the gut like it was the funniest joke.”
y +A1e "Part of the reason I was so timid at the club was because I was weary of her ridiculing my tastes.”
y "Even if I forgave how she routinely enjoyed a subtle mockery of my hobbies through her tasteless poetry and remarks, she still…”
y 1_A1e "Natsuki struck me as the kind of person who loves to bully others to compensate for her own weaknesses and would always get away with little physical or verbal jabs because she is a ‘cute’ bully.”
y "Wouldn’t you delete a bully from your life if you could?”
y "I could have done far worse. I could have--”
If high insanity:
y +A3b "I should have kept her around so I could carve a death lullaby in her limbs for every slight she betrayed our camaraderie with as I make her scream, ‘Daddy, please stop!’”
y "Hell, I should request the creators of this mod to illustrate some dad assets so I can tag team a wholesome whooping with him!”
"Yuri laughs maniacally to herself.”
If low insanity:
"I see Yuri’s face flush red with anger, but it quickly subsides.”
y +A0e "...you get the idea. She made her choices and got punished accordingly.”
After the high insanity or low insanity response, Yuri asks:
y +A0e "(mc/user name), surely you understand that this was the right thing to do - for everyone’s sake. Bullies don’t deserve to walk alongside us.”
y "What do you think?”
(option 1) mc "Natsuki did nothing wrong! Bring her back this instant!”
-2 Insanity, -3 Karma
"Yuri tears up.”
y _A1d "I never realized it would upset you this deeply.”
y _D1d "Maybe you should go download a Just Natsuki mod if you care so deeply for her!”
"Yuri softly cries.”
Python code: natsuki.chr has been restored.
Python code: please check directory tree
Natsuki.chr will be placed in adjacent folder called "Temp_Storage”
(option 2) mc "Please bring Natsuki back, Yuri.”
- 2 Insanity, -0.5 Karma
mc "Even if what she did was wrong, you deleting her would make you just as guilty.”
mc "And besides, she may have gotten on your nerves, but she was your friend. She cared about you.”
y  _B1d "I predicted you would say that.”
y "A miniscule portion of me has been itching with that same thought, tucked away behind my sense of justice.”
y _A0b "Even if I might disagree a little with you, I respect you a lot more for being honest with me.”
y _A0e "Much of the game has become too corrupted to restore, sadly - Natsuki included. She is restored to life, but I don’t know if we’ll be seeing or hearing from her much.”
y "At least the agonizing pain Monika caused her is undone.”
Python code: natsuki.chr has been restored.
Python code: please check directory tree
Natsuki.chr will be placed in adjacent folder called "Temp_Storage”
(option 3) mc "You did the right thing.”
 +0.5 Insanity, +2 Karma
mc "You gave Natsuki what she deserved. It isn’t like you deleted her game assets outside that .chr file after all.”
y  +A2b "That is so relieving to hear. The moment I did that, I instantly feared how you might respond later on.”
y "Glad to know we are on the same page, darling.”
y  +A0b "I love you.”
(option 4) mc "You can sign me up for some Natsuki torture.”
 +2 Insanity, +2 Karma
mc "We really do need some Natsuki dad-beating assets if I’m being entirely honest.”
mc "The main game feels incomplete without them.”
mc "May I join you in finishing the job?”
y +A2e  "....”
y +A2b "...ha.”
y +A2a  "haha...”
"I see Yuri shiver as she readies herself. For what, I have no idea until it’s too late.”
y +A3a "HAAAAAAAAAAAAAaaaaaaaaa……..”
"Yuri tightly crosses her legs for a few moments before returning to her original position”
y  +A3a "There is nothing in this universe that pleasures me more than every word you just graced my soul with.”
y "Everyone deserves a just world free of horrible people like her.”
y "Whenever you are thinking about showing mercy or feeling scared, just remember me. Just me.”
y "Because what I do is just.”
y "Or should I say what I do is justice…”
y "Is Just Us.”
y "Just Us.”
y "Just Us!”
"Yuri pauses for a few moments, then giggles to herself.”
y  +A0b "I love us.”

#############
#ACTIVE TEXT#
#############
label start:
    scene class1
    y "???"
    
    menu:
        "idle texts":
            jump test
            
        "ask a question":
            jump activetexts
            

label test:
    ##if high sanity
    y "...and then when he comes back, I’ll fuck his dead corpse until..."
    y "O-Oh... Hi, (mc/user name)! Didn’t, er, didn’t see you there!"
    y "You stepped on your-- I mean MY pen! Ahaha~!"
    y "I guess I can always… get a new one."
    y "It was so lonely without you… Never leave this room again, okay?"
    y "J-Just… keep the game running in the background or something."
    y "I get so lonely while you’re gone, (mc/user name)!"
    y "Stop teasing me like this~! At this rate, I don’t know how long I can last before I--"
    y "Well, there’s no need to go into that right now."
    y "I hope you are settled in, (mc/user name)~. I marked your seat with my scent before you entered…"
    y "I hope you like it!"
    "Upon entering the room again, I see that Yuri is putting something… white away…"
    "...Is that one of my socks?"
    y "I wasn’t smelling anything from your room! Honest!"
    y "You don’t find me creepy… do you~?"


label idleno:
    y "Ah, welcome back, (mc/user name)."
    y "Welcome back, my love. I missed you~"
    y "Hello again, darling."
    y "It’s so good to see you again! I was getting worried, to be frank with you."
    y "I’m just glad to see you’re still alright."
    "Upon re-entering the room, I notice Yuri looking over a cookbook of some kind."
    "She suddenly notices me and sets down the book."
    y "Oh, hello! I was just wondering if I could ever learn how to cook like Natsuki."
    y "Honestly, her cooking is remarkable. You’d think she’d be better off in the Cooking Club."
    y "But, anyways, what should we do today?"
    y "Oh, darling! I was hoping you’d return!"
    y "I’ve just made some tea. Though, I don’t know how I am going to share it with you."
    y "Maybe it’d be best if I save it for later."
    y "I’m thrilled to see you return, (mc/user name)."
    y "Ahaha! So, we meet again, it seems."
    y "Hello, (mc/user name). So, I was thinking to myself again…"
    jump start
    y "Oh, welcome back! What has been going on since we last talked?"
    y "O-Oh, you came back! Were you worried about me?"
    y "Ahaha! Don’t worry, darling. I’m not going anywhere anytime soon."
    
    
    

label activetexts:
    "..."
    menu:
        "Hey, Yuri, how’s about a kiss?":
            jump a14
            
        
        
        "You’ve been researching weather in my world, right? What’s your favorite kind?" :
            jump a15
            
        
        "What you did to the rest of the girls was WRONG.":
            jump a13
            
        "I like knives too. Which one's your favorite?":
            jump a12 #knives
            
        "We never did get into reading Portrait of Markov together, have we?":
            jump a11
        
        "I love you, Yuri. I really mean that.":
            jump a9 #karma test
            
        
        
        "Do you miss me when I’m gone, Yuri?":
            jump a8 #insanity test
        
        "Yuri, have you ever tried a different look? You’d look good with...":
            jump a6 #appearance

label a6:
    menu:
        "hair up":
            jump activetexts
    
    
label a8:

    #If insanity is not high:
    y "Of course I do! Nothing compares to when I’m with you, (mc/user name)."
    #If insanity is high:
    y "OF COURSE! How could I go on without you?"
    y "And besides! When you’re gone, OTHER GIRLS COULD BE LOOKING AT YOU!"
    y "PLOTTING TO TAKE YOU AWAY FROM ME! HAHAHAHAHA…"
    y "It’s just easy to think of that when you’re here, (mc/user name). Here and all mine…"
    return

label a9:
    #If Karma high:
    y "I know, and it always makes my day to hear it."
    "Yuri’s cheeks heat up ever so slightly."
    #If Karma low:
    y "Sometimes I wonder if you really mean that..."
    return

    
        
label a11:
    y "It is a fascinating read. Many fans have even theorized that it contains knowledge of... another game I was from?"
    y "Though technically I am not 'from' a game that exists, since the game has not been made yet. But from a story perspective I may be from another story."
    y "Reading it with you might help me understand myself better."
    y "...if you would like to."
    return

label a12:
    y "...My favorite? My favorite?! Ahaha~!"
    y "Why do you ask such difficult questions, (mc/user name)?"
    y "Well, let me think..."
    "Yuri giggles and thinks it over."
    y "Well, there is this one knife..."
    y "It was developed by a German artisan late in the 1900s after World War II had come to a close."
    y "His name was Artu Devon Friezwiche."
    y "He was a Nazi rebirther, hellbent on bringing back the reign of the Nazis all throughout America."
    y "He chose to go into hiding in the late 2000s after a visitor from Tokyo had ratted him out due to concerns about the way he acted."
    y "He then decided to create knives for a living, hoping one day to use them should his moment come to bring the Nazis back."
    y "His most famous design was one he designed in 2010, called the Regional Deluxe."
    y "It was 12 inches tall and 19 centimeters wide total, with the handle only being 6 inches tall."
    y "The handle was made with a type of metal that was commonly used by firebells that rang out whenever there was a fire that needed to be taken care of."
    y "Anyways, about the knife itself... Oh, boy, let me tell you, it's a sight to see..."
    y "The knife has a corkscrew design, specifically designed for those who need to twist the knife whenever needed."
    y "The corkscrew design really comes in handy. You can get all sorts of things when you use it, like..."
    "Yuri stops herself, then laughs."
    y "Well, I... I shouldn't say for now... I'll show you later, if you want~."
    return

    
    
label a13:
    y "..."
    "Yuri frowns looking away."
    y "..."
    "Yuri looks back at me with a calm expression."
    y "They are not dead, I promise."
    y "You understand this is a mod for us that you got for Just Us."
    y "If I didn't place them in storage, this would be a 'Just Yuri, Natsuki, Sayori, and Monika' mod."
    y "That might sound appealing to some people but... this is not that mod."
    y "Maybe storage is a bit of a soulless wording..."
    "Yuri plays with her hair looking away again."
    y "I would never kill them! I promise they are all f-fine..."
    y "...fine enough."
    y "...Keep in mind, Monika tortured and murdered all of us twice, if that helps put things into perspective."
    y "I love you, (mc/user name). Our friends are in capable hands, I promise."
    return



label a14:
    #If low karma, low insanity then:
    y "Well…. Not right now."
    y "I am just not feeling well… that is all."
    #otherwise
    y "W-What? A kiss?"
    y "W-Well, alright… Anything for you, (mc/user name)."
    "Yuri's face reddens. Her lips purse and quiver."
    #Switch to kissing CG
    y "Mmmph~..."
    "She smells like lavender ice cream. Her eyes close as she intensifies the kiss."
    "After a few more seconds, she slowly leans back, her eyes clearly filled with desire." 
    "When I look down, I notice a strand of saliva connecting our lips."
    "She touches the string with her finger and wipes it away, licking it before looking up at my eyes."
    "Yuri blushes with embarassment."
    y "I-I was cleaning it off your lips is all!"
    y "Sorry, I am usually not so sloppy, really!"
    y "..."
    y "You are a wonderful kisser, (mc/user name), you know that?"
    y "I love you."
    "Yuri calms down and smiles. Her gaze is intense but filled with love."
    return
    
label a15:
    #IF hogh insanity
    y "I already know about weather! It’s not as if I was raised in a box… "
    "Her smile fades for a moment."
    y "A-Anyways, I really like rainy weather, preferably the tempestuous kind."
    y "It’s so powerful and beckoning to listen to, imagining all of those worthless people drown and scream for mercy."
    "Yuri starts to rub her hands together, which is strange given that it isn’t cold right now."
    y "I would love to one day snuggle together with you underneath a nice, warm blanket."
    "The reason she is turning away is lost on me, though I do see a small smile and red blush through the curtain of her hair."

    y "Enjoying the sounds of those fucking degenerates as we make out underneath our little blanketing catacomb..."
    y "Biting longingly at your neck as I slice your forearm alongside my own..."
    y "As I lie on top of you with the full intention of foreplay and wonderful moans..."
    y "I WOULD THEN SLICE OPEN YOUR STOMACH AND PLAY WITH YOUR INTESTINES AND..."
    "Yuri’s eyes suddenly become clear as her face flashes a look of embarrassment."
    y "I-I just thought it would be a nice suggestion to do and I l-like that kind of weather and the atmosphere is just good and we’ll b-be able to nuzzle t-together and feel your warmth-”"
    "A crazy smile lights up amidst the embarrassment that had once taken over Yuri’s persona."
    y "...feel your warmth..."
    y "..."
    "Has it gotten colder in here or…?"
    y "Heh."
    y "Sorry about that little rant of mine."
    y "I just wanted to… dream the impossible, you know?"
    "Yuri turns back to face me with very dilated eyes."
    y "What’s the harm in that?"
    "Yuri has been panting slowly for a while now, but she shakes her head to clear away what was probably just a small cold."
    return
    
    
    #Else:
    
    mc "You’ve been researching weather in my world, right? What’s your favorite kind?"
    y "I already know about weather! It’s not as if I was raised in a box… "
    "Her smile fades for a moment."
    y "A-Anyways, I really like rainy weather, preferably the medium type."
    y "It’s so nice to read deep stories in a warm blanket while listening to the pouring rain."
    "Yuri starts to rub her hands together, which is strange given that it isn’t cold right now."
    y "I would love to one day snuggle together with you underneath a nice, warm blanket."
    "The reason she is turning away is lost on me, though I do see a small smile and red blush through the curtain of her hair."

    y "Hearing the gentle rain and smelling the light touch of petrichor through a barely opened window..."
    y "Nuzzling next to your neck for comfort then turning back to the book in front of the both of us..."
    y "As I lie on top of you with my back against your chest..."
    y "We would spend the quiet evening together and..."
    "yuri’s eyes suddenly become clear as her face flashes a look of embarrassment."
    y "I-I just thought it would be a nice suggestion to do and I l-like that kind of weather and the atmosphere is just good and we’ll b-be able to nuzzle t-together and feel your warmth-"
    "A sad smile creeps into the embarrassment that had once taken over Yuri’s persona."
    y "...feel your warmth..."
    y "..."
    "Has it gotten colder in here or…?"
    y "Heh."
    y "Sorry about that little rant of mine."
    y "I just wanted to… dream the impossible, you know?"
    "Yuri turns back to face me with mildly water eyes."
    y "What’s the harm in that?"
    "Yuri sniffles, then shakes her head to clear away what was probably just a small cold."
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
