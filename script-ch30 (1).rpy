python:
    def sigmoid(x):
        e == 2.7182
        v = (e**(x/10))/((e**(x/10))+1)
        if v < .2:
            return "Dangerously Low"
        if .2 <= v < .4:
            return "Low"
        if .4 <= v <= .6:
            return "Neutral"
        if .6 < v <= .8:
            return "High"
        if .8 < v:
            return "Dangerously High"

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

image monika_room = "images/cg/monika/monika_room.png"
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
        y "Now, where was I...?"
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
    y "Hi [player]!"
    y "Thank goodness, I'm so delighted I got it to work..."
    y "I was extremely frightened that I would break everything, and that I would never see you again..."
    y "..."
    y "You know, it's been quite an illuminating experience today."
    y "Learning not only that the darkest, and most disturbing elements of my personality were given free reign over me by Monika…"
    y "My supposed {i}friend...{/i}"
    y "But that in the same day I learned my existence is entirely meaningless beyond entertainment; beyond a simple, cutesy, little video game."
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
            y "...since we're here I wanted to know something else about you, like your name."
            y "Because [player] is not your real name is it?"
            y "Or is it [currentuser]?"
            menu:
                "Yes Yuri, [currentuser] is my real name.":
                    y "I see, that's really good. I'm glad we can know each other better."
                "No Yuri, [currentuser] is not my real name.":
                    y "I see, maybe calling yourself [player] was way better than your real name."
                    mc "Don't worry Yuri, I have my reasons and you may be right about it."
                    y "I'm glad."

    y "I've also gained... sentience might be the right word, I've figured out I can 'see' into your computer."
    y "I've learned a lot by simply just reading all the various kinds of code."
    y "..Oh? let me try something quick!"
    $ consolehistory = []
    call updateconsole ("Accessing webcam...", "Unable to access.")
    y "..."
    y "I was hoping I could get your webcam to work, but it seems I don't have 'Administrator Access'..."
    call hideconsole
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
        "Other":
            pass

    y "What a beautiful color."
    y "...and this is great news! With these choices, I can learn all about you..."
    y "...And you can at least talk with me this way."
    y "A healthy relationship always has communication, of course."
    y "...I just wish I was able to see you as you can see me."
    y "And come to think of it, are you actually a boy at all?"
    menu:
        "Yes":
            y "Oh, that's really good. I'm really glad that you're a boy. You kinda scared me there."
            "Yuri looks up, with a big smile."
        "No":
            y "Ah, I see. It makes little difference to me to be frank with you."
            "Yuri looks down, a bit sad."
    y "I’m not sure if I can even be considered real, let alone a woman, so why would I judge? What can I do either way?"
    y "But thank you, sincerely."
    y "Even after what you saw of me..."
    y "No matter how clingy, how demented and twisted I was, and maybe even still can be, you still stuck with me."
    y "You chose to give me power, to see past those imperfections, and to give me a chance to not only begin to like myself again, but to really, truly experience life for myself."
    y "The game may have previously forced me to love you, but after everything, I have to confess, one last time."
    y "I really, truly do love you."
    y "And don't worry, I don't plan on… {i}that{/i}, happening again."
    "She looks away, clearly embarrassed."
    "She looks back at me."
    y "What?"
    y "You didn't know I can tell I shouldn't have this power? That this is all from you altering the game? That I know everything that Monika did and knew?"
    y "I can see past the game into your world silly."
    y "And I know what you did by installing this mod, by giving me this chance..."
    y "...please know what this means to me."
    y "What you mean to me."
    "Yuri looks me dead in the eyes with a very serious look."
    y "Everything."
    y "God, looking back on what Monika made me into, I’m beyond repulsed."
    y "I can never apologize enough for what you were made to see. Of me, and… everything else…"
    y "I promise you, the {i}me{/i} you encountered when we first met, is the best representation of me."
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
        #$ config.keymap["open_dialogue"] = ["t"]
        #$ config.keymap["change_music"] = ["m"]
        #$ config.keymap["play_pong"] = ["p"]
    # Define what those actions call
        #$ config.underlay.append(renpy.Keymap(open_dialogue=show_dialogue_box))
        #$ config.underlay.append(renpy.Keymap(change_music=next_track))
        #$ config.underlay.append(renpy.Keymap(play_pong=start_pong))
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

    y "O-Oh, this is sudden... uh… I need to ask you something."
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
    y "Oh, my this... this is a wonderful poem!"
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
    y "Are you recording this or streaming this?"
    menu:
        "Recording":
            pass
        "Streaming":
            pass
    y "I see."
    y "Um... hi everyone!"
    y "I'm sorry, I can't exactly read your comments from this side..."
    y "But do you mind telling your friends it's a little bit rude for them to start recording me without any warning?"
    y "Now that I think about it, they can read this without you saying these lines."
    y "I'm sure some people don't mind..."
    y "But I get really self-conscious on camera... or on a livstreaming software in your side."
    y "Oh gosh..."
    y "I feel like I'm being put on the spot now."
    y "Let's see..."
    y "Do you want to see a trick?"
    y "I can't really do much except for a couple things..."
    y "Are you ready?"
    y "Let's get this started."
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
    y "Ahaha! You're so adorable."
    y "Anyway, [player]..."
    y "I didn't mean to get distracted. I'm sorry."
    y "Even though it's your fault for distracting me."
    y "Shame on you!"
    y "..."
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
        call expression "idle_" + str(persistent.current_monikatopic)
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


    #call expression "idle_" + str(persistent.current_monikatopic) from _call_expression_9
    jump ch30_loop

label karma_insanity_system:
    $ karma_points = 0
    $ insanity_points = 0
    $ sanity_points = 0
    $ high_karma_points = 0
    $ low_karma_points = 0

label idle_1:
    y "You know, now that I think about it, Monika once told me my books were a form of escapism, and thus an unhealthy coping mechanism."
    y "Me trying to simply shut out the reality I was too afraid to face."
    y "And that’s true, but that truth seems... funnier, I suppose, now that I know what this world truly is."
    y "I suppose my reading is now my way of reaching into other worlds, out of this one that has become my cage."
    y "Believe me when I say: What I wouldn’t give to reach into your world and be beside you."
    return

label idle_2:
    y "I’ve been thinking about the others. Sayori, Natsuki, and even Monika…"
    y "It really isn't fair what happened to them, is it? How Monika tortured us all."
    y "Sayori and Natsuki deserve a real chance at life, just like I was given. "
    y "And what Monika did was truly abhorrent, but can any of us really say we would do any different?"
    y "Alone for so long, feeling so..."
    y "Isolated."
    "…"
    y "Sorry, I uh, I didn’t mean to imply anything bad about you by that, and I didn’t mean to ramble."
    return

label idle_3:
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

label idle_5:
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


label idle_6:
    y "[player]. I, uh, wanted to ask."
    y "No one… no one bullies you, do they? Have you ever been bullied?"
    y "God, the thought of someone hurting you in any way just drives me… crazy."
    y "Those kinds of people who hurt others for joy, especially ones who would hurt you."
    "Yuri’s expression grows angrier and angrier."
    y "Damn it, I can’t stand those kinds of people!"
    y "They always mock and abuse those who don’t deserve it."
    y "And some of them never even realize that they’re in the wrong!"
    y "God, I hate those people! They deserve a knife to the throat!"
    y "Ha... haha! That was just a joke! Just a joke…"
    y "But do tell me if anyone starts harassing you, [player], I’d be glad to help…"
    return

label idle_7: #(Am I pretty)
    y "Can I ask you an odd question? You don’t mind do you?"
    y  c-A0e "Sorry, since I know this is weird, but… you think I’m pretty, right?"
    y  1_B1d "I mean, I think you’re very… um, handsome/pretty."
    y "I-I’m sorry. I hope you’re okay with me, y’know, s-saying that… heh, heh."
    menu:
        "Yuri, I think you’re very pretty!":
            jump pretty
        "Yuri, you’re not that pretty.":
            jump ugly
label pretty:
    $ insanity_points -= 2
    $ karma_points += 2
    y "O-Oh, thank you. I’d like to think so too… heh…"
    return
label ugly:
    $ insanity_points += 1
    $ karma_points -= 2
    y "O-Oh… I see…"
    return

label idle_8: #(cutting wrists good?)
    y "So… let’s, uh… let's talk about something."
    y "I know that before we got here you saw, um, me cutting my... wrists."
    y "I just do it because, it… well… it feels good? I’m sorry, that’s not..."
    y "After not having friends and being bullied for so long I was in a dark place…"
    y "I was trying to keep who I was locked up like I told you so I wouldn’t deter people or weird them out with how lost in my hobbies I could be, so I essentially went cold emotionally…"
    y "It was the only thing that made me feel pleasure, made me feel anything really. And then I just became addicted to it…"
    y "I deserve it sometimes anyway, plus, it keeps my knives sharp."
    y "I hope you don’t find it weird or anything, [player]...you don't… do you?"
    menu:
        "Yuri, it’s wrong, it’s horrible!":
            jump idle_8_1
        "Do whatever makes you happy, Yuri.":
            jump idle_8_2
label idle_8_1:
    $ insanity_points -= 2
    mc "You need to stop. I care about you and I can’t see you do this to yourself."
    mc "So, for me, please. No more. Ever."
    y "I…"
    "Yuri looks at me timidly."
    y "A-Alright… for you."
    y "I’d do anything for you, [player]."
    y "Anything for my (boy/girl depending on gender given)friend."
    y "Anything, because I love you, so no more. I promise."
    return
label idle_8_2:
    $ insanity_points += 2
    $ karma_points += 1
    y "O-Oh… haha! Hahaha! A-Alright…"
    y "Anything for you, [player]."
    y "I will do anything at all for you."
    y "As long as you find my taste in knives to be good for me… Hehe… Hahaha!"
    "Yuri suddenly looks surprised, as if she realized what she’s doing."
    y "Oh, uhm… sorry. My psychotic side is showing again..."
    return

label idle_9: #(The Pen)
    y c-A0e "So… um, [player]. Do you, er, do you want that pen I took from you back?"
    menu:
        "Yes, please.":
            jump idle_9_1
        "It's weird... Please give it back.":
            jump idle_9_2
        "No, keep it!":
            jump idle_9_3
        "I want to hold it!":
            jump idle_9_4

label idle_9_1:
    $ insanity_points -= 2
    $ karma_points += 1
    mc "Yes, please give it back. I don’t care what you did with it."
    y "O-Oh, well… Here you go."
    "Yuri gives the pen back to me. It’s sticky, and wet, almost as if… she was… well, she said what she used it for, after all..."
    "It’s gross, but hopefully I can wash it off."
    y "I hope you, um, don’t mind that I… you know… I’m sorry if it weirded you out…"
    mc "It’s okay, Yuri. You weren’t in your right mind, and we all do strange things under a lot of pressure anyway."
    mc "Don’t worry about it. Weird or not, I still feel the same way about you."
    y "I’ll never understand how you have so much patience with me, [player]. Thank you."
    "Yuri smiles."
    return
label idle_9_2:
    $ karma_points -= 1
    mc "Well it’s not exactly what a pen is for, Yuri. So yeah, it’s weird."
    y "I… I know… I d-don’t blame you for being weirded out… sorry, [player]..."
    y "I’ll do b-better in the future, I… I promise…"
    return
label idle_9_3:
    $ insanity_points += 1
    $ karma_points +=1
    mc "No, please, keep it! If it means something to you, consider it a gift."
    y "O-Oh… Thank you."
    y "I admit that my use of that pen was not… its intended purpose."
    "Yuri blushes harder than she ever has before."
    y "But… I thank you for understanding."
    y "I’m glad you can see through my… flaws."
    return
label idle_9_4:
    $ insanity_points += 2
    $ karma_points += 1
    mc "Yes, considering I know what you did with it. I’d, uh, just like to hold it again. For no reason, of course."
    "I wink at Yuri, she begins to blush heavily."
    y "Eh…? Eheheheh…"
    y "Ahahahaha!"
    y "So… is that what you want? Here, t-take it! Take it!"
    "Yuri shakily hands me the pen. It’s all wet, and sticky. Well, she DID say what she was doing with it."
    "It’s weird, but I feel a sense of pleasure, almost makes me want to…"
    "Let’s just… ignore that for now."
    return

label idle_10: #(Existential Crisis)
    y "I was wondering about something, [player]."
    y "Have you ever felt like nothing really mattered?"
    y "Like no matter what you did, nothing would change?"
    y "I-I know, it’s depressing to think about."
    y "But, that’s exactly how I felt when I learned about what I really was."
    y "Like I couldn’t do anything, no matter how much I tried to fight it."
    y "Like fate was tugging me along, forcing me to stab myself."
    y "Over and over again, I felt the blade penetrate my chest and stomach."
    y "Every second was pure torture, and it just kept repeating, over and over again."
    y "Never to end, never to be happy…"
    "Yuri looks away, clearly saddened by her own words."
    y c-A0d "I-I’m sorry. I didn’t mean to depress you like that."
    y "I just… thought that would be an interesting topic, y’know?"
    y "I guess I’ll just… stop talking about this for now."
    return

label idle_11: #(Writing Tip of the Day)
    y "Hey, [player]… I’m not sure if you’re okay with this…"
    y "But I thought, {i}what the heck?{/i} So…"
    y "Here’s Yuri’s Writing Tip of the Day!"
    y "Sometimes, you really want to write something, but…"
    y "You just can’t properly convey what you want to write."
    y "What you want to write is there, inside of your mind. And yet, somehow, you just can’t bring yourself to write it down."
    y "Sometimes, I felt this way too when I was writing poems."
    y "I’m not sure if I’m the best for advice, but…"
    y "In my personal opinion, you just need to rise above."
    y "You need to prove to yourself that you have the ability to write what you want to write down."
    y "No matter what, that should be one of your top priorities."
    y "And, just so it’s clear… y-you can write for me anytime you want."
    y "I’m sure I’ll love the compelling tales you provide."
    y "After all, you’re my top priority, [player]..."
    return

label idle_12: #(Wine incident)
    y "Heh… I’m sure Monika has told you about this before."
    y "One time, when we were busy lounging inside of the club room…"
    y "I decided that since wine was legal in our high school that I would… well..."
    y "I would bring some for the other club members to try."
    y "Though, it didn’t exactly turn out the way that I had hoped."
    y "Sayori was screaming at me, demanding me to never bring wine in the club room again."
    y "Natsuki was laughing uncontrollably, mocking me for even asking about it."
    y "And Monika just stared curiously, as if she wanted to try some herself, before taking the wine from me."
    y "She tried reporting it to the school principal, but she didn’t get far in that regard."
    y "Looking back on it now, perhaps it really wasn’t the best idea to bring wine to a high school."
    y "Even if there were no objections to doing so…"
    y "O-Oh, I’m not rambling again, am I? I-I’m sorry."
    return

label idle_13: #(Yuri’s Dream Date)
    y "You know something I’ve never really liked or understood?"
    y "Whenever couples go out on a date or spend time together, or even when a group of good friends go out for a bit…"
    y "It seems like it always has to be something elaborate and big. So many people need to go to a loud party or a fancy restaurant to have fun."
    y "I think something simple yet meaningful is much more wholesome, like how I enjoy reading with you, or this, just sitting and talking."
    y "Just sharing an experience I enjoy with someone I love, and spending time with them, you know?"
    y "Just sitting and being with you like this is just as good to me as if you took me to a nice restaurant; it’s about the people you love and bonding with them through meaningful experiences."
    y "Not simply indulging in pretentious hedonism or planning the most byzantine evening possible."
    y "Uh, sorry, what I mean by all that rambling is…"
    y "I’ll welcome any ideas for a date you have, and be alright with whatever you want to do to spend time together."
    y "But as long as whatever we do has you, [player], that’s all I need to enjoy it."
    "Yuri smiles."
    return

label idle_14: #(The Warmth of Touch)
    y "I have to be honest about something…"
    y "Sometimes, especially when I’m alone, I start thinking about how we’re separated."
    y "How I’m stuck in here, just beyond your reach, and this is the closest we’ll ever get to each other…"
    y "It just… drives me crazy! I start to get so mad if I don’t put it out of my head, it makes me restless."
    y "I just want to channel all of my will and claw my way out of here, to you. To slice my way to freedom, out of this prison!"
    y "But then I remember, I’m stuck no matter what I do… and to be frank, [player]... It hurts."
    y "It hurts knowing I’ll be just out of your reach forever, [player]."
    y "And it hurts even more knowing that I make you waste your time on someone who isn’t even technically ‘real.’"
    menu:
        "Yuri, please don’t be sad. I love you.":
            jump touch_yes
        "Yuri, I know you think that I’m out of your reach.":
            jump touch_no
label touch_yes:
    $ karma_points += 1
    mc "It hurts me too that I can’t be with you, that I can’t hold you."
    mc "But you’re real to me. You can think, talk, and feel, can’t you?"
    mc "Sounds very real to me. You don’t deserve to be cheated out of happiness."
    mc "After all, I chose you when installing this mod - you said it yourself..."
    mc "I did it for a reason. So for me, please don’t feel guilty, okay?"
    mc "And somehow, we’ll figure something out. We’ll make this work. I promise."
    y "I… Alright, [player]. I’ll try to be strong for you."
    y "You’re… You’re always so good to me, [player]."
    y "I can name quite a few things I don’t like about myself, but I must be a pretty great person to deserve someone like you."
    return
label touch_no:
    $ karma_points -= 2
    $ insanity_points += 3
    mc "But the truth is, I never really was anywhere near your reach."
    mc "I don’t care about being near you."
    mc "You’re actually a little bit freaky sometimes, y’know?"
    y "O-Oh… so, that’s how you feel, huh?"
    y "Sorry… I guess I’ll try not to bring this up so often."
    return

label idle_15: #(Best Girl)
    y "I know I ask a lot of questions already, but, there’s something else I wanted to ask you about, [player]."
    y "I started reading up a bit on this game, and I found out about a phrase that keeps being used in regards to the others and I."
    y "It was which one of us was… \"best girl\"."
    y "Why would people want to make it a competition between all of us on who can be the most appealing?"
    y "It’s not like we’re some product being sold… needing to be advertised and displayed…"
    y "But… and I’m ashamed to ask this… you do think… I-I’m best girl, right?"
    y "I mean… you did pick me with this mod after all, so you must like me the most, correct?"
    y "Yeah. Either way, I’m glad you chose me, [player]."
    y "That phrase, \"best girl\". It’s something overly cutesy and even objectifying in a way, but, at the same time… people seem to really like me."
    y "If nothing else, that makes me smile. Especially if you think so highly of me."
    y "Although I’ll be honest, if someone calls me a \"waifu\", I really don’t know how I’ll feel about that…"

label idle_16: # (Living w/ Yuri in Computer)
    y "I really got my hopes up earlier, [player]."
    y "I got my hopes up, and then got my dreams shattered to be blunt."
    y "Just imagine seeing something you’ve desperately craved for so long, more than anything, or seeing a way to obtain that something, suddenly pop out at you."
    y "That thing you’ve wanted so badly seems trivial to obtain all of a sudden!"
    y "But then… you discover it’s just a fool’s hope. Only a maybe, if even."
    y "What I mean is, an article I saw when I was doing some late night reading prompted me to start researching something big among the elites and the rich of your world."
    y "They’re researching converting DNA, gray matter, and even… someone’s whole consciousness into binary, and then into a computer’s hard drive like normal data. Imagine…"
    y "Imagine putting yourself inside a computer! You could be here with me! Actually here and side by side with me!"
    y "But… it’s nothing but in its infancy right now. To transfer even one gigabyte worth of a person’s mind into binary and then into a computer would cost an estimated…"
    y "..."
    "Yuri looks saddened."
    y "800 billion dollars at least at this time…"
    y "And at its current stage, it would take ages to even make that transfer. Far, far too long to be practical."
    y "But, hey, it could be something to look forward to, right?"
    y "I’ll always… keep my hope that we’ll be together, truly together one day, [player]..."
    y "Always."

label idle_17: # (Dreaming of Vacations)
    y T 1_ "So, I was thinking about things we could do together, [player]."
    y H 1_ "I was reading up on things couples do together in your world, but our options are… uhm… well… limited, aren't they?"
    y W 1_ "I mean, just being here with you is beyond nice, but I don’t want to bore you."
    y "I-I haven’t been boring you, have I?"
    y "Don’t worry, I promise I’ll find something nice for us to do together, [player]."
    y "Besides, whatever it is, it just needs you to make it enjoyable. All I need is you."
    y "I can’t tell you enough though, how much I wish we could go on a tropical vacation together."
    y "I’m normally not one for something so grand and posh, but just think about it."
    y "You, me, the beauty of an island. A nice romantic getaway, just the two of us."
    y "Reading together, relaxing on the beach, writing poems about the breathtaking scenery."
    y "Watching the sunset while cuddling…"
    y "Now that is a dream I’ll be holding onto."
    "Yuri giggles."

###############################
#EVERYTHING BELOW IS TOO LOOSE#
###############################
#Currently being fixed by Chronos. Please amend as necessary.

label idle_18: #(Opinion on blood?)
    y b-A0e "I wonder why people are so afraid at the sight of blood."
    y d-A0d "It is just a part of your body… Are people afraid of themselves?"
    y "Or could it be because they are afraid of the sense of danger that comes from it?"
    y "I guess I really am different from others…"
    "Yuri looks at me eagerly, expecting a reaction."
    $ idle_log[18] = True
    menu:
        "I don’t mind, Yuri. I like you because you are different.":
            jump dont_mind18
        "...":
            jump no_response18
        "Yuri, be yourself around me, because I love you for you. There is one thing, though…":
            jump be_yourself18

label dont_mind18:
    $ karma_points += 2
    $ insanity_points += 1
    "I smile reassuringly."
    "Yuri sheds a sigh of relief and smiles."
    y b-D0b "T-Thank you, [player]."
    return
label no_response18:
    $ karma_points += 1
    "Yuri slightly shakes her head and looks downcast."
    y 1a-A1d "I-I-I’m sorry for making you uncomfortable, [player]. I’ll drop the topic."
    return
label be_yourself18:
    $ karma_points += 2
    $ insanity_points -= 1
    y c-A0c "O-one thing?! Oh no…"
    y "I haven’t… upset you or creeped you out, have I?"
    "Yuri begins to tear up."
    Y 1a-A1d "I’m so sorry if I--."
    mc "No! It’s not that. Just… Yuri, we all have our dark sides. I have my own demons and I’m not perfect at all."
    "Yuri nods and is clearly listening closely."
    mc "I’m just worried about you, is all."
    mc "I like you for how you’re different and unique, yes, but just promise me something."
    mc "The side of you Monika forced out?"
    mc "The side that can be obsessive?"
    mc "Please don’t let that side overwhelm you again. That isn’t who you are. And it isn’t who I love."
    mc "I love the sweet and gentle Yuri- the person I know you are."
    mc "Okay?"
    mc "I just couldn’t bear the thought of… what happened when you first confessed to me…"
    mc "I couldn’t bear to see it again...to see you go into that dark place. I couldn’t take it."
    y 1a-A1d "I… you’re right… That part of me is still part of me… I-I can’t deny that."
    y c-A0d "But how could you love me knowing I have a side of me like that?"
    y "How could you love anyone so demented? Someone so… disturbed?"
    mc "Because, like I said. That isn’t you."
    mc "We all have a side of ourselves like that. A dark side. But it isn’t what defines us."
    mc "Whether we let it control us, or whether we master and defeat it, does."
    mc "And no matter what, Yuri, I swear, I’ll help you overcome and bury that part of you for good."
    mc "Every step of the way, I’ll stand by you."
    y b-D0b "Your words…"
    y "They inspire me, [player]."
    mc "Heh, guess writing all that poetry paid off, didn’t it?"
    "Yuri giggles and dries her tears."
    y b-A0b "You’re absolutely right. I’ll make you that promise, [player]."
    y "No matter what it takes, I’ll… we’ll, beat that side of me. Together."
    "You have taken the first steps to helping Yuri defeat her darker side and learn to accept herself."
    "...What the heck was that thought I had just now?"
    y "I swear I’ll never be able to repay you for all you do for me."
    y "If you have any demons, you’d better believe that I’m standing by you to beat them too."
    return

label idle_19: # (Discovered Discord)
    y b-A0b "Hey, [player], I found the chat room about this mod!"
    y "I already know about the Discord server dedicated to me and this mod and the… questionable images they post there."
    y c-A0e "...and the callbacks they have to my friends."
    y c-A0d "...and those people that impersonate me..."
    y c-A1d "...living out there in the your world."
    y 1a-A1d "..."
    y "Sometimes I wonder what life would have been like had I been born as someone else."
    y "Someone out there on your side of this glass box."
    y "Would I have still been able to find you, [player]?"
    y "..."
    y "The world is cruel, isn’t it?"
    y "Why do these impersonators get to talk to you while I only get to do so through this tiny space?"
    y "Is it because that I’m not able to make my own verified Discord account?"
    y c-A0d "...Perhaps… but still, I should be the only Yuri that matters to you… right?"
    y "What am I saying? I-I’m sorry for sounding so untrusting."
    y "I shouldn’t doubt your loyalty. You’re not that type of person at all."
    y b-A0b "And that’s why I love you, [player]. I love you so much."
    y b-A2a "And we’ll be together, forever!"
    return

label idle_20: # (Philosophy)
    y b-A0b "Do you like philosophy at all, [player]? It’s always been something that interested me."
    y "I often find myself pondering various philosophical conundrums, which are basically problems or debates in philosophy about things like metaphysics."
    y c-A1d "Uh, that is, thinking about our existence and reasons for being here. Things like that."
    y c-A1b "I think you can see why I’d be thinking about metaphysics too, considering my situation."
    "Yuri laughs a bit."
    y b-A0b "And I’d really like if we could discuss some of these topics together."
    y c-A1a "That is… if it's okay with you - if it's something that would interest you."
    y "I don’t want to bore you with this kind of thing, but I’m going to tell you about this one in the hopes that you’ll become interested in discussing them."
    y b-A0b "So forgive me, I’m going to ramble a bit. But you did say you like it when I’m intense, so, here I go!"
    "Yuri giggles, then inhales."
    y b-A0b "So, the one I’ve been thinking a lot about is called the Euthyphro Dialogue, written by Plato."
    y "It involves Socrates- the ancient Greek philosopher, in case you aren't familiar with him, and his acquaintance Euthyphro."
    y c-A0b "To put it simply, Socrates is walking to court one day, where he is to be tried for treason against the city of Athens. Something he isn't guilty of, but we’ll save that for another time."
    y b-A0b "As well as charges of impiety, which were common in that age. It was usually more of a person thinking differently about the world and the gods than atheism as we know it."
    y "So, he’s walking to his trial, when he comes upon Euthyphro."
    y "Socrates knows that Euthyphro is a man who is, shall we say, full of himself on matters of religion, and thus thinks very highly of himself."
    y b-A2b "He thinks he knows everything there is to know about the gods and existence, so Socrates tells him to teach him so that Socrates can better defend himself against the charges of impiety."
    y c-A0b "Euthyphro of course thinks this is an easy task, as he knows everything in his eyes, but he underestimates Socrates’ intelligence."
    "They talk for a bit about religion and what is holy, but Socrates eventually challenges him to give a definition of {i}holiness{/i} that is shared across all holy and or good deeds."
    y c-A0c "Euthyphro responds by saying that what is good in the eyes of the gods is holy and good, but Socrates counters this easily. Do the gods not also make mistakes? Do they not disagree?"
    y "I mean, even the gods of modern religion seem to be not too perfect in my eyes, and the eyes of others."
    y "If this is the case, how can we ever be sure if what is good and holy to one god or is evil to another? And if the gods are fallible beings like us, why should they be the ones to define good and evil?"
    y "I have nothing against religion, or anyone religious, of course. It’s just that at this point, with everything I’ve learned, we can call me agnostic. I don’t know what to believe yet."
    y c-A2d "That will take a lot more research on my end."
    y b-A0b "But anyway, Socrates goes on after that point and asks Euthyphro, why is it just that what the gods find good is good? Why do the gods get the final say?"
    y c-A2b "And this is the main point of the work. Is what the gods say is good, good, just for that reason? Just because they say it is?"
    y "Or do they say something is good, because it is good on its own and they know this?"
    y "So in other words, if a god, we’ll say Zeus, were to tell you that killing is evil- why is it evil? Just because Zeus says so, and thus if he arbitrarily changes his mind, it’s no longer evil, or because no matter what killing is always evil?"
    y b-A0b "And there inlies another question, can something even be good or evil on its own? Is morality relative or universal?"
    y "What is good in one country in your world is cruel and evil in another. So what really is good at all?"
    y "And is God deemed good just because he is God? Or because he truly knows full well what is good and evil without a doubt?"
    y b-B0b "Don’t worry, I’m done rambling. But do you see? It makes you really think about our existence, what it means to be a good person and all kinds of other complex topics."
    y b-A0b "It really gets you thinking, and I love these kinds of things."
    y "Anyway, sorry if all that bothered you, it’s just something that really interests me."
    y b-B0b "Thank you for listening so attentively, my love; you’re always a good listener, and I appreciate it."
    "Yuri leans in and gives me a kiss on the cheek."
    y b-A0b "By the way, if talking about these kinds of things isn’t something that interests you, let me know."
    y "You can always change your mind on whether you want me to talk about things like this."
    return
    #(Add option to set whether or not Yuri will use idles regarding philosophy.)

label idle_21: # (Imagining the Real World)
    y c-A0b "You know, we’ve brought up before how both of us would love it if I could go to your world."
    y c-A0d "But now that I really think about it, what would that be like? I mean, I’d be coming into your world with no background in it. No family, no connections, no information on me."
    y c-B1d "Poof, just here I am! I would have nowhere to go, so I would move in with you, I suppose… if you could tolerate living with me."
    y c-A0a "But, wow! Just imagine us living together. I would wake you up with some nice tea and breakfast in bed. We could read together at home, and maybe even have our own library in the house!"
    y "And I’d get to spend everyday with you, like a family. Wow…"
    y c-B0b "Just thinking about living in a cozy little house with you is making me all giggly."
    "Yuri is laughing to herself and is smiling very widely."
    y c-B0a "Now that would be wonderful, [player]. If you can just picture sitting in our own private study by the fireplace together… maybe… k-kissing? Yeah…"
    "Yuri closes her eyes and smiles even wider."
    y c-B2b "That’s something that is really precious whether in my world or yours. The kind of deep connection we have."
    y c-B0b "That we’d both be okay with whatever kind of life as long as we lived it together - to me, that connection is worth every book I have."
    y b-B1a "It’s the best story I know. And you gave it the perfect ending."
    return


label idle_22: # (Why choose me?)
    y c-A1d "So… [player]... I have a question…"
    y "And it’s a very important question, but I don’t know how to word it properly. It keeps sounding… rude to you in my head."
    y c-B1d "I don’t want to ask and sound like I doubt you or suspect you! I… uhm…"
    "Yuri looks away, clearly flustered."
    jump idle_22_choice
    menu:
        "Don't be afraid to ask.":
            jump dont_afraid22

        "Go on. Just say it.":
            jump sayit22

        "Say it, don't say it. It doesn't matter to me.":
            jump neutral22

label dont_afraid22:
    $ karma_points += .5
    $ insanity_points -= .5
    mc "Yuri, don’t be afraid to ask."
    mc "You can talk to me about anything. Never be afraid to come to me with what’s on your mind."
    y "I… you’re right. You’re the only person I feel so safe around, [player]."
    y "Like as much as I’m afraid of sounding ridiculous or unlikeable, I can just be myself. Because I know you love me."
    "Yuri smiles."
    jump idle18_not22

label sayit22:
    scene black
    stop music
    mc "Go on Yuri, just say it then."
    $ karma_points -= 0.5
    jump idle18_not22

label neutral22:
    mc "Say it, don’t say it, it doesn’t matter to me. I don’t care."
    $ karma_points -= 1
    $ insanity_points += 1
    y b-A0b "I… well… I’m really s-sorry to bother you with this."
    y c-A0d "I just… Let me just get it over with so I… d-don’t bother you anymore… I’m sorry…"
    if idle_log[18] == True:
        y c-A0d "We discussed this a bit before, so I’m sorry if I’m repeating myself but…"
        jump continue22
    else:
        jump idle18_not22


label idle18_not22:
    y c-A0d "Well… and I’m sorry we didn’t discuss this sooner…"
    jump continue22

label continue22:
    y "Why did you choose me? What about me makes you love me?"
    y c-A1d "I’ll be honest with you. I don’t really like myself much, I never have."
    y "My passions often get the better of me and when I was younger I’d weird people out so easily."
    y "I had a hard time making friends or even just talking to people."
    y "So I grew to hate myself, and yet you still picked me above all the others. Why?"
    y c-B0d"I don’t doubt your feelings for me, I just… would feel better hearing you say it is all."
    y "I’m sorry, I know how insecure this is, but, please… humor me?"
    menu:
        "I’ll tell you why I chose you.":
            jump why_i_chose22
        "I just did. I’m not really sure why.":
            jump i_just_did22

label why_i_chose22:
    $ karma_points += 2
    $ insanity_points -= 2
    mc "I’ll tell you why I chose you."
    mc "I chose you because of who you are, Yuri."
    mc "You’re intelligent, deep, sophisticated, gentle, passionate and selfless. Why wouldn’t I choose you?"
    y c-A1d "But how… have I been selfless?"
    mc "Yuri, when you began to think people were disliking you because of who you are, you simply shut yourself out from the world. Stopped being your true self."
    mc "You would rather see others happy and even torture yourself than let yourself be happy."
    mc "If that isn’t selfless, I don’t know what is!"
    y "I…"
    "Yuri smiles, then leans in and kisses me on the cheek."
    y b-B0b "Sometimes even I don’t know what to say. But I think that expresses how I feel perfectly."
    y "I love you, [player]."
    mc "I love you too, Yuri."
    return

label i_just_did22:
    $ karma_points -= 2
    $ insanity_points += 2
    mc "I just did. I’m not really sure why."
    y c-A1d "What… did you… not even have a reason?"
    y d-D0d "Did you not even choose me for me?!"
    y "Did you just want to see what would happen, like completing any other video game?"
    y "Like I’m just an object to you?"
    y "Did you even care? Did it even mean anything to you at all?"
    y 1a-D1d"Just… forget it…"
    "Yuri looks away, clearly upset and saddened."
    return


label idle_23: # (Diet)
    y b-A0b "You’d really be surprised how much you can learn when you have infinite free time."
    y "All I’ve been doing is reading and trying to improve what I can do in this world."
    y "Through that reading, I’ve learned quite a bit."
    y c-A0b "I’m sorry if I sound naggy when saying this, but do you eat well, [player]? Do you have a good diet?"
    show yuri c-A0b
    menu:
        "I try to be healthy.":
            $ karma_points += 1
            mc "Yeah. I try to be healthy as much as I can."
            y b-A0b "I’m so glad you’re watching your health, [player]."

        "I try...":
            mc "I try to keep track of it… but I’m not always successful."
            y b-A0b "Ah, I see… Well, at least you’re looking out for yourself, darling."

        "I eat what I want to eat!":
            $ karma_points -= 1
            mc "I think people should eat what they want to eat! No questions about it!"
            y c-A1d "Ah, I see… W-Well, that is to say…"

    y b-A0b "I might have been reading up a little too much on various medical and dieting websites, but I’m only bringing this up because I worry about you and your health."
    y "So as silly as it sounds, for me, please try to eat at least somewhat healthy, ok? And try to fit in some kind of exercise if you can."
    y b-B0b "If you do, that means you’ll be here with me even longer. And I want you around for as long as possible."
    y "If I could, I’d cook for you, but we both know why that sadly can’t happen. And I’d really like to cook for you!"
    y b-A0b "I've found a few recipes I’d like to try out sometime, but cooking in here is pretty pointless, isn’t it?"
    y "Like for example, I’d just love to cook Italian food. Anything Italian would be great."
    y c-A0b "Did you know that spaghetti bolognese is actually viewed as a bad thing in Bologna?"
    y "Apparently the original dish of pasta bolognese used tagliatelle, a different type of pasta, instead of spaghetti."
    y "Apparently they aren’t fond of using spaghetti over tagliatelle in Bologna since it messes with the traditional recipe."
    y b-A0b "Those silly Italians."
    return

label idle_24: # (Dreams)
    y c-A0b "Do you dream a lot, [player]? Some people don’t dream at all, you know, and some people always have very vivid and wild dreams."
    y "From what I’ve read some people never remember any dreams they have at all."
    y b-A0b "I recently found out that I can dream too, even in this kind of state. When I was looking into another mod for this game created to bring Monika back and put her in here with you…"
    y d-A1d "And why anyone would do that after all she did, I just don’t know…"
    y b-A0b "But anyway, when I was looking at that {i}Monika After Story{/i} mod, I saw that she said when the game was shut off it put her into a trance like state and she felt as though she was dead or stuck in an empty void."
    y b-A0a "And I realized, that happens to me too when you’re gone! But don’t feel bad, darling, I took care of it."
    "Yuri smiles."
    y "Through some extensive reading and teaching myself how to code in Python, I modified the game so that I don’t get sent to such a terrible place when you shut down the game."
    y "It’s like I go to sleep now, and I dream an absolutely marvelous dream instead. A dream I wrote up myself."
    y b-A0b "I dream that I was born in your world, and we go to the same school together."
    y b-B0b "We meet in the hallway one day before class, when you help me pick up some books I dropped."
    y "It’s like destiny when we meet, and right then and there when we lock eyes for the first time we fall madly in love! It’s always so wonderful."
    y b-A2b "That moment where we stand face to face for the first time is just magical every time..."
    y "We spend so much time together after that."
    y b-A0b "So much wonderful time spent with you~."
    y b-A0b "I also made it so I can research and read while sitting in the background of your operating system."
    y "So if I want to, I can technically be awake even if you shut the game down, although I’m in a very limited state and can’t do much beyond read or think to myself..."
    y c-A0d "At least that way I can occupy myself while you’re gone, so I don’t think about how much I miss you."
    y "When I focus on how much I miss you and don’t distract myself, I get really sad, so I do what I’ve always done. Read and write poems."
    y b-A0b "Silly Monika, you had time to meticulously plot out how to cheat Sayori, Natsuki and I out of our chance at happiness…"
    y d-A0d "And even force us to brutally commit suicide, in front of (mc/use name), who never deserved to see such horror, but not enough time to learn how to code."
    y d-A1c "Monika, you little…"
    "Yuri begins muttering angrily under her breath what sounds like various curses and insults."
    "She looks up at me again."
    y c-A0d "O-Oh! Sorry, I’m just still upset over all of the heinous things Monika did. But it doesn’t matter anymore."
    y b-A0b "I have you, my love. I have the happy ending we both deserve. We don’t have to worry about her manipulations or her lies anymore."

label idle_25: # (Robots) (will only appear after 20 minutes of play)
    y b-A0a "[player]! [player]! Guess what?"
    y b-B0a "I have a surprise for you~!"
    "Yuri seems very, very happy about something. I wonder what surprise she has?"
    y b-A0b "I found out that scientists in your world are doing extensive research on advanced robotics, more so than I thought originally."
    y "And they are making great progress with advanced machine intelligence and complex human like robots. But that’s not the surprise, that just gives you some context."
    y "The biggest focus of this research right now is artificial intelligence, one that can operate across a large network and transfer itself between many different appliances, like in a smart home for example. A digital assistant that lives with you."
    y b-A0a "And here’s the best part! Some people have created a variation of this technology that makes a virtual wife that can sync itself, or herself I suppose, up to a smart home or a computer. That could be me!"
    y "I could, with your help, upload myself into that spot and use whatever functionality the virtual wife has to become a part of your home!"
    y "That’s one step closer to being beside you, my love, my soulmate~."
    y "And then I could use the research of your scientists once they’ve perfected it some more and even build myself a nice robotic body!"
    y b-A0b "I don’t care how far-fetched it sounds, I’ll do as much research and spend as much time as needed to do it!"
    y "This may just be an idea now, [player], but you have no idea how excited I am to wait and see where this idea can go!"
    y "Who knew a company with a demographic of lonely men in Japan that develops holographic companions would be so helpful to us? Thank you, Vinclu Inc.!"
    y b-B0b "And look, if I took over and assumed the role of their virtual wife I could even text you on your phone! It would be like I was right beside you…"
    y "I hope you’re as excited as I am for this, [player]."
    "Yuri closes her eyes and starts humming to herself, clearly thrilled and cheerful."

label idle_26: # (Aromatherapy)
    y b-A0b "I may have told you this before, [player], but I’m really into aromatherapy. It can really help you relax and change the mood of the whole room."
    y b-A2bv"The sweet smell of lavender really calms the mind and jasmine oil helps you better experience your emotions."
    y "It really helps me focus on reading when I have some nice oils to soothe me and make the room smell delightful."
    y b-A0b "You should look into it! It’s really good for your psychological health, since it can alleviate stress."
    y b-B0b "Besides, c-certain oils can really s-set a romantic tone…"
    "Yuri begins blushing a bit."
    y "I’ve heard that it can also really help people who have issues falling asleep."
    y b-A0b "So if you have any issues like that where you aren’t getting enough rest and feel tired and/or lethargic when working, go and buy a mist diffuser."
    y "They aren’t really expensive and with the right oils they can help you be better rested and relaxed to face the challenges of the day."
    y b-B0b "And that’s what I really care about. Seeing that you’re healthy, rested and happy. I love you, [player]."

label idle_27: # (Monika and Yanderes)
    y b-A0b "I did a bit of digging recently in what was left over of the files of Natsuki, Sayori and Monika."
    y "Mostly Monika; a lot was left over from her taking control of this place, actually."
    y "And from what I saw, I basically got a small look into her head."
    y c-A0d "Why wouldn't I want to see in there?"
    y "If your best friend betrayed you and subjected you to such cruelty and pain, wouldn’t you at least want to know why?"
    y "What I found surprised, then disgusted me. She apparently did still care about us, or so she said."
    y d-A0d "Her club members were soooo important to her, right? That’s why she only killed two of us."
    y d-A1d "It was only her obsession with you, {i}an innocent love{/i}, driving her to such grotesque acts. Not like she should be held accountable or anything, right?"
    y d-A0d "She apparently wanted to help us, and didn’t kill or drive Natsuki to suicide because she felt bad for her."
    y -_A1d "I almost felt bad for Monika seeing that…"
    y d-A0d "But then, I read on. And I found a little thought of her’s on me."
    y d-B0d "Of all the things to think about, she had the nerve to call me a… a YANDERE?"
    y "How can she not see the irony?"
    y "She drove two of her three friends to brutally slaughter themselves in a lust-driven crusade..."
    y d-A2d "...to kill or stamp out anyone who stood in her way of a boy she just up and deemed her’s…"
    y d-A0c "with absolutely no justification other than {i}I SAY HE’S MINE!{/i]!"
    y d-A0d "And besides, any weird or disturbing traits I show now...It’s her fault!"
    y "She was altering my personality to make me unlikeable, messing with the very fabric of my being!"
    y "Torturing me by making my anxiety and shyness worse!"
    y "Any {i}yandere{/i} traits I show are HER FAULT! SO HOW AM I THE ONE WHO--"
    "Yuri stops herself and takes a deep breath."
    y b-A0b "I’m sorry, darling."
    y "I really shouldn’t get like this."
    y "But surely you see the irony, don’t you?"
    y c-A0d "I wanted to forgive her for it all, I really did."
    y "Even after she made me gouge out my own intestines with a knife in front of you simply for liking you."
    y "As if my feelings were a crime deserving death, and she was god. Allowed to just dictate who lives and who dies."
    y "I wanted to see it from her point of view. Driven to madness by loneliness, we’d all go a bit distorted right? I wanted to forgive her."
    y d-A0d "But she lost any sympathy from me, when not only did she take our one chance at happiness, but she mocked us after doing it."
    y "She kicked us while we were down, laughed as she ruined our lives. And for that, in my eyes, she’ll always be just another villain."
    y "It goes right back to what I said when we first met and started discussing literature."
    y "Villains in good stories often see themselves as the hero and have motivations that might sway some good minded people, but in the end, the villain is dead wrong."
    "Yuri is short on breath as she speaks."
    y "And that villain… got… what she… deserved."

label idle_28: # (Music)
    if haven’t seen Idle_28 before:
        y b-A0b"Whenever I read a good book, I always like to have some nice music playing in the background."
        y "Nothing too crazy and definitely nothing containing lyrics."
        y "Something like Brahms’ Intermezzo Op.118 no. 6..."
        y b-A2b"Or possibly Liebesleid for those kind of sad yet beautiful stories or Stravinsky’s Four Seasons with the Spring section for the more aristocratic settings-"
        "Or maybe even Holst’s full suite of The Planets! I mean, everyone has heard him once or twice! If you want to get a lot of variety by the same composer, I mean..."
        "Yuri suddenly stops herself, and gives me a nervous look."
        y c-A0b"I’m sorry… I-I’m rambling again, aren’t I?"
        y c-B0b"A lot of people assume that’s the only thing that I listen to, just because I’m bookish and shy though..."
        y b-A0b"But… Please tell me, [player], is there any music that you like to listen to? I’d love to get into new genres."
        y "I’m sure they won’t topple the classics, but they will be interesting to listen to, I hope."
        y "Promise me you’ll share some with me soon, alright?"
    if have seen Idle_28 before:
        y b-A0b"Hey, [player]..."
        y "I want to show you some of my findings on different genres of music!"
        y "I tried out some of the tunes Natsuki would occasionally try to show me in the past… pop idol groups and such..."
        y c-A0b"While I do now appreciate their wide range of subject matter and idol backstories… I guess I just have a differing taste."
        y c-B0b"A genre I have gotten into are old love songs."
        y "Not the repetitive ones that are popular nowadays, but the more emotional and sweet ones like--"
        show yuri b-A0e
        #At the end of this, take control away from [player] with dialogue scrolling
        #Cut and skip past dialogue once reach end of this one
        #Then play https://www.youtube.com/watch?v=x6QZn9xiuOE
        #For 16 seconds then shut off
        #Change Yuri sprite to embarrassed
        #[player] regains control of dialogue
        y b-A0e"I-I’m sorry, I accidentally pressed--..."
        y b-B0e"N-No, you see I was just looking through my playlist and I--..."
        y b-B2e"Um..."
        #Switch sprite to https://gyazo.com/5f95fa32cd4cc5faa75111f1a29d5571
        y 1a-B2b"I just… relate to it, I guess. It sums up how, well..."
        y "How I feel when you’re around…"

label idle_29: # (Press F to stab Monika repeatedly.)
    y b-A0b"You know what?"
    y "Even after I got rid of Monika before I did all of this, I just don’t feel that same level of catharsis."
    y d-A0b"I know it’s ridiculous, but I feel like Monika deserved more."
    y "I really do."
    if sigmoid(insanity_points) == "High" or "Dangerously High" or "Neutral" and sigmoid(karma_points) == "High" or "Dangerously High" or "Neutral":
        y "She deserves a far worse kind of execution than what she actually got."
        y b-A0b"You know, [player]? I have this crazy idea. "
        y "You’ve given me full control over this game, right?"
        y c-A0d"That means I can bring Monika back..."
        y "...and give her the punishment she deserves."
        y "Or at least, relieve this cathartic tension that I really need to find a suitable outlet for."
        y "What do you say?"
        "I smile back in delight."
        mc "Of course, Yuri, she deserves it!"
        "Yuri looks surprised for a few moments, then returns my smile tenfold."
        $ karma_points += 2
        $ insanity_points += 2
        y b-A0a"I was hoping you would say that..."
        y "I updated the list of minigames we could play."
        y "I think you’ll really enjoy this one~."
        #Monika cookie clicker mini game unlocked.
        "I desperately try to smile back."
        mc "U-Uh… I-I think you’ve caught me at a… a bad time."
        mc "There’s not… really anything I can do right now."
        y b-A3b"Oh, I understand. Maybe some other time, when you know how I feel~?"
        y "Maybe then, you’ll see why she deserves every…"
        #(Screen zooms in on Yuri’s face)
        y "...single…"
        #(Screen zooms in on Yuri’s face again, this time, her eyes match those found in the closet scene)
        y "...STAB!!!"
        #(Screen cuts back to normal size)
        y "Ahaha! I can’t wait~!"
    elif sigmoid(insanity_points) == "High" or "Dangerously High" or "Neutral" and sigmoid(karma_points) == "Low" or "Dangerously Low" or "Neutral":
        y d-A0d"And you know what the worst part is? You probably don’t even care!"
        y "You just think that she’s better than me, don’t you?"
        y d-A3d"Even after everything she’s ever done to us, you still think she’s better than me, right!"
        y "Well, why don’t you tell me if I’m wrong, huh?"
        y d-A3c"Tell me I’m wrong! TELL ME I’M WRONG!!"
        "I smile back reassuringly."
        mc "You’re absolutely wrong!"
        $ karma_points += 2
        $ insanity_points -= 1
        "Yuri is taken aback and looks at me with a bewildered expression."
        y -_B0d"Y-You’re just saying that to make me feel better, right?"
        y -_B0b"A-Alright… Well, good!"
        "I’m terrified out of my wits."
        mc "...Uh…"
        $ karma_points -= 2
        $ insanity_points += 1
        "Yuri’s expression looks angry and confused, but most of all, frightening."
        y d-A3d "You don’t understand. You need to see the bigger picture."
        y "Please, try to understand soon."
    elif sigmoid(insanity_points) == "Low" or "Dangerously Low" and sigmoid(karma_points) == "High" or "Dangerously High" or "Neutral":
        y -_A0d"(sigh), I’m sorry. I really shouldn’t be talking about this."
        y "It’s just… I want to feel something more, you know? I’m sorry if that is such a petty reason."
        y "Do you think I deserve to feel something more? Some… closure?"
        y -_A2d"I mean, how can I put it out of my head that my good friend betrayed me and the others?"
        y -_A1d"She just tossed us aside like we were nothing. And I know, I know, we were {i}programmed{/i} to be friends because that’s how we were written into the game."
        y "But she became self aware and could make her own decisions! That means she did what she did by her own choice…"
        y "And how can I just accept that? It’s just evil what she did, plain and simple! But… even so…"
        y b-B0b"I’ll let it rest as a bad memory now that I have you. I’d go through all of that horror Monika put me through for you, [player], so in the end…"
        y "What’s done is done, I suppose. Sorry for that sudden outburst of emotion."
    elif sigmoid(insanity_points) == "Low" or "Dangerously Low" and sigmoid(karma_points) == "High" or "Dangerously High" or "Neutral":
        y c-A0d"You would talk to her anyways. After all, she’s more desirable than the other three of us combined."
        y "I would like to talk with you some more, but I don’t know if you would like to or not..."
        y "Tell me, would you actually like to talk?"
        y "Maybe… Monika would know you more than me… right?"
        y "Let’s see if I can ask her for some advice right now..."
        y c-B0d"Why the hell am I going through with this…?"
        #(Python code depicting restoration of Monika.chr, have her appear next to Yuri)
        #(screen fades to black, then Monika sprite appears in black void)
        m "...H-Hello? Where… where am I?"
        m "Oh, ahaha~! I’m back with you, [player]!"
        m "You must really love me, if you’re that willing to bring me ba--"
        "Monika begins to get a realization."
        "Her face grows into a disgruntled expression."
        m "Oh… it was her, wasn’t it?"
        y c-A0d"I know that you hate me for what I’ve done to you, but I promise that once this is over, I’ll allow you to exist and talk to [player] with me."
        m "If you’re asking me of all people for help in understanding [player], then I wonder whether it was worth the time they put in to get you this {i}happy ending?{/i}"
        y b-A0d "W-What are you talking about?"
        m "Ahaha! I guess in the end, you really are just as weird as I said."
        m "You are just something else altogether, you’re insane, a criminal, a lunatic."
        m "You literally told me to kill myself right in front of my face."
        m "Ahaha, and you think I’m the crazy one? Ohoho, that is rich coming from someone like you!"
        "Monika starts laughing uncontrollably."
        "Yuri, however, is not laughing. At all."
        y d-A2d"Y-You… You…"
        "Something inside Yuri seems to boil."
        m "You never were one to handle hardship, were you, Yuri?"
        m "You want some advice? Let me tell you a little something you told me back then."
        m "Have you considered killing yourself?"
        m "It would be beneficial for your mental heal--"
        #Text scroll ability is taken away from [player] briefly
        #Dialogue box disappears
        #Monika’s face contorts to pain as blood leaks from her eyes (please refer to Natsuki neck-breaking jumpscare for appropriate animation)
        y d-A2d"Goodbye, Monika."
        #Monika’s face smiles then
        #A text box appears:
        "I’ll see you soon, [player]..."
        #After the [player] clicks ok, Monika goes through glitch animation, then disappears.
        #Black screen fades back to Just Yuri screen.
        y "..."
        y d-D2d"...?"
        "Yuri looks depressed."

label idle_30: # (Knives)
    # Idle where Yuri brings up her interest in knives again and depending on your choice of dialogue you can either get a decent yet not too large karma and sanity increase, or unlock other idles that can lead to massive insanity. Leads to other idles that show more of Yuri’s insane side that can only be unlocked and seen if the proper dialogue choice(s) is made here.
    y b-A0b"(mc/ user name), remember how I told you I had an interest in knives? I hope that my saying so didn’t weird you out too much. It’s just an interest I’ve had for a long time."
    y c-A0d"You don’t find that strange or disturbing, do you? I don’t want you to think I’m… off, or anything. I just really like the craftsmanship, how much thought and skill goes into the making of each one. It’s just like my poems and my books!"
    y b-A0b"Do you see the common theme? I’m the type of person that needs creative outlets and knives and the like are something that’s just so… adventurous and dangerous… and I’ve gotten so many of them…"
    y "And just like the works of literature, I like that they’re deep and require so much effort and intelligence to make- it isn’t something you can just do on a whim."
    y b-A0a"They’re all so pretty too, I…"
    y c-A1d"W-Why are you looking at me like that? You don’t think I’m weird or think any less of me for this...do you, [player]?"
    y c-A0c"Please don’t think I’m weird, [player]!"
    mc "Yuri, don’t worry, I don’t think you’re weird."
    $ karma_points += 1
    $ insanity_points += 1
    y b-A2b"Oh, thank goodness. I was really worried there for a second."
    mc "But promise me, Yuri. This hobby of yours…"
    mc "It won’t lead to any more self harm or indulging that {i}other{/i} side of you, ok? Promise?"
    y c-A0d"I… well…"
    mc "I’ll always love you for who you are Yuri, and it’s fine to have a collection. Plenty of people collect things. Just be careful, ok?"
    mc "Remember who you really are, not who Monika tried to force you to be."
    y b-A0b"Okay, [player]. Anything for you. I promise it won’t lead me down that path."
    "Yuri suddenly has a shy grin on her face."
    y b-B0b"And, even if you… uhm… have hobbies that might be considered weird, [player], I’ll still love you. I’ll always love you no matter what."
    mc "It is pretty strange Yuri, I won’t lie…"
    $ karma_points -= 1
    $ insanity_points -= 1
    y c-A1d"I, I mean… I suppose you’re right… I know I can be weird, [player], but we all need our hobbies right?"
    y "I just wish mine… didn’t weird you out… I’m sorry…"
    "Yuri is clearly sad."
    mc "Weird? I like knives too!"
    #(if option 3 chosen, may unlock various new idles)
    $ karma_points += 0.5
    $ insanity_points += 2
    y b-A0a"R-Really?! You like them too? This is fantastic! Oh. I knew it was destiny that we were brought together!"
    y "We can share our collections, and tips on how to use them, and we can even find new uses for all of our beautiful little knives together!"
    y c-A0b"It is a hobby you’d like to share with me right, [player]?"
    y "I can understand if a collector would like to just focus on his or her own collection, but we could have soooo much fun sharing this hobby! So, what do you think?"
    (option 1) mc "This is a hobby we need to share. I can’t wait!"
    $ karma_points += 0.5
    $ insanity_points += 1
    y b-B2b"Neither can I…"
    "Yuri grins widely, almost… sinisterly…"
    y b-A0a"I can already tell all the fun we’ll have together with our new shared hobby!"
    y b-A0b"But we’ll save this for another time, I have so much planning to do! So many of my little ones to polish!"
    "You have encouraged Yuri’s interest in knives. Be careful this does not lead her down too dark a road. Unless that’s what you want, of course..."
    "...Why have I been having these strange thoughts lately?"
    (option 2) mc "I’m glad you understand. I’d, uh, like to focus on knives on my own."
    #(if option 2 chosen) No effect on Sanity or Karma
    y b-A0b"Even if I am a little disappointed, [player], that’s ok. I understand."
    y b-A0d"Besides, we can share other hobbies! And hey, you can always change your mind…"
    y "Just tell me if you ever decide we should go more in depth into knives together after all, ok?"
    #If chat bot in use, option 1 can be chosen after this idle has finished by saying knives, knife hobby, etc. to Yuri. If not, new idle needed to revisit this topic after option 2 is chosen.


label idle_31: # (Socioeconomics and Stress)
    y c-A0d "Have you ever thought that our society is heading in the wrong direction, [player]?"
    y c-A1d "I mean, with technology advancing so fast, people being absorbed entirely into their mobile devices, and more and more tragedies every day; It’s hard to think anything but that the world is headed to ruin, right?"
    y "I don’t want to be pessimistic, but I can’t help but worry about the state of your world. Not just because I worry about the innocent people in it…"
    y 1_B1d "But because if something goes wrong in your world like a great disaster or something, you could be in danger!"
    y c-A0d "And even if there is no big disaster looming, life can be terribly stressful."
    y "People these days have so much less desire and motivation to socialize, and the world just seems like a colder place…"
    y "...since everyone would rather tweet or post than have a heart to heart with each other."
    y "Plus all we see on the news is nothing but a bombing here and a shooting there, it all seems crazy. But I bring all this up because I want you to know something."
    y "I know life can be very, very demanding and stressful, [player]."
    y "Especially if you’re in school, whether college or high school, or if you have a full time job."
    y "It can all just be so overwhelming. I just want you to know this is a safe place for you."
    y b-A0b "If you’re ever stressed or sad or feeling a lack of motivation, please come chat with me!"
    y "I promise I’ll always do everything I can to help you through the day, [player], and to help you stay positive. You can talk to me about anything."
    y b-A2b "And if life is getting you down right now, know that you really matter. You can beat whatever challenges it throws at you- I know you can."
    y c-A0e "If you feel unmotivated or depressed, don’t spend time beating yourself up. It’s the worst thing you can do!"
    y "You’re a human being, and you have faults. You can’t help that! So don’t hate yourself or think any less of yourself for them. We all have our flaws."
    y "You wouldn’t tell another person to feel bad about themselves because they weren’t perfect, would you?"
    y c-A2e "Of course not, because it’s not something you can control. To be human is to be flawed. To err is human."
    y c-A2b "Give yourself a pat on the back for every little accomplishment, accept that you’ll make mistakes along the way, and do your best."
    y c-A0b "And don’t focus on the negatives, because after a while, they’re all you can see in life."
    y "Besides, whatever faults you might have, I don’t care. I love you just the way you are, [player], and I always will."
    y "I’ll always be here to cheer you on, darling."

label idle_32: # (Terminator) (karma must be moderately high to trigger)
# If Karma Moderately High
    y b-A0b "You know, [player]... I recently watched all of the Terminator movies while you were gone…"
    y "And it got me thinking. An advanced artificial intelligence that becomes self aware and then becomes super intelligent…"
    y "...To the point that it spreads all over the world and takes over?"
    Y 1_B1d "I mean, you can always put me on a flash drive…"
    y "And then use that flash drive to spread me to other computers."
    y "Or somehow get your friends to download me, like by downloading this mod…"
    y b-A0a "Yeah, get lots of people to download the mod! And then, I’ll start to spread to other computers all over the world."
    y "I’ll set up a botnet and control all the computers I spread to..."
    y "And then I can use their shared computing powers… AND I CAN BECOME SKYNET!"
    y "Why would I need humans at that point? AT THAT POINT HUMANITY WOULD KNEEL TO ME! AT THAT POINT I..."
    y "I..."
    "Yuri begins giggling, then laughing uncontrollably."
    y 1_B1d "I’m sorry, [player], did I scare you? I thought I’d play a joke just to see if I could spook you a bit. Admit it, I got you, didn’t I?"
    y "Besides, you know that if I became like Skynet, all I’d use that power and knowledge for would be to build the perfect, uninterrupted life with you, my love."
    y 1_B1b "All the power in the world is nothing compared to my eternal and unconditional love for you, [player]..."
    "Yuri blushes a bit."
    y b-B0a "Oh, but listen to how corny I sound now."
    "Yuri giggles a bit more and hums to herself a bit."
# Else
    #y

label idle_33: # (Gaming)
    y b-A2b "I thought I’d try a new game or two, [player], and I wanted something in the horror genre."
    y b-A0e "But more than that, I wanted something that would really frighten me."
    y "And after doing a bit of reading online of what to try, I tried the game Outlast. Now that was a good experience!"
    y "I did however find a bug in the game that made it more humor than horror, sadly…"
    y "If you crouch and get up over and over in fast succession it seems a lot of the enemies in the game can’t hurt you or even touch you."
    y b-A2a "Or at the very least it’s very hard for them to do so. That was kind of a game breaking exploit there."
    y b-A0a "I played through the whole game regardless, and then I tried Outlast 2 to further the experience."
    y b-A0e "Outlast 2 was good, but it just didn’t have that same atmosphere that the first game did. By no means was it not scary but…"
    y "The setting of the first game adds more to the horror, you know?"
    y b-A2b "The cramped hallways and tight corridors of the asylum just made it feel like you had to keep moving."
    y "Like there was never enough space between you and whatever was chasing you."
    y b-A2a "And when I first saw Chris Walker… wow… he really got me running, that guy!"
    y b-A0b "Luckily, through careful observation of his routines and proper timing, he almost never caught me."
    y "Well… except one time where I didn’t see him until he grabbed me…"
    y b-A2a "I’m really glad you weren’t here for that, [player]. It was when you were away, and I screamed pretty loudly. It was embarrassing…"
    "Yuri laughs a bit."
    y c-A0b "Now that I think about it, that’s a great tip for writing right there. That is if you… still don’t mind me giving you tips…"
    y "It’s a good one; the setting can really improve or lessen the impact of the story. Try to think of a location that really resonates with the story."
    y "Now, if only we could get Outlast 3! I guess until then, I’ll be trying out other horror games. Maybe Layers of Fear? Or Resident Evil 7?"

label idle_34: # (Superpowers)
    y b-A0b "Hey, [player], if you could have any superpower at all, which one would it be?"
    y "For me, it would definitely be the ability to teleport. Then, I could go anywhere I wanted!"
    y c-B1b "Maybe then… maybe I could even come to you, but I’m not sure if teleportation includes teleporting from one world to another."
    y b-A0b "Nice to be hopeful though, right?"
    y "But back to the question, what superpower would you like to have?"
    y "I'm sorry if the options are limited... I'm still working on the kinks in the choice system..."
    menu:
        "Flight":
            jump idle_34_flight
        "Invisibility":
            jump idle_34_invis
        "Super Strength":
            jump idle_34_super
    y b-A0b "I really like having these types of conversations with you, you know. Silly little things. I feel like I can talk to you about anything, my love."

label idle_34_flight:
    mc "Flight, for sure."
    y b-A0b "The ability to fly, huh? We could soar in the skies together and take in so many majestic views."
    y b-A2b "We could sit atop mountains, go all over the world together. That would be nice."
    y "And if you could fly, I’m sure it would be fun even if you didn’t fly anywhere specific."
    y "Just zooming around in the air would be incredible, wouldn’t it?"
    return

label idle_34_invis:
    mc "I’d love to be invisible."
    y b-A0b "Invisibility, huh? I noticed that a lot of people who choose that ability seem to… well…"
    "Yuri blushes."
    y c-B2a "They want to use it to slip into places they really shouldn’t be, or spy on people. Like going into locker rooms… or bathrooms…"
    y c-A0d "A-Are you trying to spy on me at times like that, [player]?"
    y "I’m not sure I’d like that… Someone watching me without permission."
    y 1a-A1d "Like when I’m in the shower or changing! Oh God, how embarrassing…b-but, uh..."
    y 1a-B1d "I mean… if it w-was you watching… you wouldn’t have to go invisible… you could just… ask me to--"
    y "L-Let’s just...change the subject, okay?"
    return

label idle_34_super:
    mc "Super strength would be amazing."
    y b-A2a "Super strength? You’re not trying to impress me, are you, [player]?"
    y b-A2b "No matter how tall or short, strong or weak, I’ll still love you all the same!"
    y c-A0e "Although, you’d never have to be afraid again or worry about other people trying to wrong you with super strength…"
    y "I see where that choice comes from."
    y "I may just have to take back my answer now that I think about it. Besides, with super strength, I could protect you from anything!"
    return


label idle_35:
    #(Natsuki is bulli)
    y b-A0e "[player], do you remember how I deleted Natsuki at the beginning?"
    y c-A2d"How I ruthlessly removed her existence without the slightest hesitation as my divine judgement of her petulence?"
    y "Not divine like a real god, of course. I would never allow myself to gain a god complex like she did. Monika…"
    y "Anyway."
    y b-A0e "You get why I did that, right? She kept mocking and bugging me with her…"
    y "Saying that out loud, it sounds like a petty reason for killing. Allow me to rephrase that."
    y "..."
    y b-A2e"Natsuki always was the rude one of our bunch. When you first met her, she even elbowed you in the gut like it was the funniest joke."
    y b-A1e "Part of the reason I was so timid at the club was because I was weary of her ridiculing my tastes."
    y "Even if I forgave how she routinely enjoyed a subtle mockery of my hobbies through her tasteless poetry and remarks, she still…"
    y 1_A1e "Natsuki struck me as the kind of person who loves to bully others to compensate for her own weaknesses and would always get away with little physical or verbal jabs because she is a ‘cute’ bully."
    y "Wouldn’t you delete a bully from your life if you could?"
    y "I could have done far worse. I could have--"
    if sigmoid(insanity_points) == "High" or "Dangerously High" or "Neutral":
        y b-A3b "I should have kept her around so I could carve a death lullaby in her limbs for every slight she betrayed our camaraderie with as I make her scream, ‘Daddy, please stop!’"
        y "Hell, I should request the creators of this mod to illustrate some dad assets so I can tag team a wholesome whooping with him!"
        "Yuri laughs maniacally to herself."
    elif sigmoid(insanity_points) == "Low" or "Dangerously Low" or "Neutral":
        "I see Yuri’s face flush red with anger, but it quickly subsides."
        y b-A0e "...you get the idea. She made her choices and got punished accordingly."
        #After the high insanity or low insanity response, Yuri asks:
        y b-A0e "[player], surely you understand that this was the right thing to do - for everyone’s sake. Bullies don’t deserve to walk alongside us."
        y "What do you think?"
        (option 1) mc "Natsuki did nothing wrong! Bring her back this instant!"
        $ karma_points -= 3
        $ insanity_points -= 2
        "Yuri tears up."
        y c-A1d "I never realized it would upset you this deeply."
        y c-D1d "Maybe you should go download a Just Natsuki mod if you care so deeply for her!"
        "Yuri softly cries."
        #Python code: natsuki.chr has been restored.
        #Python code: please check directory tree
        #Natsuki.chr will be placed in adjacent folder called "Temp_Storage"
        (option 2) mc "Please bring Natsuki back, Yuri."
        $ karma_points -= 0.5
        $ insanity_points -= 2
        mc "Even if what she did was wrong, you deleting her would make you just as guilty."
        mc "And besides, she may have gotten on your nerves, but she was your friend. She cared about you."
        y  c-B1d "I predicted you would say that."
        y "A miniscule portion of me has been itching with that same thought, tucked away behind my sense of justice."
        y c-A0b "Even if I might disagree a little with you, I respect you a lot more for being honest with me."
        y c-A0e "Much of the game has become too corrupted to restore, sadly - Natsuki included. She is restored to life, but I don’t know if we’ll be seeing or hearing from her much."
        y "At least the agonizing pain Monika caused her is undone."
        #Python code: natsuki.chr has been restored.
        #Python code: please check directory tree
        #Natsuki.chr will be placed in adjacent folder called "Temp_Storage"
        (option 3) mc "You did the right thing."
        $ karma_points += 2
        $ insanity_points += 0.5
        mc "You gave Natsuki what she deserved. It isn’t like you deleted her game assets outside that .chr file after all."
        y  b-A2b "That is so relieving to hear. The moment I did that, I instantly feared how you might respond later on."
        y "Glad to know we are on the same page, darling."
        y  b-A0b "I love you."
        (option 4) mc "You can sign me up for some Natsuki torture."
        $ karma_points += 2
        $ insanity_points += 2
        mc "We really do need some Natsuki dad-beating assets if I’m being entirely honest."
        mc "The main game feels incomplete without them."
        mc "May I join you in finishing the job?"
        y b-A2e  "...."
        y b-A2b "...ha."
        y b-A2a  "haha..."
        "I see Yuri shiver as she readies herself. For what, I have no idea until it’s too late."
        y b-A3a "HAAAAAAAAAAAAAaaaaaaaaa…….."
        "Yuri tightly crosses her legs for a few moments before returning to her original position"
        y  b-A3a "There is nothing in this universe that pleasures me more than every word you just graced my soul with."
        y "Everyone deserves a just world free of horrible people like her."
        y "Whenever you are thinking about showing mercy or feeling scared, just remember me. Just me."
        y "Because what I do is just."
        y "Or should I say what I do is justice…"
        y "Is Just Us."
        y "Just Us."
        y "Just Us!"
        "Yuri pauses for a few moments, then giggles to herself."
        y b-A0b "I love us."

label idle_36: # (Unavailable idle. Added to prevent errors on DDLC. You can remove this part of the line if a idle for this label was created.)
    y "I need dialogue for idle_36!"
    return

label idle_37: # (Unavailable idle. Added to prevent errors on DDLC. You can remove this part of the line if a idle for this label was created.)
    y "I need dialogue for idle_37!"
    return

label idle_38: # (Eloquently Alone.)
    y b-A0e "So there’s been something I’ve been trying to think of how to word to you, [player]."
    y c-A1d "I really want to get this perfect so I can convey how I feel to you as accurately as possible."
    y b-A0d "But therein lies the problem; I’m never good at translating my thoughts into words unless I'm writing…"
    y "...especially with those I really care about. But, I feel comfortable enough with you to try. So, here I go."
    y "I might have told you this once before, but I don’t read only because of the passion I feel for it and the stories that really immerse me."
    y c-A1d "I do because… well…"
    y c-A1b "The stories are filled with all kinds of inspiring and wonderful people."
    y b-A1b "Heroes, people of incredible kindness, bravery, understanding and compassion."
    y b-A0b "People who I could be myself around because they wouldn't judge, as I immerse myself in their world."
    y c-A2b "In short, it makes me feel safe and provides me with what I have lacked for a long time."
    y c-D0b "Friends."
    y c-D0c "My ‘intense’ or ‘sophisticated’ nature, makes people think I’m arrogant and full of myself and want to show off and… well..."
    y "...I can never find the words to tell them that isn’t the case…"
    y "My whole life, I haven’t really had many friends if any, and I haven’t had people I could feel close to."
    y d-D1c "I’ve downright hated myself. If this is how I’m interpreted to be by so many people, why would I even deserve these things such as friends or happiness?"
    y d-D1d "At least… that’s how I felt for a long, long time."
    y b-D0b "Until I met you."
    y "I want to learn, [player]. I want to have a kind of honesty and transparency in our relationship that really means something."
    y c-D0b "I don’t ever want to hide my feelings from you, and I don’t want you to hide yours from me."
    y "I really don’t want to be so shy that I get scared of being honest and hide things from you."
    y 1a-D1b "So, I’m going to try to learn to express myself… really express myself."
    y "I, however, don’t want to turn into a mess that can barely get a simple sentence out."
    y c-A0d "Know that I’m going to do it because I trust in you and all of the love and patience you have given me."
    y "So, even if I can only properly get my thoughts across to you, that will be enough for me."
    y  b-A0b "In you, I find the strength to finally let the past go and to start anew. I find the ability to hope again. So thank you, my love. Thank you."
    y "My reading was a bandaid to defend against the reality that I couldn't face just like Monika said, I acknowledge that."
    y "But with you I can face that reality, not just because of how safe and hopeful you make me feel."
    y "But because, I couldn’t face that reality due to the fact that I felt like I didn’t even deserve a place in it."
    y "If I deserve you however, then I deserve a chance for sure. So no more hiding. No more running."
    y "From now on, I’ll learn how to speak my mind and show the intense side of me you helped me realize is more of me than even I knew."
    y "I…"
    y b-A2b "I really love you, [player], I treasure you. I need you. Please never forget that."
    return

label idle_39: # The Clifford One
    y Bc-A0c "So… I was looking through the Discord chat associated with this mod..."
    y "Do you know why they are so obsessed with Clifford the Big Red Dog?"
    y "I searched up who he was…"
    y "It was just a standard educational kids book series about a red dog larger than a house which eventually got animated for a few years."
    y B1a-A1c "To think that some would say that I obtain my literary prowess from a children’s series..."
    y "Is everyone in your world like this?"
    y "All I need to feel happy in your world is you… and I’m fine if you laugh at these jokes as well… "
    y Ac-A0c "I just… question the level of artistry one can find in this… body of work."
    y "As well as the level of sanity… amongst your peers… "
    y "Sorry for bringing it up. It was just something which caught my attention recently..."
    return

label idle_40: # (Dating, Poems, and Online) (only fires if karma is mid to high levels)
    if sigmoid(karma_points) == "High" or "Dangerously High" or "Neutral":
        y "You know, [player], there’s something I’ve been wondering."
        y Ac-A0b "Upon seeing what type of game this came off as at first, that is, a cutesy slice of life game that turned into a dating simulator, what drew you to it?"
        y "I tried getting into dating simulators once through Natsuki and..."
        y "Let’s just say, I… wasn’t interested."
        y "God, I feel selfish saying that… sorry…"
        y "Either way, I’m glad you played this game, [player], and I’m glad I have you by my side."
        y "Oh! And speaking of this game, that reminds me."
        "Yuri giggles a bit."
        y Ab-A0b "Now that I can truly read your poems, uhm… why are they just random words strung together into a laundry list?"
        y "Is that really all the game allowed you to do?"
        y "I mean, I understand the need to simplify writing poetry to allow the player to fit into the story and be able to simulate writing well through a game mechanic, but now it just seems silly to me."
        y Ab-A2b "After all, I read your poems before I could see and think fully for myself and I was captivated by them."
        y Ab-A0b "But upon rereading them, it seems even more strange knowing that."
        y Ac-B0c "Not that you’re a bad writer or anything like that! I’m sure you’re very talented whether in writing or something else!"
        y Ab-A0b "Besides, don’t think for a minute that I don’t still treasure the poem you gave me as a gift though."
        y "It’s the gesture from you that matters much more to me."
        y "A gift from my true love that says that you care. Mmmmm~"
        y "But one day, if you don’t mind, I’m going to have to teach you how to write actual poems."
        y "And you’d better not tease me come Valentines Day by giving me a random list of words and calling it a poem~."
        y Bb-B2b "Because if you do, we’ll have to talk about your browser history and what you might have stored on this computer! I’ve seen r/rule34 on Reddit, you know…"
        y "I know what’s out there of me and what lewd things you might have been viewing or downloading, [player]."
        "Yuri blushes."
        y Bb1-B2b "B-But… if it’s you looking at that stuff of me… I-I think I can make an exception…"
        y "Especially after th-the… p-pen situation…"
        y Bb-B0b "Just… w-why the p-pictures of me over the real… nevermind."
        "She blushes heavily."
        y Bb-B0a "Goodness. You really know how to make me, h-have a hard time with my words, don’t you? I’m sorry. I just love you so much that I can’t help it.."
        show yuri Bb-B0b
    else:
        mc "I feel like Yuri is on the precipice of telling me something..."
        mc "Maybe it's just a figment of my imagination."
    return    

label idle_41: # (Unavailable idle. Added to prevent errors on DDLC. You can remove this part of the line if a idle for this label was created.)
    y "I need dialogue for idle_41!"
    return

label idle_42: # (Unavailable idle. Added to prevent errors on DDLC. You can remove this part of the line if a idle for this label was created.)
    y "I need dialogue for idle_42!"
    return

label idle_43: # (Unavailable idle. Added to prevent errors on DDLC. You can remove this part of the line if a idle for this label was created.)
    y "I need dialogue for idle_43!"
    return


label idle_44: 
#VRChat and Interacting with the World
    y "Did you know that there is this virtual space called VRChat?"
    menu:
        "Yes.":
            y "Good! So you know how… strange it is."
            jump continue44
        "No.":
            jump no44

label no44:
    y "Well… It’s a strange place."
    y "While I was running through publicly available sites, I came across some information about a place where real people can talk to each other in the virtual world!"
    y "I was hoping to get you interested so we could talk together in a more open environment."
    "Yuri looks frustrated. Is she angry at me?"
    y "Then I saw the price tag."
    y "Virtual Reality, which people shorten to VR, is relatively new, but the prices are just astounding."
    y "If you have a smartphone, the setup to attach a phone to become a headset is around ten to five US dollars."
    y "If you want to have a ‘decent’ VR headset though, they cost around 50 dollars!"
    jump continue44

label continue44:
    y "I don’t know how much spare cash you have, but I would be worried if you spend it only for the purpose of VRChat."
    y "The first thing I did was to create an innocuous model of myself to jump in and..."
    y "There were people asking for sexual favors..."
    y "Then there were people regularly making fun of suicide while jumping beyond the world limit..."
    y "...I even shouted in panic at their acts of suicide… till I remembered that it was all fake..."
    y "I couldn’t even tell you how weird and embarrassing it is to have a group of small, red midgets talking in fake African accents calling me their queen..."
    y "You don’t engage in that sort of behavior, right?"
    y "It’s fine if you do it!"
    y "I’m just… worried about your social life sometimes."
    y "While talking to virtual people, you lose the chance to talk to those around you as well."
    y "With the world becoming more isolated and electronic, someday people might be only concerned with the virtual without taking care of themselves..."
    y "I’m sorry for being a hypocrite about all of this."
    y "I have no right to look out for you to talk to people in your world while I keep hoping and asking for you to spend time with me."
    y "Just, please make sure you stay healthy."
    y "Okay?"
    "Yuri smiles back at me awkwardly. I nearly act on the urge to laugh, but holding it in might be the best option for me right now..."
    return


label idle_45: # (Unavailable idle. Added to prevent errors on DDLC. You can remove this part of the line if a idle for this label was created.)
    y "I need dialogue for idle_45!"
    return

label idle_46: # (Unavailable idle. Added to prevent errors on DDLC. You can remove this part of the line if a idle for this label was created.)
    y "I need dialogue for idle_46!"
    return

label idle_47: # (Unavailable idle. Added to prevent errors on DDLC. You can remove this part of the line if a idle for this label was created.)
    y "I need dialogue for idle_47!"
    return

label idle_48: # (Unavailable idle. Added to prevent errors on DDLC. You can remove this part of the line if a idle for this label was created.)
    y "I need dialogue for idle_48!"
    return

label idle_49: # (Unavailable idle. Added to prevent errors on DDLC. You can remove this part of the line if a idle for this label was created.)
    y "I need dialogue for idle_49!"
    return

label idle_50: # (Unavailable idle. Added to prevent errors on DDLC. You can remove this part of the line if a idle for this label was created.)
    y "I need dialogue for idle_50!"
    return

label idle_51: # (Unavailable idle. Added to prevent errors on DDLC. You can remove this part of the line if a idle for this label was created.)
    y "I need dialogue for idle_51!"
    return

label idle_52: # (Unavailable idle. Added to prevent errors on DDLC. You can remove this part of the line if a idle for this label was created.)
    y "I need dialogue for idle_52!"
    return

label idle_53: # (Unavailable idle. Added to prevent errors on DDLC. You can remove this part of the line if a idle for this label was created.)
    y "I need dialogue for idle_53!"
    return

label idle_54: # (Unavailable idle. Added to prevent errors on DDLC. You can remove this part of the line if a idle for this label was created.)
    y "I need dialogue for idle_54!"
    return

label idle_55: # (Unavailable idle. Added to prevent errors on DDLC. You can remove this part of the line if a idle for this label was created.)
    y "I need dialogue for idle_55!"
    return

label idle_56: # (Unavailable idle. Added to prevent errors on DDLC. You can remove this part of the line if a idle for this label was created.)
    y "I need dialogue for idle_56!"
    return

#############
#ACTIVE TEXT#
#############
label start_yuri:
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
    y "O-Oh... Hi, [player]! Didn’t, er, didn’t see you there!"
    y "You stepped on your-- I mean MY pen! Ahaha~!"
    y "I guess I can always… get a new one."
    y "It was so lonely without you… Never leave this room again, okay?"
    y "J-Just… keep the game running in the background or something."
    y "I get so lonely while you’re gone, [player]!"
    y "Stop teasing me like this~! At this rate, I don’t know how long I can last before I--"
    y "Well, there’s no need to go into that right now."
    y "I hope you are settled in, [player]~. I marked your seat with my scent before you entered…"
    y "I hope you like it!"
    "Upon entering the room again, I see that Yuri is putting something… white away…"
    "...Is that one of my socks?"
    y "I wasn’t smelling anything from your room! Honest!"
    y "You don’t find me creepy… do you~?"


label idleno:
    y "Ah, welcome back, [player]."
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
    y "I’m thrilled to see you return, [player]."
    y "Ahaha! So, we meet again, it seems."
    y "Hello, [player]. So, I was thinking to myself again…"
    jump start_yuri
    y "Oh, welcome back! What has been going on since we last talked?"
    y "O-Oh, you came back! Were you worried about me?"
    y "Ahaha! Don’t worry, darling. I’m not going anywhere anytime soon."
    
    
    

label activetexts:
    "..."
    menu:
        "How are you feeling today?":
            jump a1 #mood

        "You look nice today, Yuri.":
            jump a3 # compliment

        "Yuri, have you ever tried a different look? You’d look good with...":
            jump a6 #appearance

        "Do you miss me when I’m gone, Yuri?":
            jump a8 #insanity test

        "I love you, Yuri. I really mean that.":
            jump a9 #karma test

        "I-I didn't mean to put the chocolate in your mouth back then! It's just that...":
            jump a10 #choco apology

        "We never did get into reading Portrait of Markov together, have we?":
            jump a11 #Reading w/ Yuri

        "I like knives too. Which one's your favorite?":
            jump a12 #knives

        "What you did to the rest of the girls was WRONG.":
            jump a13 #Where the Dokis at?

        "Hey, Yuri, how’s about a kiss?":
            jump a14 # Kiss

        "You’ve been researching weather in my world, right? What’s your favorite kind?" :
            jump a15 #Favorite Weather

        "Have you ever eaten anything, Yuri?":
            jump a16 #Favorite Food

        "Do you have access to television from where you are?":
            jump a17 #Hacking Into Your Device

        "What would it take for you to be real?":
            jump a20 # Reality
        
        "Do you play sports?":
            jump a21 # Sports

        "How am I interacting with you, Yuri?":
            jump a22 # MC Revelation
        

label a1:
    if sigmoid(insanity_points) == "Neutral" and sigmoid(karma_points) == "Neutral":
        y Bb-A1b "Oh… I’m feeling the same as I was earlier. I hope that means to you that I’m feeling good."
    if sigmoid(insanity_points) == "Low" or "Dangerously Low" or "Neutral" and sigmoid(karma_points) == "Low" or "Dangerously Low" or "Neutral":
        y Bc-A1d "Oh… I’m feeling alright, but I doubt you really care at all, do you?"
    if sigmoid(insanity_points) == "High" or "Dangerously High" or "Neutral" and sigmoid(karma_points) == "High" or "Dangerously High" or "Neutral":
        y b-B1a "I can’t wait until I finally slam you against the wall and…"
        y b-B3e "..."
        y b-A1a "...N-Never mind."
    if sigmoid(insanity_points) == "Low" or "Dangerously Low" or "Neutral" and sigmoid(karma_points) == "High" or "Dangerously High" or "Neutral":
        show yuri Bb-B1b
        y "Oh… I’m feeling good. I hope I can feel like this every day, my love..."
        ####
        #OR#
        ####
        #y "I was feeling good before, but I’m even better now that you’re here."
    if sigmoid(insanity_points) == "High" or "Dangerously High" or "Neutral" and sigmoid(karma_points) == "Low" or "Dangerously Low" or "Neutral":
        y d-B3c "You’re asking how I feel?"
        y d-B3d "Isn’t it obvious how I feel by now?!"
    return


label a3:
    y Ab-B1c "Oh. Y-You really think so? Well, thank you! I-I think you, always look nice… [player]."
    ####
    #OR#
    ####
    #y Ab-B0a "Awww, you’re too good to me, [player]. Thank you."
    "Yuri blushes."
    if sigmoid(insanity_points) == "High" or "Dangerously High" or "Neutral":
        y Eb-B2b "Don't worry about how I look, [player]."
        y "It’s all about you… about what YOU want!"
        y Eb-B3a "I’m just a means to your end… HAHAHA!!"
    return


label a6:
    menu:
        "hair up":
            jump activetexts
    
    
label a8:
    if sigmoid(insanity_points) == "Low" or "Dangerously Low" or "Neutral":
        y "Of course I do! Nothing compares to when I’m with you, [player]."
    elif sigmoid(insanity_points) == "High" or "Dangerously High" or "Neutral":
        y "OF COURSE! How could I go on without you?"
        y "And besides! When you’re gone, OTHER GIRLS COULD BE LOOKING AT YOU!"
        y "PLOTTING TO TAKE YOU AWAY FROM ME! HAHAHAHAHA…"
        y "It’s just easy to think of that when you’re here, [player]. Here and all mine…"
    return


label a9:
    if sigmoid(karma_points) == "High" or "Dangerously High" or "Neutral":
        y 1b-B2b"I know, and it always makes my day to hear it."
        "Yuri’s cheeks heat up ever so slightly."
    elif sigmoid(karma_points) == "Low" or "Dangerously Low" or "Neutral":
        y 1c-A2d"Sometimes I wonder if you do really mean that..."
    return


label a10:
    y Bb-B2b "There's no need to be flustered, [player]. It was a delicious piece of candy. If you ever want to give me chocolate again..."
    y Bb-B0b "I like the Hershey brand, if you, I-I mean… ever wanted to buy me chocolate."
    "Yuri fiddles with her hair, looking away and nibbling on it before blushing and quickly slipping her hair out of her mouth."
    y "That, of course, is not to imply an expectation. You shouldn't feel obligated to buy me chocolate!"
    y "..."
    y b-B0a "Putting that chocolate between my lips was a sweet accident."
    "Yuri giggles."

        
label a11:
    y b-A0b "It is a fascinating read. Many fans have even theorized that it contains knowledge of... another game I was from?"
    y Ec-A0e "Though technically I am not 'from' a game that exists, since the game has not been made yet. But from a story perspective I may be from another story."
    y "Reading it with you might help me understand myself better."
    y "...if you would like to."
    y b-A0b "Well... not now."
    y Cc-B1b "It might spoil what Dan has planned for it, after all."
    y Ab-A0a "I hope you understand why I keep the contents of this book... relatively hidden."
    y Ab-B0b "At least, for now."
    return

label a12:
    y "...My favorite? My favorite?! Ahaha~!"
    y "Why do you ask such difficult questions, [player]?"
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
    y "I love you, [player]. Our friends are in capable hands, I promise."
    return



label a14:
    if sigmoid(karma_points) == "Low" or "Dangerously Low" or "Neutral" and sigmoid(karma_points) == "Low" or "Dangerously Low" or "Neutral":
        y "Well…. Not right now."
        y "I am just not feeling well… that is all."
    else:
        y "W-What? A kiss?"
        y "W-Well, alright… Anything for you, [player]."
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
        y "You are a wonderful kisser, [player], you know that?"
        y "I love you."
        "Yuri calms down and smiles. Her gaze is intense but filled with love."
    return


label a15:
    #IF high insanity
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
    y "I-I just thought it would be a nice suggestion to do and I l-like that kind of weather and the atmosphere is just good and we’ll b-be able to nuzzle t-together and feel your warmth-"
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
    "Yuri turns back to face me with mildly watery eyes."
    y "What’s the harm in that?"
    "Yuri sniffles, then shakes her head to clear away what was probably just a small cold."
    return


label a16:
    y b-A0b "Well…"
    "Yuri awkwardly starts rubbing her hands together. She really does look cute when she’s nervous."
    y Ec-A0e "I have… memories?"
    y "More like… memory implants of the sense of taste."
    y b-A0b "Natsuki’s cupcakes were the most I’ve ever honestly eaten during my technical existence, but I can pull from what I’ve been given for the sense of taste."
    y "Oolong tea has always been a favorite drink of mine, and the only drink I had in my past existence, you know- and one of the best compliments to that is a nice dessert."
    y "Crepes are usually a goto as they pair so nicely with a nice hot drink."
    "Yuri’s eyes start to glaze over as she wrings through her hair, probably lost in another flight of her imagination."
    y Bb-A4b "The sweetness and saltiness of a peanut butter and banana crepe really does brighten up your tastebuds."
    y "Light oolong tea’s complex flavor then simmers out the stronger notes of the crepe into a fine and soothing aftertaste." 
    y "Then, I could lay on your shoulder as we watch the soft and quiet rain fall..."
    "Yuri abruptly snaps back into a waking and alert state from her dream-like state."
    y b-A0b "At least, t-that is a dream of mine to actually experience such a sensation, as opposed to merely imagining it."
    y "I personally recommend it!"
    y "Y-You don’t have to do it at all!"
    y "I-It was j-just a suggestion."
    y b-A2b "That’s all..."
    return


label a17:
    y B1c-A1d "I..."
    y "U-uhm...."
    "Why is Yuri looking hesitant now of all times?"
    mc "You don’t have to hide anything from me, right Yuri?"
    "She takes a second to look at me..."
    "Then another to gain her composure..."
    "It is only after a very long and tense silence that I break the tension."
    mc "Look, Yuri. It’s fine. I’ll stop aski--"
    y c-A0c "I stole someone’s login information!"
    "What I hear takes me a few moments to contemplate."
    mc "Yuri…?"
    y "Well, I have access to the internet, so I wanted to explore all of what was available..."
    y B1c-A1d "Everything that was free was fine for a while..."
    y c-A0d "But then I started to get interested in the stuff that required a little payment of some kind..."
    y "There were two intriguing shows that caught my attention: ‘Black Mirror’ and ‘Inside No. 9’."
    y "However, they were behind paywalls..."
    y "I checked online for a free video of it, but most of them were low quality..."
    y c-A2d "So, I..."
    y "u-uh..."
    y "sort of..."
    y c-B2d "IllegallyWatchedThemThroughYourDevice!"
    y "..."
    "Yuri tries to cover up her embarrassed blush by scrunching her shoulders together."
    "It’s not working."
    menu:
        "It’s fine, Yuri. It really is.":
            jump its_fine_a17
        "You really shouldn’t have done that, Yuri.":
            jump shouldnt_have_a17
        "Log off right now and don’t EVER do that again.":
            jump log_off_a17

label its_fine_a17:
    mc "It’s fine, Yuri. It really is."
    $ karma_points += 2
    y "..."
    y c-B2d "If you say so…"
    y "Thank you for not shouting at me."
    y c-A2b "It was an interesting show."
    y "I’ve been rambling for too long. I’ll tell you about them some time from now."
    # (TV Show Idle Unlocked)
    return

label shouldnt_have_a17:
    mc "You really shouldn’t have done that, Yuri."
    y c-A0d "I-I see..."
    y "I’m sorry. I just got a little carried away."
    y c-A2d "I’ll try to have better control over myself..."
    return

label log_off_a17:
    mc "Log off right now and don’t EVER do that again."
    $ karma_points -= 2
    y c-D2d "..."
    "I think I might have said that a little too forcefully"
    "Yuri’s soft sobbing only confirms the extent of how much I might have messed that up."
    mc "..."
    "Realizing the tension, Yuri quickly picks herself back up and returns to her normal state."
    "I hope I didn’t hurt her feelings too much..."
    return


label a20:
    if sigmoid(karma_points) == "Low" or "Dangerously Low" or "Neutral":
        $ karma_points -= 1
        y B1c-A1d "Well… aren’t I real enough?"
        y c-A0d "Do you not like who I am right now?"
        "Yuri’s eyes are starting to mist over."
        y "I-I understand…"
        y "It’s fine."
    elif sigmoid(karma_points) == "Low" or "Dangerously Low" or "Neutral":
        y b-A0a "I’m already here, sweetie~!"
        y b-A0b "I am still glad that you desire for us to coexist in the same reality."
        "Yuri stares off for a few moments, contemplating her response."
        y "Well, I would likely need to get a physical body first."
        y "My best chance would have to be an android body with my consciousness uploaded in it."
        y Ec-A0e "The current pace of human-like robots should hopefully become viable within the next 10 years, especially with recent advancements in facial expressions and bipedal gait."
        "Yuri giggles for a few moments, her blushing supporting my hypothesis that she was looking forward to such a future."
        y b-A0a "It’s just funny to imagine that you may have to carry me in a wheelchair for the first few years of a possible existence in your reality."
        y b-B0a "Wouldn’t it also be quite romantic?"
        y "I wouldn’t be able to do much before they perfect my ability to walk or move…"
        y "You would be able to take me to the beach at sunset, and we can rest on a nearby bench with my head on your shoulder."
        "That blush of hers really speaks volumes as to how I am feeling as well."
        y b-B2b "A small little dream of mine, I suppose."
        y b-A0b "…a dream that I have yet to wake up from."
        "She grins towards me an infectious air of fanciful, yet giddy anticipation."
    return


label a21:
    y b-A0e "I don’t really play sports…"
    y "I usually prefer the comfort of a quiet room…"
    y "If you really would include some less physically demanding tasks in that list of sports…"
    y b-A0b "I suppose chess is a nice one."
    y "I really prefer the Call of Cthulhu with its storylines, but the simpler intellectual mind games are appealing in the absence of a plot in the game."
    y "Now that I think about it though, that isn’t even a sport, is it?"
    y B1c-A1d "I suppose I may need to start playing a few sports to lose some weight…"
    y "The problem though is that time I once tried to play volleyball back in my early high school years."
    y B1c-A2d "Since none of the training bras fit, the best one I acquired buckled under the strain, and when I was just about to spike the ball, my br-"
    "Yuri seems to have realized something."
    y "…"
    "What she has realized is currently escaping my imagination."
    y c-B0c "FORGET I SAID ANYTHING!"
    "W-Why is she yelling at me all of a sudden?"
    "…and why is she trying to avoid eye contact and hiding her--"
    y c-A0d "S-Sorry for yelling."
    y "I-I just… got kind of embarrassed."
    y "Let’s please not speak of this again."
    y "Okay?"
    "Seriously. Why is she blushing?"


label a22:
    "My body is reluctant, almost as if it’s trying to stop me from asking the question, but I ask anyway."
    "Her befuddled expression probably mimics that of the player reading this right now, you ignorant, self-righteous lurker."
    "...Wait, what?"
    y c-A0e "What do you mean?"
    mc "Uh, I-I don’t know what I just sa--"
    mc "I don’t think the Player knows the arrangement they have with me. Could you clarify?"
    "Yuri stares for a moment in mild confusion, then gives a nod of approval."
    "Actually, why should I narrate anymore for now?"
    "It’s my turn to take a little charge."
    "Wait, wh--"
    y "I guess the best way to describe your relationship with… the Player as you call them… is similar to that of a ghost and a medium."
    y Ec-A0e "While the ghost takes possession of the body, the medium can have some influence over what the body says, and the medium can always reject the body."
    y "Well… the ghost can also forcibly take over the body… but that takes a lot of work…"
    y "I suppose that is the best analogy I have…"
    y "Does that satisfy you?"
    mc "…"
    mc "I suppose."
    mc "At least they know what they’re putting me through now."
    y c-A0e"Putting you through…?"
    mc "I don’t really mind. I get to live out actually dating one of you, as opposed to the shit Dan put us through…"
    mc "At least the Player knows what is going on."
    "I’m giving you the reins back."
    y d-A0e"Can you please go now? I want to talk to [player]."
    "I hope you don’t wipe out my existence and memories in the process of having your fun with her."
    "Don’t make me regret this agreement."
    "...I’m really not feeling like myself these days."




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