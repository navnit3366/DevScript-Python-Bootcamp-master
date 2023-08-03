#Application which tells future on the basis of zodiac sign
conditon = True
while conditon == True :
    print('''
    Zodiac signs
    1)Aries
    2)Taurus
    3)Gemini
    4)Cancer
    5)Leo
    6)Virgo
    7)Libra
    8)Scorpio
    9)sagittarius
    10)Capricon
    11)Aquarius
    12)Pisces
    ''')

    zodiac_sign_no = int(input("Pick your sign number and Enter: "))

    if zodiac_sign_no == 1:
        print("Today, you may have mental peace. You are likely to be busy with friends and family. You may enjoy your domestic life, it may increase understanding with your spouse. There is a new partnership in your business. New innovations may help your business to grow. Disputes in the partnerships may be resolved now.")
    elif zodiac_sign_no == 2:
        print("Is someone in your life getting a bit too full of themselves? As much as you hate arrogance, you can't let them push your buttons. They would just love to get a reaction out of you, so why give them the satisfaction? They only want attention, and they don't care whether it's good attention or bad attention. Instead, try to see their behavior as funny. Laugh like you've just heard the funniest joke. That will make it clear to them that they can't get to you.")
    elif zodiac_sign_no == 3:
        print("Don't let your actions be dictated by others' expectations today. Do whatever you feel is the right thing to do, no matter what anyone else says. Sure, you may be accused of being selfish, but only by narrow-minded people who are acting out of jealousy. And besides, your reputation is strong enough to withstand any complaints from people whose envy is turning them into small-minded poseurs. They're just jealous that you have the courage to do something truly original.")
    elif zodiac_sign_no == 4:
        print("Your upcoming plans are causing you to get a bit distracted from your daily drudgery, which is to be expected, but don't let your focus on the future keep you from getting the job done right today. The loose ends you ignore in favor of a daydream or two could come back later to tie you up on knots, and that's not something you want. Get your mind focused on the here and now by promising yourself an hour or two goof off later.")
    elif zodiac_sign_no == 5:
        print("You might be thrown into a situation that you feel you're not prepared for, but you are! Just relax and you will radiate warmth and charm. Getting nervous will only make you put up a wall that no one will want to try to vault over, so what's the point? Relax. You're great. Go forward with your mind and heart wide open. It's time to let your true personality come out. People have been waiting to see it.")
    elif zodiac_sign_no == 6:
        print("Any conversation you have with an authority figure should go very well, especially if you don't brag too much about your latest accomplishments. There is a time for tooting your own horn, but this is not it. Humility will earn you a lot more respect than pride. This is also not the time to push too hard for what you want. Let people know what your goals are, but leave it up to them whether or not they will give you the opportunity to try to achieve them.")
    elif zodiac_sign_no == 7:
        print("You could get the inside scoop on some exciting news today, which means that you could be in a power position for a while at least. Get ready for some serious attention. Others will look to you for the answers because it's going to be obvious that you have them. Be very careful about who you tell what. Once this information gets into the wrong hands, it could lead to some serious drama that you want no part of.")
    elif zodiac_sign_no == 8:
        print("The fastest way to build your self-confidence right now is to try something that you've never tried before. Sure, it might be a little scary to put yourself on the line, but when you rise to the challenge and blow everyone away, you will feel pretty darn good about yourself! You could try a new sport, a new musical instrument, or a new food. It doesn't matter. As long as it's new to you, it counts as a character-building exploration.")
    elif zodiac_sign_no == 9:
        print("A new job opportunity could come your way, so if you want to reach out and grab it, just go for it! This could involve a certain level of risk-taking on your part, so if you're not totally committed to making a change, you might want to let this chance go by. But anything worth having requires you to step out of your comfort zone a little bit. Be sure that you're not just focusing too much on fear. If you really want it, you can definitely get it!")
    elif zodiac_sign_no == 10:
        print(" You have lived long enough to know that nothing—and no one—is perfect, so why are you holding yourself to such an impossibly high standard? You are being far too demanding of yourself. Who you are right now is more than good enough, so cut yourself some slack. And if you still can't convince yourself of just how wonderful you are, then talk to a close friend. Let them massage your ego for a while. They'll be glad to.")
    elif zodiac_sign_no == 11:
        print("A recent compromise you made might appear to have been a mistake, but you should give it a little more time before you try to undo what you did. Hindsight might be 20/20, but having that clarity in retrospect is not always a helpful thing. It's best to just keep looking forward and keep your fingers crossed. It's not denial to hope for the best even though all evidence points toward something less. It's just old-fashioned optimism!")
    elif zodiac_sign_no == 12:
        print("Your latest health concern should be addressed sooner rather than later. Chances are it's caused mostly by the stress you've been under lately. You need to start taking better care of yourself! Make a promise to yourself to get at least seven hours of sleep every night. Start eating a healthy breakfast every day—and no, a cup of coffee doesn't count! Start practicing better habits, and before you know it you'll feel much more balanced and content.")
    else:
        print("You have enter wrong number........!")

    # For making the program run again when ever the user want
    #temp = input("Would you like to try again? (Y/N): ")
    #if temp == 'Y' or 'y':
    #    conditon = True
    #else:
    #    conditon = False

    # Python 1 Liner for the same conditons
    conditon = True if input("Do you want to try again? (Y/N): ") == 'Y' else False
    print("Hope you glad to know about your horoscope")
    print("Hope you will come back to us soon")
