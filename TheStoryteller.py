import time
import random
# Below is where I made the story reading definition. It works by starting at placement value in the list, and printing
# until it reaches "?END?" in the list.


def text_read(placement):
    while placement != "?END?":
        print(Stories[placement])
        time.sleep(len(Stories[placement]) / 20 + 1)
        placement += 1
        if Stories[placement] == ". . .":
            time.sleep(3)
        if Stories[placement] == "?END?":
            break


print("Input names separated by commas: (10 or less names please!)")
while True:
    Subjects = input("\r" + "",)
    if len(Subjects.split(",")) > 0 and len(Subjects.split(",")[0]) > 2:
        Subjects = Subjects.split(",")
        random.shuffle(Subjects)
        break
if len(Subjects) == 1:
    SingleStories = ["If there was ever a perfect person, " + Subjects[0] + " would be the opposite of them.",
                     "Some people are heroes, others are villains, and then there's " + Subjects[0] + ".",
                     "Be who you are on the inside, because that's what counts... Unless you're " + Subjects[0] + ".",
                     "They're perfect in every way, I didn't say anyone, but you thought of " + Subjects[0] + ".",
                     Subjects[0][0] + ".U.B.S.T.A stands for " + Subjects[0] + " is Unlovable But Still Tries Anyway.",
                     "A great misfortune lies ahead in " + Subjects[0] + "'s future... The inevitable onset of death.",
                     "If there's two kinds of people, " + Subjects[0] + " is the 3rd kind.",
                     "When God made " + Subjects[0] + ", he broke the mold... Because he realized his mistake.",
                     Subjects[0] + " has made a big contribution to science, they've proven that IQs can be negative.",
                     Subjects[0] + ": Gone, but not forgotten, unfortunately."]
    print(random.choice(SingleStories))
if len(Subjects) == 2:
    Stories = ["][==][  Asininitus PSA  ][==][",
               "\033[1;0;0mEvery day, dozens of young people like \n" + Subjects[0] + " here, suffer from Asininitus.",
               "Asininitus is a disorder that affects all of us, not just those diagnosed with it.",
               Subjects[0] + " used to have friends, but because of Asininitus, no one likes them anymore",
               "Asininitus syndrome affects the way the host responds to social activities, and deadens them.",
               "Thanks to Asininitus, " + Subjects[0] + " is a complete sociopath with no life whatsoever",
               "But with help from people like " + Subjects[1] + ", " + Subjects[0] +
               " may have a chance at a social life",
               "Thanks to " + Subjects[1] +
               "'s donation, we can continue our study on these socially deprived individuals",
               "So please, find it in your heart to donate to poor, pitiful beings like " + Subjects[0] + ".",
               "Asininitus affects everybody, and we can't fight this alone.",
               "Call 555-216-LOSER for more information.",
               "And thank you, from kids like " + Subjects[0] + ".", "*Brought to you by McDonald's, " +
               "the future employer of " + Subjects[0] + " and other Asininitus patients.", "?END?"]
    text_read(0)
if len(Subjects) == 3:
    Stories = ["][==][  Fuhrer " + Subjects[0] + "'s Legacy  ][==][",
               "It was the year 1943, WWII was at its peak and the world was on edge", "The Fuhrer " + Subjects[0] +
               " had conquered many territories in Europe and killed millions of the Jewish people.",
               "This Jewish prisoner named " + Subjects[1] + ", was left in -23 degree weather, then brutally whipped.",
               Subjects[0] + "'s reign lasted until the end of WWII, when he committed suicide by poison and pistol.",
               Subjects[0] + "'s legacy is a fearful one that contains much death, but also success and failures.",
               "Ultimately, the Fuhrer fell because of sheer overwhelming military power.",
               "Armies such as the Soviets," +
               " who were lead by the strategic " + Subjects[2] +
               " Stalin, and many others opposed him, which led to his" +
               " demise.", "?END?"]
    text_read(0)
if len(Subjects) == 4:
    Stories = ["][==][  Accurate Representation Of The Medical Field  ][==][",
               "(Drunk) Doctor " + Subjects[0] + ": W-what happened to *burp* them?",
               "(Hallucinating) Nurse " + Subjects[1] + ": The report just had a bunch of hieroglyphics on it, but I " +
               "think it said they stuck a fork into a toaster that was in a microwave, while on drugs.",
               "But first I'll consult the camouflaged iguana.",
               "(Thinks They're A Wizard) Surgeon " + Subjects[2] + ": " +
               "I'd begin operating immediately, but it might drain too much of my powers, and there's too many muggles.",
               "I may have to consult Filius Flitwick on this, but I've always hated Ravenclaw." +
               " So I'll just use my cloak of invisibility...", "*Drapes jean jacket over face and squats down*",
               "Doctor " + Subjects[0] + ": I think we sh-should *dazes off, then kneels over trashcan*",
               "Nurse " + Subjects[1] + ": I agree with the nauseous sock-monkey, we should just throw " +
               "it away; as soon as the hospital stops vigorously shaking.",
               "Doctor " + Subjects[0] + ": *Head in trashcan* I *burp* never said that.",
               "Surgeon " + Subjects[2] + ": *whispering healing spells*",
               "(Convinced They're Jesus Christ) Patient " + Subjects[3] +
               ": *Begins waking up by stretching their arms"
               " outwards like a cross*", "Patient " + Subjects[3] + ": " + "Good morning, children of God.",
               "Surgeon " + Subjects[2] + ": *Jumping to their feet* IT WORKED!", "Nurse " + Subjects[1] + ": " +
               "Ooh, the burnt toast is talking again. It needs to sleep more.",
               "Doctor " + Subjects[0] + ": *Asleep " +
               "with head in trashcan*", "Surgeon " + Subjects[2] + ": My work here is done, Slytherin needs me.",
               "*Pulls jean jacket off head*", "*Leaps out of window head first*", "Nurse " + Subjects[1] + ": " +
               "Goodbye Batman!", "Patient " + Subjects[3] + ": *After seeing the spectacle, Tears form in eyes*",
               Subjects[3] + " wept.", "?END?"]
    text_read(0)
if len(Subjects) == 5:
    BandSuffix = ["ia", "les", "ion", "ation", "bo", "ed", "ons", " Boys", " For Fears", " Orchestra", " Magic",
                  " Experience", " Sense", " Man Group", " Sabbath", " With A Side Of Doom", " 5", " Boyz"]
    BandName = Subjects[0][0] + Subjects[1][0] + Subjects[2][0] + Subjects[3][0] + Subjects[4][0] + random.choice(BandSuffix)
    Stories = ["][==][  The Band's Debut  ][==][",
               "There are some bands that become legends, some never leave, others may die.", "But one will live on" +
               " forever.", "'" + BandName + " is one of those bands. ('" + BandName[:5] + "', for short)",
               "They made their mark in 2001 with their unique Heavy-metal-folk-synth-jazz style,",
               "And they immediately found themselves at the top of the charts for a consecutive 9 minutes," +
               " where afterwards they were pushed aside by Train's 'Drops Of Jupiter'.",
               BandName + " found many hardships after their best song 'Bigfoot Is Real And So Is My Love'," +
               " left the charts.", "Their later songs, such as 'There's No Us In Love', 'Poisson', and " +
               "'The Last Thing I Had For Breakfast Was Heartache And Orange Juice' failed to take off.",
               "It resulted" + " in division forming among the band members.",
               "The beginning of the end started when the leader of" +
               " the band, " + Subjects[0] + ", began accusing fellow band members " + Subjects[1] + " and " +
               Subjects[2] + " of being Canadians.", "But the final blow came when their synth player, " + Subjects[4] +
               " died after being struck by lightning while holding their keyboard in the air during a thunderstorm" +
               " at a concert.", "Where are they now?", "Well, after they broke up, " + Subjects[0] + " stayed in" +
               " music by starting another band, under the name 'The " + Subjects[0] + "" + random.choice(BandSuffix) +
               ".", Subjects[1] + " is a deeply resentful art critic who dabbles in plumbing and dentistry.",
               Subjects[2] + " became a nomad and left all worldly possessions behind, which was a bad idea, as they" +
               " were almost immediately mugged in an alley the next day, and is in a coma to this day.",
               Subjects[3] + " is now a guidance counselor, and has successfully steered dozens of young souls away" +
               " from music by playing his band's CD.", "While their time in the sun was short, " + BandName +
               "'s legacy shall live on in the hearts of millions.", "?END?"]
    text_read(0)
if len(Subjects) == 6:
    Stories = ["][==][  " + "The Cheesecake Factory" + " v. " + Subjects[0] + "  ][==][",
               "Guard " + Subjects[2] + ": All rise for the honourable Judge " + Subjects[3] + ".",
               "Judge " + Subjects[3] + ": Please be seated, we will now begin the case of The Cheesecake Factory" +
               " v. " + Subjects[0] + ".", "Guard " + Subjects[2] + ": " + Subjects[0] + ", you are accused of " +
               "embezzling food from the aforementioned company, and you have pleaded 'not guilty'. You may begin " +
               "your defense.", "Lawyer " + Subjects[4] + ": Thank you for the introduction. I believe that my " +
               "client is innocent as their disabilities are more than just debilitating, they completely immobilize",
               "them between the days of Tuesday through Sunday, and it was within this time that the crime was " +
               "committed. Let the record show that the disease is called 'Laziness'.", "Judge " + Subjects[3] + ":" +
               " Prosecution, what is your rebuttal?", "Lawyer " + Subjects[5] + ": My client has presented a " +
               "compromise; Ahem, 'if the defendant admits to the crime and receives jail time, " +
               "they and all others in the court will receive free cheesecake for a month'",
               "Judge " + Subjects[3] + ": Defendant, your response?", "Lawyer " + Subjects[4] + ": *quietly* Will " +
               Subjects[1] + ", CEO of The Cheesecake Factory, also provide to go boxes?",
               "Lawyer " + Subjects[5] + ": *Whispering to " + Subjects[1] + "*. . . Yes, they will.",
               "Lawyer " + Subjects[4] + ": *Without consulting " + Subjects[0] + "*, We accept the compromise.",
               "Judge " + Subjects[3] + ": *Thinking of the cheesecake* Court dismissed!", "?END?"]
    text_read(0)
if len(Subjects) == 7:
    Occupations = [[" a Plumber", " a Dentist", " a Professional Human Shield", " an Underwater Welder",
                   " a Personal Chef", " a Food Taster", " a Costco Sample Person", " the bodyguard to Al Yankovic",
                   " a Dog Surfing Instructor", " a Personal Trainer", " a Professional Cuddler",
                   " a Dog Food Tester", " a Star Wars Theory Conspirator", " an Assassin",
                   " in Internet Customer Service", " a Comedian", " a Professional Line-Stander",
                   " a Fortune Cookie Writer", " an Ex-Member Of Nickelback", " a magician",
                   " a Jedi Master", " a Sith Lord", " a War Criminal", " a War Hero", " an Ex-Convict",
                   " a Voice Actor"],
                   [" a Chilean Rockstar on the verge of a life of crime", " a vigilante who's afraid of the dark",
                    " a janitor that finds a magical belt in the toilet", " a gamer with a life",
                    " a trigger-happy gun-toting grandparent with a dark past", " a lawyer with autism",
                    " a child prodigy that eventually ends up selling drugs", " a failed luchador",
                    " an inexplicably beautiful clerk at a Family Dollar Store", " scandalous factory worker #37",
                    " unnamed referee #3", " disappointed chef (stunt double) #2"]]
    Stories = ["][==][  The Interview  ][==][",
               Subjects[0] + " (Interviewer) " + ": So " + Subjects[1] + ", can you tell us about your life before " +
               "you became an actor?", Subjects[1] + ": Well, I used to be" + random.choice(Occupations[0]) +
               ", and " + "I'll admit that it was a nice thing I had going on,",
               "but when I got a call from the world famous " + "director " + Subjects[2] +
               ", I knew what my true calling was.", Subjects[0] + " (Interviewer) " +
               ": And how did you feel playing the role of " + Subjects[3] +
               " (" + random.choice(Occupations[0]) + " ) in your first movie?", Subjects[1] + ": It was awesome, " +
               "being in that kind of mindset really helps your dialogue to just kind of, form, you know?",
               Subjects[0] + " (Interviewer) " + ": And what about this last movie of yours? Where you played" +
               random.choice(Occupations[1]) + "?", Subjects[1] +
               ": Oh yeah, it was great to be working alongside great" +
               " actors such as the legendary " + Subjects[4] + " and the *always* seductive " + Subjects[5] + ".",
               "But I really think that I need to thank my agent, " + Subjects[6] + " for really being there for me.",
               Subjects[0] + " (Interviewer) " + ": But weren't they arrested for assaulting a man with a flute in " +
               "Alabama, in a case that we're now calling 'Flutegate'?", Subjects[1] + ": Well, I fired " +
               Subjects[6] + " of course, but they still have a special place in my heart.", Subjects[0] +
               " (Interviewer) " + ": " +
               "Yes, of course. Well, thank you " + Subjects[0] + " for joining us today, and to our viewers, " +
               "as always, thanks for watching.", "?END?"]
    text_read(0)
if len(Subjects) == 8:
    Company = [["McDonald's", "Chick-fil-a", "Cinnabon", "Stake 'n' Shake", "Chili's", "Burger King", "Wendy's",
                "Subway"]]
    Stories = ["][==][  The Staff Of " + random.choice(Company[0]) + "  ][==][",
               "Welcome to our company, we have some wonderful staff here, let's meet some!",
               Subjects[0] + " the Manager (secretly a communist)",
               Subjects[1] + " the Assistant Manager (killed a man for this job)",
               Subjects[2] + " the Assistant to the Manager (is planning on killing the Assistant Manager)",
               Subjects[3] + " the Head Of Cashiers (frequently embezzles)",
               Subjects[4] + " the Condiments Refiller (drinks from the nozzles when no one's looking)",
               Subjects[5] + " the Janitor (Hates literally everyone; probably will remain single)",
               Subjects[6] + " the Delivery Person (kidnapped the original delivery person)",
               Subjects[7] + " the FBI Agent who's tracking " + Subjects[1] + " for suspected murder",
               "So stop on by and meet our wonderful staff! Everyone's DYING to meet you!"]
    text_read(0)
if len(Subjects) == 9:
    Stories = ["][==][  Casualties Of War  ][==][",
               Subjects[0] + ": Leader Of The 353rd Soviet Group (Death by Heart Attack)",
               Subjects[1] + ": Foot Soldier (Death by Hypothermia)",
               Subjects[2] + ": Sniper (Death by Self-Misfire)",
               Subjects[3] + ": Strategist (Death by Changing A Light Bulb With A Faulty Wire)",
               Subjects[4] + ": Tank Commander (Pressed Self-Destruct)",
               Subjects[5] + ": Pathfinder (Died In Their Sleep)",
               Subjects[6] + ": Lieutenant (Secretly double-agent, survived)",
               Subjects[7] + ": Janitor (Killed the General, survived)",
               Subjects[8] + ": General (Death by Janitor, faked death; currently seeking revenge)"]
    text_read(0)
if len(Subjects) == 10:
    Plot = [["Non-Anthropomorphic", "Insipid", "Rebellious", "Sub-race of", "Vigilante", "Autistic", "Mute", "Deaf",
             "Blind", "Ancient", "Tradition-breaking", "Willful", "Soulful", "Racist", "Immigrant", "Former-Marine",
             "Mysterious", "Ex-smoker", "Obese", "Stubborn", "Unreasonable", "Demigod", "Exiled Royal", "Ex-Pope",
             "Undead", "Vengeful", "Humorous", "Comedic", "Strictly Medicated", "Unmedicated", "Dieting",
             "Secretive", "Widowed", "Divorced", "Seductive", "Scandalous", "Drunk", "Manic", "Insane", "Paranoid",
             "Recovering", "Law-Abiding", "Traumatized", "Deeply Broken", "Sadistic", "Masochistic", "Fraudulent",
             "", "", "", "", "", "", "", "", "", "", "", ""],
            ["Werewolf", "Sentient Marshmallow", "Cyborg", "Terracotta Warrior", "Banana Trader", "Manicurist",
             "Ent", "Elf", "Elemental", "Golem", "Lord Of The Rings Cosplayer", "Anime Obsessed Teenager",
             "Jedi Master", "Sith Lord", "Gorilla", "Gamer", "Celestial", "Rapper", "Soundcloud Rapper",
             "Youtuber", "Junkie", "Desk Jockey", "Immortal Falconer", "DJ", "Master of Parkour", "Mouse"],
            [", ", ", ", ", ", " From Beyond The Rift,", "(Who's Seeking Vengeance For The Murder Of His Family)",
             " Who's Secretly An Ex-Member Of Fallout Boy,", " From The Future,", " With A Stutter,",
             " (With A Gambling Addiction),", " With Friends In High Places,", " Of The Underworld,", " With Fleas,",
             " Who's Addicted To Smelling Things,", " With An Unusually Large Nose,", " With No Friends,", "", "", "",
             "", " (Who Everyone loves to hate),", " With A Dark Past,", " Who Cries Themselves To Sleep,",
             " With The Government In Their Pocket,", " Who's Prone To Manic Episodes,",
             " Who Was Framed For A Crime They Didn't Commit,",
             " Who Falsely Testified And Got Someone Arrested For A Crime They Didn't Commit,",
             " (Who's A Closet Vegan)", " That's Occasionally Sober,"],
            [" a dog show", " a wrestling match", " a heavy-metal-folk-synth-jazz concert", " the scene of a robbery",
             " a movie premier", " an opera", " a horse race", " a joust", " a renaissance festival",
             " a cooking competition", " a bar fight", " the end of pier discussing hypothetical physics",
             " a cult ritual", " an underground tortoise fighting club", " a rave", " an ethics board review"],
            ["quickly", "be forced to", "slowly", "eventually", "find how to", "(despite all odds)", "immediately",
             "surely", "begrudgingly", "absolutely", "inevitably", "certainly"],
            ["the Force", "the Dark Side", "the Jedi", "Kung Fu", "Karate", "Taekwondo", "magic", "street fighting",
             "the Super Saiyan", "wizardry", "mixed martial arts", "Jujutsu", "fencing", "kickboxing", "Judo",
             "Aikido", "Krav Maga", "wrestling", "the luchador", "Sumo wrestling", "Stick-fighting", "parkour",
             "the assassin", "the Bo Staff", "Muay Thai", "Brazilian Jiu-jitsu", "jousting"],
            ["The Executioner", "The Not-So-Friendly Person", "The Thug", "The Rogue", "The Shadow Stalker",
             "The Bone-Crusher", "Bonesaw", "The Mini-Boss", "Dark Vaper", "Hawk Lie", "White Cheetah", "Brown Puma"],
            ["Little Hero 4", "Just Us League", "The Advantages", Subjects[0] + Subjects[1] + Subjects[6] + Subjects[7],
             "Generic Super Team", "Super Awesome Mega Epic Team Harbinger Intuitive Nexus Gods" +
             " (SAME THING, for short)"]]
    Stories = ["][==][  The Pilot  ][==][",
               "*Cue epic music with deep base intervals*", Subjects[0] + " is a/an " + random.choice(Plot[0]) +
               " " + random.choice(Plot[1]) + random.choice(Plot[2]), "and the other is " + Subjects[1] +
               ", a/an " + random.choice(Plot[0]) + " " + random.choice(Plot[1]) + random.choice(Plot[2]),
               "alone, they are weak, but together they are unbeatable; they are " + Subjects[0] + " and " +
               Subjects[1] + "!", "*Theme song*", ". . .", "Their story started when they were at" +
               random.choice(Plot[3]), "where (after they began to leave) a fire started, and threatened to burn" +
               " down the whole place!", "Both of our heroes dashed back to try and save everyone, and by the end of " +
               "the night, they had saved almost everyone...", "Everyone except " + Subjects[0] +
               "'s best friend " + Subjects[2] + " who was crushed by a falling beam, and " + Subjects[3] +
               ", who had raised " + Subjects[1] + " since they were young.", "Both of them vowed to find out the" +
               " culprit behind this heinous crime, but little did they know that they would " +
               random.choice(Plot[4]) + " become friends in the process...", "After months of investigations, " +
               "they had received a tip from " + Subjects[4] + ", the Chief Of Police" + random.choice(Plot[2]),
               "telling them how there was an illegal underground corporation that was most likely responsible" +
               " for the fire.", "It was run by " + Subjects[5] + ", a homicidal maniac with a history in arson.",
               "Both " + Subjects[0] + " and " + Subjects[1] + " leapt to action! They went to the coordinates" +
               " that " + Subjects[4] + " had left them, but it was just an empty warehouse!",
               "But then, at that moment, the warehouse doors had closed behind them!", "The Chief sold them out!",
               "That lying dirty scum!", "But at that moment, soldiers began going in the building from all entrances!",
               "But these aren't military, they belong to " + Subjects[5] + "!", "Just when things seemed bleakest, ",
               "Chief Of Police " + Subjects[4] + " drove threw the front door and began shooting at the soldiers!",
               "Just as our heroes ran (per the Chief's instructions), " + Subjects[4] + " left his car and" +
               " began running towards the soldiers with grenades in his hands.", "After " + Subjects[0] + " and " +
               Subjects[1] + " were far enough away, the Chief let go and blew up the warehouse along with the" +
               " soldiers... and themselves.", Subjects[1] + " swore to avenge the Chief's death.",
               "And now our heroes knew where to go, as the soldiers left their vehicles outside.",
               "But our heroes couldn't take on " + Subjects[5] + " on their own, they needed some help...",
               "After some searching, they came across " + Subjects[6] + ", a/an " + random.choice(Plot[0]) + " " +
               random.choice(Plot[1]) + random.choice(Plot[2]), "and " + Subjects[7] + ", a/an " +
               random.choice(Plot[0]) + " " + random.choice(Plot[1]) + random.choice(Plot[2]) + ".",
               "Now, they were ready to defeat " + Subjects[5] + ". . .", "But as they began their journey, " +
               Subjects[6] + " pointed out that they have no training! So, (begrudgingly) they looked on Craiglist" +
               " for someone willing to give lessons on how to fight.", "And that's how they found Sensei " +
               Subjects[8] + ", someone who bought their degree online, but nevertheless promised to teach them in" +
               " the ways of " + random.choice(Plot[5]) + ".", "It wasn't long before our intrepid group became " +
               "Masters.", "But before our heroes left, Sensei " + Subjects[8] + " warned them about " + Subjects[9] +
               ".", Subjects[9] + " is the guard to " + Subjects[5] + "'s office, and they have such a reputation, " +
               "that they're nickname is " + random.choice(Plot[6]) + ".", "The heroes listened and bowed to their" +
               " Sensei.", "Once they arrived at their enemy's building, " + Subjects[6] + " and " + Subjects[7] +
               " volunteered to fight " + Subjects[9] + ", and " + Subjects[0] + " would fight " + Subjects[5] +
               " with " + Subjects[1] + ".", "It was a long and hard battle, but using the ways of Sensei " +
               Subjects[8] + " (who at this moment was on their couch, drinking beer), they brought " + Subjects[5] +
               " to justice.", "Our heroes then went on to form the greatest superhero team of all time, " +
               random.choice(Plot[7]) + "!"]
    text_read(0)

# This is all pretty straight-forward
