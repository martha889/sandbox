"""
A program to analyze lyrics of an artist (simply show the frequency of words used)

Taylor Swift's kaggle database has been used in this program (lyrics till the Lover album)

"""

punc = {',', '?', ':', ';', "'", '"', '-', ')', '('}


def lyrics_to_frequencies(lyrics):
    my_dict = {}
    lyrics = ''.join([x for x in lyrics if x not in punc]).split()

    for word in lyrics:
        if word.lower() in my_dict:
            my_dict[word.lower()] += 1
        else:
            my_dict[word.lower()] = 1

    op = []

    for w in sorted(my_dict, key=my_dict.get, reverse=True):
        if len(w) >= 10:
            print(w, my_dict[w])


taylor_swift = """
He said the way my blue eyes shined
Put those Georgia stars to shame that night
I said, "That's a lie"
Just a boy in a Chevy truck
That had a tendency of gettin' stuck
On backroads at night
And I was right there beside him all summer long
And then the time we woke up to find that summer gone
But when you think Tim McGraw
I hope you think my favorite song
The one we danced to all night long
The moon like a spotlight on the lake
When you think happiness
I hope you think that little black dress
Think of my head on your chest
And my old faded blue jeans
When you think Tim McGraw
I hope you think of me
September saw a month of tears
And thankin' God that you weren't here
To see me like that
But in a box beneath my bed
Is a letter that you never read
From three summers back
It's hard not to find it all a little bittersweet
And lookin' back on all of that, it's nice to believe
When you think Tim McGraw
I hope you think my favorite song
The one we danced to all night long
The moon like a spotlight on the lake
When you think happiness
I hope you think that little black dress
Think of my head on your chest
And my old faded blue jeans
When you think Tim McGraw
I hope you think of me
And I'm back for the first time since then
I'm standin' on your street
And there's a letter left on your doorstep
And the first thing that you'll read is:
"When you think Tim McGraw
I hope you think my favorite song
Someday you'll turn your radio on
I hope it takes you back to that place"
When you think happiness
I hope you think that little black dress
Think of my head on your chest
And my old faded blue jeans
When you think Tim McGraw
I hope you think of me
Oh, think of me
Mmmm
He said the way my blue eyes shine
Put those Georgia stars to shame that night
I said, "That's a lie"
State the obvious, I didn't get my perfect fantasy
I realize you love yourself more than you could ever love me
So go and tell your friends that I'm obsessive and crazy
That's fine, I'll tell mine that you're gay
By the way
I hate that stupid old pickup truck
You never let me drive
You're a redneck heartbreak
Who's really bad at lying
So watch me strike a match
On all my wasted time
As far as I'm concerned you're
Just another picture to burn
There's no time for tears
I'm just sitting here planning my revenge
There's nothing stopping me
From going out with all of your best friends
And if you come around saying sorry to me
My daddy's gonna show you how sorry you'll be
I hate that stupid old pickup truck
You never let me drive
You're a redneck heartbreak
Who's really bad at lying
So watch me strike a match
On all my wasted time
As far as I'm concerned you're
Just another picture to burn
And if you're missing me
You'd better keep it to yourself
'Cause coming back around here
Would be bad for your health
Cause I hate that stupid old pickup truck
You never let me drive
You're a redneck heartbreak
Who's really bad at lying
So watch me strike a match
On all my wasted time
In case you haven't heard
I really really hate that
I hate that stupid old pickup truck
You never let me drive
You're a redneck heartbreak
Who's really bad at lying
So watch me strike a match
On all my wasted time
As far as I'm concerned you're
Just another picture to burn
Burn, burn, burn, baby, burn
You're just another picture to burn
Baby, burn
Drew looks at me
I fake a smile so he won't see
That I want and I'm needing
Everything that we should be
I'll bet she's beautiful, that girl he talks about
And she's got everything that I have to live without
Drew talks to me
I laugh 'cause it's so damn funny
That I can't even see
Anyone when he's with me
He says he's so in love, he's finally got it right
I wonder if he knows he's all I think about at night
He's the reason for the teardrops on my guitar
The only thing that keeps me wishing on a wishing star
He's the song in the car
I keep singing, don't know why I do...
Drew walks by me
Can't he tell that I can't breathe?
And there he goes, so perfectly
The kind of flawless I wish I could be
She'd better hold him tight, give him all her love
Look in those beautiful eyes and know she's lucky 'cause
He's the reason for the teardrops on my guitar
The only thing that keeps me wishing on a wishing star
He's the song in the car
I keep singing, don't know why I do...
So I drive home alone, as I turn off the light
I'll put his picture down and maybe get some sleep tonight
He's the reason for the teardrops on my guitar
The only one who's got enough of me to break my heart
He's the song in the car
I keep singing, don't know why I do...
He's the time taken up, but there's never enough
And he's all that I need to fall into
Drew looks at me
I fake a smile so he won't see
I don't know what I want, so don't ask me
Cause I'm still trying to figure it out
Don't know what's down this road, I'm just walking
Trying to see through the rain coming down
Even though I'm not the only one
Who feels the way I do
I'm alone, on my own, and that's all I know
I'll be strong, I'll be wrong, oh but life goes on
Oh, I'm just a girl, trying to find a place in this world
Got the radio on, my old blue jeans
And I'm wearing my heart on my sleeve
Feeling lucky today, got the sunshine
Could you tell me what more do I need
And tomorrow's just a mystery, oh yeah
But that's OK
I'm alone, on my own, and that's all I know
I'll be strong, I'll be wrong, oh but life goes on
Oh, I'm just a girl, trying to find a place in this world
Maybe I'm just a girl on a mission
But I'm ready to fly
I'm alone, on my own, and that's all I know
I'll be strong, I'll be wrong, oh but life goes on
Oh I'm alone, on my own, and that's all I know
Oh I'm just a girl, trying to find a place in this world
Oh I'm just a girl
Oh I'm just a girl, oh, oh
Oh I'm just a girl
You have a way of coming easily to me
And when you take, you take the very best of me
So I start a fight cause I need to feel something
And you do what you want cause I'm not what you wanted
Oh what a shame, what a rainy ending given to a perfect day
Just walk away, no use defending words that you will never say
And now that I'm sitting here thinking it through
I've never been anywhere cold as you
You put up walls and paint them all a shade of gray
And I stood there loving you and wished them all away
And you come away with a great little story
Of a mess of a dreamer with the nerve to adore you
Oh what a shame, what a rainy ending given to a perfect day
Just walk away, no use defending words that you will never say
And now that I'm sitting here thinking it through
I've never been anywhere cold as you
You never did give a damn thing honey but I cried, cried for you
And I know you wouldn't have told nobody if I died, died for you
(Died for you)
Oh what a shame, what a rainy ending given to a perfect day
Every smile you fake is so condescending
Counting all the scars you made
And now that I'm sitting here thinking it through
I've never been anywhere cold as you
I didn't know what I would find
When I went looking for a reason, I know
I didn't read between the lines
And, baby, I've got nowhere to go
I tried to take the road less traveled by
But nothing seems to work the first few times
Am I right?
So how can I ever try to be better?
Nobody ever lets me in
I can still see you, this ain't the best view
On the outside looking in
I've been a lot of lonely places
I've never been on the outside
You saw me there, but never knew
I would give it all up to be
A part of this, a part of you
And now it's all too late so you see
You could've helped if you had wanted to
But no one notices until it's too
Late to do anything
So how can I ever try to be better?
Nobody ever lets me in
I can still see you, this ain't the best view
On the outside looking in
I've been a lot of lonely places
I've never been on the outside
So how can I ever try to be better?
Nobody ever lets me in
I can still see you, this ain't the best view
On the outside looking in
I've been a lot of lonely places
I've never been on the outside
Seems the only one who doesn't see your beauty
Is the face in the mirror looking back at you
You walk around here thinking you're not pretty
But that's not true, 'cause I know you
Hold on
Baby you're losing it
The water's high
You're jumping into it
And letting go
And no one knows
That you cry
But you don't tell anyone
That you might
Not be the golden one
And you're tied together with a smile
But you're coming undone
I guess it's true that love was all you wanted
'Cause you're giving it away like it's extra change
Hoping it will end up in his pocket
But he leaves you out like a penny in the rain
Oh, 'cause it's not his price to pay
Not his price to pay
Hold on
Baby you're losing it
The water's high
You're jumping into it
And letting go
And no one knows
That you cry
But you don't tell anyone
That you might
Not be the golden one
And you're tied together with a smile
But you're coming undone
Hold on
Baby you're losing it
The water's high
You're jumping into it
And letting go
And no one knows
That you cry
But you don't tell anyone
That you might
Not be the golden one
And you're tied together with a smile
But you're coming undone
You're tied together with a smile
But you're coming undone oh
Goodbye, baby
With a smile, baby, baby
Cory's eyes are like a jungle
He smiles, it's like the radio
He whispers songs into my window
In words that nobody knows
These pretty girls on every corner
They watch him as he's walking home
Saying, "Does he know?"
Will you ever know?
You're beautiful
Every little piece love
And don't you know
You're really gonna be someone
Ask anyone
And when you find everything you looked for
I hope your life will lead you back to my door
Oh, but if it don't
Stay beautiful
Cory finds another way to be
The highlight of my day
I'm taking pictures in my mind
So I can save them for a rainy day
It's hard to make a conversation
When he's taking my breath away
I should say, hey, by the way
You're beautiful
Every little piece love
And don't you know
You're really gonna be someone
Ask anyone
And when you find everything you looked for
I hope your life will lead you back to my door
Oh, but if it don't
Stay beautiful
If you and I are a story
That never gets told
If what you are is a daydream
I'll never get to hold
At least you'll know
You're beautiful
Every little piece love
And don't you know
You're really gonna be someone
Ask anyone
And when you find everything you looked for
I hope your life will lead you back to my front door
Oh, but if it don't
Will you stay
Beautiful, beautiful, beautiful?
Beautiful, beautiful, beautiful?
La la la
Oh, oh, oh, oh
Oh, but if it don't
Stay beautiful
Stay beautiful
Na, na, na, na, na
It's strange to think the songs we used to sing
The smiles, the flowers, everything is gone
Yesterday I found out about you
Even now just looking at you: feels wrong
You say that you'd take it all back, given one chance
It was a moment of weakness and you said, "Yes"
You should've said, "No", you should've gone home
You should've thought twice 'fore you let it all go
You should've know that word, 'bout what you did with her
Get back to me (get back to me)
And I should've been there, in the back of your mind
I shouldn't be asking myself, "Why?"
You shouldn't be begging for forgiveness at my feet
You should've said no, baby, and you might still have me
You can see that I've been crying
Baby you know all the right things to say
But do you honestly expect me to believe
We could ever be the same?
You say that the past is the past, you need one chance
It was a moment of weakness and you said, "Yes"
You should've said, "No", you should've gone home
You should've thought twice 'fore you let it all go
You should've know that word, 'bout what you did with her
Get back to me (get back to me)
And I should've been there, in the back of your mind
I shouldn't be asking myself, "Why?"
You shouldn't be begging for forgiveness at my feet
You should've said no, baby, and you might still have me
I can't resist
Before you go tell me this
Was it worth it?
Was she worth this?
No no, no, no
You should've said, "No", you should've gone home
You should've thought twice 'fore you let it all go
You should've know that word, 'bout what you did with her
Get back to me (get back to me)
And I should've been there, in the back of your mind
I shouldn't be asking myself, "Why?"
You shouldn't be begging for forgiveness at my feet
You should've said no, baby, and you might still have me
She said, I was seven and you were nine
I looked at you like the stars that shined
In the sky, the pretty lights
And our daddies used to joke about the two of us
Growing up and falling in love and our mamas smiled
And rolled their eyes and said oh my my my
Take me back to the house in the backyard tree
Said you'd beat me up, you were bigger than me
You never did, you never did
Take me back when our world was one block wide
I dared you to kiss me and ran when you tried
Just two kids, you and I
Oh my my my my
Well, I was sixteen when suddenly
I wasn't that little girl you used to see
But your eyes still shined like pretty lights
And our daddies used to joke about the two of us
They never believed we'd really fall in love
And our mamas smiled and rolled their eyes
And said oh my my my
Take me back to the creek beds we turned up
Two A.M. riding in your truck and all I need is you next to me
Take me back to the time we had our very first fight
The slamming of doors instead of kissing goodnight
You stayed outside till the morning light
Oh my my my my
A few years had gone and come around
We were sitting at our favorite spot in town
And you looked at me, got down on one knee
Take me back to the time when we walked down the aisle
Our whole town came and our mamas cried
You said I do and I did too
Take me home where we met so many years before
We'll rock our babies on that very front porch
After all this time, you and I
I'll be eighty-seven; you'll be eighty-nine
I'll still look at you like the stars that shine
In the sky, oh my my my
I was riding shotgun with my hair undone
In the front seat of his car
He's got a one-hand feel on the steering wheel
The other on my heart
I look around, turn the radio down
He says, "Baby is something wrong?"
I say, "Nothing, I was just thinking
How we don't have a song"
And he says
Our song is the slamming screen door
Sneakin' out late, tapping on your window
When we're on the phone and you talk real slow
'Cause it's late and your mama don't know
Our song is the way you laugh
The first date: "Man, I didn't kiss her, and I should have"
And when I got home 'fore I said amen
Asking God if he could play it again
I was walking up the front porch steps
After everything that day
Had gone all wrong and been trampled on
And lost and thrown away
Got to the hallway, well on my way
To my lovin' bed
I almost didn't notice all the roses
And the note that said
Our song is the slamming screen door
Sneakin' out late, tapping on your window
When we're on the phone and you talk real slow
'Cause it's late and your mama don't know
Our song is the way you laugh
The first date: "Man, I didn't kiss her, and I should have"
And when I got home 'fore I said amen
Asking God if he could play it again
I've heard every album, listened to the radio
Waited for something to come along
That was as good as our song
'Cause our song is the slamming screen door
Sneakin' out late, tapping on his window
When we're on the phone and he talks real slow
'Cause it's late and his mama don't know
Our song is the way he laughs
The first date: "Man, I didn't kiss him, and I should have"
And when I got home 'fore I said amen
Asking God if he could play it again
Play it again
I was riding shotgun with my hair undone
In the front seat of his car
I grabbed a pen and an old napkin
And I wrote down our song
Friday night beneath the stars
In a field behind your yard
You and I are painting pictures in the sky
And sometimes we don't say a thing
Just listen to the crickets sing
Everything I need is right here by my side
And I know everything about you
I don't wanna live without you
I'm only up when you're not down
Don't wanna fly if you're still on the ground
It's like no matter what I do
Well you drive me crazy half the time
The other half I'm only trying to let you know that what I feel is true
And I'm only me when I'm with you
Just a small town boy and girl
Living in a crazy world
Trying to figure out what is and isn't true
And I don't try to hide my tears
The secrets or my deepest fears
Through it all nobody gets me like you do
And you know everything about me
You say that you can't live without me
I'm only up when you're not down
Don't wanna fly if you're still on the ground
It's like no matter what I do
Well you drive me crazy half the time
The other half I'm only trying to let you know that what I feel is true
And I'm only me when I'm with you
When I'm with anybody else it's so hard to be myself
Only you can tell
That I'm only up when you're not down
Don't wanna fly if you're still on the ground
It's like no matter what I do
Well you drive me crazy half the time
The other half I'm only trying to let you know that what I feel is true
And I'm only me
Who I wanna be
Well, I'm only me when I'm with you
With you
Uh huh
Yeah
She can't see the way your eyes
Light up when you smile
She'll never notice how you stop and stare
Whenever she walks by
And you can't see me wanting you the way you want her
But you are everything to me
I just want to show you
She don't even know you
She's never going to love you like I want to
And you just see right through me
If you only knew me
We could be a beautiful
Miracle
Unbelievable
Instead of just invisible
There's a fire inside of you
That can't help but shine through
She's never going to see the light
No matter what you do
And all I think about is how to make you think of me
And everything that we could be
I just want to show you
She don't even know you
She's never going to love you like I want to
And you just see right through me
If you only knew me
We could be a beautiful
Miracle
Unbelievable
Instead of just invisible
Like shadows in a faded light
Oh, we're invisible
I just want to open your eyes
And make you realize
I just want to show you
She don't even know you
Baby, let me love you
Let me want you
You just see right through me
But if you only knew me
We could be a beautiful
Miracle
Unbelievable
Instead of just invisible
She can't see the way your eyes
Light up when you smile
Why would you wanna break a perfectly good heart?
Why would you wanna take our love and tear it all apart, now?
Why would you wanna make the very first scar?
Why would you wanna break a perfectly good heart?
Maybe I should've seen the signs, should've read the writing on the wall
And realized by the distance in your eyes that I would be the one to fall
No matter what you say, I still can't believe
That you would walk away
It don't make sense to me, but
Why would you wanna break a perfectly good heart?
Why would you wanna take our love and tear it all apart,now?
Why would you wanna make the very first scar?
Why would you wanna break a perfectly good heart?
It's not unbroken anymore
How do I get it back the way it was before?
Why would you wanna break a perfectly good heart?
Why would you wanna take our love and tear it all apart, now?
Why would you wanna make the very first scar?
Why would you wanna break a perfectly good heart?
Why would you wanna break a perfectly good heart?
Why would you wanna take our love and tear it all apart, now?
Why would you wanna make the very first scar?
Why would you wanna break a perfectly good heart?
There's something 'bout the way
The street looks when it's just rained
There's a glow off the pavement
You walk me to the car
And you know I wanna ask you to dance right there
In the middle of the parking lot, yeah
Oh, yeah
We're driving down the road
I wonder if you know
I'm trying so hard not to get caught up now
But you're just so cool
Run your hands through your hair
Absent mindedly making me want you
And I don't know how it gets better than this
You take my hand and drag me head first
Fearless
And I don't know why but with you I'd dance in a storm in my best dress
Fearless
So baby drive slow
'til we run out of road in this one horse town
I wanna stay right here in this passenger's seat
You put your eyes on me
In this moment now capture it, remember it
And I don't know how it gets better than this
You take my hand and drag me head first
Fearless
And I don't know why but with you I'd dance in a storm in my best dress
Fearless
Well you stood there with me in the doorway
My hands shake, I'm not usually this way but
You pull me in and I'm a little more brave
It's the first kiss, it's flawless, really something
It's fearless
Oh, yeah
And I don't know how it gets better than this
You take my hand and drag me head first
Fearless
And I don't know why but with you I'd dance in a storm in my best dress
Fearless
And I don't know how it gets better than this
You take my hand and drag me head first
Fearless
And I don't know why but with you I'd dance in a storm in my best dress
Fearless
Oh oh
Oh yeah
You take a deep breath and you walk through the doors
It's the morning of your very first day
You say hi to your friends you ain't seen in a while
Try and stay out of everybody's way
It's your freshman year and you're going to be here
For the next four years in this town
Hoping one of those senior boys will wink at you and say
"You know, I haven't seen you around before"
Because when you're fifteen and somebody tells you they love you
You're going to believe them
And when you're fifteen feeling like there's nothing to figure out
Well, count to ten, take it in
This is life before you know who you're going to be
Fifteen
You sit in class next to a redhead named Abigail
And soon enough you're best friends
Laughing at the other girls who think they're so cool
We'll be outta here as soon as we can
And then you're on your very first date and he's got a car
And you're feeling like flying
And your momma's waiting up and you're thinking he's the one
And you're dancing 'round your room when the night ends
When the night ends
Because when you're fifteen and somebody tells you they love you
You're going to believe them
When you're fifteen and your first kiss
Makes your head spin 'round
But in your life you'll do things greater than
Dating the boy on the football team
But I didn't know it at fifteen
When all you wanted was to be wanted
Wish you could go back and tell yourself what you know now
Back then I swore I was going to marry him someday
But I realized some bigger dreams of mine
And Abigail gave everything she had to a boy
Who changed his mind and we both cried
Because when you're fifteen and somebody tells you they love you
You're going to believe them
And when you're fifteen, don't forget to look before you fall
I've found time can heal most anything
And you just might find who you're supposed to be
I didn't know who I was supposed to be at fifteen
La la la la la la la la la la
La la la la la la la la la la
La la la la la la
Your very first day
Take a deep breath girl
Take a deep breath as you walk through the doors
We were both young when I first saw you
I close my eyes, and the flashback starts
I'm standing there
On a balcony in summer air
See the lights, see the party, the ball gowns
See you make your way through the crowd
And say, "hello"
Little did I know
That you were Romeo, you were throwing pebbles
And my daddy said, "stay away from Juliet"
And I was crying on the staircase
Begging you, "please don't go," and I said
Romeo, take me somewhere we can be alone
I'll be waiting, all there's left to do is run
You'll be the prince and I'll be the princess
It's a love story baby just say "yes"
So I sneak out to the garden to see you
We keep quiet, 'cause we're dead if they knew
So close your eyes
Escape this town for a little while
'Cause you were Romeo, I was a scarlet letter
And my daddy said, "Stay away from Juliet"
But you were everything to me
I was begging you please don't go and I said
Romeo, take me somewhere we can be alone
I'll be waiting, all there's left to do is run
You'll be the prince and I'll be the princess
It's a love story baby just say "yes"
Romeo, save me, they're trying to tell me how to feel
This love is difficult, but it's real
Don't be afraid, we'll make it out of this mess
It's a love story baby just say "yes"
Oh, oh
I got tired of waiting
Wondering if you were ever coming around
My faith in you was fading
When I met you on the outskirts of town, and I said
Romeo save me I've been feeling so alone
I keep waiting for you but you never come
Is this in my head? I don't know what to think
He knelt to the ground and pulled out a ring
And said: "Marry me Juliet
You'll never have to be alone
I love you and that's all I really know
I talked to your dad, go pick out a white dress
It's a love story baby just say 'yes'"
Oh, oh
Oh, oh
Because we were both young when I first saw you
Hey Stephen, I know looks can be deceiving
But I know I saw a light in you
And as we walked we were talking
I didn't say half the things I wanted to
Of all the girls tossing rocks at your window
I'll be the one waiting there even when it's cold
Hey Stephen, boy, you might have me believing
I don't always have to be alone
'Cause I can't help it if you look like an angel
Can't help it if I wanna kiss you in the rain so
Come feel this magic I've been feeling since I met you
Can't help it if there's no one else
Mmm, I can't help myself
Hey Stephen, I've been holding back this feeling
So I got some things to say to you
I've seen it all, so I thought
But I never seen nobody shine the way you do
The way you walk, way you talk, way you say my name
It's beautiful, wonderful, don't you ever change
Hey Stephen, why are people always leaving?
I think you and I should stay the same
'Cause I can't help it if you look like an angel
Can't help it if I wanna kiss you in the rain so
Come feel this magic I've been feeling since I met you
Can't help it if there's no one else
Mmm, I can't help myself
They're dimming the street lights, you're perfect for me
Why aren't you here tonight?
I'm waiting alone now, so come on and come out
And pull me near and shine, shine, shine
Hey Stephen, I could give you fifty reasons
Why I should be the one you choose
All those other girls, well, they're beautiful
But would they write a song for you?
'Cause I can't help it if you look like an angel
Can't help it if I wanna kiss you in the rain so
Come feel this magic I've been feeling since I met you
Can't help it if there's no one else
Mmm, I can't help myself
'Cause I can't help it if you look like an angel
Can't help it if I wanna kiss you in the rain so
Come feel this magic I've been feeling since I met you
Can't help it if there's no one else
Mmm, I can't help myself
Myself
Can't help myself
I can't help myself
Say you're sorry, that face of an angel
Comes out just when you need it to
As I paced back and forth all this time
'Cause I honestly believed in you
Holdin' on, the days drag on
Stupid girl, I shoulda known, I shoulda known
That I'm not a princess, this ain't a fairytale
I'm not the one you'll sweep off her feet, lead her up the stairwell
This ain't Hollywood, this is a small town
I was a dreamer before you went and let me down
Now it's too late for you and your white horse
To come around
Baby I was naive, got lost in your eyes
And never really had a chance
My mistake I didn't know to be in love
You had to fight to have the upper hand
I had so many dreams about you and me
Happy endings, now I know
That I'm not a princess, this ain't a fairytale
I'm not the one you'll sweep off her feet, lead her up the stairwell
This ain't Hollywood, this is a small town
I was a dreamer before you went and let me down
Now it's too late for you and your white horse
To come around
And there you are on your knees
Beggin' for forgiveness, beggin' for me
Just like I always wanted
But I'm so sorry
'Cause I'm not your princess, this ain't our fairytale
I'm gonna find someone someday
Who might actually treat me well
This is a big world, that was a small town
There in my rear view mirror disappearing now
And it's too late for you and your white horse
Now it's too late for you and your white horse
To catch me now
Oh, whoa, whoa, whoa
Try and catch me now, oh
It's too late to catch me now
You're on the phone with your girlfriend, she's upset
She's going off about something that you said
'Cause she doesn't get your humor like I do
I'm in the room, it's a typical Tuesday night
I'm listening to the kind of music she doesn't like
And she'll never know your story like I do
But she wears short skirts, I wear T-shirts
She's Cheer Captain and I'm on the bleachers
Dreaming about the day when you wake up and find
That what you're looking for has been here the whole time
If you could see that I'm the one who understands you
Been here all along, so why can't you see?
You belong with me, you belong with me
Walking the streets with you and your worn-out jeans
I can't help thinking this is how it ought to be
Laughing on a park bench, thinking to myself
Hey, isn't this easy?
And you've got a smile that could light up this whole town
I haven't seen it in a while since she brought you down
You say you're fine, I know you better than that
Hey, whatcha doing with a girl like that?
She wears high heels, I wear sneakers
She's Cheer Captain and I'm on the bleachers
Dreaming about the day when you wake up and find
That what you're looking for has been here the whole time
If you could see that I'm the one who understands you
Been here all along, so why can't you see?
You belong with me
Standing by and waiting at your back door
All this time how could you not know, baby?
You belong with me, you belong with me
Oh, I remember you driving to my house
In the middle of the night
I'm the one who makes you laugh
When you know you're 'bout to cry
And I know your favorite songs
And you tell me 'bout your dreams
Think I know where you belong
Think I know it's with me
Can't you see that I'm the one who understands you
Been here all along, so why can't you see?
You belong with me
Standing by and waiting at your back door
All this time how could you not know, baby?
You belong with me, you belong with me
You belong with me
Have you ever thought just maybe
You belong with me?
You belong with me
I see your face in my mind as I drive away
'Cause none of us thought it was
Going to end that way
People are people
And sometimes we change our minds
But it's killing me to see you go after all this time
Mm mm mm, mm mm mm, mm mm
Mm mm mm, mm mm mm, mm mm
Music starts playing like the end of a sad movie
It's the kind of ending you
Don't really want to see
'Cause it's tragedy and it'll only bring you
Down
Now I don't know what to be without you around
And we know it's never simple, never easy
Never a clean break, no one here to
Save me
You're the only thing I know like the back of my hand
And I can't
Breathe
Without you but I have to breathe
Without you but I have to
Never wanted this, never want to see you hurt
Every little bump in the road I tried to swerve
But people are people
And sometimes it doesn't work out
Nothing we say is gonna save us from the fall out
It's 2 A.M
Feeling like I just lost a friend
Hope you know it's not easy
Easy for me
It's 2 A.M
Feeling like I just lost a friend
Hope you know this ain't easy
Easy for me
Sorry, sorry
Sorry, (Yeah eh) sorry
Sorry, sorry
Sorry
I took a chance
I took a shot
And you might think I'm bulletproof
But I'm not
You took a swing
I took it hard
And down here from the ground I see who you are
I'm sick and tired of your attitude
I'm feeling like I don't know you
You tell me that you love me, then you cut me down
And I need you like a heartbeat
But you know you got a mean streak
That makes me run for cover when you're around
And here's to you and your temper
Yes, I remember what you said last night
And I know, that you see, what you're doing to me
Tell me why
You could write a book on how to ruin someone's perfect day
Well I get so confused and frustrated
Forget what I'm trying to say, oh
I'm sick and tired of your reasons
I got no one to believe in
You tell me that you want me, then push me around
And I need you like a heartbeat
But you know you got a mean streak
That makes me run for cover when you're around
Here's to you and your temper
Yes, I remember what you said last night
And I know, that you see, what you're doing to me
Tell me why
Why do you have to make me feel small
So you can feel whole inside?
Why do you have to put down my dreams
So you're the only thing on my mind?
I'm sick and tired of your attitude
I'm feeling like I don't know you
You tell me that you want me, then cut me down
I'm sick and tired of your reasons
I've got no one to believe in
You ask me for my love, then you push me around
Here's to you and your temper
Yes, I remember what you said last night
And I know that you see what you're doing to me
Tell me why (why)
Tell me why (why)
I take a step back, let you go
I told you I'm not bulletproof
Now you know
All this time I was wasting hoping you would come around
I've been giving out chances every time and all you do is let me down
And it's taken me this long baby but I've figured you out
And you're thinking we'll be fine again but not this time around
You don't have to call anymore
I won't pick up the phone
This is the last straw
Don't wanna hurt anymore
And you can tell me that you're sorry
But I don't believe you baby like I did before
You're not sorry (No no no no)
You're looking so innocent
I might believe you if I didn't know
Could've loved you all my life if you hadn't left me waiting in the cold
And you've got your share of secrets
And I'm tired of being last to know
And now you're asking me to listen 'cause it's worked each time before but
You don't have to call anymore
I won't pick up the phone
This is the last straw
Don't wanna hurt anymore
And you can tell me that you're sorry
But I don't believe you baby like I did before
You're not sorry (No no no no)
You're not sorry (No no no no)
You had me crawling for you honey and it never would have gone away
You used to shine so bright but I watched all of it fade so
You don't have to call anymore
I won't pick up the phone
This is the last straw
There's nothing left to beg for
And you can tell me that you're sorry
But I don't believe you baby like I did before
You're not sorry (No no no no)
You're not sorry (No no no no)
(No, no, no...)
He is sensible and so incredible
And all my single friends are jealous
He says everything I need to hear and it's like
I couldn't ask for anything better
He opens up my door and I get into his car
And he says you look beautiful tonight
And I feel perfectly fine
But I miss screaming and fighting and kissing in the rain
And it's 2am and I'm cursing your name
You're so in love that you act insane
And that's the way I loved you
Breaking down and coming undone
It's a roller coaster kind of rush
And I never knew I could feel that much
And that's the way I loved you
He respects my space
And never makes me wait
And he calls exactly when he says he will
He's close to my mother
Talks business with my father
He's charming and endearing
And I'm comfortable
He can't see the smile I'm faking
And my heart's not breaking
'Cause I'm not feeling anything at all
And you were wild and crazy
Just so frustrating intoxicating
Complicated, got away by some mistake and now
I miss screaming and fighting and kissing in the rain
It's 2am and I'm cursing your name
I'm so in love that I acted insane
And that's the way I loved you
Breaking down and coming undone
It's a roller coaster kind of rush
And I never knew I could feel that much
And that's the way I loved you oh, oh
And that's the way I loved you oh, oh
Never knew I could feel that much
And that's the way I loved you
Once upon a time
I believe it was a Tuesday when I caught your eye
And we caught onto something
I hold onto the night, you looked me in the eye and told me you loved me
Were you just kidding?
'Cause it seems to me, this thing is breaking down
We almost never speak
I don't feel welcome anymore
Baby what happened, please tell me?
'Cause one second it was perfect, now you're halfway out the door
And I stare at the phone, he still hasn't called
And then you feel so low you can't feel nothing at all
And you flashback to when he said forever and always
Oh, and it rains in your bedroom
Everything is wrong
It rains when you're here and it rains when you're gone
'Cause I was there when you said forever and always
Was I out of line?
Did I say something way too honest, made you run and hide
Like a scared little boy
I looked into your eyes
Thought I knew you for a minute, now I'm not so sure
So here's to everything coming down to nothing
Here's to silence that cuts me to the core
Where is this going?
Thought I knew for a minute, but I don't anymore
And I stare at the phone, he still hasn't called
And then you feel so low you can't feel nothing at all
And you flashback to when he said forever and always
Oh, and it rains in your bedroom
Everything is wrong
It rains when you're here and it rains when you're gone
'Cause I was there when you said forever and always
You didn't mean it baby, I don't think so
Oh, back up, baby, back up
Did you forget everything?
Back up, baby, back up
Did you forget everything?
'Cause it rains in your bedroom
Everything is wrong
It rains when you're here and it rains when you're gone
'Cause I was there when you said forever and always
Oh I stare at the phone, he still hasn't called
And then you feel so low you can't feel nothing at all
And you flashback to when we said forever and always
And  it rains in your bedroom
Everything is wrong
It rains when you're here and it rains when you're gone
'Cause I was there when you said forever and always
You didn't mean it baby, you said forever and always, yeah
I'm five years old, it's getting cold, I've got my big coat on
I hear your laugh and look up smiling at you, I run and run
Past the pumpkin patch and the tractor rides
Look now, the sky is gold
I hug your legs and fall asleep on the way home
I don't know why all the trees change in the fall
But I know you're not scared of anything at all
Don't know if Snow White's house is near or far away
But I know I had the best day with you today
I'm thirteen now
And don't know how my friends could be so mean
I come home crying and you hold me tight and grab the keys
And we drive and drive until we found a town far enough away
And we talk and window shop 'til I've forgotten all their names
I don't know who I'm going to talk to now at school
But I know I'm laughing on the car ride home with you
Don't know how long it's going to take to feel okay
But I know I had the best day with you today
I have an excellent father, his strength is making me stronger
God smiles on my little brother, inside and out
He's better than I am
I grew up in a pretty house and I had space to run
And I had the best days with you
There is a video I found from back when I was three
You set up a paint set in the kitchen and you're talking to me
It's the age of princesses and pirate ships and the seven dwarfs
And Daddy's smart
And you're the prettiest lady in the whole wide world
And now I know why all the trees change in the fall
I know you were on my side even when I was wrong
And I love you for giving me your eyes
For staying back and watching me shine
And I didn't know if you knew, so I'm taking this chance to say
That I had the best day with you today
And it's a sad picture, the final blow hits you
Somebody else gets what you wanted again and
You know it's all the same, another time and place
Repeating history and you're getting sick of it
But I believe in whatever you do
And I'll do anything to see it through
Because these things will change
Can you feel it now?
These walls that they put up to hold us back will fall down
This revolution, the time will come
For us to finally win
And we'll sing hallelujah, we'll sing hallelujah
Oh, oh
So we've been outnumbered, raided, and now cornered
It's hard to fight when the fight ain't fair
We're getting stronger now, finding things they never found
They might be bigger but we're faster and never scared
You can walk away, say we don't need this
But there's something in your eyes says we can beat this
'Cause these things will change
Can you feel it now?
These walls that they put up to hold us back will fall down
This revolution, the time will come
For us to finally win
And we'll sing hallelujah, we'll sing hallelujah
Oh, oh
Tonight we stand, get off our knees
Fight for what we've worked for all these years
And the battle was long, it's the fight of our lives
But we'll stand up champions tonight
It was the night things changed
Can you see it now?
These walls that they put up to hold us back fell down
It's a revolution, throw your hands up
'Cause we never gave in
And we'll sing hallelujah, we sang hallelujah
Hallelujah
You were in college, working part-time, waiting tables
Left a small town and never looked back
I was a flight risk, with a fear of falling
Wondering why we bother with love, if it never lasts
I say, "Can you believe it?"
As we're lying on the couch
The moment, I could see it
Yes, yes, I can see it now
Do you remember, we were sitting there, by the water?
You put your arm around me for the first time
You made a rebel of a careless man's careful daughter
You are the best thing that's ever been mine
Flash forward, and we're taking on the world together
And there's a drawer of my things at your place
You learn my secrets and figure out why I'm guarded
You say we'll never make my parents' mistakes
But we got bills to pay
We got nothing figured out
When it was hard to take
Yes, yes
This is what I thought about:
Do you remember, we were sitting there, by the water?
You put your arm around me for the first time
You made a rebel of a careless man's careful daughter
You are the best thing that's ever been mine
Do you remember all the city lights on the water?
You saw me start to believe for the first time
You made a rebel of a careless man's careful daughter
You are the best thing that's ever been mine
And I remember that fight, 2:30 AM
As everything was slipping right out of our hands
I ran out, crying, and you followed me out into the street
Braced myself for the goodbye
'Cause that's all I've ever known
Then, you took me by surprise
You said, "I'll never leave you alone."
You said, "I remember how we felt, sitting by the water
And every time I look at you, it's like the first time
I fell in love with a careless man's careful daughter
She is the best thing that's ever been mine"
Hold on, make it last
Hold on, never turn back
You made a rebel of a careless man's careful daughter
You are the best thing that's ever been mine
Yeah, yeah
Do you believe it?
(Hold on)
We're gonna make it now
(Hold on)
And I can see it
Yeah, yeah
I can see it now (see it now)
The way you move is like a full on rainstorm
And I'm a house of cards
You're the kind of reckless
That should send me running
But I kinda know that I won't get far
And you stood there in front of me
Just close enough to touch
Close enough to hope you couldn't see
What I was thinking of
Drop everything now
Meet me in the pouring rain
Kiss me on the sidewalk
Take away the pain
'Cause I see sparks fly whenever you smile
Get me with those green eyes, baby, as the lights go down
Give me something that'll haunt me when you're not around
'Cause I see sparks fly whenever you smile
My mind forgets to remind me
You're a bad idea
You touch me once and it's really something
You find I'm even better than you imagined I would be
I'm on my guard for the rest of the world
But with you I know it's no good
And I could wait patiently but I really wish you would
Drop everything now
Meet me in the pouring rain
Kiss me on the sidewalk
Take away the pain
'Cause I see sparks fly whenever you smile
Get me with those green eyes, baby, as the lights go down
Give me something that'll haunt me when you're not around
'Cause I see sparks fly whenever you smile
I run my fingers through your hair and watch the lights go wild
Just keep on keeping your eyes on me, it's just wrong enough to make it feel right
And lead me up the staircase
Won't you whisper soft and slow?
I'm captivated by you, baby, like a firework show
Drop everything now
Meet me in the pouring rain
Kiss me on the sidewalk
Take away the pain
'Cause I see sparks fly whenever you smile
Get me with those green eyes, baby, as the lights go down
Give me something that'll haunt me when you're not around
'Cause I see sparks fly whenever you smile
And the sparks fly
Oh, baby, smile
And the sparks fly
I'm so glad you made time to see me
How's life, tell me, how's your family
I haven't seen them in a while
You've been good, busier than ever
We small talk, work and the weather
Your guard is up and I know why
'Cause the last time you saw me
Is still burned in the back of your mind
You gave me roses and I left them there to die
So this is me swallowing my pride
Standing in front of you, saying I'm sorry for that night
And I'd go back to December all the time
It turns out freedom ain't nothing but missing you
Wishing I'd realized what I had when you were mine
I'd go back to December, turn around and make it alright
I go back to December all the time
These days I haven't been sleeping
Staying up playing back myself leaving
When your birthday passed and I didn't call
And I think about summer, all the beautiful times
I watched you laughing from the passenger side and
Realized I loved you in the fall
And then the cold came
The dark days when fear crept into my mind
You gave me all your love and all I gave you was goodbye
So this is me swallowing my pride
Standing in front of you, saying I'm sorry for that night
And I'd go back to December all the time
It turns out freedom ain't nothing but missing you
Wishing I'd realized what I had when you were mine
I'd go back to December, turn around and change my own mind
I go back to December all the time
I miss your tan skin, your sweet smile, so good to me, so right
And how you held me in your arms that September night
The first time you ever saw me cry
Maybe this is wishful thinking
Probably mindless dreaming
But if we loved again I swear I'd love you right
I'd go back in time and change it, but I can't
So if the chain is on your door, I understand
But this is me swallowing my pride
Standing in front of you saying I'm sorry for that night
And I'd go back to December...
It turns out freedom ain't nothing but missing you
Wishing I'd realized what I had when you were mine
I'd go back to December, turn around and make it alright
I'd go back to December, turn around and change my own mind
I go back to December all the time
All the time
I am not the kind of girl
Who should be rudely barging in
On a white veil occasion
But you are not the kind of boy
Who should be marrying the wrong girl
I sneak in and see your friends
And her snotty little family
All dressed in pastel
And she is yelling at a bridesmaid
Somewhere back inside a room
Wearing a gown shaped like a pastry
This is surely not
What you thought it would be
I lose myself in a daydream
Where I stand and say
Don't say yes, run away now
I'll meet you when you're out
Of the church at the back door
Don't wait or say a single vow
You need to hear me out
And they said "speak now"
Fond gestures are exchanged
And the organ starts to play
A song that sounds like a death march
And I am hiding in the curtains
It seems that I was uninvited
By your lovely bride-to-be
She floats down the aisle
Like a pageant queen
But I know you wish it was me
You wish it was me (Don't you)
Don't say yes, run away now
I'll meet you when you're out
Of the church at the back door
Don't wait or say a single vow
You need to hear me out
And they said "speak now"
Don't say yes, run away now
I'll meet you when you're out
Of the church at the back door
Don't wait or say a single vow
You need to hear me out
And they said "speak now"
Ooh, la-da-da-da, oh
Ooh, ooh
(Say a single vow)
I hear the preacher say
"Speak now or forever hold your peace"
There's the silence, there's my last chance
I stand up with shaking hands, all eyes on me
Horrified looks from everyone in the room
But I'm only looking at you
I am not the kind of girl
Who should be rudely barging in
On a white veil occasion
But you are not the kind of boy
Who should be marrying the wrong girl
(Hehe!)
Don't say yes, run away now
I'll meet you when you're out
Of the church at the back door
Don't wait or say a single vow
You need to hear me out
And they said "speak now"
And you say
"Let's run away now
I'll meet you when
I'm out of my tux at the back door"
Baby, I didn't say my vows
So glad you were around when they said
"Speak now"
Long were the nights when
My days once revolved around you
Counting my footsteps
Praying the floor won't fall through... again
My mother accused me of losing my mind
But I swore I was fine
You paint me a blue sky
Then go back and turn it to rain
And I lived in your chess game
But you changed the rules everyday
Wonderin' which version of you I might get on the phone, tonight
Well I stopped pickin' up and this song is to let you know why
Dear John, I see it all now that you're gone
Don't you think I was too young to be messed with
The girl in the dress cried the whole way home
I shoulda' known
Well maybe it's me
And my blind optimism to blame
Or maybe it's you and your sick need
To give love and take it away
And you'll add my name to your long list of traitors
Who don't understand
And I look back in regret how I ignored when they said
"Run as fast as you can"
Dear John, I see it all now that you're gone
Don't you think I was too young to be messed with
The girl in the dress cried the whole way home
Dear John, I see it all now it was wrong
Don't you think nineteen's too young
To be played by your dark, twisted games
When I loved you so?
I shoulda' known
You are an expert at sorry
And keeping the lines blurry
Never impressed by me acing your tests
All the girls that you've run dry have tired lifeless eyes
'Cause you burned them out
But I took your matches
Before fire could catch me
So don't look now
I'm shining like fireworks
Over your sad empty town, yeah
Oh, oh, oh, oh, oh, oh
Dear John, I see it all now that you're gone
Don't you think I was too young to be messed with
The girl in the dress cried the whole way home
I see it all now that you're gone
Don't you think I was too young to be messed with
The girl in the dress
Wrote you a song, you shoulda' known
You shoulda' known
Don't you think I was too young
You shoulda' known
You, with your words like knives
And swords and weapons that you use against me
You have knocked me off my feet again
Got me feeling like I'm nothing
You, with your voice like nails on a chalkboard
Calling me out when I'm wounded
You, picking on the weaker man
But you can take me down with just one single blow
But you don't know what you don't know
Someday, I'll be living in a big old city
And all you're ever gonna be is mean
Someday, I'll be big enough so you can't hit me
And all you're ever gonna be is mean
Why you gotta be so mean?
You, with your switching sides
And your wildfire lies and your humiliation
You have pointed out my flaws again
As if I don't already see them
I walk with my head down, trying to block you out
'Cause I'll never impress you
I just want to feel okay again
I bet you got pushed around
Somebody made you cold
But the cycle ends right now
'Cause you can't lead me down that road
And you don't know what you don't know
Someday, I'll be living in a big old city
And all you're ever gonna be is mean
Someday, I'll be big enough so you can't hit me
And all you're ever gonna be is mean
Why you gotta be so mean?
And I can see you years from now in a bar
Talking over a football game
With that same big loud opinion
But nobody's listening
Washed up and ranting about the same old bitter things
Drunk and grumbling on about how I can't sing
But all you are is mean
All you are is mean
And a liar, and pathetic, and alone in life
And mean, and mean, and mean, and mean
But someday I'll be living in a big old city
And all you're ever going to be is mean, yeah!
Someday, I'll be big enough so you can't hit me
And all you're ever going to be is mean
Why you gotta be so mean?
Someday, I'll be living in a big old city
(Why you gotta be so mean?)
And all you're ever gonna be is mean
(Why you gotta be so mean?)
Someday, I'll be big enough so you can't hit me
(Why you gotta be so mean?)
And all you're ever gonna be is mean
Why you gotta be so mean?
I used to think one day we'd tell the story of us
How we met
And the sparks flew instantly
And people would say they're the lucky ones
I used to know my place was a spot next to you
Now I'm searching the room for an empty seat
'Cause lately I don't even know what page you're on
Oh, a simple complication
Miscommunications lead to fallout
So many things that I wish you knew
So many walls up that I can't break through
Now I'm standing alone in a crowded room
And we're not speaking
And I'm dying to know
Is it killing you like it's killing me?
Yeah, I don't know what to say since a twist of fate, when it all broke down
And the story of us looks a lot like a tragedy now
Next chapter
How'd we end up this way?
See me nervously pulling at my clothes and trying to look busy
And you're doing your best to avoid me
I'm starting to think one day I'll tell the story of us
Of how I was losing my mind when I saw you here
But you held your pride like you should have held me
Oh, I'm scared to see the ending
Why are we pretending this is nothing?
I'd tell you I miss you, but I don't know how
I've never heard silence quite this loud
Now I'm standing alone in a crowded room
And we're not speaking
And I'm dying to know
Is it killing you like it's killing me?
Yeah, and I don't know what to say since a twist of fate, when it all broke down
And the story of us looks a lot like a tragedy now
This is looking like a contest
Of who can act like they care less
But I liked it better when you were on my side
The battle's in your hands now
But I would lay my armor down
If you say you'd rather love than fight
So many things that you wish I knew
But the story of us might be ending soon
Now I'm standing alone in a crowded room
And we're not speaking
And I'm dying to know
Is it killing you like it's killing me?
Yeah, and I don't know what to say since a twist of fate, when it all broke down
And the story of us looks a lot like a tragedy now, now, now
And we're not speaking
And I'm dying to know is it killing you like it's killing me?
Yeah
And I don't know what to say since a twist of fate, because we're going down
And the story of us looks a lot like a tragedy now
The End
Your little hand's wrapped around my finger
And it's so quiet in the world tonight
Your little eyelids flutter cause you're dreaming
So I tuck you in, turn on your favorite night light
To you everything's funny, you got nothing to regret
I'd give all I have, honey
If you could stay like that
Oh darling, don't you ever grow up
Don't you ever grow up, just stay this little
Oh darling, don't you ever grow up
Don't you ever grow up, it could stay this simple
I won't let nobody hurt you, won't let no one break your heart
And no one will desert you
Just try to never grow up, never grow up
You're in the car on the way to the movies
And you're mortified your mom's dropping you off
At 14 there's just so much you can't do
And you can't wait to move out someday and call your own shots
But don't make her drop you off around the block
Remember that she's getting older too
And don't lose the way that you dance around in your pj's getting ready for school
Oh darling, don't you ever grow up
Don't you ever grow up, just stay this little
Oh darling, don't you ever grow up
Don't you ever grow up, it could stay this simple
No one's ever burned you, nothing's ever left you scarred
And even though you want to, just try to never grow up
Take pictures in your mind of your childhood room
Memorize what it sounded like when your dad gets home
Remember the footsteps, remember the words said
And all your little brother's favorite songs
I just realized everything I have is someday gonna be gone
So here I am in my new apartment
In a big city, they just dropped me off
It's so much colder that I thought it would be
So I tuck myself in and turn my night light on
Wish I'd never grown up
I wish I'd never grown up
Oh I don't wanna grow up, wish I'd never grown up
I could still be little
Oh I don't wanna grow up, wish I'd never grown up
It could still be simple
Oh darling, don't you ever grow up
Don't you ever grow up, just stay this little
Oh darling, don't you ever grow up
Don't you ever grow up, it could stay this simple
Won't let nobody hurt you
Won't let no one break your heart
And even though you want to, please try to never grow up
Oh, don't you ever grow up
Oh, never grow up, just never grow up
There I was again tonight
Forcing laughter, faking smiles
Same old tired, lonely place
Walls of insincerity, shifting eyes and vacancy
Vanished when I saw your face
All I can say is
It was enchanting to meet you
Your eyes whispered "have we met?"
Across the room your silhouette
Starts to make its way to me
The playful conversation starts
Counter all your quick remarks
Like passing notes in secrecy
And it was
Enchanting to meet you
All I can say is
I was enchanted to meet you
This night is sparkling
Don't you let it go
I'm wonderstruck
Blushing all the way home
I'll spend forever
Wondering if you knew
I was enchanted to meet you
The lingering question kept me up
2AM, who do you love?
I wonder 'til I'm wide awake
And now I'm pacing back and forth
Wishing you were at my door
I'd open up and you would say "hey"
It was
Enchanting to meet you
All I know is I was
Enchanted to meet you
This night is sparkling
Don't you let it go
I'm wonderstruck
Blushing all the way home
I'll spend forever
Wondering if you knew
This night is flawless
Don't you let it go
I'm wonderstruck
Dancing around all alone
I'll spend forever
Wondering if you knew
I was enchanted to meet you
This is me praying that
This was the very first page
Not where the storyline ends
My thoughts will echo your name
Until I see you again
These are the words I held back
As I was leaving too soon
I was enchanted to meet you
Please don't be in love
With someone else
Please don't have somebody
Waiting on you
Please don't be in love
With someone else
Please don't have somebody
Waiting on you
This night is sparkling
Don't you let it go
I'm wonderstruck
Blushing all the way home
I'll spend forever
Wondering if you knew
This night is flawless
Don't you let it go
I'm wonderstruck
Dancing around all alone
I'll spend forever
Wondering if you knew
I was enchanted to meet you
Please don't be in love
With someone else
Please don't have somebody
Waiting on you
Now go stand in the corner and think about what you did
Ha, time for a little revenge
The story starts when it was hot and it was summer and
I had it all, I had him right there, where I wanted him
She came along, got him alone, and let's hear the applause
She took him faster than you can say sabotage
I never saw it coming, wouldn't have suspected it
I underestimated just who I was dealing with
She had to know the pain was beating on me like a drum
She underestimated just who she was stealing from
She's not a saint and she's not what you think
She's an actress, whoa
She's better known for the things that she does
On the mattress, whoa
Soon she's gonna find stealing other people's toys
On the playground won't make you many friends
She should keep in mind, she should keep in mind
There is nothing I do better than revenge, ha!
She looks at life like it's a party and she's on the list
She looks at me like I'm a trend and she's so over it
I think her ever-present frown is a little troubling
And she thinks I'm psycho 'cause I like to rhyme her name with things
But sophistication isn't what you wear or who you know
Or pushing people down to get you where you wanna go
Oh, they didn't teach you that in prep school, so it's up to me
But no amount of vintage dresses gives you dignity
She's not a saint and she's not what you think
She's an actress, whoa
She's better known for the things that she does
On the mattress, whoa
Soon she's gonna find stealing other people's toys
On the playground won't make you many friends
She should keep in mind, she should keep in mind
There is nothing I do better than revenge, HA!
I'm just another thing for you to roll your eyes at, honey
You might have him, but haven't you heard?
I'm just another thing for you to roll your eyes at, honey
You might have him, but I always get the last word
Whoa, whoa-ah-oh
She's not a saint and she's not what you think
She's an actress, whoa
She's better known for the things that she does
On the mattress, whoa
Soon she's gonna find stealing other people's toys
On the playground won't make you many friends
She should keep in mind, she should keep in mind
There is nothing I do better than revenge, HA!
Do you still feel like you know what you're doing?
'Cause I don't think you do, oh
Do you still feel like you know what you're doing?
I don't think you do, I don't think you do
Let's hear the applause
Come on, show me how much better you are (so much better, yeah?)
See you deserve some applause
'Cause you're so much better
She took him faster than you could say sabotage
I guess you really did it this time
Left yourself in your warpath
Lost your balance on a tightrope
Lost your mind trying to get it back
Wasn't it easier in your lunchbox days?
Always a bigger bed to crawl into
Wasn't it beautiful when you believed in everything
And everybody believed in you?
It's alright, just wait and see
Your string of lights is still bright to me
Oh, who you are is not where you've been
You're still an innocent
You're still an innocent
Did some things you can't speak of
But at night you live it all again
You wouldn't be shattered on the floor now
If only you had seen what you know now then
Wasn't it easier in your firefly-catching days?
When everything out of reach, someone bigger brought down to you
Wasn't it beautiful running wild 'til you fell asleep
Before the monsters caught up to you?
It's alright, just wait and see
Your string of lights is still bright to me
Ohwho you are is not where you've been
You're still an innocent
It's okay, life is a tough crowd
32, and still growing up now
Who you are is not what you did
You're still an innocent
Time turns flames to embers
You'll have new Septembers
Every one of us has messed up too
Lives change like the weather
I hope you remember
Today is never too late to be brand new
It's alright, just wait and see
Your string of lights is still bright to me
Oh, who you are is not where you've been
You're still an innocent
It's okay, life is a tough crowd
32, and still growing up now
Who you are is not what you did
You're still an innocent
You're still an innocent
Lost your balance on a tightrope
It's never too late to get it back
You and I walk a fragile line
I have known it all this time
But I never thought I'd live to see it break
It's getting dark and it's all too quiet
And I can't trust anything now
And it's coming over you like it's all a big mistake
Whoa, holding my breath
Won't lose you again
Something's made your eyes go cold
C'mon, c'mon, don't leave me like this
I thought I had you figured out
Something's gone terribly wrong
You're all I wanted
C'mon, c'mon, don't leave me like this
I thought I had you figured out
Can't breathe whenever you're gone
Can't turn back now I'm haunted
Stood there and watched you walk away
From everything we had
But I still mean every word I said to you
He will try to take away my pain
And he just might make me smile
But the whole time I'm wishing it was you instead
Oh, holding my breath
Won't see you again
Something keeps me holding onto nothing
C'mon, c'mon, don't leave me like this
I thought I had you figured out
Something's gone terribly wrong
You're all I wanted
C'mon, c'mon, don't leave me like this
I thought I had you figured out
Can't breathe whenever you're gone
Can't turn back now I'm haunted
I know
I know
I just know
You're not gone, you can't be gone, no
C'mon, c'mon, don't leave me like this
I thought I had you figured out
Something's gone terribly wrong
Won't finish what you started
C'mon, c'mon, don't leave me like this
I thought I had you figured out
Can't breathe whenever you're gone
Can't turn back now I'm haunted
(Oh oh oh oh oh oh oh oh oh)
You and I walk a fragile line
I have known it all this time
Never ever thought I'd see it break
Never thought I'd see it
I still remember the look on your face
Lit through the darkness at 1:58
The words that you whispered
For just us to know
You told me you loved me
So why did you go away?
Away
I do recall now the smell of the rain
Fresh on the pavement
I ran off the plane
That July 9th
The beat of your heart
It jumps through your shirt
I can still feel your arms
But now I'll go sit on the floor
Wearing your clothes
All that I know is
I don't know how to be something you miss
I never thought we'd have a last kiss
Never imagined we'd end like this
Your name, forever the name on my lips
I do remember the swing of your step
The life of the party, you're showing off again
And I roll my eyes and then
You pull me in
I'm not much for dancing
But for you I did
Because I love your handshake, meeting my father
I love how you walk with your hands in your pockets
How you kissed me when I was in the middle of saying something
There's not a day I don't miss those rude interruptions
But now I'll go sit on the floor
Wearing your clothes
All that I know is
I don't know how to be something you miss
I never thought we'd have a last kiss
Never imagined we'd end like this
Your name, forever the name on my lips
So I'll watch your life in pictures like I used to watch you sleep
And I feel you forget me like I used to feel you breathe
And I keep up with our old friends just to ask them how you are
Hope it's nice where you are
And I hope the sun shines
And it's a beautiful day
And something reminds you
You wish you had stayed
You can plan for a change in weather and time
But I never planned on you changing your mind
So I'll go sit on the floor
Wearing your clothes
All that I know is
I don't know how to be something you miss
I never thought we'd have a last kiss
Never imagined we'd end like this
Your name, forever the name on my lips
Just like our last kiss
Forever the name on my lips
Forever the name on my lips
Just like our last
I said remember this moment, in the back of my mind
The time we stood with our shaking hands
The crowds in the stands went wild
We were the Kings and the Queens
And they read off our names
The night you danced like you knew our lives
Would never be the same
You held your head like a hero
On a history book page
It was the end of a decade
But the start of an age
Long live the walls we crashed through
All the kingdom lights shined just for me and you
I was screaming long live all the magic we made
And bring on all the pretenders
One day, we will be remembered
I said remember this feeling
I passed the pictures around
Of all the years that we stood there
On the side-lines wishing for right now
We are the Kings and the Queens
You traded your baseball cap for a crown
When they gave us our trophies
And we held them up for our town
And the cynics were outraged
Screaming "this is absurd"
Cause for a moment a band of thieves
In ripped up jeans got to rule the world
Long live the walls we crashed through
All the kingdom lights shined just for me and you
I was screaming long live all the magic we made
And bring on all the pretenders
I'm not afraid
Long live all the mountains we moved
I had the time of my life fighting dragons with you
I was screaming long live that look on your face
And bring on all the pretenders
One day, we will be remembered
Hold on to spinning around
Confetti falls to the ground
May these memories break our fall
Will you take a moment?
Promise me this
That you'll stand by me forever
But if God forbid fate should step in
And force us into a goodbye
If you have children some day
When they point to the pictures
Please tell them my name
Tell them how the crowds went wild
Tell them how I hope they shine
Long live the walls we crashed through
I had the time of my life, with you
Long, long live the walls we crashed through
All the kingdom lights shined just for me and you
I was screaming long live all the magic we made
And bring on all the pretenders
I'm not afraid
Singing, long live all the mountains we moved
I had the time of my life fighting dragons with you
And long, long live that look on your face
And bring on all the pretenders
One day, we will be remembered
Elevator buttons and morning air
Strangers' silence makes me want to take the stairs
If you were here we'd laugh about their vacant stares
But right now my time is theirs
Seems like there's always someone who disapproves
They'll judge it like they know about me and you
And the verdict comes from those with nothing else to do
The jury's out, but my choice is you
So don't you worry your pretty little mind
People throw rocks at things that shine
And life makes love look hard
The stakes are high, the water's rough
But this love is ours
You never know what people have up their sleeves
Ghosts from your past gonna jump out at me
Lurking in the shadows with their lip gloss smiles
But I don't care 'cause right now you're mine
And you'll say
Don't you worry your pretty little mind
People throw rocks at things that shine
And life makes love look hard
The stakes are high, the water's rough
But this love is ours
And it's not theirs to speculate if it's wrong
And your hands are tough, but they are where mine belong
And I'll fight their doubt and give you faith
With this song for you
'Cause I love the gap between your teeth
And I love the riddles that you speak
And any snide remarks from my father about your tattoos will be ignored
'Cause my heart is yours
So don't you worry your pretty little mind
People throw rocks at things that shine
And life makes love look hard
Don't you worry your pretty little mind
People throw rocks at things that shine
But they can't take what's ours
They can't take what's ours
The stakes are high, the water's rough
But this love is ours
Last night I heard my own heart beating
Sounded like footsteps on my stairs
Six months gone and I'm still reaching
Even though I know you're not there
I was playing back a thousand memories, baby
Thinkin' 'bout everything we've been through
Maybe I've been going back too much lately
When time stood still and I had you
Come back, come back, come back to me like
You would, you would if this was a movie
Stand in the rain outside till I came out
Come back, come back, come back to me like
You could, you could if you just said you're sorry
I know that we could work it out somehow
But if this was a movie you'd be here by now
I know people change and these things happen
But I remember how it was back then
Wrapped up in your arms and our friends were laughing
Cause nothing like this ever happened to them
Now I'm pacing down the hall, chasing down your street
Flashback to the night when you said to me
"Nothing's gonna change, not for me and you"
Not before I knew how much I had to lose
Come back, come back, come back to me like
You would, you would if this was a movie
Stand in the rain outside till I came out
Come back, come back, come back to me like
You could, you could if you just said you're sorry
I know that we could work it out somehow
But if this was a movie you'd be here by now
If you're out there, if you're somewhere, if you're moving on
I've been waiting for you ever since you've been gone
I just want it back the way it was before
And I just want to see you back at my front door
And I say "Come back, come back, come back to me like
You would before you said it's not that easy
Before the fight, before I locked you out"
But I take it all back now
Come back, come back, come back to me like
You would, you would if this was a movie
Stand in the rain outside till I came out
Come back, come back, come back to me like
You could, you could if you just said you're sorry
I know that we could work it out somehow
But if this was a movie you'd be here by now
You'd be here by now
It's not the kind of ending you want to see now
Baby, what about the ending?
Oh, I thought you'd be here by now
Thought you'd be here by now
Tall, dark, and superman
He puts papers in his briefcase and drives away
To save the world or go to work
It's the same thing to me
He's got his mother's eyes, his father's ambition
I wonder if he knows how much that I miss him
I hang on every word you say, yay
"And you smile and say, ""How are you??,8,2010
Taylor Swift,Speak Now,Superman,17,I say"
I always forget to tell you, I love you, I love you forever
I watch superman fly away
You've got a busy day today
Go save the world, I'll be around
I watch superman fly away
Come back I'll be with you someday
I'll be right here on the ground
When you come back down
Tall, dark and beautiful
He's complicated, he's irrational
But I hope someday you'll take me away and save the day, yeah
Something in his deep brown eyes has me sayin'
He's not all bad like his reputation
And I can't hear one single word they say
And you'll leave, got places to be and I'll be OK
I always forget to tell you I love you, I loved you from the very first day
I watch superman fly away
You've got a busy day today
Go save the world, I'll be around
I watch superman fly away
Come back I'll be with you someday
I'll be right here on the ground
When you come back down
And I watch you fly around the world
And I hope you don't save some other girl
Don't forget, don't forget about me
I'm far away but I never let you go
I'm love-struck and looking out the window
Don't forget, don't forget where I'll be
Right here wishing the flowers were from you
Wishing the card was from you
Wishing the call was from you
'Cause I loved you from the very first day
I watch superman fly away
You've got a busy day today
Go save the world, I'll be around
Forever and ever here
I watch superman fly away
I swear I'll be with you someday
I'll be right here on the ground
When you come back down
La, la, la, la, la, la
La, la, la, la, la, la
When you come back down
I'm walking fast through the traffic lights
Busy streets and busy lives
And all we know is touch and go
We are alone with our changing minds
We fall in love till it hurts or bleeds, or fades in time
And I never saw you coming
And I'll never be the same
You come around and the armor falls
Pierce the room like a cannon ball
Now all we know, is don't let go
We are alone just you and me
Up in your room and our slates are clean
Just twin fire signs, four blue eyes
So you were never a saint
And I've loved in shades of wrong
We learn to live with the pain
Mosaic broken hearts
But this love is brave and wild
And I never saw you coming
And I'll never be the same
This is a state of grace
This is the worthwhile fight
Love is a ruthless game
Unless you play it good and right
These are the hands of fate
You're my Achilles heel
This is the golden age of something good
And right and real
And I never saw you coming
And I'll never be the same
And I never saw you coming
And I'll never be the same
This is a state of grace
This is a worthwhile fight
Love is a ruthless game
Unless you play it good and right
Loving him is like driving a new Maserati
Down a dead-end street
Faster than the wind, passionate as sin
Ending so suddenly
Loving him is like trying to change your mind
Once you're already flying through the free fall
Like the colors in autumn, so bright
Just before they lose it all
Losing him was blue like I'd never known
Missing him was dark grey, all alone
Forgetting him was like trying to know somebody you never met
But loving him was red
Touching him was like realizing all you ever wanted
Was right there in front of you
Memorizing him was as easy as knowing
All the words to your old favorite song
Fighting with him was like trying to solve a crossword
And realizing there's no right answer
Regretting him was like wishing you never found out
That love could be that strong
Losing him was blue like I'd never known
Missing him was dark grey, all alone
Forgetting him was like trying to know somebody you never met
But loving him was red
Remembering him comes in flashbacks and echoes
Tell myself it's time now, gotta let go
But moving on from him is impossible
When I still see it all in my head
In burning red
Loving him was red
Losing him was blue like I'd never known
Missing him was dark grey, all alone
Forgetting him was like trying to know somebody you never met
But loving him was red
And that's why he's spinning 'round in my head
Comes back to me, burning red
Yeah, yeah
His love was like driving a new Maserati down a dead-end street
Put your lips close to mine
As long as they don't touch
Out of focus, eye to eye
Till the gravity's too much
And I'll do anything you say
If you say it with your hands
And I'd be smart to walk away
But you're quick sand
This slope is treacherous
This path is reckless
This slope is treacherous
And I I I like it
I can't decide if it's a choice
Getting swept away
I hear the sound of my own voice
Asking you to stay
And all we are is skin and bone trained to get along
Forever going with the flow but you're friction
This slope is treacherous
This path is reckless
This slope is treacherous
And I I I like it
Two headlights shine through the sleepless night
And I will get you get you alone
Your name has echoed through my mind
And I just think you should think you should know
That nothing safe is worth the drive
And I will follow you follow you home, follow you follow you home
This hope is treacherous
This daydream is dangerous
This slope is treacherous
And I-I-I, I-I-I, I-I-I
Two headlights shine through the sleepless night
And I will get you get you alone
Your name has echoed through my mind
And I just think you should think you should know
That nothing safe is worth the drive
And I will follow you follow you home, follow you follow you home
This hope is treacherous
This daydream is dangerous
This hope is treacherous
I-I-I, I-I-I, I-I-I ...
Two headlights shine through the sleepless night
And I will get you get you alone
Your name has echoed through my mind
And I just think you should think you should know
That nothing safe is worth the drive
And I will follow you follow you home, follow you follow you home
I'll follow you follow you home, follow you follow you home
This slope is treacherous
And I-I-I like it
Once upon a time, a few mistakes ago
I was in your sights, you got me alone
You found me, you found me, you found me
I guess you didn't care, and I guess I liked that
And when I fell hard, you took a step back
Without me, without me, without me
And he's long gone, when he's next to me
And I realize the blame is on me
'Cause I knew you were trouble when you walked in
So shame on me now
Flew me to places I'd never been
Till you put me down, oh
I knew you were trouble when you walked in
So shame on me now
Flew me to places I'd never been
Now I'm lying on the cold hard ground
Oh, oh
Trouble, trouble, trouble
Oh, oh
Trouble, trouble, trouble
No apologies, he'll never see you cry
Pretends he doesn't know that he's the reason why
You're drowning, you're drowning
You're drowning
And I heard you moved on, from whispers on the street
A new notch in your belt is all I'll ever be
And now I see, now I see
Now I see
He was long gone when he met me
And I realize the joke is on me, hey!
I knew you were trouble when you walked in
So shame on me now
Flew me to places I'd never been
Till you put me down, oh
I knew you were trouble when you walked in
So shame on me now
Flew me to places I'd never been
Now I'm lying on the cold hard ground
Oh, oh
Trouble, trouble, trouble
Oh, oh
Trouble, trouble, trouble
And the saddest fear, comes creeping in
That you never loved me
Or her, or anyone, or anything, yeah!
I knew you were trouble when you walked in
So shame on me now
Flew me to places I'd never been
Till you put me down, oh
I knew you were trouble when you walked in
So shame on me now
Flew me to places I'd never been
Now I'm lying on the cold hard ground
Oh, oh
Trouble, trouble, trouble
Oh, oh
Trouble, trouble, trouble
I walked through the door with you, the air was cold
But something 'bout it felt like home somehow and I
Left my scarf there at your sister's house
And you've still got it in your drawer, even now
Oh, your sweet disposition
And my wide-eyed gaze
We're singing in a car getting lost Upstate
The autumn leaves falling down like pieces into place
And I can picture it after all these days
And I know it's long gone, and that magic's not here no more
And I might be okay, but I'm not fine at all
'Cause there we are again on that little town street
You almost ran the red 'cause you were looking over at me
Wind in my hair, I was there, I remember it all too well
Photo album on the counter
Your cheeks were turning red
You used to be a little kid with glasses in a twin-sized bed
And your mother's telling stories 'bout you on the tee ball team
You taught me about your past thinking your future was me
And I know it's long gone, and there was nothing else I could do
And I forget about you long enough to forget why I needed to
'Cause there we are again in the middle of the night
We're dancing round the kitchen in the refrigerator light
Down the stairs, I was there, I remember it all too well, yeah
And maybe we got lost in translation
Maybe I asked for too much
But maybe this thing was a masterpiece
'Till you tore it all up
Running scared, I was there, I remember it all too well
And you call me up again just to break me like a promise
So casually cruel in the name of being honest
I'm a crumpled up piece of paper lying here
'Cause I remember it all, all, all... too well
Time won't fly it's like I'm paralyzed by it
I'd like to be my old self again
But I'm still trying to find it
After plaid shirt days and nights when you made me your own
Now you mail back my things and I walk home alone
But you keep my old scarf from that very first week
'Cause it reminds you of innocence and it smells like me
You can't get rid of it, 'cause you remember it all too well, yeah
Because there we are again when I loved you so
Back before you lost the one real thing you've ever known
It was rare, I was there, I remember it all too well
Wind in my hair, you were there, you remember it all
Down the stairs, you were there, you remember it all
It was rare, I was there, I remember it all too well
It feels like a perfect night to dress up like hipsters
And make fun of our exes, uh uh, uh uh
It feels like a perfect night for breakfast at midnight
To fall in love with strangers, uh uh, uh uh
Yeah
We're happy, free, confused, and lonely at the same time
It's miserable and magical, oh yeah
Tonight's the night when we forget about the deadlines
It's time, uh uh
I don't know about you, but I'm feeling 22
Everything will be alright if you keep me next to you
You don't know about me, but I bet you wanted to
Everything will be alright if we just keep dancing like we're 22
22
It seems like one of those nights
This place is too crowded, too many cool kids, uh uh, uh uh
(Who's Taylor Swift, anyway? Ew)
It seems like one of those nights
We ditch the whole scene and end up dreaming
Instead of sleeping
Yeah
We're happy, free, confused, and lonely in the best way
It's miserable and magical, oh yeah
Tonight's the night when we forget about
The heartbreaks, it's time
Oh oh
I don't know about you, but I'm feeling 22
Everything will be alright if you keep me next to you
You don't know about me, but I bet you wanted to
Everything will be alright if we just keep dancing like we're 22
22
I don't know about you
22, 22
It feels like one of those nights
We ditch the whole scene
It feels like one of those nights
We won't be sleeping
It feels like one of those nights
You look like bad news, I gotta have you
I gotta have you
I don't know about you, but I'm feeling 22
Everything will be alright if you keep me next to you
You don't know about me, but I bet you wanted to
Everything will be alright if we just keep dancing like we're 22
22
Dancing like 22, yeah, 22, yeah yeah
It feels like one of those nights
We ditch the whole scene
It feels like one of those nights
We won't be sleeping
It feels like one of those nights
You look like bad news, I gotta have you
I gotta have you
I bet this time of night you're still up
I bet you're tired from a long hard week
I bet you're sitting in your chair by the window
Looking out at the city
And I bet sometimes you wonder about me
And I just want to tell you
It takes everything in me not to call you
And I wish I could run to you
And I hope you know that
Everytime I don't
I almost do, I almost do
I bet you think I either moved on or hate you
慍ause each time you reach out there's no reply
I bet it never, ever occurred to you that I can't say hello to you
And risk another goodbye
And I just want to tell you
It takes everything in me not to call you
And I wish I could run to you
And I hope you know that
Everytime I don't
I almost do, I almost do
Oh, we made quite a mess, babe
It's probably better off this way
And I confess, baby
In my dreams you're touching my face
And asking me if I'd want to try again with you
And I almost do
And I just want to tell you
It takes everything in me not to call you
And I wish I could run to you
And I hope you know that
Everytime I don't
I almost do, I almost do
I bet this time of night you're still up
I bet you're tired from a long hard week
I bet you're sittin' in your chair by the window
Looking out at the city
And I hope sometimes you wonder about me
I remember when we broke up, the first time
Saying, "This is it, I've had enough" 'cause, like
We hadn't seen each other in a month
When you said you needed space ?what<U+203D>
Then you come around again and say
"Baby, I miss you and I swear I'm gonna change; trust me"
Remember how that lasted for a day?
I say, "I hate you," we break up, you call me, "I love you"
Ooh梠oh梠oh梠oh梠oh
We called it off again last night but
Ooh梠oh梠oh梠oh梠oh
This time, I'm telling you, I'm telling you
We are never, ever, ever getting back together
We are never, ever, ever getting back together
You go talk to your friends, talk to my friends, talk to me
But we are never, ever, ever, ever getting back together
Like, ever
I'm really gonna miss you picking fights and me
Falling for it screaming that I'm right and you
Would hide away and find your peace of mind
With some indie record that's much cooler than mine
Ooh梠oh梠oh梠oh梠oh
We called it off again last night but
Ooh梠oh梠oh梠oh梠oh
This time, I'm telling you, I'm telling you
We are never, ever, ever getting back together
We are never, ever, ever getting back together
You go talk to your friends, talk to my friends, talk to me
But we are never, ever, ever, ever getting back together
Ooh梠oh梠oh梠oh梠oh (yeah!)
Ooh梠oh梠oh梠oh梠oh (yeah!)
Ooh梠oh梠oh梠oh梠oh (yeah!)
Oh梠h梠h!
I used to think that we were forever, ever
And I used to say, "Never say never"
Huh, so he calls me up and he's like, "I still love you"
And I'm like, "I just?I mean, this is exhausting, you know?
Like, we are never getting back together, like, ever"
We are never, ever, ever getting back together
We are never, ever, ever getting back together
You go talk to your friends, talk to my friends, talk to me
But we are never, ever, ever, ever getting back together
We?(ooh梠oh梠oh梠oh梠oh, ooh梠oh梠oh梠oh梠oh)
梘etting back together
We?(ooh梠oh梠oh梠oh梠oh, ooh梠oh梠oh梠oh梠oh)
梘etting back together
You go talk to your friends, talk to my friends, talk to me (talk to me)
But we are never, ever, ever, ever getting back together
I'm pretty sure we almost broke up last night
I threw my phone across the room, at you
I was expecting some dramatic turn away but you stay
This morning I said we should talk about it
'Cause I read you should never leave a fight unresolved
That's when you came in wearing a football helmet
And said okay let's talk
And I said
Stay, stay, stay
I've been loving you for quite some time, time, time
You think that it's funny when I'm mad, mad, mad
But I think that it's best if we both stay
Before you I'd only dated self-indulgent takers
Who took all of their problems out on me
But you carry my groceries and now I'm always laughing
And I love you because you have given me no choice but to
Stay, stay, stay
I've been loving you for quite some time, time, time
You think that it's funny when I'm mad, mad, mad
But I think that it's best if we both stay, stay, stay, stay
You took the time to memorize me, my fears, my hopes and dreams
I just like hanging out with you, all the time
All those times that you didn't leave it's been occurring to me
I'd like to hang out with you, for my whole life
Stay, and I'll be loving you for quite some time
No one else is gonna love me when I get mad, mad, mad
So I think that it's best if we both stay, stay
Stay, stay, stay, stay!
Stay, stay, stay
I've been loving you for quite some time, time, time
You think that it's funny when I'm mad, mad, mad
But I think that it's best if we both stay, stay
Stay, stay, stay, stay!
Stay, stay, stay
I've been loving you for quite some time, time, time
You think that it's funny when I'm mad, mad, mad
But I think that it's best if we both stay
(ha-haha-eee, It's so fun)
Find myself at your door
Just like all those times before
I'm not sure how I got there
All roads they lead me here
I imagine you are home
In your room, all alone
And you open your eyes into mine
And everything feels better
And right before your eyes
I'm breaking
No fuss, no reasons why
Just you and me
(e-he-e-he-e-he-e-he-e-he-e-he-e-he-e-he)
This is the last time I'm asking you this
Put my name at the top of your list
This is the last time I'm asking you why
You break my heart in the blink of an eye
(eye, eye)
You find yourself at my door
Just like all those times before
You wear your best apology
But I was there to watch you leave
And all the times I let you in
Just for you to go again
Disappear when you come back
Everything is better
And right before your eyes
I'm aching
No fuss, nowhere to hide
Just you and me
(e-he-e-he-e-he-e-he-e-he-e-he-e-he-e-he)
This is the last time I'm asking you this
Put my name at the top of your list
This is the last time I'm asking you why
You break my heart in the blink of an eye
(eye, eye)
Gary Lightbody
This is the last time you tell me I've got it wrong
This is the last time I say it's been you all along
This is the last time I let you in my door
This is the last time, I won't hurt you anymore
Oh-ho, oh-ho, oh-ho, oh-ho
Oh-ho, oh-ho, oh-ho, oh-ho
This is the last time I'm asking you this
Put my name at the top of your list
This is the last time I'm asking you why
You break my heart in the blink of an eye
Gary Lightbody
This is the last time I'm asking you this
(This is the last time I'm asking you this)
Put my name at the top of your list
(Put my name at the top of your list)
This is the last time I'm asking you why
(This is the last time I'm asking you why)
You break my heart in the blink of an eye
(You break my heart)
This is the last time I'm asking you, last time I'm asking you
Last time I'm asking you this
This is the last time I'm asking you, last time I'm asking you
Last time I'm asking you this
This is the last time I'm asking you, last time I'm asking you
Last time I'm asking you this
This is the last time I'm asking you, last time I'm asking you
Last time I'm asking you this
I was reminiscing just the other day
While having coffee all alone and Lord, it took me away
Back to a first-glance feeling on New York time
Back when you fit my poems like a perfect rhyme
Took off faster than a green light, go
Hey, you skip the conversation when you already know
I left a note on the door with a joke we'd made
And that was the first day
And darling, it was good never looking down
And right there where we stood was holy ground
Spinning like a girl in a brand new dress
We had this big wide city all to ourselves
We blocked the noise with the sound of 'I need you'
And for the first time I had something to lose
And I guess we fell apart in the usual way
And the story's got dust on every page
But sometimes I wonder how you think about it now
And I see your face in every crowd
'Cause darling, it was good never looking down
And right there where we stood was holy ground
Tonight I'm gonna dance for all that we've been through
But I don't wanna dance if I'm not dancing with you
Tonight I'm gonna dance like you were in this room
But I don't wanna dance if I'm not dancing with you
It was good never looking down
And right there where we stood was holy ground
Tonight I'm gonna dance for all that we've been through
But I don't wanna dance if I'm not dancing with you
Tonight I'm gonna dance like you were in this room
But I don't wanna dance if I'm not dancing with you
Long handwritten note, deep in your pocket
Words, how little they mean, when you're a little too late
I stood right by the tracks, your face in a locket
Good girls, hopeful they'll be and long they will wait
We had a beautiful magic love there
What a sad beautiful tragic love affair
In dreams, I meet you in warm conversation
We both wake in lonely beds, different cities
And time is taking its sweet time erasing you
And you've got your demons and darling they all look like me
We had a beautiful magic love there
What a sad beautiful tragic love affair
Distance, timing, breakdown, fighting
Silence, the train runs off its tracks
Kiss me, try to fix it, could you just try to listen?
Hang up, give up, and for the life of us we can't get back
We had a beautiful magic love there
What a sad beautiful tragic love affair
We had a beautiful magic love there
What a sad beautiful tragic love affair
We had a beautiful magic love there
What a sad beautiful tragic love affair
New to town with a made up name
In the angel city, chasing fortune and fame
And the camera flashes, make it look like a dream
You had it figured out since you were in school
Everybody loves pretty, everybody loves cool
So overnight you look like a sixties' queen
Another name goes up in lights, like diamonds in the sky
And they'll tell you now, you're the lucky one
Yeah, they'll tell you now, you're the lucky one
But can you tell me now, you're the lucky one, oh, oh, oh
Now it's big black cars, and Riviera views
And your lover in the foyer doesn't even know you
And your secrets end up splashed on the news front page
And they tell you that you're lucky
But you're so confused
Cause you don't feel pretty, you just feel used
And all the young things line up to take your place
Another name goes up in lights
You wonder if you'll make it out alive
And they'll tell you now, you're the lucky one
Yeah, they'll tell you now, you're the lucky one
But can you tell me now, you're the lucky one, oh, oh, oh
It was a few years later, I showed up here
And they still tell the legend of how you disappeared
How you took the money and your dignity, and got the hell out
They say you bought a bunch of land somewhere
Chose a rose garden over Madison Square
And it took some time, but I understand it now
慍ause now my name is up in lights, but I think you got it right
Let me tell you now, you're the lucky one
Let me tell you now, you're the lucky one
Let me tell you now, you're the lucky one, oh, oh, oh
And they'll tell you now, you're the lucky one
Yeah, they'll tell you now, you're the lucky one
And they'll tell you now, you're the lucky one, oh, oh, oh
Oh, whoa, oh, oh
All I knew this morning when I woke
Is I know something now, know something now I didn't before
And all I've seen since 18 hours ago is green eyes and freckles and your smile
In the back of my mind making me feel like
I just want to know you better
Know you better, know you better now
I just want to know you better
Know you better, know you better now
I just want to know you better
Know you better, know you better now
I just want to know you, know you, know you
'Cause all I know is we said hello
And your eyes look like coming home
All I know is a simple name, everything has changed
All I know is you held the door
You'll be mine and I'll be yours
All I know since yesterday is everything has changed
Taylor Swift
And all my walls stood tall painted blue
And I'll take them down
Take them down and open up the door for you
And all I feel in my stomach is butterflies
The beautiful kind, making up for lost time
Taking flight, making me feel like
I just want to know you better
Know you better, know you better now
I just want to know you better
Know you better, know you better now
I just want to know you better
Know you better, know you better now
I just want to know you, know you, know you
'Cause all I know is we said hello
And your eyes look like coming home
All I know is a simple name, everything has changed
All I know is you held the door
You'll be mine and I'll be yours
All I know since yesterday is everything has changed
Come back and tell me why
I'm feeling like i've missed you all this time
And meet me there tonight
And let me know that it's not all in my mind
I just want to know you better
Know you better, know you better now
I just want to know you, know you, know you
'Cause all I know is we said hello
And your eyes look lIke coming home
All I know is a simple name, everything has changed
All I know is you held the door
You'll be mine and I'll be yours
All I know since yesterday is everything has changed
All I know is we said hello
So dust off your highest hopes
All I know is pouring rain
And everything has changed
All I know is a new found grace
All my days, I'll know your face
All I know since yesterday is everything has changed
I said, "Oh my, what a marvelous tune"
It was the best night, never would forget how we moved
The whole place was dressed to the nines
And we were dancing, dancing
Like we're made of starlight
Like we're made of starlight
I met Bobby on the boardwalk, summer of '45
Picked me up, late one night at the window
We were 17 and crazy, running wild, wild
Can't remember what song it was playing when we walked in
The night we snuck into a yacht club party
Pretending to be a duchess and a prince
And I said, "Oh my, what a marvelous tune"
It was the best night, never would forget how we moved
The whole place was dressed to the nines
And we were dancing, dancing
Like we're made of starlight, starlight
Like we're made of starlight, starlight
He said, "Look at you worrying too much about things you can't change
You'll spend your whole life singing the blues if you keep thinking that way"
He was trying to skip rocks on the ocean saying to me
"Don't you see the starlight, starlight?
Don't you dream impossible things?"
Like, "Oh my, what a marvelous tune"
It was the best night, never would forget how we moved
The whole place was dressed to the nines
And we were dancing, dancing
Like we're made of starlight, starlight
Like we're made of starlight, starlight
Ooh, ooh, he's talking crazy
Ooh, ooh, dancing with me
Ooh, ooh, we could get married
Have ten kids and teach 'em how to dream
Oh my, what a marvelous tune
It was the best night, never would forget how we moved
The whole place was dressed to the nines
And we were dancing, dancing
Like we're made of starlight, starlight
Like we're made of starlight, starlight
Like we're made of starlight, starlight
Like we dream impossible dreams
Like starlight, starlight
Like we dream impossible dreams
Don't you see the starlight, starlight?
Don't you dream impossible things?
Took a deep breath in the mirror
He didn't like it when I wore high heels
But I do
Turn the lock and put my headphones on
He always said he didn't get this song but I do, I do
Walked in expecting you'd be late
But you got here early and you stand and wave
I walk to you
You pull my chair out and help me in
And you don't know how nice that is but I do
And you throw your head back laughing like a little kid
I think it's strange that you think I'm funny 'cause he never did
I've been spending the last eight months
Thinking all love ever does is break and burn and end
But on a Wednesday in a cafe, I watched it begin again
You said you never met one girl who
Had as many James Taylor records as you
But I do
We tell stories and you don't know why I'm coming off a little shy
But I do
And you throw your head back laughing like a little kid
I think it's strange that you think I'm funny 'cause he never did
I've been spending the last eight months
Thinking all love ever does is break and burn and end
But on a Wednesday in a cafe, I watched it begin again
And we walked down the block, to my car
And I almost brought him up
But you start to talk about the movies
That your family watches every single Christmas
And I want to talk about that
And for the first time what's past is past
'Cause you throw your head back laughing like a little kid
I think it's strange that you think I'm funny 'cause he never did
I've been spending the last eight months
Thinking all love ever does is break and burn and end
But on a Wednesday in a cafe, I watched it begin again
But on a Wednesday in a cafe, I watched it begin again
You should've been there
Should've burst through the door
With that 'baby I'm right here' smile
And it would've felt like
A million little shining stars had just aligned
And I would've been so happy
Christmas lights glisten
I've got my eye on the door
Just waiting for you to walk in
But the time is ticking
People ask me how I've been
As I comb back through my memory
How you said you'd be here
You said you'd be here
And it was like slow motion
Standing there in my party dress
In red lipstick
With no one to impress
And they're all laughing
As I'm looking around the room
But there was one thing missing
And that was the moment I knew
And the hours pass by
Now I just wanna be alone
But your close friends always seem to know
When there's something really wrong
So they follow me down the hall
And there in the bathroom
I try not to fall apart
And the sinking feeling starts
As I say hopelessly
"He said he'd be here"
And it was like slow motion
Standing there in my party dress
In red lipstick
With no one to impress
And they're all laughing
And asking me about you
But there was one thing missing
And that was the moment I knew
What do you say
When tears are streaming down your face
In front of everyone you know?
And what do you do when the one
Who means the most to you
Is the one who didn't show?
You should've been here
And I would've been so happy
And it was like slow motion
Standing there in my party dress
In red lipstick
With no one to impress
And they're all standing around me singing
"Happy birthday to you"
But there was one thing missing
And that was the moment I knew
Oh-oh-oh-oh-oh-oh-oh-oh-oh-oh-oh-oh
I knew
Oh-oh-oh-oh-oh-oh-oh-oh-oh-oh-oh-oh
You call me later
And said, "I'm sorry I didn't make it"
And I said, "I'm sorry too"
And that was the moment I knew
You said it in a simple way
4 AM, the second day
How strange that I don't know you at all
Stumbled through the long goodbye
One last kiss, then catch your flight
Right when I was just about to fall
I told myself don't get attached
But in my mind I play it back
Spinning faster than the plane that took you
And this is when the feeling sinks in
I don't wanna miss you like this
Come back be here, come back be here
I guess you're in New York today
I don't wanna need you this way
Come back be here, come back be here
The delicate beginning rush
The feeling you can know so much
Without knowing anything at all
And now that I can put this down
If I had known what I'd known now
I never would have played so nonchalant
Taxi cabs and busy streets
That never bring you back to me
I can't help but wish you took me with you
And this is when the feeling sinks in
I don't wanna miss you like this
Come back be here, come back be here
I guess you're in London today
I don't wanna need you this way
Come back be here, come back be here
This is falling in love in the cruelest way
This is falling for you and you are worlds away
New York be here
But you're in London and I break down
Cause it's not fair that you're not around
I don't wanna miss you like this
Come back be here
Come back be here
Don't look at me, you got a girl at home
And everybody knows that, everybody knows that
Don't look at me, you got a girl at home
And everybody knows that, everybody knows that
I don't even know her
But I feel a responsibility to do what's upstanding and right
It's kinda like a code, yeah
And you've been getting closer and closer
And crossing so many lines
And it would be a fine proposition
If I was a stupid girl
But honey I am no one's exception
This I have previously learned
So don't look at me, you got a girl at home
And everybody knows that, everybody knows that
Don't look at me, you got a girl at home
And everybody knows that, everybody knows that
I see you turn off your phone
Now you've got me alone, and I say
Don't look at me, you got a girl at home
And everybody knows that, everybody knows that
I just want to make sure
You understand perfectly you're the kind of man who makes me sad
While she waits up, you chase down the newest thing
And take for granted what you have
And it would be a fine proposition
If I was a stupid girl
And yeah, I might go with it
If I hadn't once been just like her
So don't look at me, you got a girl at home
And everybody knows that, everybody knows that
Don't look at me, you got a girl at home
And everybody knows that, everybody knows that
I see you turn off your phone
Now you've got me alone, and I say
Don't look at me, you got a girl at home
And everybody knows that, everybody knows that
Call a cab, lose my number
You're about to lose your girl
Call a cab, lose my number
Let's consider this lesson learned
Want to see you pick up your phone
And tell her you're coming home
Don't look at me, you got a girl at home
And everybody knows that, everybody knows that
It would be a fine proposition
If I hadn't once been just like her
Walking through a crowd, the village is aglow
Kaleidoscope of loud heartbeats under coats
Everybody here wanted something more
Searching for a sound we hadn't heard before
And it said
Welcome to New York!
It's been waiting for you
Welcome to New York
Welcome to New York
Welcome to New York!
It's been waiting for you
Welcome to New York
Welcome to New York
It's a new soundtrack
I could dance to this beat (beat)
Forevermore
The lights are so bright
But they never blind me (me)
Welcome to New York!
It's been waiting for you
Welcome to New York
Welcome to New York
When we first dropped our bags on apartment floors
Took our broken hearts, put them in a drawer
Everybody here was someone else before
And you can want who you want
Boys and boys and girls and girls
Welcome to New York!
It's been waiting for you
Welcome to New York
Welcome to New York
Welcome to New York!
It's been waiting for you
Welcome to New York
Welcome to New York
It's a new soundtrack
I could dance to this beat (beat)
Forevermore
The lights are so bright
But they never blind me (me)
Welcome to New York!
It's been waiting for you
Welcome to New York
Welcome to New York
Like any great love, it keeps you guessing
Like any real love, it's ever-changing
Like any true love, it drives you crazy
But you know you wouldn't change anything, anything, anything
Welcome to New York!
It's been waiting for you
Welcome to New York
Welcome to New York
Welcome to New York!
It's been waiting for you
Welcome to New York
Welcome to New York
It's a new soundtrack
I could dance to this beat (beat)
Forevermore
The lights are so bright
But they never blind me (me)
Welcome to New York!
It's been waiting for you
Welcome to New York
Welcome to New York
Nice to meet you, where you been?
I could show you incredible things
Magic, madness, heaven, sin
Saw you there, and I thought
"Oh my God, look at that face
You look like my next mistake
Love's a game, wanna play?" Ayy
New money, suit and tie
I can read you like a magazine
Ain't it funny? Rumors fly
And I know you heard about me
So hey, let's be friends
I'm dyin' to see how this one ends
Grab your passport and my hand
I can make the bad guys good for a weekend
So it's gonna be forever
Or it's gonna go down in flames
You can tell me when it's over, mm
If the high was worth the pain
Got a long list of ex-lovers
They'll tell you I'm insane
'Cause you know I love the players
And you love the game
'Cause we're young and we're reckless
We'll take this way too far
It'll leave you breathless, hmm
Or with a nasty scar
Got a long list of ex-lovers
They'll tell you I'm insane
But I've got a blank space, baby
And I'll write your name
Cherry lips, crystal skies
I could show you incredible things
Stolen kisses, pretty lies
You're the King, baby, I'm your Queen
Find out what you want
Be that girl for a month
Wait, the worst is yet to come, oh no
Screaming, crying, perfect storms
I can make all the tables turn
Rose garden filled with thorns
Keep you second guessin' like
"Oh my God, who is she?"
I get drunk on jealousy
But you'll come back each time you leave
'cause, darling, I'm a nightmare
Dressed like a daydream
So it's gonna be forever
Or it's gonna go down in flames
You can tell me when it's over, mm
If the high was worth the pain
Got a long list of ex-lovers
They'll tell you I'm insane
'Cause you know I love the players
And you love the game
'Cause we're young and we're reckless
We'll take this way too far
It'll leave you breathless, hmm
Or with a nasty scar
Got a long list of ex-lovers
They'll tell you I'm insane
But I've got a blank space, baby
And I'll write your name
Boys only want love if it's torture
Don't say I didn't, say I didn't, warn ya
Boys only want love if it's torture
Don't say I didn't, say I didn't, warn ya
So it's gonna be forever
Or it's gonna go down in flames
You can tell me when it's over, mm
If the high was worth the pain
Got a long list of ex-lovers
They'll tell you I'm insane
'Cause you know I love the players
And you love the game
'Cause we're young and we're reckless
We'll take this way too far
It'll leave you breathless, hmm
Or with a nasty scar
Got a long list of ex-lovers
They'll tell you I'm insane
But I've got a blank space, baby
And I'll write your name
Midnight
You come and pick me up, no headlights
Long drive
Could end in burning flames or paradise
Fade into view
Oh, It's been a while since I have even heard from you
(Heard from you)
And I should just tell you to leave cause I
Know exactly where it leads, but I
Watch us go round and round each time
You got that James Dean daydream look in your eye
And I got that red lip classic thing that you like
And when we go crashing down, we come back every time
Cause we never go out of style, we never go out of style
You got that long hair, slicked back, white t-shirt
And I got that good girl faith and a tight little skirt
And when we go crashing down, we come back every time
Cause we never go out of style, we never go out of style
So it goes
He can't keep his wild eyes on the road (mmm)
Takes me home
Lights are off, he's taking off his coat (mmm, yeah)
I say "I've heard
Oh, that you've been out and about with some other girl"
Some other girl
He says "What you heard is true, but I
Can't stop thinking 'bout you and I"
I said "I've been there too a few times"
Cause you got that James Dean daydream look in your eye
And I got that red lip classic thing that you like
And when we go crashing down, we come back every time
Cause we never go out of style, we never go out of style
You got that long hair, slicked back, white t-shirt
And I got that good girl faith and a tight little skirt
And when we go crashing down, we come back every time
Cause we never go out of style, we never go out of style
Take me home
Just take me home
Yeah, just take me home
(Out of style)
Oh, you got that James Dean daydream look in your eye
And I got that red lip classic thing that you like
And when we go crashing down, we come back everytime
Cause we never go out of style, we never go out of style
Looking at it now
It all seems so simple
We were lying on your couch
I remember
You took a Polaroid of us
Then discovered (then discovered)
The rest of the world was black and white
But we were in screaming color
And I remember thinking?9
Are we out of the woods yet? Are we out of the woods yet?
Are we out of the woods yet? Are we out of the woods?
Are we in the clear yet? Are we in the clear yet?
Are we in the clear yet? In the clear yet? Good
Are we out of the woods yet? Are we out of the woods yet?
Are we out of the woods yet? Are we out of the woods?
Are we in the clear yet? Are we in the clear yet?
Are we in the clear yet? In the clear yet? Good
(Are we out of the woods?)
Looking at it now
Last December (last December)
We were built to fall apart
Then fall back together (back together)
Your necklace hanging from my neck
The night we couldn't quite forget
When we decided, we decided
To move the furniture so we could dance
Baby, like we stood a chance
Two paper airplanes flying, flying, flying
And I remember thinking?29
Are we out of the woods yet? Are we out of the woods yet?
Are we out of the woods yet? Are we out of the woods?
Are we in the clear yet? Are we in the clear yet?
Are we in the clear yet? In the clear yet? Good
Are we out of the woods yet? Are we out of the woods yet?
Are we out of the woods yet? Are we out of the woods?
Are we in the clear yet? Are we in the clear yet?
Are we in the clear yet? In the clear yet? Good
(Are we out of the woods?)
Remember when you hit the brakes too soon?
Twenty stitches in a hospital room
When you started crying, baby, I did too
When the sun came up, I was looking at you
Remember when you couldn't take the heat?
I walked out and said I'm setting you free
But the monsters turned out to be just trees
When the sun came up, you were looking at me
You were looking at me, ooh
You were looking at me
(Are we out of the woods yet? Are we out of the woods yet?)
(Are we out of the woods yet? Are we out of the woods?)
I remember
(Are we in the clear yet? Are we in the clear yet?)
(Are we in the clear yet? In the clear yet? Good)
Oh, I remember!
Are we out of the woods yet? Are we out of the woods yet?
Are we out of the woods yet? Are we out of the woods?
Are we in the clear yet? Are we in the clear yet?
Are we in the clear yet? In the clear yet? Good
Are we out of the woods yet? Are we out of the woods yet?
Are we out of the woods yet? Are we out of the woods?
Are we in the clear yet? Are we in the clear yet?
Are we in the clear yet? In the clear yet? Good
Are we out of the woods yet? Are we out of the woods yet?
Are we out of the woods yet? Are we out of the woods?
Are we in the clear yet? Are we in the clear yet?
Are we in the clear yet? In the clear yet? Good
Are we out of the woods yet? Are we out of the woods yet?
Are we out of the woods yet? Are we out of the woods?
Are we in the clear yet? Are we in the clear yet?
Are we in the clear yet? In the clear yet? Good
People like you always want back
The love they gave away
And people like me wanna believe you
When you say you've changed
The more I think about it now
The less I know
All I know is that you drove us
Off the road
(Stay!) Hey
All you had to do was stay
Had me in the palm of your hand
Then why'd you have to go and lock me out when I let you in?
(Stay!) Hey
Now you say you want it back
Now that it's just too late
Well, could've been easy
All you had to do was (stay!)
All you had to do was (stay!)
All you had to do was (stay!)
All you had to do was (stay!)
All you had to do was stay
Here you are now calling me up
But I don't know what to say
I've been picking up the pieces
Of the mess you made
People like you always want back
The love they pushed aside
But people like me are gone forever
When you say goodbye
(Stay!) Hey
All you had to do was stay
Had me in the palm of your hand
Then why'd you have to go and lock me out when I let you in?
(Stay!) Hey
Now you say you want it back
Now that it's just too late
Well, could've been easy
All you had to do was (stay!)
All you had to do was (stay!)
All you had to do was (stay!)
All you had to do was (stay! stay! stay! stay! stay!)
Let me remind you
This was what you wanted (Oh! Oh! Oh-oh-oh!)
You ended it
You were all I wanted (Oh! Oh! Oh-oh-oh!)
But not like this
Not like this... not like this...
Oh! All you had to do was!
(Stay!) Hey
All you had to do was stay
Had me in the palm of your hand
Then why'd you want to go and lock me out when I let you in?
(Stay!) Hey
Now you say you want it back
Now that it's just too late
Well, could've been easy
All you had to do was
(Stay!) Hey
All you had to do was stay
Had me in the palm of your hand
Then why'd you have to go and lock me out when I let you in?
(Stay!) Hey
Now you say you want it back
Now that it's just too late (all you had to do was stay)
Well, could've been easy
All you had to do was (stay!)
All you had to do was (stay!) (ahh-ooh)
All you had to do was (stay!)
All you had to do was (stay!) (Oo-oo-whoa)
All you had to do was (stay!)
I stay out too late
Got nothing in my brain
That's what people say, mmm, mmm
That's what people say, mmm, mmm
I go on too many dates
But I can't make them stay
At least that's what people say, mmm, mmm
That's what people say, mmm, mmm
But I keep cruisin'
Can't stop, won't stop movin'
It's like I got this music in my mind
Saying it's gonna be alright
'Cause the players gonna play, play, play, play, play
And the haters gonna hate, hate, hate, hate, hate
Baby, I'm just gonna shake, shake, shake, shake, shake
I shake it off,  I shake it off
Heartbreakers gonna break, break, break, break, break
And the fakers gonna fake, fake, fake, fake, fake
Baby, I'm just gonna shake, shake, shake, shake, shake
I shake it off, I shake it off
I never miss a beat
I'm lightning on my feet
And that's what they don't see, mmm, mmm
That's what they don't see, mmm, mmm
I'm dancing on my own (dancing on my own)
I make the moves up as I go (moves up as I go)
And that's what they don't know, mmm, mmm
That's what they don't know, mmm, mmm
But I keep cruisin'
Can't stop, won't stop groovin'
It's like I got this music in my mind
Saying it's gonna be alright
'Cause the players gonna play, play, play, play, play
And the haters gonna hate, hate, hate, hate, hate
Baby, I'm just gonna shake, shake, shake, shake, shake
I shake it off,  I shake it off
Heartbreakers gonna break, break, break, break, break
And the fakers gonna fake, fake, fake, fake, fake
Baby, I'm just gonna shake, shake, shake, shake, shake
I shake it off, I shake it off
Shake it off, I shake it off
I, I, I shake it off, I shake it off
I, I, I shake it off, I shake it off
I, I, I shake it off, I shake it off
Hey, hey, hey
Just think while you've been getting down and out about the liars
And dirty, dirty cheats of the world you could've been getting down to this sick beat
My ex-man brought his new girlfriend
She's like, 揙h my God? but I'm just gonna shake
And to the fella over there with the hella good hair
Won't you come on over, baby, we can shake, shake, shake
Yeah, oh, oh, oh, oh
'Cause the players gonna play, play, play, play, play
And the haters gonna hate, hate, hate, hate, hate (haters gonna hate)
Baby, I'm just gonna shake, shake, shake, shake, shake
I shake it off,  I shake it off
Heartbreakers gonna break, break, break, break, break (mmhm)
And the fakers gonna fake, fake, fake, fake, fake (fake n' fake n' fake)
Baby, I'm just gonna shake, shake, shake, shake, shake
I shake it off, I shake it off
Shake it off, I shake it off
I, I, I shake it off, I shake it off
I, I, I shake it off, I shake it off
I, I, I shake it off, I shake it off
Shake it off, I shake it off
I, I, I shake it off, I shake it off
I, I, I shake it off, I shake it off
I, I, I shake it off, I shake it off (yeah!)
Shake it off, I shake it off
I, I, I shake it off, I shake it off (you got to)
I, I, I shake it off, I shake it off
I, I, I shake it off, I shake it off
It's 2:00 AM, in your car
Windows down, you pass my street, the memories start
You say it's in the past
You drive straight ahead
You're thinking that I hate you now
Cause you still don't know what I never said
I wish you would come back
Wish I never hung up the phone like I did, and I
Wish you knew that
I'd never forget you as long as I live, and I
Wish you were right here, right now
It's all good
I wish you would
It's 2:00 AM, in my room
Headlights pass the window pane
I think of you
We're a crooked love
In a straight line down
Makes you want to run and hide
Then it makes you turn right back around
I wish you would come back
Wish I never hung up the phone like I did, and I
Wish you knew that
I'd never forget you as long as I live, and I
Wish you were right here, right now
It's all good
I wish you would
I wish we could go back
And remember what we were fighting for, and I
Wish you knew that
I miss you too much to be mad anymore, and I
Wish you were right here, right now
It's all good
I wish you would
(I, I, I-I, I, I, I wish I, wish I)
(I, I, I-I, I, I, I wish I, wish I)
(I, I, I-I, I, I, I wish I, wish I) x7
You always knew how to push my buttons
You give me everything and nothing
This mad mad love makes you come running
Stand back where you stood
I wish you would, I wish you would
(I wish you would, I wish you would)
I wish you would, I wish you would
(I wish you would, I wish you would)
2:00 AM, here we are
See your face, hear my voice in the dark
We're a crooked love
In a straight line down
Makes you wanna run and hide
But it made us turn right back around
I wish you would come back
Wish I never hung up the phone like I did, I
Wish you knew that
I'd never forget you as long as I live, and I
Wish you were right here, right now
It's all good
I wish you would
I wish you would come back
Wish I never hung up the phone like I did, I
Wish you knew that
I'd never forget you as long as I live, and I
Wish you were right here, right now
It's all good
I wish you would
I wish we could go back
And remember what we were fighting for, and I
Wish you knew that
I miss you too much to be mad anymore, and I
Wish you were right here, right now
It's all good
I wish you would
(I, I, I-I, I, I, I wish I, wish I) x8
You always knew how to push my buttons
You give me everything and nothing
This mad mad love makes you come running
Stand back where you stood
I wish you would, I wish you would
(I wish you would, I wish you would)
I wish you would, I wish you would
(I wish you would, I wish you would, I wish you would)
(I wish you would)
I wish you would
'Cause baby, now we've got bad blood
You know it used to be mad love
So take a look what you've done
'Cause baby, now we've got bad blood, hey
Now we've got problems
And I don't think we can solve 'em
You made a really deep cut
And baby, now we've got bad blood, hey!
Did you have to do this?
I was thinking that you could be trusted
Did you have to ruin what was shiny?
Now it's all rusted
Did you have to hit me where I'm weak?
Baby, I couldn't breathe
And rub it in so deep
Salt in the wound like you're laughing right at me
Oh, it's so sad to
Think about the good times
You and I
'Cause baby, now we've got bad blood
You know it used to be mad love
So take a look what you've done
'Cause baby, now we've got bad blood, hey
Now we've got problems
And I don't think we can solve 'em
You made a really deep cut
And baby, now we've got bad blood, hey!
Did you think we'd be fine?
Still got scars in my back from your knives
So don't think it's in the past
These kind of wounds they last and they last
Now, did you think it all through?
All these things will catch up to you
And time can heal, but this won't
So if you come in my way
Just don't
Oh, it's so sad to
Think about the good times
You and I
'Cause baby, now we've got bad blood
You know it used to be mad love
So take a look what you've done
'Cause baby, now we've got bad blood, hey
Now we've got problems
And I don't think we can solve 'em
You made a really deep cut
And baby, now we've got bad blood, hey!
Band-aids don't fix bullet holes
You say sorry just for show
You live like that, you live with ghosts
Band-aids don't fix bullet holes
You say sorry just for show
If you live like that, you live with ghosts
If you love like that, blood runs cold!
'Cause baby, now we've got bad blood
You know it used to be mad love
So take a look what you've done
'Cause baby, now we've got bad blood, hey!
Now we've got problems
And I don't think we can solve 'em
You made a really deep cut
And baby, now we've got bad blood, hey!
'Cause baby, now we've got bad blood
You know it used to be mad love
So take a look what you've done
'Cause baby, now we've got bad blood, hey!
Now we've got problems
And I don't think we can solve 'em
You made a really deep cut
And baby, now we've got bad blood, hey!
He said, "Let's get out of this town
Drive out of this city, away from the crowds"
I thought, "Heaven can't help me now"
Nothing lasts forever, but this is gonna take me down
He's so tall and handsome as hell
He's so bad, but he does it so well
I can see the end as it begins
My one condition is
Say you'll remember me
Standing in a nice dress
Staring at the sunset, babe
Red lips and rosy cheeks
Say you'll see me again
Even if it's just in your
Wildest dreams, ah-aah haa
Wildest dreams, ah-aah haa
I said, "No one has to know what we do"
His hands are in my hair, his clothes are in my room
And his voice is a familiar sound
Nothing lasts forever, but this is gettin' good now
He's so tall and handsome as hell
He's so bad, but he does it so well
And when we've had our very last kiss
My last request, it is
Say you'll remember me
Standing in a nice dress
Staring at the sunset, babe
Red lips and rosy cheeks
Say you'll see me again
Even if it's just in your
Wildest dreams, ah-aah haa (ah-aah haa)
Wildest dreams, ah-aah haa
You'll see me in hindsight, tangled up with you all night
Burnin' it down
Someday when you leave me, I'd bet these memories
Follow you around
You'll see me in hindsight, tangled up with you all night
Burning (burning) it (it) down (down)
Someday when you leave me, I'll bet these memories
Follow (follow) you (you) around (around)
(Follow you around)
Say you'll remember me
Standing in a nice dress
Staring at the sunset, babe
Red lips and rosy cheeks
Say you'll see me again
Even if it's just pretend
Say you'll remember me
Standing in a nice dress
Staring at the sunset, babe
Red lips and rosy cheeks
Say you'll see me again
Even if it's just in your (pretend, just pretend)
Wildest dreams, ah-aah haa (ah-aah-aah-aah-aah-haa)
In your wildest dreams, ah-aah haa
Even if it's just in your
Wildest dreams, ah-aah haa
In your wildest dreams, ah-aah haa
Uh, uh, uh
Uh, uh, uh
Uh-uh, uh-uh
Stand there like a ghost
Shaking from the rain, rain
She'll open up the door and say, "Are you insane?"
Say it's been a long six months
And you were too afraid to tell her what you want, want
And that's how it works
That's how you get the girl
And then you say, I want you for worse or for better
I would wait forever and ever
Broke your heart, I'll put it back together
I would wait forever and ever
And that's how it works
That's how you get the girl, girl (oh-oh, oh-oh)
And that's how it works
That's how you get the girl, girl
Remind her how it used to be, be, yeah-yeah
With pictures in frames of kisses on cheeks, cheeks
Tell her how you must have lost your mind, ooh-ooh
When you left her all alone and never told her why, why
And that's how it works
That's how you lost the girl
And now you say?25
I want you for worse or for better
I would wait forever and ever (ever and ever)
Broke your heart, I'll put it back together
I would wait forever and ever
And that's how it works
That's how you get the girl, girl (oh-oh, oh-oh)
And that's how it works
That's how you get the girl, girl
Yeah, yeah
And you know-oh, oh, oh, oh, oh, oh, oh, oh, oh, oh
That I don't want you to go, oh, oh
Remind me how it used to be
Pictures in frames of kisses on cheeks
And say you want me, yeah-yeah
And then you say?40
I want you for worse or for better (worse of for better)
I would wait forever and ever (and ever)
Broke your heart, I'll put it back together
I would wait forever and ever (I want you forever and ever)
And that's how it works
That's how you get the girl, girl (that's how it works!)
And that's how it works
That's how you get the girl, girl (get the girl! That's how it works!)
And that's how it works
That's how you get the girl, girl
And that's how it works
That's how you get the girl, girl
That's how it works, that's how you got the girl
Clear blue water, high tides came and brought you in
And I could go on and on, on and on
And I will
Skies grew darker, currents swept you out again
And you are just gone and gone, gone and gone
In silent screams and wildest dreams
I never dreamed of this
This love is good, this love is bad
This love is alive back from the dead
These hands had to let it go free
And this love came back to me
Tossing, turning, struggle through the night with someone new
And I could go on and on, on and on
Lantern, burning, flickered in my mind for only you
But you were still gone, gone, gone
Been losing grip, sinking ships
You showed up just in time
This love is good, this love is bad
This love is alive back from the dead
These hands had to let it go free
And this love came back to me
This love left a permanent mark
This love is glowing in the dark
These hands had to let it go free
And this love came back to me
Your kiss, my cheek, I watched you leave
Your smile, my ghost, I fell to my knees
When you're young you just run
But you come back to what you need
This love is good, this love is bad
This love is alive back from the dead
These hands had to let it go free
And this love came back to me
This love left a permanent mark
This love is glowing in the dark
These hands had to let it go free
And this love came back to me
You stand with your hand on my waistline
It's a scene and we're out here in plain sight
I can hear them whisper as we pass by
It's a bad sign (bad sign)
Something happens when everybody finds out
See the vultures circling dark clouds
Love's a fragile little flame
It could burn out, it could burn out
'Cause they got the cages, they got the boxes
And guns
They are the hunters, we are the foxes
And we run
Baby, I know places we won't be found
And they'll be chasing their tails trying to track us down
'Cause I, I know places we can hide
I know places, I know places
Lights flash and we'll run for the fences
Let them say what they want, we won't hear it
Loose lips sink ships all the damn time
Not this time
Just grab my hand and don't ever drop it
My love
They are the hunters, we are the foxes
And we run
Baby, I know places we won't be found
And they'll be chasing their tails trying to track us down
'Cause I, I know places we can hide
I know places, I know places
They are the hunters, we are the foxes
And we run
Just grab my hand and don't ever drop it
My love
Baby, I know places we won't be found
And they'll be chasing their tails trying to track us down
'Cause I, I know places we can hide
I know places, I know places
They take their shots, we're bulletproof
(I know places)
And you know for me, it's always you
(I know places)
In the dead of night, your eyes so green
(I know places)
And I know for you, it's always me
(I know places)
The drought was the very worst
When the flowers that we'd grown together died of thirst
It was months and months of back-and-forth
You're still all over me like a wine-stained dress I can't wear anymore
Hung my head as I lost the war
And the sky turned black like a perfect storm
Rain came pouring down
When I was drowning, that's when I could finally breathe
And by morning, gone was any trace of you
I think I am finally clean
There was nothing left to do
When the butterflies turned to dust that covered my whole room
So I punched a hole in the roof
Let the flood carry away all my pictures of you
The water filled my lungs, I screamed so loud
But no one heard a thing
Rain came pouring down
When I was drowning, that's when I could finally breathe
And by morning, gone was any trace of you
I think I am finally clean
I think I am finally clean
Ten months sober, I must admit
Just because you're clean don't mean you don't miss it
Ten months older, I won't give in
Now that I'm clean, I'm never gonna risk it
The drought was the very worst
When the flowers that we'd grown together died of thirst
Rain came pouring down
When I was drowning, that's when I could finally breathe
And by morning, gone was any trace of you
I think I am finally clean
Rain came pouring down
When I was drowning, that's when I could finally breathe
And by morning, gone was any trace of you
And I think I am finally clean
Flashing lights and we
Took a wrong turn and we
Fell down a rabbit hole
You held on tight to me
Cause nothing's as it seems and spinning out of control
Didn't they tell us don't rush into things?
Didn't you flash your green eyes at me?
Haven't you heard what becomes of curious minds?
Didn't it all seem new and exciting?
I felt your arms twistin' round me
I should have slept with one eye open at night
We found Wonderland, you and I got lost in it
And we pretended it could last forever (ey, ey)
We found Wonderland, you and I got lost in it
And life was never worse but never better (ey, ey)
(Ey, ey, ey, ey, ey)
In Wonderland
(Ey, ey, ey, ey, ey)
In Wonderland
(Ey, ey, ey, ey, ey)
In Wonderland
(Ey, ey, ey, ey, ey)
In Wonderland
So we went on our way, too in love to think straight
All alone or so it seemed
But there was strangers watching
And whispers turned to talking
And talking turned to screams, oh
Didn't they tell us don't rush into things
Didn't you flash your green eyes at me
Didn't you calm my fears with a Cheshire cat smile
Didn't it all feel new and exciting
I felt your arms twisting round me
Its all fun and games till somebody loses their mind
But darlin'
We found Wonderland, you and I got lost in it
And we pretended it could last forever (ey, ey)
We found Wonderland, you and I got lost in it
And life was never worse but never better (ey, ey)
(Ey, ey, ey, ey, ey)
In Wonderland
(Ey, ey, ey, ey, ey)
In Wonderland
(Ey, ey, ey, ey, ey)
In Wonderland
(Ey, ey, ey, ey, ey)
In Wonderland
I reached for you but you were gone
I knew I had to go back home
You searched the world for something else
To make you feel like what we had
And in the end in Wonderland
We both went mad
Oh!
We found Wonderland, you and I got lost in it
We pretended it could last forever, last forever (ey, ey)
We found Wonderland, you and I got lost in it (got lost in it)
And life was never worse but never better, never better (ey, ey)
(Ey, ey, ey, ey, ey)
We found Wonderland, you and I got lost in it (in Wonderland)
(Ey, ey, ey, ey, ey)
We pretended it could last forever (in Wonderland)
(Ey, ey, ey, ey, ey)
We found Wonderland, you and I got lost in it (in Wonderland)
(Ey, ey, ey, ey, ey)
And life was never worse but never better
In Wonderland
One look, dark room, meant just for you
Time moved too fast, you play it back
Buttons on a coat, lighthearted joke
No proof, not much, but you saw enough
Small talk, he drives, coffee at midnight
The light reflects the chain on your neck
He says, "Look up" and your shoulders brush
No proof, one touch, you felt enough
You can hear it in the silence, silence, you
You can feel it on the way home, way home, you
You can see it with the lights out, lights out
You are in love, true love
You are in love
Morning, his place, burnt toast, Sunday
You keep his shirt, he keeps his word
And for once you let go of your fears and your ghosts
One step, not much, but it said enough
You kiss on side walks, you fight and you talk
One night he wakes, strange look on his face
Pauses, then says "You're my best friend."
And you knew what it was, he is in love
You can hear it in the silence, silence, you
You can feel it on the way home, way home, you
You can see it with the lights out, lights out
You are in love, true love
And so it goes...
You two are dancing in the snowglobe round and round
And he keeps a picture of you in his office downtown
And you understand now why they lost their minds and fought the wars
And why I spent my whole life trying to put it into words
'Cause you can hear it in the silence
You can feel it on the way home
You can see it with the lights out
You are in love, true love
You are in love!
You can hear it in the silence, silence, you
You can feel it on the way home, way home, you
You can see it with the lights out, lights out
You are in love, true love
You are in love
You can hear it in the silence, silence, you
You can feel it on the way home, way home, you
You can see it with the lights out, lights out
You are in love, true love
You are in love
We're all bored, we're all so tired of everything
We wait for trains that just aren't coming
We show off our different scarlet letters
Trust me, mine is better
We're so young, but we're on the road to ruin
We play dumb but we know exactly what we're doing
We cry tears of mascara in the bathroom
Honey, life is just a classroom
'Cause baby I could build a castle
Out of all the bricks they threw at me
And every day is like a battle
But every night with us is like a dream
Baby we're the new romantics
Come on, come along with me
Heartbreak is the national anthem
We sing it proudly
We're too busy dancing to get knocked off our feet
Baby we're the new romantics
The best people in life are free
We're all here, the lights and noise are blinding
We hang back it's all in the timing
It's poker, you can't see it in my face
But I'm about to play my Ace
We need love but all we want is danger
We team up then switch sides like a record changer
The rumors are terrible and cruel
But honey most of them are true
'Cause baby I could build a castle
Out of all the bricks they threw at me
And every day is like a battle
But every night with us is like a dream
Baby we're the new romantics
Come on, come along with me
Heartbreak is the national anthem
We sing it proudly
We're too busy dancing to get knocked off our feet
Baby we're the new romantics
The best people in life are free
Please take my hand and
Please take me dancing and
Please leave me stranded
It's so romantic, it's so romantic
'Cause baby I could build a castle
Out of all the bricks they threw at me
And every day is like a battle
But every night with us is like a dream
'Cause baby I could build a castle
Out of all the bricks they threw at me
And every day is like a battle
But every night with us is like a dream
Baby we're the new romantics
Come on, come along with me
Heartbreak is the national anthem
We sing it proudly
We're too busy dancing to get knocked off our feet
Baby we're the new romantics
The best people in life are free
Knew he was a killer first time that I saw him
Wondered how many girls he had loved and left haunted
But if he's a ghost, then I can be a phantom
Holdin' him for ransom, some
Some boys are tryin' too hard, he don't try at all though
Younger than my exes, but he act like such a man, so
I see nothing better, I keep him forever
Like a vendetta-ta
I, I, I see how this is gon' go
Touch me and you'll never be alone
I-Island breeze and lights down low
No one has to know
In the middle of the night, in my dreams
You should see the things we do, baby
In the middle of the night, in my dreams
I know I'm gonna be with you
So I take my time
Are you ready for it?
Knew I was a robber first time that he saw me
Stealing hearts and running off and never sayin' sorry
But if I'm a thief, then he can join the heist, and
We'll move to an island, and
And he can be my jailer, Burton to this Taylor
Every love I've known in comparison is a failure
I forget their names now, I'm so very tame now
Never be the same now, now
I, I, I see how this is gon' go
Touch me and you'll never be alone
I-Island breeze and lights down low
No one has to know (no one has to know)
In the middle of the night, in my dreams
You should see the things we do, baby
In the middle of the night in my dreams
I know I'm gonna be with you
So I take my time
Are you ready for it?
Oh, are you ready for it?
Baby, let the games begin
Let the games begin
Let the games begin
Baby, let the games begin
Let the games begin
Let the games begin
I, I, I see how this is gon' go
Touch me and you'll never be alone
I-Island breeze and lights down low
No one has to know
In the middle of the night, in my dreams
You should see the things we do, baby
In the middle of the night, in my dreams
I know I'm gonna be with you
So I take my time
In the middle of the night
Baby, let the games begin
Let the games begin
Let the games begin
Are you ready for it?
Baby, let the games begin
Let the games begin
Let the games begin
Are you ready for it?
Future
I wanna be your end game
I wanna be your first string
I wanna be your A-Team (
whoa, whoa, whoa
I wanna be your end game, end game
Future
Big reputation, big reputation
Ooh, you and me, we got big reputations, ah
And you heard about me, ooh
I got some big enemies (
yeah
Big reputation, big reputation
Ooh, you and me would be a big conversation, ah (
git, git
And I heard about you, ooh (
yeah
You like the bad ones, too
You so dope, don't overdose
I'm so stoked, I need a toast
We do the most, I'm in the Ghost like I'm whippin' a boat
I got a reputation, girl that don't precede me (yeah)
I'm one call away whenever you need me (yeah)
I'm in a G5 (yeah), come to the A-Side (yeah)
I got a bad boy persona, that's what they like (what they like)
You love it, I love it, too 'cause you my type (you my type)
You hold me down, and I protect you with my life
&amp; Future
I don't wanna touch you, I don't wanna be
Just another ex-love, you don't wanna see
I don't wanna miss you (
I don't wanna miss you
Like the other girls do
I don't wanna hurt you, I just wanna be
Drinking on a beach with you all over me
I know what they all say (
I know what they all say
But I ain't tryna play
I wanna be your end game (end game)
I wanna be your first string (first string)
I wanna be your A-Team (A-Team)
I wanna be your end game, end game
Knew her when I was young
Reconnected when we were little bit older, both sprung
I got issues and chips on both of my shoulders
Reputation precedes me, in rumors, I'm knee-deep
The truth is, it's easier to ignore it, believe me
Even when we'd argue, we'd not do it for long
And you understand the good and bad end up in the song
For all your beautiful traits, and the way you do it with ease
For all my flaws, paranoia, and insecurities
I've made mistakes and made some choices, that's hard to deny
After the storm, something was born on the 4th of July
I've passed days without fun, this end game is the one
With four words on the tip of my tongue, I'll never say it
I don't wanna touch you, I don't wanna be
Just another ex-love you don't wanna see
I don't wanna miss you (I don't wanna miss you)
Like the other girls do
I don't wanna hurt you, I just wanna be
Drinking on a beach with you all over me
I know what they all say, yeah
But I ain't tryna play
I wanna be your end game (end game)
I wanna be your first string (wanna be your first string)
I wanna be your A-Team (A-Team)
I wanna be your end game, end game
&amp; Future
Big reputation, big reputation
Ooh, you and me, we got big reputations, ah
And you heard about me, ooh
I got some big enemies
Hey, big reputation, big reputation
Ooh, 
you and me would be a big conversation
, ah
And I heard about you, 
ooh
You like the bad ones, too
I hit you like bang, we tried to forget it, but we just couldn't
And I bury hatchets, but I keep maps of where I put 'em
Reputation precedes me, they told you I'm crazy
I swear I don't love the drama, it loves me
And I can't let you go, your hand prints on my soul
It's like your eyes are liquor, it's like your body is gold
You've been calling my bluff on all my usual tricks
So here's the truth from my red lips
Future,
&amp; Ed Sheeran
I wanna be your end game (end game)
I wanna be your first string (
me and you,
 first string)
I wanna be your A-Team (
be your A-Team now,
 A-Team)
I wanna be your end game, end game
I wanna be your end game (oh, I do)
I wanna be your first string (first string)
I wanna be your A-Team (A-Team)
I wanna be your end game, end game
I never trust a narcissist, but they love me
So I play 'em like a violin
And I make it look oh-so-easy
'Cause for every lie I tell them, they tell me three
This is how the world works
Now all he thinks about is me
I can feel the flames on my skin
Crimson red paint on my lips
If a man talks shit, then I owe him nothing
I don't regret it one bit, 'cause he had it coming
They say I did something bad
Then why's it feel so good?
They say I did something bad
But why's it feel so good?
Most fun I ever had
And I'd do it over and over and over again if I could
It just felt so good, good
I never trust a playboy, but they love me
So I fly 'em all around the world
And I let them think they saved me
They never see it comin', what I do next
This is how the world works
You gotta leave before you get left
I can feel the flames on my skin
He says, "Don't throw away a good thing"
But if he drops my name, then I owe him nothin'
And if he spends my change, then he had it comin'
They say I did something bad
Then why's it feel so good?
They say I did something bad
But why's it feel so good?
Most fun I ever had
And I'd do it over and over and over again if I could
It just felt so good, good
It just felt so good
They're burning all the witches even if you aren't one
They got their pitchforks and proof, their receipts and reasons
They're burning all the witches even if you aren't one
So light me up (light me up), light me up (light me up)
Light me up, go ahead and light me up (light me up)
Light me up (light me up), light me up (light me up)
Light me up (light me up), light me up
They say I did something bad
Then why's it feel so good?
They say I did something bad
But why's it feel so good?
Most fun I ever had
And I'd do it over and over and over again if I could
It just felt so good, good
Oh, you say I did something bad
(You say I did something bad?)
Why's it feel so good, good?
So bad, why's it feel so good?
Why's it feel, why's it feel so good? (bad)
It just felt so good, good
Don't blame me, your love made me crazy
If it doesn't, you ain't doin' it right
Lord, save me, my drug is my baby
I'll be usin' for the rest of my life
I've been breakin' hearts a long time
And toyin' with them older guys
Just playthings for me to use
Something happened for the first time
In the darkest little paradise
Shakin', pacin', I just need you
For you, I would cross the line
I would waste my time
I would lose my mind
They say, "She's gone too far this time"
Don't blame me, your love made me crazy
If it doesn't, you ain't doin' it right
Lord, save me, my drug is my baby
I'll be usin' for the rest of my life
Don't blame me, your love made me crazy
If it doesn't, you ain't doin' it right
Oh, Lord, save me, my drug is my baby
I'll be usin' for the rest of my life
My name is whatever you decide
And I'm just gonna call you mine
I'm insane, but I'm your baby (your baby)
Echoes (echoes) of your name inside my mind
Halo, hiding my obsession
I once was poison ivy, but now I'm your daisy
And baby, for you, I would fall from grace
Just to touch your face
If you walk away
I'd beg you on my knees to stay
Don't blame me, your love made me crazy
If it doesn't, you ain't doin' it right
Lord, save me, my drug is my baby
I'll be usin' for the rest of my life
Don't blame me, your love made me crazy
If it doesn't, you ain't doin' it right
Oh, Lord, save me, my drug is my baby
I'll be usin' for the rest of my life
I get so high, oh!
Every time you're, every time you're lovin' me
You're lovin' me
Trip of my life, oh!
Every time you're, every time you're touchin' me
You're touchin' me
Every time you're, every time you're lovin' me
Oh, Lord, save me
My drug is my baby
I'll be usin' for the rest of my life
Usin' for the rest of my life, oh!
Don't blame me, your love made me crazy
If it doesn't, you ain't doin' it right (doin' it right, no!)
Lord, save me, my drug is my baby
I'll be usin' for the rest of my life, oh
Don't blame me, your love made me crazy
If it doesn't, you ain't doin' it right (you ain't doin' it...)
Oh, Lord, save me, my drug is my baby
I'll be usin' for the rest of my life (I'll be usin', I'll be usin')
I get so high, oh!
Every time you're, every time you're lovin' me
You're lovin' me
Oh, Lord, save me
My drug is my baby
I'll be usin' for the rest of my life
This ain't for the best
My reputation's never been worse, so
You must like me for me?3
We can't make
Any promises now, can we, babe?
But you can make me a drink
Dive bar on the East Side, where you at?
Phone lights up my nightstand in the black
Come here, you can meet me in the back
Dark jeans and your Nikes, look at you
Oh damn, never seen that color blue
Just think of the fun things we could do
'Cause I like you
This ain't for the best
My reputation's never been worse, so
You must like me for me?16
Yeah, I want you
We can't make
Any promises now, can we, babe?
But you can make me a drink
Is it cool that I said all that?
Is it chill that you're in my head?
'Cause I know that it's delicate (delicate)
Is it cool that I said all that?
Is it too soon to do this yet?
'Cause I know that it's delicate
Isn't it? Isn't it? Isn't it? Isn't it?
Isn't it? Isn't it? Isn't it?
Isn't it... delicate?
Third floor on the West Side, me and you
Handsome, you're a mansion with a view
Do the girls back home touch you like I do?
Long night, with your hands up in my hair
Echoes of your footsteps on the stairs
Stay here, honey, I don't wanna share
'Cause I like you
This ain't for the best
My reputation's never been worse, so
You must like me for me?39
Yeah, I want you...
We can't make
Any promises now, can we, babe?
But you can make me a drink
Is it cool that I said all that?
Is it chill that you're in my head?
'Cause I know that it's delicate (delicate)
Is it cool that I said all that?
Is it too soon to do this yet?
'Cause I know that it's delicate
Isn't it? Isn't it? Isn't it? Isn't it?
Isn't it? Isn't it? Isn't it?
Isn't it delicate?
Sometimes I wonder when you sleep
Are you ever dreaming of me?
Sometimes when I look into your eyes
I pretend you're mine, all the damn time
'Cause I like you
Is it cool that I said all that?
Is it chill that you're in my head?
'Cause I know that it's delicate (delicate)
(Yeah, I want you)
Is it cool that I said all that?
Is it too soon to do this yet?
'Cause I know that it's delicate (delicate)
'Cause I like you
Is it cool that I said all that?
Isn't it? Isn't it? Isn't it? Isn't it?
Is it chill that you're in my head?
Isn't it? Isn't it? Isn't it? Isn't it?
'Cause I know that it's delicate
Isn't it? Isn't it? Isn't it? Isn't it?
(Yeah, I want you)
Is it cool that I said all that?
Isn't it? Isn't it? Isn't it? Isn't it?
Is it too soon to do this yet?
Isn't it? Isn't it? Isn't it?
'Cause I know that it's delicate
Isn't it delicate?
I don't like your little games
Don't like your tilted stage
The role you made me play
Of the fool, no, I don't like you
I don't like your perfect crime
How you laugh when you lie
You said the gun was mine
Isn't cool, no, I don't like you (oh)
But I got smarter, I got harder in the nick of time
Honey, I rose up from the dead, I do it all the time
I've got a list of names and yours is in red, underlined
I check it once, then I check it twice, oh!
Ooh, look what you made me do
Look what you made me do
Look what you just made me do
Look what you just made me?16
Ooh, look what you made me do
Look what you made me do
Look what you just made me do
Look what you just made me do
I don't like your kingdom keys
They once belonged to me
You asked me for a place to sleep
Locked me out and threw a feast (what?)
The world moves on, another day, another drama, drama
But not for me, not for me, all I think about is karma
And then the world moves on, but one thing's for sure
Maybe I got mine, but you'll all get yours
But I got smarter, I got harder in the nick of time
Honey, I rose up from the dead, I do it all the time
I've got a list of names and yours is in red, underlined
I check it once, then I check it twice, oh!
Ooh, look what you made me do
Look what you made me do
Look what you just made me do
Look what you just made me?36
Ooh, look what you made me do
Look what you made me do
Look what you just made me do
Look what you just made me do
I don't trust nobody and nobody trusts me
I'll be the actress starring in your bad dreams
I don't trust nobody and nobody trusts me
I'll be the actress starring in your bad dreams
I don't trust nobody and nobody trusts me
I'll be the actress starring in your bad dreams
I don't trust nobody and nobody trusts me
I'll be the actress starring in your bad dreams
(Ooh, look what you made me do
Look what you made me do
Look what you just made me do
Look what you just made me?52
Ooh, look what you made me do
Look what you made me do
Look what you just made me?
"I'm sorry, the old Taylor can't come to the phone right now
"Why? Oh, 'cause she's dead!" (Oh)
Ooh, look what you made me do
Look what you made me do
Look what you just made me do
Look what you just made me?61
Ooh, look what you made me do
Look what you made me do
Look what you just made me do
Look what you just made me do
Ooh, look what you made me do
Look what you made me do
Look what you just made me do
Look what you just made me?69
Ooh, look what you made me do
Look what you made me do
Look what you just made me do
Look what you just made me do
See you in the dark
All eyes on you, my magician
All eyes on us
You make everyone disappear, and
Cut me into pieces
Gold cage, hostage to my feelings
Back against the wall
Trippin', trip-trippin' when you're gone
'Cause we break down a little
But when you get me alone, it's so simple
'Cause baby, I know what you know
We can feel it
And all the pieces fall
Right into place
Getting caught up in a moment
Lipstick on your face
So it goes?17
I'm yours to keep
And I'm yours to lose
You know I'm not a bad girl, but I
Do bad things with you
So it goes?22
Met you in a bar
All eyes on me, your illusionist
All eyes on us
I make all your gray days clear
And wear you like a necklace
I'm so chill, but you make me jealous
But I got your heart
Skippin', skip-skippin' when I'm gone
'Cause we break down a little
But when I get you alone, it's so simple
'Cause baby, I know what you know
We can feel it
And all the pieces fall
Right into place
Getting caught up in a moment
Lipstick on your face
So it goes?39
I'm yours to keep
And I'm yours to lose
You know I'm not a bad girl, but I
Do bad things with you
So it goes?44
Come here, dressed in black now
So, so, so it goes
Scratches down your back now
So, so, so it goes
You did a number on me
But, honestly, baby, who's counting?
I did a number on you
But, honestly, baby, who's counting?
You did a number on me
But, honestly, baby, who's counting?
Who's counting?
(1, 2, 3)
And all the pieces fall (pieces fall)
Right into place
Getting caught up in a moment (caught up, caught up)
Lipstick on your face
So it goes (goes)?61
I'm yours to keep (oh)
And I'm yours to lose (baby)
You know I'm not a bad girl, but I
Do bad things with you
So it goes?66
Come here, dressed in black now
So, so, so it goes
Scratches down your back now
So, so, so it goes
Come here, dressed in black now
So, so, so it goes
Scratches down your back now
So, so, so it goes
Gorgeous
You should take it as a compliment
That I got drunk and made fun of the way you talk
You should think about the consequence
Of your magnetic field being a little too strong
And I got a boyfriend, he's older than us
He's in the club doing I don't know what
You're so cool, it makes me hate you so much
(I hate you so much)
Whiskey on ice, Sunset and Vine
You've ruined my life by not being mine
You're so gorgeous
I can't say anything to your face
'Cause look at your face
And I'm so furious
At you for making me feel this way
But what can I say?
You're gorgeous
You should take it as a compliment
That I'm talking to everyone here but you
And you should think about the consequence
Of you touching my hand in a darkened room
If you've got a girlfriend, I'm jealous of her
But if you're single that's honestly worse
'Cause you're so gorgeous it actually hurts
(Honey, it hurts)
Ocean blue eyes looking in mine
I feel like I might sink and drown and die
You're so gorgeous
I can't say anything to your face
'Cause look at your face
And I'm so furious
At you for making me feel this way
But what can I say?
You're gorgeous
You make me so happy it turns back to sad
There's nothing I hate more than what I can't have
And you are so gorgeous it makes me so mad
You make me so happy it turns back to sad, yeah
There's nothing I hate more than what I can't have
Guess I'll just stumble on home to my cats
Alone
Unless you wanna come along
You're so gorgeous
I can't say anything to your face
'Cause look at your face
And I'm so furious
At you for making me feel this way
But what can I say?
You're gorgeous
You make me so happy it turns back to sad
There's nothing I hate more than what I can't have
And you are so gorgeous it makes me so mad
You're gorgeous
You make me so happy it turns back to sad
There's nothing I hate more than what I can't have
You are so gorgeous it makes me so mad
You're gorgeous
No, nothing good starts in a getaway car
It was the best of times, the worst of crimes
I struck a match and blew your mind
But I didn't mean it
And you didn't see it
The ties were black, the lies were white
In shades of gray in candlelight
I wanted to leave him
I needed a reason
X marks the spot where we fell apart
He poisoned the well, I was lyin' to myself
I knew it from the first Old Fashioned, we were cursed
We never had a shotgun shot in the dark
(Oh!)
You were drivin' the getaway car
We were flyin', but we never get far
Don't pretend it's such a mystery
Think about the place where you first met me
Ridin' in a getaway car
There were sirens in the beat of your heart
I shoulda known I'd be the first to leave
Think about the place where you first met me
In a getaway car, oh-oh-oh
No, they never get far, oh-oh-ahh
No, nothing good starts in a getaway car
It was the great escape, the prison break
The light of freedom on my face
But you weren't thinkin'
And I was just drinkin'
Well, he was runnin' after us, I was screamin', "Go, go, go!"
But with three of us, honey, it's a sideshow
And a circus ain't a love story
And now we're both sorry (we're both sorry)
X marks the spot where we fell apart
He poisoned the well, every man for himself
I knew it from the first Old Fashioned, we were cursed
It hit you like a shotgun shot to the heart
(Oh!)
You were drivin' the getaway car
We were flyin', but we'd never get far
Don't pretend it's such a mystery
Think about the place where you first met me
Ridin' in a getaway car
There were sirens in the beat of your heart
Shoulda' known I'd be the first to leave
Think about the place where you first met me
In a getaway car, oh-oh-oh
No, they never get far, oh-oh-ahh
No, nothing good starts in a getaway car
We were jet-set, Bonnie and Clyde (oh-oh)
Until I switched to the other side
To the other si-i-i-i-ide
It's no surprise I turned you in (oh-oh)
'Cause us traitors never win
I'm in a getaway car
I left you in a motel bar
Put the money in a bag and I stole the keys
That was the last time you ever saw me
(Oh!)
Drivin' the getaway car
We were flyin', but we never get far (don't pretend)
Don't pretend it's such a mystery
Think about the place where you first met me
Ridin' in a getaway car
There were sirens in the beat of your heart (shoulda' known)
Shoulda' known I'd be the first to leave
Think about the place where you first met me
In a getaway car, oh-oh-oh
No, they never get far, oh-oh-ahh
No, nothing good starts in a getaway car
I was ridin' in a getaway car
I was cryin' in a getaway car
I was dyin' in a getaway car
Said goodbye in a getaway car
Ridin' in a getaway car
I was cryin' in a getaway car
I was dyin' in a getaway car
Said goodbye in a getaway car
I'm perfectly fine, I live on my own
I made up my mind, I'm better off bein' alone
We met a few weeks ago
Now you try on callin' me baby, like tryin' on clothes
Salute to me, I'm your American Queen
And you move to me like I'm a Motown beat
And we rule the kingdom inside my room
'Cause all the boys and their expensive cars
With their Range Rovers and their Jaguars
Never took me quite where you do
And all at once, you are the one I have been waiting for
King of my heart, body, and soul, ooh whoa
And all at once, you're all I want, I'll never let you go
King of my heart, body, and soul, ooh whoa
And all at once, I've been waiting, waiting
Ooh whoa, ooh whoa
And all at once, you are the one, I have been waiting, waiting
Body and soul, ooh whoa
And all at once
Late in the night, the city's asleep
Your love is a secret I'm hoping, dreaming, dying to keep
Change my priorities
The taste of your lips is my idea of luxury
Salute to me, I'm your American Queen
And you move to me like I'm a Motown beat
And we rule the kingdom inside my room
(Inside my room, oh)
'Cause all the boys and their expensive cars
With their Range Rovers and their Jaguars
Never took me quite where you do
And all at once, you are the one I have been waiting for
King of my heart, body, and soul, ooh whoa
And all at once, you're all I want, I'll never let you go
King of my heart, body, and soul, ooh whoa
And all at once, I've been waiting, waiting
Ooh whoa, ooh whoa
And all at once, you are the one, I have been waiting (waiting), waiting (waiting)
Body and soul, ooh whoa
And all at once
Is this the end of all the endings?
My broken bones are mending
With all these nights we're spending
Up on the roof with a school girl crush
Drinking beer out of plastic cups
Say you fancy me, not fancy stuff
Baby, all at once, this is enough
And all at once, you are the one I have been waiting for
King of my heart, body, and soul, ooh whoa
And all at once, you are the one I have been waiting for
King of my heart, body, and soul, ooh whoa
And all at once, you're all I want, I'll never let you go
King of my heart (my heart), body, and soul (my soul), ooh whoa
And all at once, I've been waiting, waiting
Ooh whoa, ooh whoa (ooh whoa)
And all at once, 'cause you're the one I have been waiting, waiting
Body and soul, ooh whoa
And all at once
I, I loved you in secret
First sight, yeah, we love without reason
Oh, twenty-five years old
Oh, how were you to know? And
My, my love had been frozen
Deep blue, but you painted me golden
Oh, and you held me close
"Oh, how was I to know? I?,8,2017
Taylor Swift,reputation,Dancing With Our Hands Tied,11,Could've spent forever with your hands in my pockets,9,2017
Taylor Swift,reputation,Dancing With Our Hands Tied,11,Picture of your face in an invisible locket,10,2017
Taylor Swift,reputation,Dancing With Our Hands Tied,11,You said there was nothing in the world that could stop it,11,2017
Taylor Swift,reputation,Dancing With Our Hands Tied,11,I had a bad feeling,12,2017
Taylor Swift,reputation,Dancing With Our Hands Tied,11,And darling"
People started talking, putting us through our paces
I knew there was no one in the world who could take it
I had a bad feeling
But we were dancing
Dancing with our hands tied, hands tied
Yeah, we were dancing
Like it was the first time, first time
Yeah, we were dancing
Dancing with our hands tied, hands tied
Yeah, we were dancing
And I had a bad feeling
But we were dancing
I, I loved you in spite of
Deep fears that the world would divide us
So, baby, can we dance?
Oh, through an avalanche? And
Say, say that we got it
I'm a mess, but I'm the mess that you wanted
Oh, 'cause it's gravity
"Oh, keeping you with me, I?,33,2017
Taylor Swift,reputation,Dancing With Our Hands Tied,11,Could've spent forever with your hands in my pockets,34,2017
Taylor Swift,reputation,Dancing With Our Hands Tied,11,Picture of your face in an invisible locket,35,2017
Taylor Swift,reputation,Dancing With Our Hands Tied,11,You said there was nothing in the world that could stop it,36,2017
Taylor Swift,reputation,Dancing With Our Hands Tied,11,I had a bad feeling,37,2017
Taylor Swift,reputation,Dancing With Our Hands Tied,11,But we were dancing,38,2017
Taylor Swift,reputation,Dancing With Our Hands Tied,11,Dancing with our hands tied"
Yeah, we were dancing
Like it was the first time, first time
Yeah, we were dancing
Dancing with our hands tied, hands tied
Yeah, we were dancing
(Knew we had our hands tied)
And I had a bad feeling
But we were dancing
I'd kiss you as the lights went out
Swaying as the room burned down
I'd hold you as the water rushes in
If I could dance with you again
I'd kiss you as the lights went out
Swaying as the room burned down
I'd hold you as the water rushes in
If I could dance with you again
(Again!)
Dancing with our hands tied, hands tied
(Oh) Yeah, we were dancing
Like it was the first time, first time
Yeah, we were dancing (oh!)
Dancing with our hands tied, hands tied
(Dancing with our hands tied)
Yeah, we were dancing
And I had a bad feeling (had a bad feeling)
But we were dancing
Hands tied, hands tied
(Dancing)
Our secret moments in a crowded room
They got no idea about me and you
There is an indentation in the shape of you
Made your mark on me, a golden tattoo
All of this silence and patience, pining and anticipation
My hands are shaking from holding back from you
Ha, ah, ah
All of this silence and patience, pining and desperately waiting
My hands are shaking from all this
Ah, ha, ha, ha-ah
Say my name and everything just stops
I don't want you like a best friend
Only bought this dress so you could take it off
Take it oh, ha, ha, ha-ah
Carve your name into my bedpost
'Cause I don't want you like a best friend
Only bought this dress so you could take it off
Take it oh, ha, ha, ha-ah
Inescapable, I'm not even gonna try
And if I get burned, at least we were electrified
I'm spilling wine in the bathtub
You kiss my face and we're both drunk
Everyone thinks that they know us
But they know nothing about?24
All of this silence and patience, pining and anticipation
My hands are shaking from holding back from you
Ha, ah, ah
All of this silence and patience, pining and desperately waiting
My hands are shaking from all this
Ah, ha, ha, ha-ah
Say my name and everything just stops
I don't want you like a best friend
Only bought this dress so you could take it off
Take it oh, ha, ha, ha-ah
Carve your name into my bedpost
'Cause I don't want you like a best friend
Only bought this dress so you could take it off
Take it oh, ha, ha...
Ha-ah-ah, ha-ah-ah, ha-ah-ah-ah
Only bought this dress so you could take it off
Ha-ah-ah, ha-ah-ah, ha-ah-ah-ah
Only bought this dress so you could take it off
Flashback when you met me
Your buzzcut and my hair bleached
Even in my worst times, you could see the best of me
Flashback to my mistakes
My rebounds, my earthquakes
Even in my worst lies, you saw the truth in me
And I woke up just in time
Now I wake up by your side
My one and only, my lifeline
I woke up just in time
Now I wake up by your side
My hands shake, I can't explain this
Ah, ha, ha, ha-ah
Say my name and everything just stops...
I don't want you like a best friend
Only bought this dress so you could take it off
Take it oh, ha, ha, ha-ah
Carve your name into my bedpost
'Cause I don't want you like a best friend
Only bought this dress so you could take it off
Take it oh, ha, ha, ha-ah
There is an indentation in the shape of you
Only bought this dress so you could take it off
You made your mark on me, golden tattoo
Only bought this dress so you could take it off
It was so nice throwing big parties
Jump into the pool from the balcony
Everyone swimming in a champagne sea
And there are no rules when you show up here
Bass beat rattling the chandelier
Feeling so Gatsby for that whole year
So why'd you have to rain on my parade?
I'm shaking my head and locking the gates
This is why we can't have nice things, darling
Because you break them
I had to take them away
This is why we can't have nice things, honey
Did you think I wouldn't hear all the things you said about me?
This is why we can't have nice things
It was so nice being friends again
There I was, giving you a second chance
But then you stabbed in the back while shaking my hand
And therein lies the issue
Friends don't try to trick you
Get you on the phone and mind-twist you
And so I took an axe to a mended fence
But I'm not the only friend you've lost lately
If only you weren't so shady
This is why we can't have nice things, darling
Because you break them
I had to take them away
This is why we can't have nice things, honey
Did you think I wouldn't hear all the things you said about me?
This is why we can't have-
Here's a toast to my real friends
They don't care about the he-said-she-said
And here's to my baby
He ain't reading what they call me lately
And here's to my momma
Had to listen to all this drama
And here's to you
'Cause forgiveness is a nice thing to do
Haha, I can't even say it with a straight face
This is why we can't have nice things, darling (darling)
Because you break them
I had to take them away
This is why we can't have nice things, honey
Did you think I wouldn't hear all the things you said about me?
This is why we can't have nice things, darling
(And here's to my real friends)
Because you break them
I had to take them away
(And here's to my baby)
This is why we can't have nice things, darling
(He didn't care about that he-said-she-said)
Did you think I wouldn't hear all the things you said about me?
This is why we can't have nice things
My castle crumbled overnight
I brought a knife to a gunfight
They took the crown, but it's alright
All the liars are calling me one
Nobody's heard from me for months
I'm doin' better than I ever was
'Cause
My baby's fit like a daydream
Walking with his head down
I'm the one he's walking to
So call it what you want, yeah
Call it what you want to
My baby's fly like a jet stream
High above the whole scene
Loves me like I'm brand new
So call it what you want, yeah
Call it what you want to
All my flowers grew back as thorns
Windows boarded up after the storm
He built a fire just to keep me warm
All the drama queens taking swings
All the jokers dressing up as kings
They fade to nothing when I look at him
And I know I make the same mistakes every time
Bridges burn, I never learn
At least I did one thing right
I did one thing right
I'm laughing with my lover, makin' forts under covers
Trust him like a brother
Yeah, you know I did one thing right
Starry eyes sparkin' up my darkest night
My baby's fit like a daydream
Walking with his head down
I'm the one he's walking to
So call it what you want, yeah
Call it what you want to
My baby's fly like a jet stream
High above the whole scene
Loves me like I'm brand new
Call it what you want, call it what you want, call it
So call it what you want, yeah
Call it what you want to
I want to wear his initial on a chain round my neck
Chain round my neck
Not because he owns me
But 'cause he really knows me
Which is more than they can say, I...
I recall late November
Holdin' my breath, slowly I said
"You don't need to save me
But would you run away with me?"
Yes (would you run away?)
My baby's fit like a daydream
Walking with his head down
I'm the one he's walking to
Call it what you want, call it what you want, call it
So call it what you want, yeah
Call it what you want to
My baby's fly like a jet stream
High above the whole scene
Loves me like I'm brand new
Call it what you want, call it what you want, call it
So call it what you want, yeah
Call it what you want to
(Call it what you want, call it)
(Call it what you want, call it what you want, call it)
(Call it what you want, call it what you want, call it)
(Call it what you want, call it what you want, call it)
(Call it what you want, call it what you want, call it)
(Call it what you want, call it what you want, call it)
(Call it what you want, call it what you want, call it)
Call it what you want, yeah
Call it what you want?to
There's glitter on the floor after the party
Girls carrying their shoes down in the lobby
Candle wax and Polaroids on the hardwood floor
You and me from the night before, but
Don't read the last page
But I stay when you're lost, and I'm scared
And you're turning away
I want your midnights
But I'll be cleaning up bottles with you on New Year's Day
You squeeze my hand three times in the back of the taxi
I can tell that it's gonna be a long road
I'll be there if you're the toast of the town, babe
Or if you strike out and you're crawling home
Don't read the last page
But I stay when it's hard, or it's wrong
Or we're making mistakes
I want your midnights
But I'll be cleaning up bottles with you on New Year's Day
Hold on to the memories, they will hold on to you
Hold on to the memories, they will hold on to you
Hold on to the memories, they will hold on to you
And I will hold on to you
Please don't ever become a stranger
Whose laugh I could recognize anywhere
Please don't ever become a stranger
Whose laugh I could recognize anywhere
There's glitter on the floor after the party
Girls carrying their shoes down in the lobby
Candle wax and Polaroids on the hardwood floor
You and me forevermore
Don't read the last page
But I stay when it's hard, or it's wrong
Or we're making mistakes
I want your midnights
But I'll be cleaning up bottles with you on New Year's Day
Hold on to the memories, they will hold on to you
Hold on to the memories, they will hold on to you
Hold on to the memories, they will hold on to you
And I will hold on to you
Please don't ever become a stranger
(To the memories, they will hold on to you)
Whose laugh I could recognize anywhere
(Hold on to the memories, they will hold on to you)
Please don't ever become a stranger
(Hold on to the memories, they will hold on to you)
Whose laugh I could recognize anywhere
(I will hold on to you)
"""
pink_floyd = '''lyrics
"""Moon in both [houses]...""...Scorpio, [Arabian Skies], Libra...""...Pluto was not discovered until 1930...""
Lime and limpid green, a second scene
A fight between the blue you once knew
Floating down, the sound resounds
Around the icy waters underground
Jupiter and Saturn, Oberon, Miranda and Titania
Neptune, Titan, stars can frighten

Blinding signs flap
Flicker, flicker, flicker, blam
Pow, pow
Stairway scare Dan Dare who’s there?

Lime and limpid green, the sound surrounds
The icy waters under
Lime and limpid green, the sound surrounds
The icy waters underground"
"Lucifer Sam, siam cat
Always sitting by your side
Always by your side

That cat’s something I can’t explain

Jennifer Gentle, you’re a witch
You’re the left side, he’s the right side
Oh, no!

That cat’s something I can’t explain

Lucifer, go to sea
Be a hip cat, be a ship’s cat
Somewhere, anywhere

That cat’s something I can’t explain

At night prowling, sifting sand
Hiding around on the ground
He’ll be found when you’re around

That cat’s something I can’t explain"
"There was a king who ruled the land
His Majesty was in command
With silver eyes the scarlet eagle
Showered silver on the people...

Oh, Mother
Tell me more

Why’d’ya have to leave me there
Hanging in my infant air
Waiting?
You only have to read the lines
They’re scribbly black and everything shines

Across the stream with wooden shoes
With bells to tell the king the news
A thousand misty riders climb up
Higher once upon a time
Wandering and dreaming
The words have different meaning
Yes, they did


For all the time spent in that room
The doll’s house, darkness, old perfume
And fairy stories held me high
On clouds of sunlight floating by

Oh, Mother
Tell me more
Tell me more

Aaaaaaaah
Aaaaaaaah
Aaaaaaaah"
"Alone in the clouds all blue
Lying on an eiderdown

Yippee! You can’t see me
But I can you

Lazing in the foggy dew
Sitting on a unicorn

No fair, you can’t hear me
But I can you

Watching buttercups cup the light
Sleeping on a dandelion

Too much, I won’t touch you
But then I might

Screaming through the starlit sky
Traveling by telephone

Hey ho, here we go
Ever so high

Alone in the clouds all blue
Lying on an eiderdown

Yippee! You can’t see me
But I can you"
"TCH TCH
AHH (AHH)
TCH TCH
AHH AHH
Doi doi
AHH AHH
Doi doi
TCH TCH (doi doi)
DOI DOI
TCH TCH AHHHH"
"Doctor, doctor!
I’m in bed (Doctor, doctor)
Achin’ head (Doctor, doctor)
Gold is lead (Doctor, doctor)
Choke on bread (Doctor, doctor)
Underfed (Doctor, doctor)
Gold is lead (Doctor, doctor)
Jesus bled (Doctor, doctor)
Pain is red (Doctor, doctor)
Dark doom
Gruel ghoul, greasy spoon
Used spoon, June bloom


Music seems to help the pain
Seems to motivate the brain
Doctor kindly tell your wife that
I’m alive
Flowers thrive
Realise
Realise
Realise"

"I want to tell you a story
Bout’ a little man, If I can
A gnome named Grimble Crumble
And little gnomes stay in their homes
Eating, sleeping
Drinking their wine

He wore a scarlet tunic
A blue green hood, it looked quite good
He had a big adventure
Amidst the grass, fresh air at last
Wining, dining
Biding his time

And then one day
Hooray!
Another way for gnomes to say
Ooooooh my

Look at the sky, look at the river
Isn’t it good?
Look at the sky, look at the river
Isn’t it good?
Winding, finding places to go

And then one day – hooray!
Another way for gnomes to say
Ooooooh my
Ooooooh my"
"All movement is accomplished in six stages
And the seventh brings return
The seven is the number of the young light
It forms when darkness is increased by one

Change returns success
Going and coming without error
Action brings good fortune
Sunset

The time is with the month of winter solstice
When the change is due to come
Thunder in the other course of heaven
Things cannot be destroyed once and for all

Change returns success
Going and coming without error
Action brings good fortune
Sunset, sunrise

All movement is accomplished in six stages
And the seventh brings return
The seven is the number of the young light
It forms when darkness is increased by one

Change returns success
Going and coming without error
Action brings good fortune
Sunset, sunrise"
"The black and green scarecrow as everyone knows
Stood with a bird on his hat and straw everywhere
He didn’t care

He stood in a field where barley grows

His head did no thinking
His arms didn’t move except when the wind cut up rough
And mice ran around on the ground

He stood in a field where barley grows

The black and green scarecrow is sadder than me
But now he’s resigned to his fate
‘Cause life’s not unkind – he doesn’t mind

He stood in a field where barley grows"
"I’ve got a bike, you can ride it if you like
It’s got a basket, a bell that rings
And things to make it look good
I’d give it to you if I could, but I borrowed it

You’re the kind of girl that fits in with my world
I’ll give you anything, everything if you want things

I’ve got a cloak it’s a bit of a joke
There’s a tear up the front
It’s red and black, I’ve had it for months
If you think it could look good, then I guess it should

You’re the kind of girl that fits in with my world
I’ll give you anything, everything if you want things

I know a mouse, and he hasn’t got a house
I don’t know why I call him Gerald
He’s getting rather old, but he’s a good mouse

You’re the kind of girl that fits in with my world
I’ll give you anything, everything if you want things

I’ve got a clan of gingerbread men
Here a man, there a man, lots of gingerbread men
Take a couple if you wish. They’re on the dish

You’re the kind of girl that fits in with my world
I’ll give you anything, everything if you want things

I know a room of musical tunes
Some rhyme, some ching, most of them are clockwork
Let’s go into the other room and make them work"
"Emily tries but misunderstands (ah ooh)
She’s often inclined to borrow somebody’s dreams ’til tomorrow

There is no other day
Let’s try it another way
You’ll lose your mind and play
Free games for May
See Emily play

Soon after dark, Emily cries (ah ooh)
Gazing through trees in sorrow, hardly a sound ’til tomorrow

There is no other day
Let’s try it another way
You’ll lose your mind and play
Free games for May
See Emily play

Put on a gown that touches the ground (ah ooh)
Float on a river forever and ever, Emily (Emily)

There is no other day
Let’s try it another way
You’ll lose your mind and play
Free games for May
See Emily play"
"Far, far, far, far away – way
People heard him say – say
I will find a way – way
There will come a day – day
Something will be done

Then at last the mighty ship
Descending on a point of flame
Made contact with the human race
At Mildenhall

Now, now, now is the time – time
Time to be – be – be aware

Carter’s father saw him there and
Knew the road revealed to him
The living soul of Hereward the Wake

Oh, my, something in my eye – eye
Something in the sky – sky
Waiting there for me

The outer lock rolled slowly back
The service men were heard to sigh
For there revealed in glowing robes
Was Lucy in the sky

Oh – oh – did you ever know – know
Never ever will they
I cannot say

Summoning his cosmic powers
And glowing slightly from his toes
His psychic emanations flowed"
"Remember a day before today
A day when you were young
Free to play alone with time
Evening never come

Sing a song that can’t be sung
Without the morning’s kiss
Queen – you shall be it if you wish
Look for your king

Why can’t we play today?
Why can’t we stay that way?

Climb your favourite apple tree
Try to catch the sun
Hide from your little brother’s gun
Dream yourself away

Why can’t we reach the sun?
Why can’t we blow the years away?
Blow away
Blow away
Remember
Remember
Remember"
"Little by little the night turns around
Counting the leaves which tremble at dawn
Lotuses lean on each other in yearning
Under the eaves the swallow is resting

Set the controls for the heart of the sun

Over the mountain watching the watcher
Breaking the darkness, waking the grapevine
One inch of love is one inch of shadow
Love is the shadow that ripens the wine

Set the controls for the heart of the sun

The heart of the sun, the heart of the sun
The heart of the sun, the heart of the sun
The heart of the sun, the heart of the sun
The heart of the sun, the heart of the sun
The heart of the sun, the heart of the sun
The heart of the sun, the heart of the sun
The heart of the sun, the heart of the sun

Witness the man who raves at the wall
Making the shape of his question to Heaven
Whether the sun will fall in the evening
Will he remember the lesson of giving?

Set the controls for the heart of the sun

The heart of the sun, the heart of the sun
The heart of the sun, the heart of the sun
The heart of the sun, the heart of the sun
The heart of the sun, the heart of the sun
The heart of the sun, the heart of the sun
The heart of the sun, the heart of the sun
The heart of the sun, the heart of the sun"
"Corporal Clegg had a wooden leg
He won it in the war
In 1944
Corporal Clegg had a medal too
In orange, red, and blue
He found it in the zoo
Dear oh dear oh were they really sad for me?
Dear oh dear oh will they really laugh at me?

Mrs. Clegg, you must be proud of him
Mrs. Clegg, another drop of gin?

Corporal Clegg umbrella in the rain
He’s never been the same
No one is to blame
Corporal Clegg received his medal in a dream
From Her Majesty the Queen
His boots were very clean

Mrs. Clegg, you must be proud of him
Mrs. Clegg, another drop of gin?"

"Marigolds are very much in love
But he doesn’t mind
Picking up his sister, he makes his way into the see-saw land
All the way
She smiles

She goes up while he goes down, down

Sits on a stick in the river
Laughter in his sleep
Sister’s throwing stones, hoping for a hit
He doesn’t know so then

She goes up while he goes down, down

Another time, aaah
Another day, aaah
A brother’s way to leave
Another time, aaah
Another day, aaah

She’ll be selling plastic flowers
On a Sunday afternoon
Picking up weeds, she hasn’t got the time to care
All can see
He’s not there

She grows up for another man, and he’s down

Another time, another day
A brother’s way to leave
Another time, another day
Another time, another day
A brother’s way to leave"
"It’s awfully considerate of you to think of me here
And I’m most obliged to you for making it clear that I’m not here
And I never knew the moon could be so big
And I never knew the moon could be so blue
And I’m grateful that you threw away my old shoes
And brought me here instead dressed in red
And I’m wondering who could be writing this song

I don’t care if the sun don’t shine
And I don’t care if nothing is mine
And I don’t care if I’m nervous with you
I’ll do my loving in the winter

And the sea isn’t green
And I love the Queen
And what exactly is a dream?
And what exactly is a joke?"





"In a churchyard by a river
Lazing in the haze of midday
Laughing in the grasses and the graves
Yellow bird, you are not lone
In singing and in flying on
In laughing and in leaving
Willow weeping in the water
Waving to the river daughters
Swaying in the ripples and the reeds
On a trip to Cirrus Minor
Saw a crater in the sun
A thousand miles of moonlight later"
"I was standing by the Nile
When I saw the lady smile
I would take her out for a while
For a while

Like tears left like a child
How her golden hair was blowing wild
Then she spread her wings to fly
For to fly

Soaring high above the breezes
Going always where she pleases
She will make it to the islands in the sun

I will follow in her shadow
As I watch her from my window
One day I will catch her eye

She is calling from the deep
Summoning my soul to endless sleep
She is bound to drag me down
Drag me down"
"We smile and smile
We smile and smile
Laughter echoes in your eyes

We climb and climb
We climb and climb
Footfalls softly in the pines

We cry and cry
We cry and cry
Sadness passes in a while

We roll and roll
We roll and roll
Help me roll away the stone"

"Heavy hung the canopy of blue
Shade my eyes and I can see you
White is the light that shines through the dress that you wore

She lay in the shadow of the wave
Hazy were the visions of her playing
Sunlight on her eyes but moonshine made her blind ev’ry time

Green is the colour of her kind
Quickness of the eye deceives the mind
Envy is the bond between the hopeful and the damned"
"The path you tread is narrow and the drop is shear and very high
The ravens all are watching from a vantage point nearby
Apprehension creeping like a tube-train up your spine
Will the tightrope reach the end? Will the final couplet rhyme?

And it’s high time, Cymbaline
It’s high time, Cymbaline
Please, wake me

A butterfly with broken wings is falling by your side
The ravens all are closing in, there’s nowhere you can hide
Your manager and agent are both busy on the phone
Selling coloured photographs to magazines back home

And it’s high time, Cymbaline
It’s high time, Cymbaline
Please, wake me

The lines converging where you stand
They must have moved the picture plane
The leaves are heavy around your feet
You hear the thunder of the train
And suddenly it strikes you that they’re moving into range
And Doctor Strange is always changing size

And it’s high time! (high time), Cymbaline
It’s high time, Cymbaline
Please, wake me

And it’s high time, Cymbaline
It’s high time, Cymbaline
Please, wake me"
"I’m so afraid
Of all the mistakes that I’ve made
Shaking every time that I awake
I feel like a cardboard cut-out man

So build me a time
When the characters rhyme
And the story line is kind

I’ve aged and aged since the first page
I’ve lived every line that you wrote
Take me down, take me down
From the shelf above your head

And build me a time
When the characters rhyme
And the story line is kind

I live where I’m left
On the shelf like the rest
And the epilogue reads like a sad song
Please pick up your camera
And use me again

And build me a time
When the characters rhyme
And the storyline is kind
Yeaaaah!"
"Pass the tequila, Manuel
(glug, snort)
Listen, gringo, laugh at my lisp and I kill you
I think
This Spanish music
It sets my soul on fire
Lovely señorita
Your eyes are like stars
Your teeth are like pearls
Your ruby lips"
"""Moon in both [houses]...""...Scorpio, [Arabian Skies], Libra...""...Pluto was not discovered until 1930...""
Lime and limpid green, a second scene
A fight between the blue you once knew
Floating down, the sound resounds
Around the icy waters underground
Jupiter and Saturn, Oberon, Miranda and Titania
Neptune, Titan, stars can frighten

Blinding signs flap
Flicker, flicker, flicker, blam
Pow, pow
Stairway scare Dan Dare who’s there?

Lime and limpid green, the sound surrounds
The icy waters under
Lime and limpid green, the sound surrounds
The icy waters underground"
Careful with that axe, Eugene
"Little by little the night turns around
Counting the leaves which tremble at dawn
Lotuses lean on each other in yearning
Under the eaves the swallow is resting

Set the controls for the heart of the sun

Over the mountain watching the watcher
Breaking the darkness, waking the grapevine
One inch of love is one inch of shadow
Love is the shadow that ripens the wine

Set the controls for the heart of the sun

The heart of the sun, the heart of the sun
The heart of the sun, the heart of the sun
The heart of the sun, the heart of the sun
The heart of the sun, the heart of the sun
The heart of the sun, the heart of the sun
The heart of the sun, the heart of the sun
The heart of the sun, the heart of the sun

Witness the man who raves at the wall
Making the shape of his question to Heaven
Whether the sun will fall in the evening
Will he remember the lesson of giving?

Set the controls for the heart of the sun

The heart of the sun, the heart of the sun
The heart of the sun, the heart of the sun
The heart of the sun, the heart of the sun
The heart of the sun, the heart of the sun
The heart of the sun, the heart of the sun
The heart of the sun, the heart of the sun
The heart of the sun, the heart of the sun"


"“Icy wind of night be gone this is not your domain”
In the sky a bird was heard to cry
Misty morning whisperings and gentle stirring sounds
Belied the deathly silence that lay all around

Hear the lark and harken to the barking of the dog fox
Gone to ground
See the splashing of the kingfisher flashing to the water
And a river of green is sliding unseen beneath the trees
Laughing as it passes through the endless summer, making for the sea

In the lazy water meadow I lay me down
All around me golden sun flakes settle on the ground
Basking in the sunshine of a bygone afternoon
Bringing sounds of yesterday into this city room

Hear the lark and harken to the barking of the dog fox
Gone to ground
See the splashing of the kingfisher flashing to the water
And a river of green is sliding unseen beneath the trees
Laughing as it passes through the endless summer, making for the sea

In the lazy water meadow I lay me down
All around me golden sun flakes covering the ground
Basking in the sunshine of a bygone afternoon
Bringing sounds of yesterday into my city room

Hear the lark and harken to the barking of the dog fox
Gone to ground
See the splashing of the kingfisher flashing to the water
And a river of green is sliding unseen beneath the trees
Laughing as it passes through the endless summer, making for the sea"
"Aye an’ a bit of Mackeral settler rack and ruin ran it doon by the haim, ‘ma place well I slapped me and I slapped it doon in the side and I cried, cried, cried
The fear a fallen down taken never back the raize and then Craig Marion fet out wi’ ye Claymore out mi pocket a’ ran doon, doon the middin stain picking the fiery horde that was fallen around ma feet
Never he cried, never shall it get me alive
Ye rotten hound of the burnie crew. Well I snatched fer the blade O my claymore cut and thrust and I fell doon before him round his feet
Aye!
(That was pretty avant-garde, wasn’t it?)
A roar he cried frae the bottom of his heart that I would nay fall but as dead, dead as ‘a can be by his feet; de ya ken?
…and the wind cried Mary
Thank you"
"Following the path as it leads towards
The darkness in the north
Weary stranger’s faces show their sympathy
They’ve seen that hope before

And if you want to stay for a little bit
Rest your aching limbs for a little bit
For you the night is beckoning
And now you can’t delay
You hear the night birds calling you
But you can’t catch the words they say
Close your ears and eyes, be on your way

Mist is swirling, creatures crawling
Hear the roar get louder in your ears
You know the folly was your own
But the force behind can’t conquer all you fears

And if you want to stay for a little bit
Rest your aching limbs for a little bit
For you the night is beckoning
And now you can’t delay
You hear the night birds calling you
But you can’t catch the words they say
Close your ears and eyes, be on your way

Throw your thoughts back many years
To the time when love was life with every morning
Perhaps a day will come
When the lights will be as clear as on that morning

And if you want to stay for a little bit
Rest your aching limbs for a little bit
For you the night is beckoning
And now you can’t delay
You hear the night birds calling you
But you can’t catch the words they say
Close your ears and eyes, be on your way"

"""Here is a loud announcement""

""Silence in the studio!"""
"If I were a swan, I’d be gone
If I were a train, I’d be late
And if I were a good man
I’d talk with you more often than I do

If I were asleep, I could dream
If I were afraid, I could hide
If I go insane
Please don’t put your wires in my brain

If I were the moon, I’d be cool
If I were a rule, I would bend
If I were a good man
I’d understand the spaces between friends

If I were alone, I would cry
And if I were with you, I’d be home and dry
And if I go insane
Will you still let me join in with the game?

If I were a swan, I’d be gone
If I were a train, I’d be late again
If I were a good man
I’d talk with you more often than I do"
"
Would you like to say something before you leave?

Perhaps you’d care to state exactly how you feel

We say goodbye before we’ve said hello

I hardly even like you, I shouldn’t care at all

We met just six hours ago, the music was too loud

From your bed I gained a day and lost a bloody year


And I would like to know:

How do you feel?

How do you feel? Oh

How do you feel?

How do you feel? Oh


Paaaaaa pa-pap paaaaaaa

Pa-pa paaaa pa-pa pap pa paaaaa

Pa pap pa paaaa


Not a single word was said, the night still hid our fears

Occasionally you showed a smile but what was the need

I felt the cold far too soon in a room of 95

My friends are lying in the sun, I wish that I was there

Tomorrow brings another town another girl like you

Have you time before you leave to greet another man?


Just you let me know:

How do you feel?

How do you feel? Oh

How do you feel?

How do you feel? Oh


Paaaaaa pa paaaaaaa

Pa-pa paaaa pa-pa pa pa pa-pa pa-pa pap paaaaa

Pap pa pa-pap paaaa


Goodbye to you

Charlotte Pringle’s due

I’ve had enough

For one day
"
"When the fat old sun in the sky is falling
Summer evening birds are calling
Summer Sunday and a year
The sound of music in my ears

Distant bells, new mown grass smells
Song sweet
By the river holding hands
Roll me up and lay me down

And if you see, don’t make a sound
Pick your feet up off the ground
And if you hear as the warm night falls
The silver sound from a tongue so strange
Sing to me, sing to me

When that fat old sun in the sky is falling
Summer evening birds are calling
Children’s laughter in my ears
The last sunlight disappears

And if you see, don’t make a sound
Pick your feet up off the ground
And if you hear as the warm night falls
The silver sound from a tongue so strange
Sing to me, sing to me

When that fat old sun in the sky is falling"
"
Oh, uh, me flakes, then uh, scrambled eggs, bacon, sausages, tomatoes... toast, coffee... marmalade, I like marmalade. Yes, porridge is nice. Any cereal, I like all cereals... oh God. Kickoff is 10am


Breakfast in Los Angeles, macrobiotic stuff


I don’t mind a barrack where I can bury my stuff in

I got a terrible back. When I work, it hurts me

...it’s ready for the gig

I don’t know

This electrical stuff I can’t bother with it so...

All my head’s a blank

"
One of these days, I’m going to cut you into little pieces
"A cloud of eiderdown
Draws around me
Softening a sound

Sleepy time, when I lie
With my love by my side
And she’s breathing low

And the candle dies

When night comes down, you lock the door
The book falls to the floor
As darkness falls, the waves roll by
The seasons change, the wind is warm

Now wakes the owl, now sleeps the swan
Behold a dream, the dream is gone
Green fields, a cold rain is falling
In a golden dawn


And deep beneath the ground
The early morning sounds
And I go down

Sleepy time, when I lie
With my love by my side
And she’s breathing low

And I rise, like a bird
In the haze, when the first rays
Touch the sky
And the night winds die"
"You say the hill’s too steep to climb
Chiding
You say you’d like to see me try
Climbing
You pick the place and I’ll choose the time

And I will climb that hill in my own way
Just wait a while for the right day
And as I rise above the tree line and the clouds
I look down, hearing the sound of the things you’ve said today

Fearlessly the idiot faced the crowd
Smiling
Merciless the magistrate turns ’round
Frowning
And who’s the fool who wears the crown?

And go down in your own way
And every day is the right day
And as you rise above the fear-lines in his brow
You look down, hearing the sound of the faces in the crowd

Walk on, walk on, with hope in your heart
And you’ll never walk alone
You’ll never walk alone
Liverpool! Liverpool!"
"As I reach for a peach, slide a rind down behind
The sofa in San Tropez
Breakin’ a stick with a brick on the sand
Ridin’ a wave in the wake of an old sedan
Sleepin’ alone in the drone of the darkness
Scratched by the sand that fell from my love
Deep in my dreams and I still hear her callin’

“If you’re alone, I’ll come ho-ho-home”

Backward and homebound, the pigeon, the dove
Gone with the wind and the rain, on an airplane
Born in a home with no silver spoon
I’m drinking champagne like a good tycoon
Sooner than wait for a break in the weather
I’ll gather my far-flung thoughts together
Speeding away on the wind to a new day

If you’re alone, I’ll come ho-ho-home

And I pause for a while by a country stile
And listen to the things they say
Diggin’ for gold in a hole in my hand
Open a book, take a look at the way things stand
And you’re leading me down to the place by the sea
I hear your soft voice calling to me
Making a date for later by phone

And if you’re alone, I’ll come ho-ho-home"
"I was in the kitchen
Seamus, that’s the dog, was outside
Well, I was in the kitchen
Seamus, my old hound, was outside
Well you know, the sun sinks slowly
But my old hound dog sat right down and cried"
"Overhead the albatross hangs motionless upon the air
And deep beneath the rolling waves in labyrinths of coral caves
The echo of a distant time comes willowing across the sand
And everything is green and submarine

And no one showed us to the land
And no one knows the where’s or why’s
But something stirs and something tries
And starts to climb towards the light

Strangers passing in the street
By chance two separate glances meet
And I am you and what I see is me
And do I take you by the hand
And lead you through the land
And help me understand the best I can?

And no one calls us to move on
And no one forces down our eyes
No one speaks and no one tries
No one flies around the sun


Cloudless every day you fall
Upon my waking eyes
Inviting and inciting me to rise
And through the window in the wall
Come streaming in on sunlight wings
A million bright ambassadors of morning

And no one sings me lullabies
And no one makes me close my eyes
So I throw the windows wide
And call to you across the sky"


"Bridges burning gladly merging with the shadow
Flickering between the lines
Stolen moments floating softly on the air
Born on wings of fire and climbing higher

Ancient bonds are breaking
Moving on and changing sides
Dreaming of a new day
Cast aside the other way
(Magic vision stirring
Kindled by and burning
Flames rise in her eyes)

The door stands ajar
The walls that once were high
Beyond the gilded cage
Beyond the reach of ties
The moment is at hand
She breaks the golden band"
"Come on, my friends
Let’s make for the hills
They say there’s gold and I’m looking for thrills
You can get your hands on whatever we find
Because I’m only coming along for the ride

Well, you go your way
I’ll go mine
I don’t care if we get there on time
Everybody’s searching for something, they say
I’ll get my kicks on the way

Over the mountains, across the sea
Who knows what will be waiting for me?
I could sail forever to strange sounding names
Faces of people and places don’t change

All I have to do is just close my eyes
To see the seagulls wheeling in those far distant skies
All I want to tell you, all I want to say
Is count me in on the journey
Don’t expect me to stay"
"Heaven sent the promised land

Looks alright from where I stand

’Cause I’m the man on the outside looking in

Waiting on the first step

Show me where the key is kept

Point me down the right line because it’s time


To let me in from the cold

Turn my lead into gold

’Cause there’s a chill wind blowing in my soul

And I think I’m growing old


Flash the readies

Wot’s… uh-the deal?

Got to make it to the next meal

Try to keep up with the turning of the wheel

Mile after mile

Stone after stone

Turn to speak but you’re alone

Million miles from home, you’re on your own


So let me in from the cold

Turn my lead into gold

Cause there’s a chill wind blowing in my soul

And I think I’m growing old


Fire bright by candlelight

And her by my side

And if she prefers we will never stir again

Someone sent the promised land

And I grabbed it with both hands

Now I’m the man on the inside looking out


Hear me shout""Come on in !""

""What’s the news and where’ ve you been?""

Cause there’s no wind left in my soul

And I’ve grown old
"

"
You shout in your sleep

Perhaps the price is just too steep

Is your conscience at rest

If once put to the test?

You awake with a start

To just the beating of your heart

Just one man beneath the sky

Just two ears, just two eyes


You set sail across the sea

Of long past thoughts and memories

Childhood’s end, your fantasies

Merge with harsh realities

And then as the sail is hoist

You find your eyes are growing moist

All the fears never voiced

Say you have to make your final choice


Who are you and who am I

To say we know the reason why?

Some are born; some men die

Beneath one infinite sky

There’ll be war, there’ll be peace

But everything one day will cease

All the iron turned to rust;

All the proud men turned to dust

And so all things, time will mend

So this song will end
"
"One, two, free, four!
The memories of a man in his old age
Are the deeds of a man in his prime
You shuffle in gloom of the sickroom
And talk to yourself as you die
Life is a short, warm moment
And death is a long cold rest
You get your chance to try in the twinkling of an eye:
Eighty years, with luck, or even less
So all aboard for the American tour
And maybe you’ll make it to the top
And mind how you go, and I can tell you, ’cause I know
You may find it hard to get off
You are the angel of death
And I am the dead man’s son
And he was buried like a mole in a fox hole
And everyone is still on the run
And who is the master of fox hounds?
And who says the hunt has begun?
And who calls the tune in the courtroom?
And who beats the funeral drum?
The memories of a man in his old age
Are the deeds of a man in his prime
You shuffle in gloom in the sickroom
And talk to yourself as you die"
"Stay and help me to end the day
And if you don’t mind
We’ll break a bottle of wine
Stick around and maybe we’ll put one down
’Cause I wanna find what lies behind those eyes

Midnight blue
Burning gold
A yellow moon
Is growing cold

I rise, looking through my morning eyes
Surprised to find you by my side
Rack my brain to try to remember your name
To find the words to tell you good-bye

Morning dues
Newborn day
Midnight blue
Turned to gray


Midnight blue
Burning gold
A yellow moon
Is growing cold"

"*Heartbeat*

I’ve been mad for fucking years
Absolutely years, been over the edge for yonks
Been working me buns off for bands
I’ve always been mad, I know I’ve been mad
Like the most of us have
Very hard to explain why you’re mad
Even if you’re not mad
Hahahahahahaha!
Ah-ah-ah..."
"Breathe, breathe in the air
Don’t be afraid to care
Leave but don’t leave me
Look around and choose your own ground

For long you live and high you fly
And smiles you’ll give and tears you’ll cry
And all you touch and all you see
Is all your life will ever be

Run, rabbit, run
Dig that hole, forget the sun
And when at last the work is done
Don’t sit down, it’s time to dig another one

For long you live and high you fly
But only if you ride the tide
And balanced on the biggest wave
You race towards an early grave"
"Have your baggage and your passports ready and then follow the green line to customs and immigration. BA flight 215 to Rome, Cairo and Lagos

Live for today, gone tomorrow. That’s me
*Laughs*"
"Ticking away the moments that make up the dull day
Fritter and waste the hours in an offhand way
Kicking around on a piece of ground in your hometown
Waiting for someone or something to show you the way
Tired of lying in the sunshine, staying home to watch the rain
You are young and life is long and there is time to kill today
And then, one day, you find, ten years have got behind you
No one told you when to run, you missed the starting gun


And you run, and you run to catch up with the sun, but it’s sinking
Racing around to come up behind you again
The sun is the same in a relative way, but you’re older
Shorter of breath, and one day closer to death
Every year is getting shorter, never seem to find the time
Plans that either come to naught or half a page of scribbled lines
Hanging on in quiet desperation is the English way
The time is gone, the song is over, thought I’d something more to say


Home, home again
I like to be here when I can
And when I come home cold and tired
It’s good to warm my bones beside the fire
Far away across the field
The tolling of the iron bell
Calls the faithful to their knees
To hear the softly spoken magic spells"
"I am not frightened of dying
Any time will do, I don’t mind
Why should I be frightened of dying?
There’s no reason for it, you’ve gotta go sometime

Oh-oh, oh-oh, oh, oh-oh-oh
Oh, oh-oh-oh, oh, oh
Oh-oh, oh-oh, oh, oh-oh-oh
Oh-oh-oh-oh
Oh, oh, oh, oh
Ah-oh, ah-oh-oh
Ah-ah, ah-ah, ah-ah, ah-ah, ah-oh, oh-oh
Oh, oh-oh
Oh, oh-oh
Oh, oh-oh
Ah-ah, ah-ah, ah-ah, ah-ah, ah-oh

I never said I was frightened of dying

Ooh-ooh, ooh, ooh, oh, oh-oh-oh-ah
Ah-ah-ah-ah-eah-eah-eah
Oh, oh, oh, oh-oh, oh
Oh, oh-oh, oh-oh, oh-oh, oh-ooh
Oh, oh-oh, oh-oh, oh-oh, oh-ooh
Oh, oh-oh"
"Money, get away
You get a good job with more pay and you’re okay
Money, it’s a gas
Grab that cash with both hands and make a stash
A new car, caviar, four-star daydream
Think I’ll buy me a football team

Money, get back
I’m alright, Jack, keep your hands off of my stack
Money, it’s a hit
And don’t give me that do-goody-good bullshit
I’m in the high-fidelity first class travelling set
And I think I need a Lear jet



Money, it’s a crime
Share it fairly, but don’t take a slice of my pie
Money, so they say
Is the root of all evil today
But if you ask for a rise, it’s no surprise
That they’re giving none away

Away, away, away
Away, away, away
Away, ooh...

- Yeah -- (chuckles) -- I was in the right!
- Yes, absolutely in the right!
- I certainly was in the right!
- Yeah, I was definitely in the right; that geezer was cruising for a bruising...
- Yeah
- Why does anyone do anything?
- I don’t know, I was really drunk at the time...
- I was just telling him it was in, he could get it in number two. He was asking why it wasn’t coming up on fader eleven. After, I was yelling and screaming and telling him why it wasn’t coming up on fader eleven. It came to a heavy blow, which sorted the matter out"
"Us (Us, us, us, us, us) and them (Them, them, them, them)
And after all we’re only ordinary men
Me (Me, me, me, me, me) and you (You, you, you, you, you)
God only knows it’s not what we would choose to do
""Forward"" he cried from the rear
And the front rank died
And the general sat and the lines on the map
Moved from side to side

Black (Black, black, black, black) and blue (Blue, blue, blue, blue)
And who knows which is which and who is who
Up (Up, up, up, up, up) and down (Down, down, down, down)
And in the end it’s only round and round, and round
""Haven’t you heard it’s a battle of words?""
The poster bearer cried
""Listen, son,"" said the man with the gun
""There’s room for you inside""

I mean, they’re not gonna kill ya
So if you give ’em a quick short, sharp, shock
They won’t do it again
Dig it? I mean he get off lightly
’Cause I would’ve given him a thrashing
I only hit him once!
It was only a difference of opinion
But really, I mean good manners don’t cost nothing do they, eh?


Down (Down, down, down, down) and out (Out, out, out, out)
It can’t be helped but there’s a lot of it about
With (With, with, with, with), without
And who’ll deny it’s what the fighting’s all about?
Out of the way, it’s a busy day
I’ve got things on my mind
For the want of the price of tea and a slice
The old man died"

"The lunatic is on the grass
The lunatic is on the grass
Remembering games and daisy chains and laughs
Got to keep the loonies on the path
The lunatic is in the hall
The lunatics are in my hall
The paper holds their folded faces to the floor
And every day the paperboy brings more

And if the dam breaks open many years too soon
And if there is no room upon the hill
And if your head explodes with dark forebodings too
I’ll see you on the dark side of the moon

The lunatic is in my head (Hahahahahahaha!)
The lunatic is in my head
You raise the blade
You make the change
You rearrange me till I’m sane
You lock the door
And throw away the key
And there’s someone in my head but it’s not me

And if the cloud bursts, thunder in your ear
You shout and no one seems to hear
And if the band you’re in starts playing different tunes
I’ll see you on the dark side of the moon

I can’t think of anything to say except
Hahahahahahaha!
I think it’s marvellous!
Hahaha..."
"All that you touch and all that you see
All that you taste, all you feel
And all that you love and all that you hate
All you distrust, all you save
And all that you give and all that you deal
And all that you buy, beg, borrow, or steal
And all you create and all you destroy
And all that you do and all that you say
And all that you eat and everyone you meet (Everyone you meet)
And all that you slight and everyone you fight
And all that is now and all that is gone
And all that’s to come and everything under the sun is in tune
But the sun is eclipsed by the moon

There is no dark side in the moon really
Matter of fact it’s all dark
*Heartbeat*"
"Remember when you were young
You shone like the Sun

Shine on, you crazy diamond

Now there’s a look in your eyes
Like black holes in the sky

Shine on, you crazy diamond

You were caught in the crossfire of childhood and stardom
Blown on the steel breeze
Come on, you target for faraway laughter
Come on, you stranger, you legend, you martyr, and shine

You reached for the secret too soon
You cried for the Moon

Shine on, you crazy diamond

Threatened by shadows at night
And exposed in the light

Shine on (Shine on), you crazy diamond (You crazy diamond)

Well, you wore out your welcome with random precision
Rode on the steel breeze
Come on, you raver, you seer of visions
Come on, you painter, you piper, you prisoner, and shine"
"Welcome, my son
Welcome to the machine
Where have you been?
It’s alright, we know where you’ve been
You’ve been in the pipeline, filling in time
Provided with toys and ’Scouting for Boys’
You bought a guitar to punish your ma
And you didn’t like school
And you know you’re nobody’s fool
So welcome to the machine


Welcome, my son
Welcome to the machine
What did you dream?
It’s alright, we told you what to dream
You dreamed of a big star
He played a mean guitar
He always ate in the Steak Bar
He loved to drive in his Jaguar
So welcome to the machine"
"Come in here, dear boy, have a cigar, you’re gonna go far
You’re gonna fly high, you’re never gonna die
You’re gonna make it if you try, they’re gonna love you
Well, I’ve always had a deep respect an’ I mean that most sincerely
The band is just fantastic, that is really what I think
Oh, by the way, which one’s Pink?

And did we tell you the name of the game, boy?
We call it riding the gravy train

We’re just knocked out, we heard about the sell-out
You gotta get an album out, you owe it to the people
We’re so happy we can hardly count
Everybody else is just green, have you seen the chart?
It’s a hell of a start, it could be made into a monster
If we all pull together as a team

And did we tell you the name of the game, boy?
We call it riding the gravy train"
"— And disciplinary remains mercifully
Yes and um, I’m with you Derek, this star nonsense
Yes, yes
Now which is it?
I am sure of it


So, so you think you can tell
Heaven from Hell
Blue skies from pain
Can you tell a green field
From a cold steel rail
A smile from a veil
Do you think you can tell?

Did they get you to trade
Your heroes for ghosts
Hot ashes for trees
Hot air for a cool breeze
Cold comfort for change
Did you exchange
A walk-on part in the war
For a lead role in a cage?

How I wish, how I wish you were here
We’re just two lost souls, swimming in a fish bowl
Year after year
Running over the same old ground
What have we found?
The same old fears
Wish you were here"
"Nobody knows where you are
How near or how far

Shine on you crazy diamond

Pile on many more layers
And I’ll be joining you there

Shine on you crazy diamond

And we’ll bask in the shadow of yesterday’s triumph
And sail on the steel breeze
Come on, you boy child, you winner and loser
Come on, you miner for truth and delusion, and shine!"
"If you didn’t care what happened to me
And I didn’t care for you
We would zigzag our way through the boredom and pain
Occasionally glancing up through the rain
Wondering which of the buggers to blame
And watching for pigs on the wing"
"You got to be crazy, you gotta have a real need
You gotta sleep on your toes and when you’re on the street
You got to be able to pick out the easy meat with your eyes closed
And then moving in silently, down wind and out of sight
You got to strike when the moment is right without thinking
And after a while, you can work on points for style
Like the club tie, and the firm handshake
A certain look in the eye and an easy smile
You have to be trusted by the people that you lie to
So that when they turn their backs on you
You’ll get the chance to put the knife in

You gotta keep one eye looking over your shoulder
You know, it’s going to get harder, and harder, and harder
As you get older
Yeah, and in the end you’ll pack up and fly down south
Hide your head in the sand
Just another sad old man
All alone and dying of cancer


And when you lose control, you’ll reap the harvest you have sown
And as the fear grows, the bad blood slows and turns to stone
And it’s too late to lose the weight you used to need to throw around
So have a good drown, as you go down all alone
Dragged down by the stone

(Stone, stone, stone...)

Gotta admit that I’m a little bit confused
Sometimes it seems to me as if I’m just being used
Gotta stay awake, gotta try and shake off this creeping malaise
If I don’t stand my own ground, how can I find my way out of this maze
Deaf, dumb and blind, you just keep on pretending
That everyone’s expendable, and no one has a real friend
And it seems to you the thing to do would be to isolate the winner
Everything’s done under the sun
But you believe at heart everyone’s a killer


Who was born in a house full of pain
Who was trained not to spit in the fan
Who was told what to do by the man
Who was broken by trained personnel
Who was fitted with collar and chain
Who was given a pat on the back
Who was breaking away from the pack
Who was only a stranger at home
Who was ground down in the end
Who was found dead on the phone
Who was dragged down by the stone
Who was dragged down by the stone"
"*Pig snorts*

Big man, pig man
Haha, charade you are
Wooh!
You well-heeled big wheel
Haha, charade you are
And when your hand is on your heart
You’re nearly a good laugh, almost a joker
With your head down in the pig bin
Sayin’, ""Keep on digging""
Pig stain on your fat chin
What do you hope to find
Down in the pig mine?

You’re nearly a laugh
You’re nearly a laugh, but you’re really a cry

Bus stop rat bag
Haha, charade you are
You fucked up old hag
Haha, charade you are
You radiate cold shafts of broken glass
You’re nearly a good laugh
Almost worth a quick grin
You like the feel of steel
You’re hot stuff with a hatpin
And good fun with a handgun

You’re nearly a laugh
You’re nearly a laugh, but you’re really a cry


Hey you, Whitehouse
Haha, charade you are
You house proud town mouse
Haha, charade you are
You’re tryin’ to keep our feelings off the street
You’re nearly a real treat
All tight lips and cold feet
And do you feel abused?
You! Gotta stem the evil tide
And keep it all on the inside

Mary, you’re nearly a treat
Mary, you’re nearly a treat, but you’re really a cry"
"Harmlessly passing your time in the grassland away
Only dimly aware of a certain unease in the air
You better watch out
There may be dogs about
I’ve looked over Jordan, and I have seen
Things are not what they seem

What do you get for pretending the danger’s not real
Meek and obedient, you follow the leader
Down well trodden corridors into the valley of steel
What a surprise!
A look of terminal shock in your eyes
Now things are really what they seem
No, this is no bad dream

(stone, stone, stone...)
The Lord is my shepherd, I shall not want
He makes me down to lie
Through pastures green He leadeth me the silent waters by
With bright knives He releaseth my soul
He maketh me to hang on hooks in high places
He converteth me to lamb cutlets
For lo, He hath great power, and great hunger
When cometh the day we lowly ones
Through quiet reflection, and great dedication
Master the art of karate
Lo, we shall rise up
And then we’ll make the bugger’s eyes water

Bleating and babbling we fell on his neck with a scream
Wave upon wave of demented avengers
March cheerfully out of obscurity into the dream
Have you heard the news?
The dogs are dead!
You better stay home
And do as you’re told
Get out of the road if you want to grow old"
"You know that I care what happens to you
And I know that you care for me too
So I don’t feel alone or the weight of the stone
Now that I’ve found somewhere safe to bury my bones
And any fool knows a dog needs a home
A shelter from pigs on the wing"
"
Ooh, babe, don’t leave me now


Don’t say it’s the end of the road

Remember the flowers I sent

I need you, babe

To put through the shredder in front of my friends


Oh, babe, don’t leave me now


How could you go?

When you know how I need you

(Need you, need you, need you, need you, need you, need you)

To beat to a pulp on a Saturday night


Oh, babe, don’t leave me now


How can you treat me this way?

Running away

Ooh, babe, why are you running away?


Ooh, babe

Ooh, babe

Ooh, babe

Ooh, ooh

Argh!
"
"...we came in?

(Ah, ah)
So ya thought ya might like to go to the show
(Doo, doo, doo, doo)
To feel the warm thrill of confusion, that space cadet glow
(Doo, doo, doo, doo)
Tell me is something eluding you, sunshine?
Is this not what you expected to see?
If you wanna find out what’s behind these cold eyes
You’ll just have to claw your way through this disguise

Lights!
Roll the sound effects!
Action!
Drop it, drop it on ’em
Drop it on them!

*Bomber’s flying*
*Baby crying*"
"Momma loves her baby
And daddy loves you too
And the sea may look warm to you, babe
And the sky may look blue
Ooh ooh ooh ooh, babe
Ooh ooh ooh, baby blue
Ooh ooh ooh ooh
Ooh ooh, babe

If you should go skating
On the thin ice of modern life
Dragging behind you the silent reproach
Of a million tear stained eyes
Don’t be surprised, when a crack in the ice
Appears under your feet
You slip out of your depth and out of your mind
With your fear flowing out behind you as you claw the thin ice"
"Daddy’s flown across the ocean
Leaving just a memory
A snapshot in the family album
Daddy, what else did you leave for me?
Daddy, what d’ya leave behind for me?
All in all, it was just a brick in the wall
All in all, it was all just bricks in the wall


Hey!
*Children’s playing*"
"You! Yes, you!
Stand still, Laddy!

When we grew up and went to school
There were certain teachers who would hurt the children
In any way they could (oof!)
By pouring their derision upon anything we did
Exposing every weakness
However carefully hidden by the kids (*Laughs*)

But in the town, it was well known when they got home at night Their fat and psychopathic wives would thrash them
Within inches of their lives

Ooh-ooh, ooh-ooh
Ooh-ooh, ooh-ooh
Ooh-ooh, ooh-ooh
Ooh"
"We don’t need no education
We don’t need no thought control
No dark sarcasm in the classroom
Teacher, leave them kids alone
Hey! Teacher! Leave them kids alone!

All in all, it’s just another brick in the wall
All in all, you’re just another brick in the wall

We don’t need no education
We don’t need no thought control
No dark sarcasm in the classroom
Teachers leave them kids alone
Hey! Teacher! Leave us kids alone!

All in all, you’re just another brick in the wall
All in all, you’re just another brick in the wall


Wrong, do it again! *Children playing*
Wrong, do it again!
If you don’t eat your meat, you can’t have any pudding!
(Wrong, do it again!)
How can you have any pudding if you don’t eat your meat?
(Wrong, do it again!)
You! Yes! You behind the bike sheds! Stand still, laddie!
(If you don’t eat your meat, you can’t have any pudding!
How can you have any pudding if you don’t eat your meat?)
(You! Yes! You behind the bike sheds! Stand still, laddie!)
*Children playing*
*Phone beeping sound*"
"Mother, do you think they’ll drop the bomb?
Mother, do you think they’ll like this song?
Mother, do you think they’ll try to break my balls?
Ooh-ah, mother, should I build the wall?

Mother, should I run for president?
Mother, should I trust the government?
Mother, will they put me in the firing line?
Ooh-ah, is it just a waste of time?

Hush now, baby, baby, don’t you cry
Mamma’s gonna make all of your nightmares come true
Mamma’s gonna put all of her fears into you
Mamma’s gonna keep you right here, under her wing
She won’t let you fly, but she might let you sing
Mamma’s gonna keep baby cosy and warm
Ooooh, babe
Ooooh, babe
Ooh, babe
Of course, Mamma’s gonna help build the wall


Mother, do you think she’s good enough–for me?
Mother, do you think she’s dangerous–to me?
Mother, will she tear your little boy apart?
Ooh-ah, mother, will she break my heart?

Hush now, baby, baby, don’t you cry
Mamma’s gonna check out all your girlfriends for you
Mamma won’t let anyone dirty get through
Mamma’s gonna wait up until you get in
Mamma will always find out where you’ve been
Mamma’s gonna keep baby healthy and clean
Ooooh, babe
Ooooh, babe
Ooh, babe
You’ll always be baby to me

Mother, did it need to be so high?"
"Look Mummy
There’s an airplane up in the sky

Ooh-ooh, ooh, ooh, ooh
Ooh-ooh, ooh, ooh, ooh
Ooh-ooh, ooh, ooh, ooh

Di-di-di-did you see the frightened ones?
Di-di-di-did you hear the falling bombs?
Di-di-di-did you ever wonder
Why we had to run for shelter
When the promise of a brave new world
Unfurled beneath the clear blue sky?

Ooh-ooh, ooh, ooh, ooh
Ooh-ooh, ooh, ooh, ooh
Ooh-ooh, ooh, ooh, ooh

Di-di-di-did you see the frightened ones?
Di-di-di-did you hear the falling bombs?
The flames are all long gone, but the pain lingers on

Goodbye blue sky
Goodbye blue sky
Goodbye
Goodbye"
"What shall we use to fill the empty spaces
Where we used to talk?
How should I fill the final places?
How should I complete the wall?"
"I am just a new boy
A stranger in this town
Where are all the good times?
Who’s gonna show this stranger around?

Ooh, I need a dirty woman
Ooh, I need a dirty girl

Will some woman in this desert land
Make me feel like a real man?
Take this rock and roll refugee
Ooh, baby, set me free

Ooh, I need a dirty woman
Ooh, I need a dirty girl


Ooh, I need a dirty woman
Ooh, I need a dirty girl

*Phone beeping*
""Hello?""
""Yes, a collect call for Mrs.Floyd from Mr.Floyd.Will you accept the charge from the United States? ""
*Phone clicks*
""Oh, he hung up.That’s your residence? Well, I wonder why he hung up.Is there supposed to be someone out there besides your wife there to answer?""
*Phone redials and beeps again*
""Hello?""
""This is the United States calling.Are we reaching...""
*Phone clicks*
""See, he keeps hanging up.There’s a man answering."""
"""Oh my God!What a fabulous room!Are all these your guitars?""
(""I’m sorry sir, I didn’t mean to startle you"")
""God!This place is bigger than our apartment!""
(""Let me know when you’re entering a room"")
(""Yes, sir"")
""Um, can I get a drink of water? ""
(""I was wondering about"")
""You want some, huh?""
(""Yes"")
""Oh wow!Hey, look at this tub!Wanna take a bath?""
(""I’ll have to find out from Mrs.Bancroft what time she wants to meet us, for her main"")
""What are you watching?""
(""If you’ll just let me know as soon as you can, Mrs.Bancroft...Mrs.Bancroft"")
""Hello?""
(""I don’t understand"")
""Are you feeling okay?""

Day after day, the love turns gray
Like the skin of the dying man
And night after night, we pretend it’s all right
But I have grown older, and you have grown colder
And nothing is very much fun any more
And I can feel one of my turns coming on
I feel cold as a razor blade, tight as a tourniquet
Dry as a funeral drum

Run to the bedroom, in the suitcase on the left
You’ll find my favourite axe
Don’t look so frightened, this is just a passing phase
One of my bad days
Would you like to watch TV? Or get between the sheets?
Or contemplate the silent freeway?
Would you like something to eat? Would you like to learn to fly?
Would ya? Would you like to see me try?
Ah, no!


Would you like to call the cops?
Do you think it’s time I stopped?
Why are you running away?"
"*Sounds from TV*

I don’t need no arms around me
And I don’t need no drugs to calm me
I have seen the writing on the wall
Don’t think I need anything at all
No, don’t think I’ll need anything at all

All in all, it was all just bricks in the wall
All in all, you were all just bricks in the wall"
"Goodbye, cruel world, I’m leaving you today
Goodbye, goodbye, goodbye
Goodbye, all you people, there’s nothing you can say
To make me change my mind, goodbye"
"Hey you
Out there in the cold, getting lonely, getting old
Can you feel me?
Hey you
Standing in the aisles with itchy feet and fading smiles
Can you feel me?
Hey you
Don’t help them to bury the light
Don’t give in without a fight

Hey you
Out there on your own, sitting naked by the phone
Would you touch me?
Hey you
With your ear against the wall, waiting for someone to call out
Could you touch me?
Hey you
Would you help me to carry the stone?
Open your heart, I’m coming home


But it was only fantasy
The wall was too high, as you can see
No matter how he tried, he could not break free
And the worms ate into his brain


Hey you
Out there on the road, always doing what you’re told
Can you help me?
Hey you
Out there beyond the wall, breaking bottles in the hall
Can you help me?
Hey you
Don’t tell me there’s no hope at all
Together we stand, divided we fall

(We fall, we fall, we fall, we fall, we fall, we fall, we fall, we fall...)"
"""Well, only got an hour of daylight left.Better get started""
""Isn’t it unsafe to travel at night?""
""It’ll be a lot less safe to stay here.Your father’s gonna pick up our trail before long""
""Can Lorca ride?""
""He’ll have to ride.Lorca, time to go!Chengra, thank you for everything.Let’s go.""
""Goodbye Chengra""
""Goodbye, Missy!""
""I’ll be back--one day""

Is there anybody out there?
Is there anybody out there?
Is there anybody out there?
Ah, is there anybody out there?"
"""But there’s somebody else that needs taking care of in Washington..""
""Who’s that?""
""Rose Pilchitt!""
""Rose Pilchitt? Who’s that?""
*Kid screams in background*
(Shut up!)
""36 - 24 - 36 * laughs * does that answer your question?""
(Oi! I’ve got a little black book with my poems in!)
""Who’s she? ""
""She was ’Miss Armoured Division’ in 1961...""

I’ve got a little black book with my poems in
Got a bag with a toothbrush and a comb in
When I’m a good dog they sometimes throw me a bone in
I got elastic bands keeping my shoes on
Got those swollen hand blues
I’ve got thirteen channels of shit on the T.V. to choose from
I’ve got electric light
And I’ve got second sight
I’ve got amazing powers of observation

And that is how I know
When I try to get through
On the telephone to you
There will be nobody home

I’ve got the obligatory Hendrix perm
And the inevitable pinhole burns
All down the front of my favourite satin shirt
I’ve got nicotine stains on my fingers
I’ve got a silver spoon on a chain
I’ve got a grand piano to prop up my mortal remains
I’ve got wild staring eyes
And I’ve got a strong urge to fly
But I’ve got nowhere to fly to (fly to.. fly to.. fly to..)

Ooh, babe, when I pick up the phone
(""Surprise,surprise,surprise..."")
There’s still nobody home

I’ve got a pair of Gohills boots
And I’ve got fading roots"
"Does anybody here remember Vera Lynn?
Remember how she said that
We would meet again some sunny day?
Vera, Vera, what has become of you?
Does anybody else in here feel the way I do?"
"Bring the boys back home
Bring the boys back home
Don’t leave the children on their own, no, no
Bring the boys back home

""Wrong,do it again!""
*knock* ""Time to go!""
""Are you feeling okay?""
""He keeps hanging up,and it’s a man answering!""
""Hahahahaha!!!!!!""
Is there anybody out there?"
"Hello? (Hello, hello, hello)
Is there anybody in there?
Just nod if you can hear me
Is there anyone home?
Come on (Come on, come on), now
I hear you’re feeling down
Well, I can ease your pain
And get you on your feet again
Relax (Relax, relax, relax)
I’ll need some information first
Just the basic facts
Can you show me where it hurts?

There is no pain, you are receding
A distant ship, smoke on the horizon
You are only coming through in waves
Your lips move, but I can’t hear what you’re saying
When I was a child, I had a fever
My hands felt just like two balloons
Now I’ve got that feeling once again
I can’t explain, you would not understand
This is not how I am

I have become comfortably numb


I have become comfortably numb

Okay (Okay, okay, okay)
Just a little pinprick
There’ll be no more
But you may feel a little sick
Can you stand up? (Stand up, stand up)
I do believe it’s working, good
That’ll keep you going through the show
Come on, it’s time to go

There is no pain, you are receding
A distant ship, smoke on the horizon
You are only coming through in waves
Your lips move, but I can’t hear what you’re saying
When I was a child, I caught a fleeting glimpse
Out of the corner of my eye
I turned to look, but it was gone
I cannot put my finger on it now
The child is grown, the dream is gone

I have become comfortably numb"
"(Ah-ah) Ooh, ooh-hoo, ooh, ooh
(Ah-ah)
(Ah-ah)
(Ooh-ma, ah, ooh-pa) Must the show go on?
(Ooh-pa, take me home, take me home, take me home)
(Ooh-ma, let me go, let me go, let me go)

There must be some mistake, I didn’t mean to let them
Take away my soul, am I too old, is it too late?
(Ooh-ma, ooh-pa) Where has the feeling gone?
(Ooh-ma, ooh-pa) Will I remember the song?

(Ooh, ooh, ah) The show must go on"
"So ya thought ya might like to go to the show
To feel the warm thrill of confusion, that space cadet glow
I’ve got some bad news for you sunshine
Pink isn’t well, he stayed back at the hotel
And they sent us along as a surrogate band
We’re gonna find out where you fans really stand

Are there any queers in the theater tonight?
Get them up against The Wall
(Against The Wall)
Now there’s one in the spotlight, he don’t look right to me
Get him up against The Wall
(Against The-)
And that one looks Jewish and that one’s a coon!
Who let all of this riff-raff into the room?
There’s one smoking a joint and another with spots
If I had my way, I’d have all of ya shot!"
"Run, run, run, run
Run, run, run, run
Run, run, run, run
Run, run, run, run

You better make your face up with your favourite disguise
With your button down lips and your roller blind eyes
With your empty smile and your hungry heart
Feel the bile rising from your guilty past
With your nerves in tatters as the cockleshell shatters
And the hammers batter down your door
You better run!


Run, run, run, run
Run, run, run, run
Run, run, run, run
Run, run, run, run

You better run all day and run all night
And keep your dirty feelings deep inside
And if you’re taking your girlfriend out tonight
You better park the car well out of sight
’Cause if they catch you in the back seat trying to pick her locks
They’re gonna send you back to Mother in a cardboard box
You better run!"
"""Eins, zwei, drei, alle!""
Ooh-ooh, you cannot reach me now
Ooh-ooh, no matter how you try
Goodbye, cruel world, it’s over
Walk on by

Sittin’ in a bunker here behind my wall
Waitin’ for the worms to come (Worms to come)
In perfect isolation here behind my wall
Waitin’ for the worms to come

Testing. One. Two. One. Two. We’re all going to convene at 1:15 outside Brixton Town Hall where we will be going...

(Waiting) To cut out the deadwood
(Waiting) To clean up the city
(Waiting) To follow the worms
(Waiting) To put on a black shirt
(Waiting) To weed out the weaklings
(Waiting) To smash in their windows and kick in their doors
(Waiting) For the final solution to strengthen the strain
(Waiting) To follow the worms
(Waiting) To turn on the showers and fire the ovens
(Waiting) For the queens and the coons and the reds and the Jews
(Waiting) To follow the worms

Would you like to see Britannia Rule again
My friend?
All you have to do is follow the worms
Would you like to send our coloured cousins home again
My friend?
All you need to do is follow the worms

Stop!"
"I wanna go home
Take off this uniform and leave the show
But I’m waiting in this cell, because I have to know
(Have to know, have to know...)
Have I been guilty all this time?
(Have to know, have to know, have to know, have to know...)
(Time, time, time, time...)"
"Good morning, Worm your honour
The crown will plainly show the prisoner
Who now stands before you
Was caught red-handed showing feelings
Showing feelings of an almost human nature
This will not do
Call the schoolmaster!

I always said he’d come to no good in the end your honour
If they’d let me have my way I could have flayed him into shape
But my hands were tied, the bleeding hearts and artists
Let him get away with laughter, let me hammer him today

Crazy, toys in the attic
I am crazy, truly gone fishing
They must have taken my marbles away!
(Crazy, toys in the attic, he is crazy)

You little shit, you’re in it now, I hope they throw away the key
You should have talked to me more often than you did, but no!
You had to go your own way
Have you broken any homes up lately?
""Just five minutes,Worm your honour,him and me,alone""

Babe!
Come to mother baby, let me hold you in my arms
M’lud I never wanted him to get in any trouble
Why’d he ever have to leave me?
Worm, your honour, let me take him home

Crazy, over the rainbow
I am crazy, bars in the window
There must have been a door there in the wall
When I came in
(Crazy, over the rainbow, he is crazy)

The evidence before the court is incontrovertible
There’s no need for the jury to retire
In all my years of judging, I have never heard before
Of someone more deserving of the full penalty of law
The way you made them suffer, your exquisite wife and mother
Fills me with the urge to defecate
(Go on, Judge, shit on him!)
Since, my friend, you have revealed your deepest fear
I sentence you to be exposed before your peers
Tear down the wall!

Tear down the wall!
Tear down the wall!
Tear down the wall!
Tear down the wall!
Tear down the wall!
Tear down the wall!
Tear down the wall!
Tear down the wall!
*Explosion*
*Bricks crumbling*"
"All alone, or in twos
The ones who really love you
Walk up and down, outside the wall
Some hand in hand
And some gathered together in bands
The bleeding hearts and the artists make their stand
And when they’ve given you their all
Some stagger and fall, after all it’s not easy
Banging your heart against some mad bugger’s wall

Isn’t this where..."
"“…announced plans to build a nuclear fallout shelter at Peterborough in Cambridgeshire…”
“…three high court judges have cleared the way…”
“…It was announced today that the replacement for the Atlantic
Conveyor, the container ship lost in the Falklands conflict would be built in Japan. A spokesman for…”
“…moving in. They say the third world countries, like Bolivia, which produce the drug are suffering from rising violence…”

Tell me true, tell me why, was Jesus crucified?
Was it for this that Daddy died?
Was it for you? Was it me?
Did I watch too much T.V.?
Is that a hint of accusation in your eyes?
If it wasn't for the Nips
Being so good at building ships
The yards would still be open on the Clyde
And it can't be much fun for them
Beneath the rising sun
With all their kids committing suicide
What have we done, Maggie, what have we done?
What have we done to England?

Should we shout, should we scream
“What happened to the post war dream?”
Oh, Maggie, Maggie, what did we do?"
"They flutter behind you your possible pasts
Some bright-eyed and crazy, some frightened and lost
A warning to anyone still in command
“Ranks! Fire!”
Of their possible future, to take care
In derelict sidings the poppies entwine
With cattle trucks lying in wait for the next time

Do you remember me? How we used to be?
Do you think we should be closer?

She stood in the doorway, the ghost of a smile
Haunting her face like a cheap hotel sign
Her cold eyes imploring the men in their Macs
For the gold in their bags or the knives in their backs
Stepping up boldly one put out his hand
He said, “I was just a child then, now I’m only a man.”

Do you remember me? How we used to be?
Do you think we should be closer?

By the cold and religious we were taken in hand
Shown how to feel good and told to feel bad
(Tongue tied and terrified we learned how to pray
Now our feelings run deep and cold as the clay)
Strung out behind us the banners and flags
Of our possible pasts lie in tatters and rags

Do you remember me? How we used to be?
Do you think we should be closer?"
"When you’re one of the few to land on your feet
What do you do to make ends meet? (teach)
Make 'em mad, make 'em sad, make 'em add two and two
Or make 'em me, or make 'em you, make 'em do what you want them to
Make 'em laugh, make 'em cry, make 'em lie down and die"
"It was just before dawn one miserable
Morning in black Forty-Four
When the forward commander was told to sit tight
When he asked that his men be withdrawn
And the Generals gave thanks as the other ranks
Held back the enemy tanks for a while
And the Anzio bridgehead was held for the price
Of a few hundred ordinary lives

And kind old King George sent Mother a note
When he heard that Father was gone
It was, I recall, in the form of a scroll
With gold leaf and all
And I found it one day
In a drawer of old photographs, hidden away
And my eyes still grow damp to remember
His Majesty signed with his own rubber stamp

It was dark all around, there was frost in the ground
When the Tigers broke free
And no one survived
From the Royal Fusiliers Company Z
They were all left behind
Most of them dead, the rest of them dying
And that's how the High Command
Took my daddy from me"
"Floating down, through the clouds
Memories come rushing up to meet me now
But in the space between the heavens
And in the corner of some foreign field
I had a dream
I had a dream
Good-bye Max
Good-bye Ma
After the service, when you’re walking slowly to the car
And the silver in her hair shines in the cold November air
You hear the tolling bell
And touch the silk in your lapel
And as the tear drops rise to meet the comfort of the band
You take her frail hand
And hold on to the dream!
A place to stay
“Oi! A real one …”
Enough to eat
Somewhere old heroes shuffle safely down the street
Where you can speak out loud
About your doubts and fears
And what’s more no-one ever disappears
You never hear their standard issue kicking in your door
You can relax on both sides of the tracks
And maniacs don’t blow holes in bandsmen by remote control
And everyone has recourse to the law
And no one kills the children anymore
And no one kills the children anymore
Night after night
Going round and round my brain
His dream is driving me insane
In the corner of some foreign field
The gunner sleeps tonight
What’s done is done
We cannot just write off his final scene
Take heed of the dream
Take heed"
"Button your lip andon’t let the shield slip
Take a fresh grip on your bullet proof mask
And if they try to break down your disguise with their questions
You can hide, hide, hide
Behind paranoid eyes
You put on our brave face and slip over the road for a jar
Fixing your grin as you casually lean on the bar
Laughing too loud at the rest of the world
With the boys in the crowd
You can hide, hide, hide
“I’ll tell you what, I’ll give you three blacks, and play you for five\“
Behind petrified eyes\ n“ Ta!You was unlucky there son”\ nYou believed in their stories of fame, fortune and glory
Now you’ re lost in a haze of alcohol soft middle age\ nThe pie in the sky turned out to be miles too high
And you hide, hide, hide\ n“ Time gentleman!”
Behind brown and mild eyes
“ Oi!”"
"(Hey!Get your filthy hands off my desert!)
(What he say?)

Brezhnev took Afghanistan
Begin took Beirut
Galtieri took the Union Jack
And Maggie, over lunch one day
Took a cruiser with all hands
Apparently, to make him give it back"
"Take all your overgrown infants away somewhere
And build them a home, a little place of their own\ nThe Fletcher Memorial Home\ nFor Incurable Tyrants and Kings\ n\ nAnd they can appear to themselves every day\ nOn closed circuit T.V
To make sure they’re still real
It’s the only connection they feel

Ladies and gentlemen, please welcome, Reagan and Haig
Mr.Begin and friend, Mrs.Thatcher, and Paisley
“ Hello Maggie!”
Mr.Brezhnev and party\ n“ Scusi dov’ è il bar? ”
The ghost of McCarthy,
The memories of Nixon.
“ Who’ s the bald chap? ”
“ Good - bye!”
And now, adding colour
A group of anonymous Latin - American meat packing glitterati

Did they expect us to treat them with any respect?
They can polish their medals and sharpen their smiles,
And amuse themselves playing games for awhile
Boom boom, bang bang, lie down you’ re dead\ n\ n\ nSafe in the permanent gaze of a cold glass eye\ nWith their favourite toys\ nThey’ll be good girls and boys
In the Fletcher Memorial Home for colonial\ nWasters of life and limb\ nIs everyone in?
Are you having a nice time?
(Goodbye!)
Now the final solution can be applied "
"They disembarked in 45
And no - one spoke and no - one smiled
There were too many spaces in the line\ nGathered at the cenotaph\ nAll agreed with the hand on heart\ nTo sheath the sacrificial Knifes\ nBut now\ nShe stands upon Southampton dock\ nWith her handkerchief\ nAnd her summer frock clings\ nTo her wet body in the rain\ nIn quiet desperation knuckles\ nWhite upon the slippery reins\ nShe bravely waves the boys goodbye again\ n\ nAnd still the dark stain spreads between\ nTheir shoulder blades\ nA mute reminder of the poppy fields and graves\ nAnd when the fight was over
We spent what they had made, but
In the bottom of our hearts we felt the final cut"
"Through the fish - eyed lens of tear stained eyes
I can barely define the shape of this moment in time
And far from flying high in clear blue skies
I'm spiraling down to the hole in the ground where I hide
If you negotiate the minefield in the drive
And beat the dogs and cheat the cold electronic eyes
And if you make it past the shotguns in the hall
Dial the combination, open the priesthole
And if I'm in I'll tell you (What's behind the wall)
(Yahoo!)

There's a kid who had a big hallucination
Making love to girls in magazines
He wonders if you're sleeping with your new found faith
Could anybody love him
Or is it just a crazy dream?

And if I show you my dark side
Will you still hold me tonight?
And if I open my heart to you
And show you my weak side
What would you do?
Would you sell your story to Rolling Stone?
Would you take the children away
And leave me alone?
And smile in reassurance
As you whisper down the phone?
Would you send me packing?
Or would you take me home?

Thought I oughta bare my naked feelings
Thought I oughta tear the curtain down
I held the blade in trembling hands
Prepared to make it but just then the phone rang
I never had the nerve to make the final cut

“Hello? Listen, I think I've got it.“
“Okay, listen, it's a- Hahahaha!”"
"Fuck all that, we've got to get on with these
(Fuck all that, fuck all that)
Got to compete with the wily Japanese
There’s too many home fires burning and not enough trees
(Fuck all that)
So fuck all that, we've gotta get on with these
(Gotta get on with these)

Can’t stop, lose job
Mind gone, silicon
Tsar bomb, what bomb?
Get away, pay day
Make hay, break down
Need fix, big six
Click, click
Hold on, oh no
Bingo! (Bingo!)

Make them laugh, make them cry
Make them dance in the aisles
Make them pay, make them stay
Make them feel okay

Not now John, we've got to get on with the film show
(Gotta get on, gotta get on)
Hollywood waits at the end of the rainbow
(End of the rainbow)
Who cares what it’s about as long as the kids go
(As long as the kids go)
So, not now John, we've gotta get on with the show
(Gotta get on with the show, gotta get on, gotta get on)


(Gotta get on, gotta get on, gotta get on)
Hang on John I've got to get on with this
(Gotta get on, gotta get on)
I don’t know what it is, but it fits on here like- tsss
Come at the end of the shift, we’ll go and get pissed
But not now now John, I've gotta get on with this
(Gotta get on with this, gotta get on)

Hold on John, I think there’s something good on
I used to read books but...
It could be the news, or some other amusement
Could be reusable shows

Fuck all that, we've gotta get on with these
(Doo, doo, wah)
Got to compete with the wily Japanese
(Gotta get on, gotta get on)
No need to worry about the Vietnapeace
(Doo, doo, wah)
Got to bring the Russian Bear to his knees
(Gotta get on)
Well, maybe not the Russian Bear, maybe the Swedes
(Doo, doo, wah)
We showed Argentina, now let’s go and show these
(Gotta get on, gotta get on)
Make us feel tough and wouldn't Maggie be pleased?
(Doo, doo, wah)
Na, na, na, na, na, na, na
One, two, Free Four!
(One, two, Free Four!)

S'cusi, dov'è il bar? (What?)
Se parakalo, pou einai to bar?
S’il vous plaît, où est le bar? (Say it in English!)
Oi, where’s the fucking bar John? (Oh, now you’re talking!)
(Oh! Rule Britannia! Britannia rules the day)
Down! Go, Maggie!
Hammer, Hammer, Hammer, Hammer, now!"
"In my rear view mirror the sun is going down
Sinking behind bridges in the road
And I think of all the good things
That we have left undone
And I suffer premonitions, confirm suspicions
Of the holocaust to come

The rusty wire that holds the cork that keeps the anger in
Gives way and suddenly it’s day again
The sun is in the east
Even though the day is done
Two suns in the sunset, hmph
Could be the human race is run

Like the moment when the brakes lock
And you slide towards the big truck (“Oh no!”)
You stretch the frozen moments with your fear 
And you’ll never hear their voices (”Daddy, Daddy!”)
And you’ll never see their faces
You have no recourse to the law anymore

And as the windshield melts and my tears evaporate
Leaving only charcoal to defend
Finally I understand
The feelings of the few
Ashes and diamonds, foe and friend
We were all equal in the end

“…and now the weather. Tomorrow will be cloudy with scattered showers spreading from the east …
With an expected high of 4000 degrees Celsius”"
"*Boat floating*

When the child like view of the world went, nothing replaced it... Nothing replaced it… Nothing replaced it…
I do not like being asked to... I do not like being asked to... I do not like being asked to...
Other people replaced it... Someone who knows"
"Into the distance, a ribbon of black
Stretched to the point of no turning back
A flight of fancy on a wind swept field
Standing alone my senses reel
A fatal attraction is holding me fast
How can I escape this irresistible grasp?

Can’t keep my eyes from the circling sky
Tongue-tied and twisted
Just an earth-bound misfit, I

Ice is forming on the tips of my wings
Unheeded warnings, I thought I thought of everything
No navigator to find my way home
Unladen, empty and turned to stone

A soul in tension that’s learning to fly
Condition grounded but determined to try

Can’t keep my eyes from the circling skies
Tongue-tied and twisted
Just an earth-bound misfit, I

Above the planet on a wing and a prayer
My grubby halo, a vapor trail in the empty air
Across the clouds I see my shadow fly
Out of the corner of my watering eye
A dream unthreatened by the morning light
Could blow this soul right through the roof of the night

There’s no sensation to compare with this
Suspended animation, a state of bliss

Can’t keep my mind from the circling skies
Tongue-tied and twisted
Just an earth-bound misfit, I"
"Dogs of war and men of hate
With no cause, we don’t discriminate
Discovery is to be disowned
Our currency is flesh and bone
Hell opened up and put on sale
Gather round and haggle
For hard cash we will lie and deceive
Even our Masters don’t know the webs we weave

One world, it’s a battleground
One world, and we will smash it down
One world… One world

Invisible transfers, long distance calls
Hollow laughter in marble halls
Steps have been taken, a silent uproar
Has unleashed the dogs of war
You can’t stop what has begun
Signed, sealed, they deliver oblivion
We all have our dark side to say the least
And dealing in death is the nature of the beast

One world, it’s a battleground
One world, and they're gonna smash it down
One world… One world


One world… One world


The dogs of war don’t negotiate
The dogs of war won’t capitulate
They will take and you will give
And you must die so that they may live
You can knock at any door
But wherever you go, you know they’ve been there before
Well winners can lose and things can get strained
But whatever you change you know the dogs remain

One world, it’s a battleground
One world, and we gonna smash it down
One world… One world

One world… One world
One world… One world"
"A restless eye across a weary room
A glazed look and I was on the road to ruin
The music played and played as we whirled without end
No hint, no word her honour to defend
“I will, I will” she sighed to my request\ nAnd then she tossed her mane while my resolve was put to the test\ nThen drowned in desire, our souls on fire\ nI led the way to the funeral pyre\ nAnd without a thought of the consequence\ nI gave in to my decadence

One slip, and down the hole we fall\ nIt seems to take no time at all\ nA momentary lapse of reason\ nThat binds a life for life\ nA small regret, you won’ t forget\ nThere’ ll be no sleep in here tonight\ n\ nWas it love or was it the idea of being in love? 
Or was it the hand of fate, that seemed to fit just like a glove? 
The moment slipped by and soon the seeds were sown\ nThe year grew late and neither one wanted to remain alone\ n\ nOne slip, and down the hole we fall\ nIt seems to take no time at all\ nA momentary lapse of reason\ nThat binds a life to a life\ nOne regret, you will never forget\ nThere’ ll be no sleep in here tonight\ n\ nOne slip… one slip… "
"On the turning away
From the pale and downtrodden
And the words they say
Which we won’t understand
“Don’ t accept that what’ s happening\ nIs just a case ofall the suffering\ nOr you’ ll find that you’ re joining in 
The turning away”

It’s a sin that somehow
Light is changing to shadow
And casting its shroud
Over all we have known
Unaware how the ranks have grown
Driven on by a heart of stone
We could find that we’re all alone
In the dream of the proud

On the wings of the night
As the daytime is stirring
Where the speechless unite
In a silent accord
Using words you will find are strange
Mesmerized as they light the flame
Feel the new wind of change
On the wings of the night


No more turning away
From the weak and the weary
No more turning away
From the coldness inside
Just a world that we all must share
It’s not enough just to stand and stare
Is it only a dream that there’ll be?
No more turning away?"
"One sound, one single sound
One kiss, one single kiss
A face outside the window pane
However did it come to this?
A man who ran: a child who cried
A girl who heard, a voice that lied
The sun that burned a fiery red
The vision of an empty bed

The use of force, he was so tough
She’ll soon submit, she’s had enough
The march of fate, the broken will
Someone is lying very still
He has laughed and he has cried
He has fought and he has died
He’s just the same as all the rest
He’s not the worst, and he’s not the best


And still, this ceaseless murmuring
The babbling that I brook
The seas of faces, eyes upraised
The empty screen, the vacant look
A man in black on a snow white horse
A pointless life has run its course
The red rimmed eyes, the tears still run
As he fades into the setting sun"

"I have always been here
I have always looked out from behind these eyes
It feels like more than a lifetime
Feels like more than a lifetime

Sometimes I get tired of the waiting
Sometimes I get tired of being in here
Is this the way that it's always been?
Could it ever have been different?

Do you ever get tired of the waiting?
Do you ever get tired of being in there?
Don't worry, nobody lives forever
Nobody lives forever"

"I will always be here
I will always look out from behind these eyes
It’s only a lifetime
It’s only a lifetime
It’s only a lifetime"
"The sweet smell of a great sorrow lies over the land
Plumes of smoke rise and merge into the leaden sky:
A man lies and dreams of green fields and rivers
But awakes to a morning with no reason for waking
He’s haunted by the memory of a lost paradise
In his youth or a dream, he can’t be precise
He’s chained forever to a world that’s departed
It’s not enough, it’s not enough

His blood has frozen and curdled with fright
His knees have trembled and given way in the night
His hand has weakened at the moment of truth
His step has faltered

One world, one soul
Time pass, the river roll

And he talks to the river of lost love and dedication
And silent replies that swirl invitation
Flow dark and troubled to an oily sea
A grim intimation of what is to be
There’s an unceasing wind that blows through this night
And there’s dust in my eyes, that blinds my sight
And silence that speaks so much louder than words
Of promises broken"

"As you look around this room tonight
Settle in your seat and dim the lights
Do you want my blood, do you want my tears?
What do you want?
(What do you want from me?)
Should I sing until I can’t sing anymore?
Play these strings until my fingers are raw

You're so hard to please

What do you want from me?

Do you think that I know something you don’t know? (What do you want from me?)
If I don’t promise you the answers would you go? (What do you want from me?)
Should I stand out in the rain?
Do you want me to make a daisy chain for you?

I’m not the one you need

What do you want from me?

You can have anything you want
You can drift, you can dream, even walk on water
Anything you want
You can own everything you see
Sell your soul for complete control
Is that really what you need?
You can lose yourself this night
See inside, there is nothing to hide
Turn and face the light

What do you want from me?"
"Did you know
It was all going to go so wrong for you?
And did you see
It was all going to be so right for me?
Why did we tell you then
You were always the golden boy then
And that you’d never lose that light in your eyes?

Hey you
Did you ever realize what you’d become?
And did you see
That it wasn’t only me you were running from?
Did you know all the time but it never bothered you anyway?
Leading the blind while I stared out the steel in your eyes

The rain fell slow
Down on all the roofs of uncertainty
I thought of you
And the years and all the sadness fell away from me
And did you know?
(Did you know)
I never thought that you’d lose that light in your eyes"

"On the day the wall came down
They threw the locks onto the ground
And with glasses high we raised a cry for freedom had arrived
On the day the wall came down
The Ship of Fools had finally run aground
Promises lit up the night like paper doves in flight

I dreamed you had left my side
No warmth, not even pride remained
And even though you needed me
It was clear that I could not do a thing for you

Now life devalues day by day
As friends and neighbors turn away
And there’s a change that, even with regret, cannot be undone
Now frontiers shift like desert sands
While nations wash their bloodied hands
Of loyalty, of history, in shades of grey

I woke to the sound of drums
The music played, the morning sun streamed in
I turned and I looked at you
And all but the bitter residues slipped away...
Slipped away"
"From morning to night I stayed out of sight
Didn’t recognize I’d become
No more than alive; I’d barely survive
In a word… overrun

Won’t hear a sound (He’s curled into the corner)
From my mouth (But still the screen is flickering)
I’ve spent too long (With an endless stream of garbage to)
On the inside out (…curse the place)
My skin is cold (In a sea of random images)
To the human touch (The self-destructing animal)
This bleeding heart’s (Waiting for the waves to break)
Not beating much

I murmured a vow of silence and now
I don’t even hear when I think aloud
Extinguished by light I turn on the night
Wear its darkness with an empty smile

I’m creeping back to life
My nervous system all awry
I’m wearing the inside out

Look at him now
He’s paler somehow
But he’s coming around
He’s starting to choke
It’s been so long since he spoke
Well he can have the words right from my mouth

And with these words I can see
Clear through the clouds that covered me
Just give it time then speak my name
Now we can hear ourselves again
I’m holding out (He’s standing on the threshold)
For the day (Caught in fiery anger)
When all the clouds (And hurled into the furnace he’ll)
Have blown away (…curse the place)
I’m with you now (He’s torn in all directions)
Can speak your name (And still the screen is flickering)
Now we can hear (Waiting for the flames to break)
Ourselves again"
"Her love rains down on me easy as the breeze
I listen to her breathing, it sounds like the waves on the sea
I was thinking all about her, burning with rage and desire
We were spinning into darkness; the earth was on fire

She could take it back, she might take it back someday

So I spied on her, I lied to her, I made promises I cannot keep
Then I hear their laughter rising, rising from the deep
And I make her prove her love for me, I take all that I can take
And I push her to the limit to see if she will break

She might take it back, she could take it back some day

Ring-a-ring o’ roses
A pocket full of posies
A-tishoo! A-tishoo!
We all fall down

Now I have seen the warnings, screaming from all sides
It’s easy to ignore them, God knows I’ve tried
All of this temptation, you know it turned my faith to lies
Until I couldn’t see the danger or hear the rising tide

She can take it back, she will take it back some day
She can take it back, she will take it back some day
She will take it back, she will take it back some day"
"Where were you when I was burned and broken?
While the days slipped by from my window watching
And where were you when I was hurt and I was helpless?
‘Cause the things you say and the things you do surround me
While you were hanging yourself on someone else’s words
Dying to believe in what you heard
I was staring straight into the shining sun

Lost in thought and lost in time
While the seeds of life and the seeds of change were planted
Outside, the rain fell dark and slow
While I pondered on this dangerous but irresistible pastime
I took a heavenly ride through our silence
I knew the moment had arrived
For killing the past and coming back to life

I took a heavenly ride through our silence
I knew the waiting had begun
And headed straight… into the shining sun"
"For millions of years mankind lived just like the animals
Then something happened which unleashed the power of our imagination
We learned to talk

There’s a silence surrounding me
I can’t seem to think straight
I’ll sit in the corner
And no one can bother me
I think I should speak now (Why won’t you talk to me?)
I can’t seem to speak now (You never talk to me)
My words won’t come out right (What are you thinking?)
I feel like I’m drowning (What are you feeling?)
I’m feeling weak now (Why won’t you talk to me?)
But I can’t show my weakness (You never talk to me)
I sometimes wonder (What are you thinking?)
Where do we go from here (What are you feeling?)

It doesn’t have to be like this
All we need to do is make sure we keep talking

(Why won’t you talk to me?) I feel like I’m drowning
(You never talk to me) You know I can’t breathe now
(What are you thinking?) We’re going nowhere
(What are you feeling?) We’re going nowhere
(Why won’t you talk to me?)
(You never talk to me)
(What are you thinking?)
(Where do we go from here?)

It doesn’t have to be like this
All we need to do is make sure we keep talking"
"I was spending my time in the doldrums
I was caught in a cauldron of hate
I felt persecuted and paralysed
I thought that everything else would just wait
While you are wasting your time on your enemies
Engulfed in a fever of spite
Beyond your tunnel vision reality fades
Like shadows into the night
To martyr yourself to caution
Is not going to help at all
‘Cause there’ll be no safety in numbers
When the right one walks out of the door

“Ladies and gentlemen!
The winner\ nBy a knockout”

Can you see your days blighted by darkness?
Is it true you beat your fists on the floor?
Stuck in a world of isolation
While the ivy grows over the door
So I open my door to my enemies
And I ask “could we wipe the slate clean?”
But they tell me to please go fuck myself
You know you just can’t win"
"Beyond the horizon of the place we lived when we were young
In a world filled with magnets and miracles
Our thoughts strayed constantly and without boundary
The ringing of the division bell had begun
Along the Long Road and on down the Causeway
Do they still meet there by the Cut
There was a ragged band that followed in our footsteps
Running before time took our dreams away
Leaving the myriad small creatures trying to tie us to the ground
To a life consumed by slow decay

The grass was greener
The light was brighter
With friends surrounded
The nights of wonder

Looking beyond the embers of bridges glowing behind us
To a glimpse of how green it was on the other side
Steps taken forwards but sleepwalking back again
Dragged by the force of some inner tide
At a higher altitude with flag unfurled
We reached the dizzy heights of that dreamed of world


Encumbered forever by desire and ambition
There's a hunger still unsatisfied
Our weary eyes still stray to the horizon
Though down this road we've been so many times

The grass was greener
The light was brighter
The taste was sweeter
The nights of wonder
With friends surrounded
The dawn mist glowing
The water flowing
The endless river
For ever and ever


""Is that Charlie? Hello Charlie!
Great..."""
"We certainly have an unspoken understanding
But a lot of things unsaid as well

We shout and argue and fight, and work it on out

The sum is greater than the parts"












"Speech has allowed the communication of ideas, enabling human beings to work together to build the impossible
Mankind's greatest achievements have come about by talking
Our greatest hopes could become reality in the future, with the technology at our disposal, the possibilities are unbounded

All we need to do is make sure we keep talking
"



"We bitch and we fight
Diss each other on sight
But this thing we do
These times together
Rain or shine or stormy weather
This thing we do
With world-weary grace
We've taken our places
We could curse it or nurse it and give it a name
Or stay home by the fire, filled by desire
Stoking the flame
But we’re here for the ride

It's louder than words
This thing that we do
Louder than words
The way it unfurls
It's louder than words
The sum of our parts
The beat of our hearts
Is louder than words
Louder than words

The strings bend and slide
As the hours glide by
An old pair of shoes, your favorite blues
Gonna tap out the rhythm
Let's go with the flow, wherever it goes
We're more than alive

It's louder than words
This thing that we do
Louder than words
The way it unfurls
It's louder than words
The sum of our parts
The beat of our hearts
Is louder than words
Louder than words
Louder than words
This thing they call soul
Is there with a pulse
Louder than words
Louder than words"



'''

print(lyrics_to_frequencies(taylor_swift))




