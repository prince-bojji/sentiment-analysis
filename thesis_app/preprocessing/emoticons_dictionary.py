def transform_emoticons(text):
    # Mapping emoticons to their emoticon equivalents
    emoticon_dict = {
        #A
        "-|--'" : "Airplane",
        ":-o" : "Alarmed",
        "::-)" : "Alien",
        "'.'" : "Alien",
        ">-)" : "Alien",
        ":8)" : "Alien",
        "(+^+)" : "Alien",
        "(#*#)" : "Alien",
        "0=)" : "Angel",
        "O:)" : "Angel",
        "(a)" : "Angel",
        "O:-)" : "Angel",
        "0-)<" : "Angel",
        "0;)" : "Angel",
        "0:)" : "Angel",
        "0*-)" : "Angel",
        "J^" : "Angel",
        ":-t" : "Angry",
        "X-(" : "Angry",
        "X(" : "Angry",
        ":-@" : "Angry",
        ":@" : "Angry",
        ">-(" : "Angry",
        "D<" : "Angry",
        "X-(" : "Angry",
        ">:(" : "Angry",
        ">:-(" : "Angry",
        "-_-+" : "Angry",
        ":-Z" : "Angry",
        ">(" : "Angry",
        ">:-o" : "Angry",
        ">:-0" : "Angry",
        "^w^" : "Anime_Smile",
        "@_@" : "Annoyed",
        "¬¬" : "Annoyed",
        ">_<*" : "Annoyed",
        ":/" : "Annoyed",
        ">:-(" : "Annoyed",
        "¬_¬" : "Annoyed",
        ">: o" : "Antelope",
        "m(_)m" : "Apology",
        "=D>" : "Applause",
        "0-+" : "April",
        ">A<" : "Archangel",
        ">--->>" : "Arrow",
        "<---<<<" : "Arrow",
        "<|-)" : "Asian",
        "|-I" : "Asleep",
        "(0)-<-<" : "Astronaut",
        "~X(" : "At_Wits_End",
        "(au)" : "Auto",
        ":S" : "Awkward",

        #B
        ":=8)" : "Baboon",
        "~:0" : "Baby",
        "~O><" : "Baby",
        "[{-_-}]" : "Baby",
        "~:O" : "Baby",
        "X:-)" : "Bad_Hair_Day",
        "=.=" : "Bad_Idea",
        "C:-|" : "Bald",
        "(8-)" : "Bald",
        ":-)-S=~" : "Ballerina",
        "o~" : "Balloon",
        "(::( )::)" : "Band-Aid",
        "(::[]::)" : "Band-Aid",
        "~'v" : "Bangs",
        ":-%" : "Banker",
        ":-C~" : "Barfing",
        "8o|" : "Baring Teeth",
        ": 8-1" : "Bart_Simpson",
        "d:-)" : "Baseball_Player",
        "d:-p" : "Baseball_Player",
        "d: )" : "Baseball_Player",
        "^v^" : "Bat",
        "(^+.+^)" : "Bat",
        "B-|" : "Batman",
        "B-)" : "Batman",
        ";;)" : "Battling_Eyelashes",
        "('')-.-('')" : "Bear",
        "(''')-.-(''')" : "Bear",
        ":)#" : "Beard",
        "(:-{~" : "Beard",
        ":-)}" : "Beard",
        ":-{)>" : "Beard",
        "(#_#)" : "Beaten_Up",
        "(O_.)" : "Beaten_Up",
        "(=_—)" : "Beaten_Up",
        ": =" : "Beaver",
        "o_0" : "Bewildered",
        "(*)/ (*)" : "Bicycle",
        ":D" : "Big_Grin",
        ":-D" : "Big_Grin",
        ":-(|)" : "Big_Lips",
        "*<:)" : "Birthday_Hat",
        "<>:-)" : "Bishop",
        "!-(" : "Black_Eye",
        "#-)" : "Blinking",
        "^^" : "Blissful",
        "<^^*>" : "Blissful",
        "(@)/(@)" : "Bloodshot Eyes",
        ':-">' : "Blushing",
        '=">' : "Blushing",
        ":-*>" : "Blushing",
        "=^}" : "Blushing",
        ':")' : "Blushing",
        "=^_^=": "Blushing",
        "=<_<=" : "Blushing",
        ":*-)" : "Blushing",
        ':">' : "Blushing",
        ">//<" : "Blushing",
        "#^_^#" : "Blushing",
        "@=" : "Bomb",
        ":-o" : "Bored",
        "(-_-)" : "Bored",
        "\-o" : "Bored",
        ":z" : "Bored",
        "@-@" : "Bored",
        ":-)8" : "Bow_Tie",
        ":-)x" : "Bow_Tie",
        "o(^_-)O" : "Boxer",
        "(:-)" : "Boy",
        ":-)^<" : "Boy",
        ":-#" : "Braces",
        ":-{#}" : "Braces",
        "=#" : "Braces",
        "%-(" : "Broken_Glasses",
        "</3" : "Broken_Heart",
        "=((" : "Broken_Heart",
        "<~3" : "Broken_Heart",
        "^ ○ ^" : "Bubbly_Girl",
        ":-(=)" : "Buckteeth",
        ":B" : "Bucktooth",
        ":^(" : "Bummed_out",
        "(=^_^=)" : "Bunny",
        "(O:3" : "Bunny",

        #C
        ":-c" : "Call_Me",
        "~M'" : "Camel",
        "(p)" : "Camera",
        "o=" : "Candle",
        "~=" : "Candle",
        ">(///)<" : "Candy",
        "((-_(-_-)_-))" : "Care_Crowd",
        "($)" : "Cash",
        ">'o'<" : "Cat",
        "=^.^=" : "Cat",
        ">'.'<" : "Cat",
        "(^-_-^)" : "Cat",
        "=^_^=" : "Cat",
        "q:-)" : "Catcher",
        "~o(:-)" : "Cave_Diver",
        ":-@" : "Chatterbox",
        ":( )" : "Chatterbox",
        "（⌒▽⌒）" : "Cheerful",
        "(＾▽＾)" : "Cheerful",
        "C=:-)" : "Chef",
        "(-: =3" : "Chef",
        "(:=3" : "Chef",
        "~:>" : "Chicken",
        "<°)" : "Chicken",
        "(*>" : "Chicken",
        "8^" : "Chicken",
        "-{:-]" : "Chinese_Hat",
        "^)_(^" : "Chubby",
        "(='.'=)" : "Chubby_Cat",
        "(:)" : "Clam",
        ":O)" : "Clown",
        "(c:>*" : "Clown",
        "=:-)" : "Cobbler",
        "(_)>" : "Coffee",
        "C[_]" : "Coffee_Cup",
        "╹﹏╹" : "Cold",
        "?_?" : "Cold_Stare",
        "(co)" : "Computer",
        ":-r" : "Concentrating",
        ":^)" : "Confounded",
        ":-Q" : "Confused",
        ":-/" : "Confused",
        ":-S" : "Confused",
        ":s" : "Confused",
        ":-$" : "Confused",
        "(@_@)" : "Confused",
        "=?" : "Confused",
        ",':(" : "Confused",
        "(p_q)" : "Confused",
        "-.-?" : "Confused",
        "?:|" : "Confused",
        ":-?" : "Confused",
        "o_O" : "Confused",
        ":~/" : "Confused",
        "B-)" : "Cool",
        ":B)" : "Cool",
        "B)" : "Cool",
        "3:-O" : "Cow",
        "3:O" : "Cow",
        "<):-)" : "Cowboy",
        "<):)" : "Cowboy",
        "C):)" : "Cowboy",
        "(-:(3" : "Cowboy",
        "C):-)" : "Cowboy",
        "{:-)" : "Cowgirl",
        "%-)" : "Crazy",
        ">.<" : "Cross-Eyed",
        ":_(" : "Crying",
        ":*(" : "Crying",
        "T_T" : "Crying",
        ":((" : "Crying",
        ":'(" : "Crying",
        ";_;" : "Crying",
        "QQ" : "Crying",
        "T^T" : "Crying",
        "='(" : "Crying",
        "i_i" : "Crying",
        ":'-C" : "Crying",
        ";-;" : "Crying",
        ":-(" : "Crying",
        ":~-(" : "Crying",
        "(!_!)" : "Crying",
        "(ToT)" : "Crying",
        ":'-(" : "Crying",
        ";(" : "Crying",
        "T.T" : "Crying",
        ":cry:" : "Crying",
        "-,_-," : "Crying",
        "(¬‿¬)" : "Cunning",
        "|_|" : "Cup",
        "C(_)" : "Cup",
        "|_P" : "Cup",
        "@:-)" : "Curly_Hair",
        "8:-)" : "Curly_Hair",
        ":-@!" : "Cursing",
        "X3" : "Cute",
        "n_n" : "Cute",
        "o-)" : "Cyclops",
        "O-(" : "Cyclops",
        ".)" : "Cyclops",
        "Q-)" : "Cyclops",
        "*-(" : "Cyclops",
        "O.)" : "Cyclops",
        "๏-)" : "Cyclops",

        #D
        "\:D/" : "Dancing",
        "\o/" : "Dancing",
        "*-*" : "Dazed",
        "*_*" : "Dazed",
        "x_x" : "Dead",
        "x.x" : "Dead",
        "XP" : "Dead",
        "(u_u)" : "Dead",
        "._." : "Depressed",
        "(._.)" : "Depressed",
        ">:)" : "Devil",
        ":|" : "Disappointed",
        ":-|" : "Disappointed",
        "-__-" : "Disinterested",
        "d^_^b" : "DJ",
        "d[-_-]b" : "DJ",
        "(>.<)" : "Doh",
        ": T" : "Doubtful",
        "\%/" : "Drink",
        ":P" : "Drooling",
        ":P~" : "Drooling",
        ":p~~" : "Drooling",
        ":)_" : "Drooling",
        ":*)" : "Drunk",
        "o_O" : "Drunk",
        ":#)" : "Drunk",
        "<:-)" : "Dunce",
        "<:-|" : "Dunce",

        #E
        "p^_^q" : "Earphones",
        "::--((" : "Earthquake",
        ":g" : "Eating",
        ":K" : "Eating",
        ":~" : "Elephant",
        "~:3" : "Elephant",
        "@=)" : "Elvis",
        "2:)" : "Elvis",
        "?:-p" : "Elvis",
        "5:-)" : "Elvis_Presley",
        "&:-)" : "Elvis_Presley",
        ":-$" : "Embarrassed",
        ":$" : "Embarrassed",
        ":-[" : "Embarrassed",
        "(#^.^#)" : "Embarrassed",
        "//_^" : "Emo",
        "(//.^)" : "Emo",
        "(//_^)" : "Emo",
        "(//_-)" : "Emo",
        "c//_+." : "Emo",
        "//_T)o." :  "Emo",
        "d(//^)b" :  "Emo",
        ">:3" :  "Evil_Cuteness",
        "):D}" :  "Evil_Face",
        ":{)" : "Evil_Face",
        ">:~>" :  "Evil_Face",
        ">:{)>" : "Evil_Face",
        "]}:-)>" : "Evil_Face",
        ">:D": "Evil_Laugh",
        ">=)" : "Evil_Smile",
        "/^^\!" : "Exasperated",
        ":-O" : "Excited",
        "(*-*)" : "Excited",
        ":o" : "Excited",
        "#-)" : "Exhausted",
        "P-)" : "Eye_Patch",
        "b-)" : "Eye_Patch",
        "}=D" : "Eyebrows",

        #F
        ":&" : "Fail",
        "v v" : "Fangs",
        "o,..,o" : "Fangs",
        "<><" : "Fish",
        "\@_O_@/" : "Flexing",
        "t(-_-t)" : "Flipping_The_Bird",
        ";D" : "Flirting",
        ";-)" : "Flirty",
        ";3" : "Flirty Grin",
        "D';" : "FML",
        ":-!" : "Foot_In_Mouth",
        ":'|" : "Freezing",
        ":pd:" : "French_Kiss",
        ":bq:" : "French_Kiss",
        "P*" : "French_Kiss",
        "8-|" : "Frightened",
        "8)" : "Frog",
        "8)~~*" : "Frog",
        ":(?)" : "Frog",
        ":-(" : "Frown",
        ":(" : "Frown",
        ":-(" : "Frowning",
        "X[" : "Frustrated",
        "><" : "Frustrated",
        "B/" : "Frustrated",
        ">.<*" : "Frustrated",
        ":-L" : "Frustrated",
        "B-}" : "Funny",
        "*:*" : "Fuzzy",

        #G
        ":-(*)" : "Gag_Me",
        "=:o" : "Gasp",
        "3>(" : "Geezer",
        "(D:-]" : "General",
        "<('')>" : "Ghost",
        "(x)" : "Girl",
        "(-_-)#" : "Girl",
        ">:[" : "Glaring",
        "\_/" : "Glass",
        "8-)" : "Glasses",
        "B-)" : "Glasses",
        "8)" : "Glasses",
        "B)" : "Glasses",
        "o/" : "Gold",
        "(ToT)/~~~" : "Goodbye",
        "8-]" : "Googly-Eyed",
        ":8]" : "Gorilla",
        "8:]" : "Gorilla",
        "|<:-)" : "Graduate",
        "L:-)" : "Graduate",
        "Q:-)" : "Graduate",
        "$_$" : "Greedy",
        "$__$" : "Greedy",
        "\o o/" : "Greeting",
        ":->" : "Grin",
        ":D" : "Grin",
        ":oP" : "Grin",
        ":-!" : "Gross",
        ">:(" : "Grumpy",
        "^_^;" : "Guilty",
        "︻┳テ=一" : "Gun",
        "︻デ═一" : "Gun",
        "S:~)" : "Guy",

        #H
        "((:D" : "Hair",
        "#:-)" : "Hair",
        "L-:" : "Half_Smile",
        "=)" : "Happy",
        ":-)" : "Happy",
        ":)" : "Happy",
        "^.^" : "Happy",
        "(:" : "Happy",
        "^-^" : "Happy",
        "8D" : "Happy",
        "(^_^)" : "Happy",
        "8^)" : "Happy",
        ":-}" : "Happy",
        ":)))" : "Happy",
        "(^ u ^)" : "Happy",
        "B^)" : "Happy",
        "8-D" : "Happy",
        "8^D" : "Happy",
        "^=^" : "Happy",
        "uwu" : "Happy_Anime_Face",
        "OwO" : "Happy_Furry_Animal",
        ':")' : "Happy_Tears",
        ">O<" : "Harry_Potter_Snitch",
        "q=)" : "Hat",
        "0(o.o)0" : "Headphones",
        "d(-_-)b" : "Headphones",
        "<3" : "Heart",
        "\,,/" : "Heavy_Metal",
        "o/\o" : "High_Five",
        "^_^/" : "High_Five",
        ":-/" : "Hmmm",
        "{ }" : "Hug",
        "<(^.^<)" : "Huge",
        ":0" : "Hungry",
        ":-[]" : "Hungry",
        "XD" : "Hyper",
        "<(*.*<)" : "Huggle",
        ":D<" : "Hugs",

        #I
        ":^)" : "I_Do_Not_Know",
        "X_X" : "I_Do_Not_Want_to_See",
        "_\m/" : "I_Love_You",
        "< }" : "Ice_Cream",
        "*-:)" : "Idea",
        "(*_*)" : "In_Love",
        ":]" : "In_Love",
        ":-]" : "In_Love",
        "._." : "Inadequate",
        ":-S" : "Incoherent",
        "(o_O)" : "Incredulous",
        ":-|" : "Indifferent",
        ":-I" : "Indifferent",
        "0:-)" : "Innocent",
        "O:D" : "Innocent",
        "?_?" : "Irritated",
        ":<|" : "Ivy_League",

        #J
        "8(>_<)8" : "Jealous",
        "8-)" : "Joe Cool",
        "((*J*))" : "John_Lennon",
        "(8 {" : "John_Lennon",
        ":-]" : "Jovial",
        "o(^o^)o" : "Joyful",
        "\ ^_^ /" : "Joyful",
        "(=^ ^=)" : "Joyful",
        ":-DD" : "Jubilant",

        #K
        "(:-#" : "Keeping Quiet",
        "X:-)" : "Kid",
        "\VVV/" : "King",
        "<( '.' )>" : "Kirby",
        "<(^.^)>" : "Kirby",
        "<('.'<)" : "Kirby",
        "(>'.')>" : "Kirby",
        "<(^_^)>" : "Kirby",
        "<('.')>" : "Kirby",
        "<('-'<)" : "Kirby",
        "(>'')>" : "Kirby",
        "c(-_-c)" : "Kirby",
        "c(','c)" : "Kirby",
        "^(^.^)^" : "Kirby",
        "<(•-•<)" : "Kirby",
        ":-)*" : "Kiss",
        ":-X" : "Kiss",
        ":-*" : "Kiss",
        ":*)" : "Kiss",
        "8^*" : "Kiss",
        ":+" : "Kiss",
        ":*" : "Kiss",
        ":%" : "Kiss",
        ":}{:" : "Kisses",
        ":**:" : "Kissing",
        "(-}{-)" : "Kissing",
        "( '}~{' )" : "Kissing",
        "( '}{' )" : "Kissing",
        "(}{)" : "Kissing",
        "(=^-^=)" : "Kitten",
        "^..^" : "Kitten",
        "=^.^=" : "Kitty",
        "=+=" : "Kitty",
        ":3" : "Kitty",
        "=^w^=" : "Kitty",
        "(=^･ｪ･^=)" : "Kitty",
        ">>:-|" : "Klingon",
        "+<||-)" : "Knight",
        "@(*o*)@" : "Koala",
        "(-O-)" : "Koala",
        ":*)O" : "Koala",

        #L
        "-.-" : "Lame",
        "l8r)" : "Later",
        ":)" : "Laughing",
        ":))" : "Laughing",
        "XD" : "Laughing",
        ":L" : "Laughing",
        ":'D" : "Laughing",
        "=^D" : "Laughing",
        ">8-D" : "Laughing",
        "(^_^)" : "Laughing",
        "=-D" : "Laughing",
        "=D" : "Laughing_Out_Loud",
        "X-D" : "Laughing_Out_Loud",
        ")-:" : "Left-handed_Sad_Face",
        "(-:" : "Left-handed_Smiley_Face",
        ":^o" : "Liar_Liar",
        ":-9" : "Licking",
        ":3" : "Lion",
        ":-*" : "Lips_are_Sealed",
        ":()" : "Lipstick",
        ">-<" : "Livid",
        "d-_-b" : "Listening_to_Music",
        "d^_^b" : "Listening_to_Music",
        "@---" : "Lollipop",
        ":~)" : "Long_Nose",
        "<@> <@>" : "Look_at_Me",
        ">_>" : "Looking",
        "<_<" : "Looking",
        ">.>" : "Looking",
        "L-)" : "Loser",
        "<3" : "Love",
        ":x" : "Love_Struck",
        "__." : "Lying_Down",

        #M
        "=/" : "Mad",
        ">=(" : "Mad",
        "~:(" : "Mad",
        ">=[" : "Mad",
        ">}:-(" : "Mad",
        ":U" : "Mad",
        ")8^(" : "Mad",
        ">_<" : "Mad",
        ":-/" : "Mad",
        ":x" : "Mad",
        ":-x" : "Mad",
        "=/" : "Mad",
        ">:-I" : "Mean",
        "@_@" : "Mesmerized",
        "\m/" : "Metal",
        "lml" : "Metal",
        "lml_" : "Metal",
        ":p" : "Mischievous",
        ":}" : "Mischievous",
        "=)=" : "Mixed_Feelings",
        ":D:" : "Mixed_Feelings",
        ":-{" : "Mustache",
        ":{" : "Mustache",
        "={D" : "Mustache",
        ":{D" : "Mustache",

        #N
        ":-SS" : "Nailbiting",
        "_:^)" : "Native American",
        "~,~" : "Napping",
        ":3" : "Naughty_Grin",
        ":-B" : "Nerd",
        "8-|" : "Nerd",
        "8-B" : "Nerd",
        "B-|" : "Nerd",
        "8|" : "Nerd",
        "B|" : "Nerd",
        "(:^(" : "Nose",

        #O
        "O_o" : "Oddball",
        ":-j" : "Oh_Go_On",
        "|:-{)~" : "Old_Man",
        ":)]" : "On_the_Phone",
        "':-(" : "One_Eyebrow",
        ">.-)" : "One-Eyed_Smile",
        ":-D" : "Open-Mouthed_Smile",
        ":d" : "Open-Mouthed_Smile",
        ":>" : "Open-Mouthed_Smile",
        "E:-)" : "Operator",
        "^_^" : "Overjoyed",
        ".^_^." : "Overjoyed",
        "-(*o*)-" : "Owl",
        "(^o^)" : "Owl",
        "^(OvO)^" : "Owl",
        "~@v@~" : "Owl",
        "{0,0}" : "Owl",
        "}°,°{" : "Owl",

        #P
        ":v" : "Pacman",
        "(>_<)" : "Painful",
        "8:(" : "Panda",
        "\(>o<)/" : "Panicking",
        "<:o)" : "Party",
        "<o)" : "Party",
        "*<(:)" : "Party_Hat",
        "<l:0" : "Partying",
        "(:V" : "Pato",
        ":)>-" : "Peace",
        "('v')" : "Penguin",
        "<(^)" : "Penguin",
        "8>" : "Penguin",
        ":-/" : "Perplexed",
        "XP" : "Perplexed",
        "0~0" : "Perplexed",
        "<:^]" : "Person",
        ">:P" : "Phbbbbt",
        ":=)" : "Pig",
        "<(:-)" : "Pilgrim",
        "(__)" : "Pill",
        ":---)" : "Pinnochio",
        "<%)" : "Pizza",
        "<|" : "Pizza",
        ":^r" : "Playful",
        "(^̮^)" : "Pleased",
        ":-I" : "Poker_Face",
        "~@~" : "Poop",
        ":<" : "Pout",
        "\o/" : "Praise The Lord",
        "_/\_" : "Prayer",
        "+:-)" : "Priest",
        "\<><>/" : "Prince",
        "\&&&/" : "Princess",
        ":}" : "Princess",
        ":&" : "Puke",
        "(^:^)" : "Pumpkin",
        "(~~)" : "Pumpkin",
        "*|" : "Punch",
        "-:-/" : "Punk",
        "-:(" : "Punk_Rocker",

        #Q
        "\%/" : "Queen",
        ":?:" : "Question",

        #R
        "8:3" : "Rabbit",
        ">-=]" : "Rabbit",
        "('.')" : "Rabbit",
        "~~:-(" : "Rain",
        "/:)" : "Raised_Eyebrow",
        ">=D" : "Revenge",
        "(})" : "Right_Hug",
        ":|]" : "Robot",
        ":]" : "Robot",
        ":]]" : "Robot",
        "[:]" : "Robot",
        "<(-_-)>" : "Robot",
        "~(o_o)~" : "Robot",
        "\m/(**)\m/" : "Rock_On",
        "\m/@_@\m/" : "Rock_On",
        "\m/>.<\m/" : "Rocker",
        "\m/(><)\m/" : "Rocker",
        "\m/(>.<)\m/" : "Rocker",
        "\m/(*o*)\m/" : "Rocking_Out",
        "\m/" : "Rocking",
        "8-|" : "Rolling_Eyes",
        ">>" : "Rolling_Eyes",
        "9_9" : "Rolling_Eyes",
        "@@" : "Rolling_Eyes",
        "c.c" : "Rolling_Eyes",
        "=))" :   "Rolling_On_The_Floor_Laughing",

        #S
        "=(" : "Sad",
        ":-(" : "Sad",
        ":(" : "Sad",
        "T.T" : "Sad",
        "=[" : "Sad",
        ":c" : "Sad",
        "D:" : "Sad",
        "Y_Y" : "Sad",
        "v.v" : "Sad",
        "(/_\)" : "Sad",
        "):" : "Sad",
        ";-(" : "Sad",
        ";~;" : "Sad",
        ";^;" : "Sadness",
        "/:-)" : "Sailor",
        "M:-)" : "Salute",
        "*<]:{)" : "Santa",
        "*<(:-{)}" : "Santa",
        "*<:-)" : "Santa_Claus",
        "*<|:-{)}" : "Santa_Claus",
        "<|:)}" : "Santa_Claus",
        "0<[]:-)>>" : "Santa_Claus",
        "*<|:o)>" : "Santa_Claus",
        "<[]:o{|>" : "Santa_Claus",
        "*<[]:o{|>" : "Santa_Claus",
        ":-7" : "Sarcastic",
        ";s" : "Sarcastic",
        ":S" : "Sarcastic",
        "D:" : "Scared",
        ":!" : "Scared",
        "!:-)" : "Scholar",
        "*s*" : "School",
        "8<" : "Scissor",
        ";^!" : "Secret",
        "8==8" : "Secret_Telling",
        "=O" : "Shocked",
        "o_o" : "Shocked",
        ":-o" : "Shocked",
        "8-0" : "Shocked",
        "(*•*)" : "Shocked",
        ":-V" : "Shouting",
        ":\/" : "Shouting",
        ":^V" : "Shouting",
        "|----D" : "Shovel",
        "(*^_^*)" : "Shy",
        "-_-" : "Shy",
        "(^^;)" : "Shy",
        "(#^.^#)" : "Shy",
        ":-&" : "Sick",
        "+o(" : "Sick",
        "(-__-)" : "Sick",
        "=P" : "Silly",
        "(^o^)" : "Singing",
        "]:" : "Skateboard",
        "o->-</:" : "Skater",
        ":-/" : "Skeptical",
        ":-7" : "Skeptical",
        ":/" : "Skeptical",
        "(-_-)" : "Sleeping",
        "Z_Z" : "Sleeping",
        "<-.->" : "Sleeping",
        ":-)" : "Smile",
        ":)" : "Smile",
        ":|)" : "Smile",
        "C:" : "Smile",
        ":A" : "Smile",
        "=]" : "Smile",
        ":]" : "Smile",
        ":=)" : "Smile",
        ":^J" : "Smiling",
        "^^" : "Smiling",
        "^&^" : "Smiling",
        ":-1" : "Smirk",
        ":-," : "Smirk",
        ":-d~" : "Smoker",
        ":-Q" : "Smoking",
        ":- i" : "Smoking",
        ":-?" : "Smoking",
        ":>" : "Smug",
        "@_v" : "Snail",
        "_@_v" : "Snail",
        "_@v" : "Snail",
        "~@~:" : "Snail",
        "~<:<<<<<>" : "Snake",
        "<=====<>~" : "Snake",
        ":-`|" : "Sniffling",
        ":<)" : "Snobby",
        "|^O" : "Snoring",
        "(:>])( )( )" : "Snowman",
        "(:^)_)_)" : "Snowman",
        "[l:^)" : "Snowman",
        "(:-)(°°°)" : "Snowman",
        "/:-)" : "Soldier",
        "c]:{D" : "Sombrero",
        ">.<" : "Sour",
        ":-|" : "Speechless",
        ":|" : "Speechless",
        "^;;^" : "Spider",
        "^''^" : "Spider",
        ">:-I" : "Spock",
        "(><)" : "Squinting",
        "-_-" : "Squinting",
        "*~*" : "Star_Gazed",
        ";@" : "Streaming_Mad",
        "|:-|" : "Stern",
        "O-[--<" : "Stick_figure",
        ">-/-@" : "Stick Man",
        ":-P" : "Sticking_Tounge_Out",
        ":P" : "Sticking_Tounge_Out",
        ">:P" : "Sticking_Tounge_Out",
        ":-r" : "Sticking_Tounge_Out",
        ":pp" : "Sticking_Tounge_Out",
        "(:-p)" : "Sticking_Tounge_Out",
        ":-{ -__-:" : "Stinky",
        ":|" : "Straight face",
        "@?@" : "Stunned",
        "[o].[o]" : "Stunned",
        "&;-P" : "Suave",
        "8-)" : "Sunglasses",
        "B-)" : "Sunglasses",
        "B-D" : "Sunglasses",
        "B:-)" : "Sunglasses",
        "8-|" : "Sunglasses",
        "8|" : "Sunglasses",
        "B-|" : "Sunglasses",
        "8)" : "Sunglasses",
        "_\|/_" : "Sunset",
        ":o" : "Surprised",
        ":-O" : "Surprised",
        ":O" : "Surprised",
        "{:o" : "Surprised",
        ":-()" : "Surprised",
        "=0" : "Surprised",
        "*.*" : "Surprised",
        "(O.O)" : "Surprised",
        "=^o" : "Surprised",
        "=^0" : "Surprised",
        "0-0" : "Suspense",
        ":#" : "Swearing",
        "`:-)" : "Sweating",
        "(:|" : "Sweating",
        "8-)" : "Sunglasses",
        "__/\o_" : "Swimming",
        "x_O" : "Swollen Eye",

        #T
        ":-{ }" : "Talking",
        ":^y" : "Talking",
        ":y" : "Talking",
        ":p" : "Teasing",
        "B^P" : "Teasing",
        ":^P" : "Teasing",
        "8^P" : "Teasing",
        ":O)" : "Teddy_Bear",
        "\(-_- )" : "Thank_You",
        ":-?" : "Thinking",
        "*-)" : "Thinking",
        ":?" : "Thinking",
        "(p_-)" : "Thinking",
        "q('-')p" : "Thumbs_Down",
        ":-q" : "Thumbs_Down",
        "d'-'" : "Thumbs_Up",
        "d'-'b" : "Thumbs_Up",
        ":-bd" : "Thumbs_Up",
        "(^-^)b" : "Thumbs_Up",
        "d-(^.^)z" : "Thumbs_Up",
        ":-t" : "Time Out",
        "=_=" : "Tired",
        "(:|" : "Tired",
        "%-|" : "Tired",
        "%-/" : "Tired",
        "(z_z~.)" : "Tired",
        "(=_=)" : "Tired",
        ":-&" : "Tongue_Tied",
        "(:@" : "Tongue_Tied",
        "[|:)" : "Top Hat",
        "=')" : "Touched",
        "{:-)" : "Toupee",
        "(>_<)>" : "Troubled",
        "(^_^;)" : "Troubled",
        "<.<" : "Troublemaker",

        #U
        ".-=-." : "UFO",
        "=-O" : "Uh-oh",
        "(o|o)" : "Ultraman",
        "(---," : "Umbrella",
        "(ㆆ_ㆆ)" : "Unamused",
        "x:-/" : "Uncertain",
        "/:-|" : "Undecided",
        ":<" : "Unhappy",
        "|:-)" : "Unibrow",
        "|:" : "Unimpressed",
        "（￣～￣）" : "Unimpressed",
        ":/" : "Unsure",
        ">.<" : "Upset",
        "D:<" : "Upset",
        ">=P" : "Upset",
        ">-:O" : "Upset",
        ".-." : "Upside_Down",
        "P:" : "Upward_Lick",

        #V
        ":-E" : "Vampire",
        "(';.;')" : "Vampire",
        "@,.,@" : "Vampire",
        "(o,..,o)" : "Vampire",
        "(=,..,=)" : "Vampire",
        ":-[" : "Vampire",
        ":(=" : "Vampire",
        ":-[" : "Vampire_Bat",
        "^,..,^" : "Vampire_Bat",
        "(^-^:)" : "Vampire_Bite",
        "=D" : "Very_Happy",
        ":-))" : "Very_Happy",
        ":-((" : "Very_Sad",
        "v(^_^)v" : "Victory",
        ":O=" : "Vomit",
        "](-[3" : "Viking",

        #W
        ":-w" : "Waiting",
        "(^_^)/" : "Waving",
        ";w;" : "Weeping",
        ":-P" : "Whatever",
        "-_-" : "Whatever",
        ":-1" : "Whatever",
        "(¬_¬)" : "Whatever",
        ";-/" : "Whatever",
        ":'-(" : "Whining",
        ':-"' : "Whistling",
        "8-O" : "Wide_eyed",
        ";p" : "Winking",
        ";-P" : "Winking",
        ";^)" : "Winking",
        ",-)" : "Winking",
        "(^_~)" : "Winking",
        "9-)" : "Winking",
        ";-)" : "Winking",
        ";)" : "Winking",
        "~_^" : "Winking",
        ";()" : "Winking",
        "o.o?" : "Wondering",
        ":^)" : "Wondering",
        ":-S" : "Worried",
        ">w<" : "Worried",
        ":S" : "Worried",

        #X
        "(xx)" : "Xbox",
        "[x]" : "Xbox",

        #Y
        "_/)" : "Yacht",
        "|-O" : "Yawn",
        "(:|" : "Yawn",
        ".'U" : ".'U",
        ">:O" : "Yelling",
        "=^Y" : "Yelling",
        ":-(0)" : "Yelling",
        ":(*)" : "Yelling",
        "<(-_-)>" : "Yoda",
        "<(-.-)>" : "Yoda",
        ":-0>" : "Yuck_Face",
        ":-9" : "Yum",

        #Z
        ":#" : "Zip_It",
        "F(x_x)F" : "Zombie",
        "[¬º-°]¬" : "Zombie",
        "(-_0)" : "Zombie"
    }

    # Replace each emoticon with its corresponding emoticon equivalent
    for emoticon, unicode_equiv in emoticon_dict.items():
        text = text.replace(emoticon, " Emoticon_"+unicode_equiv +" ")

    return (text)