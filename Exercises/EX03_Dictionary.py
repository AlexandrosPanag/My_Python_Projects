#the <'''> refers to a multiple lines string


Song_Words_As_Weapons_By_Korn = '''All I really want is something beautiful to say 
Keep me locked up in your broken mind
I keep searchin, never been able to find a
Light behind your dead eyes
Not anything at all
You keep living in your own lie, ever deceitful and ever unfaithful
Keep me guessin, keep me terrified
Take everything from my world
Say can you help me right before the fall
Take what you can and leave me to the wolves
Keep me dumb, keep me paralyzed
Why try swimming? I'm drowning in fables
You're not that saint that you externalize
You're not anything at all
It's oh-so playful when you demonize
To spit out the hateful, you're willing and able
Words are weapons I'd be terrified
You're nothing in my world
Say can you help me right before the fall
Take what you can and leave me to the wolves
All I really want is something beautiful to say
Keep me guessin, keep me terrified
All I really want is something beautiful to say
You keep livin' in your own lie
All I really want is something beautiful to say
To never fade away, I wanna live forever!
All I really want is something beautiful to say
To never fade away, I wanna live forever!
You keep living in your own lie
Keep me guessin, keep me terrified
All I really want is something beautiful to say
Say can you help me right before the fall
Take what you can and leave me to the wolves
All I really want is something beautiful to say
Words are weapons I'd be terrified
All I really want is something beautiful to say
Keep me guessin, keep me terrified
All I really want is something beautiful to say
To never fade away, I wanna live forever!
All I really want is something beautiful to say
To never fade away, I wanna live forever!'''


print(Song_Words_As_Weapons_By_Korn)

#alphabetical order sorting
list_words=Song_Words_As_Weapons_By_Korn.split()
list_words.sort()
print(list_words)

#length of the words

print(" The length of the words is:{}".format(len(list_words)))

#calculate the length of the chars

Song_Words_As_Weapons_By_Korn= Song_Words_As_Weapons_By_Korn.replace(" ","").replace("\n","") #replace the gap betweeen each word with nothing,then replace new line with nothing
print("The length of characters is:{}".format(len(Song_Words_As_Weapons_By_Korn)))