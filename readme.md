## Science Hurricane

This is a bad grad school-themed rock n'roll love ballad.

It is also a computer program written in [Rockstar](https://codewithrockstar.com). It simulates adaptive evolution, tracking the fate of a mutation favoured by natural selection and plotting its frequency in the population through time. Paste the song in [the Rockstar online interpreter](https://codewithrockstar.com/online) to see it in action.

```
(Science Hurricane)

The reviewer is snickering. Wide-eyed, delighted!
The effort was irrelevant. Waste.
The reviews are very clever
Your paper is uninspired. Scientific megahogwash
Your heart is uninspired. Washed-out, incompetent...
Impostor Syndrome is over powering

Love is hardship
Reviewers are over-conceited autocrats
Your degree is soul-murder
Put your degree with your paper into the future
Let failure be your degree with the effort of your paper
Let your curse be your degree over love

Your dreams are unthinkable to accomplish
Your failures are progressing to pain
The night is all encompassing
Publishing is past reach
Your thunder is lost
Let your youth be your degree

My guitar says enough! This is not your fate, love

Academia takes regrets
Put regrets into the fire
Put regrets of the future with failure into my song
Put regrets of failure with your youth into a tornado
Let research be my song without regrets of failure
Let writing be a tornado without regrets of your youth
Let your fangs be the fire of research with writing
Put your fangs without regrets of writing into the thesis
Give back regrets of research over the thesis

Rock my love
While your heart is weaker than the reviewer,
Let the lightning be academia taking your heart
Put the lightning into your heart
Rock my love with your heart

Let your claws be my love
The manuscript is yet sufficient
Put your claws over the manuscript into my song
Turn up my song
If the manuscript is stronger than your claws,
My song is all-burning

My guitar says listen! To the Science Hurricane in you

The hurricane is whispering
The storm is whispering
lightning says allele frequency
A thunderbolt says generations

Cast your failures into Rock N Roll
Cast the night into drumbeats
Cast reviewers into a tsunami
Cast Impostor Syndrome into a volcano
Cast the reviews into tempest
Cast publishing into thunder
Put drumbeats of your thunder into your science
Whisper lightning
Let your heartbeat be a volcano

While love is stronger than the storm,
Let your hope be your degree without the storm of your curse
Put the storm with your degree into fists
Put your degree without fists of your curse into academia
Let your power be your science with Rock N Roll
If the storm is the hurricane,
Let your power be a tsunami with tempest, your heartbeat, drumbeats, Rock N Roll

If the storm is love without your degree,
Let your power be a volcano with tempest, your heartbeat, drumbeats, Rock N Roll

Your voice is thundering
While your voice is weaker than your claws,
Let your strength be your voice
Put my love at your strength into your cry
Cast the night into the science
If your cry is stronger than academia and your hope is stronger than your cry
Cast your dreams into the science

Let your power be with the science
Let your voice be with my song

Whisper your power
Build the storm up

Put your science into your talk
Let your talk be with thunder of the manuscript
Shout your talk

Put your science with a tsunami into the paper
Let the paper be with drumbeats of the manuscript
Let the paper be with my song of the manuscript
Let the paper be with drumbeats
Put the paper with a thunderbolt into your thesis
Scream your thesis
```

### The science bit

The ballad simulates a classic population genetics model describing the trajectory of an allele favoured by natural selection in a single locus of an infinite diploid population<sup>1</sup>. Fitness of the genotypes are parameterized as:

	w(AA) = 1 + s
	w(Aa) = 1 + hs
	w(aa) = 1
	
Where `A` is the beneficial mutation.

To change the dominance, switch the line:

* The default mutation has additive effect (h = 0.5): `The effort was irrelevant. Waste.`
* To make it recessive (h = 0): `The effort was irrelevant!`
* To make it dominant (h = 1): `The effort was purposeless!`

To change selection strength:

* The default is s = 0.01: `Your paper is uninspired. scientific megahogwash`
* To make it a stronger mutation with s = 0.1: `Your paper is uninspired. Unwarranted!`
* To make it a weaker mutation with s = 0.001: `Your paper is uninspired. Completely, definitely unqualified`

You can also change the starting frequency of the beneficial mutation (the default is 1%) and the plotting dimensions.

<sup>1</sup> Described in, for instance, equation 1.6 of _Evolutionary Theory: Mathematical and Conceptual Foundations_ (Rice, 2004).

### The coding bit

`popgen.py` contains the simulation and plotting code in readable Python. (Most of the code is dedicated to doing the ASCII plot in an embarassingly bare-bones way.) I adapted the logic into boring ("minimalist") Rockstar; the script `sing.py` converts that into proper ("idiomatic") Rockstar. The final version of the ballad is the idiomatic file plus capitalization and slight reordering of lines.

### Big thank you

...to [Dylan Beattie](https://dylanbeattie.net/) for creating Rockstar and providing the inspiration to become, finally, one of those rockstar scientists everyone keeps talking about.