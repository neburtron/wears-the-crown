---
# The Head that Wears the Crown
"The Head that Wears the Crown" is an ambitious project inspired by narrative-driven games like Dwarf Fortress, RimWorld, and Crusader Kings. It aims to create a dynamic story generator game with gameplay similar to "Sort the Court," where players make decisions each turn, influencing the simulated world powered by Language Learning Models (LLMs).

## Project Vision
The goal is to give the sort of complete freedom within a world with rules provided by the games mentioned above, but focused around talking to AI agents. Through also simulating the world through LLMs rolling dice, alongside the direct impacts of what you say, hopefully this results in a much more flexable point of contact with the world, enabling you to just invent the combustion engine in the 1300s given way way way too much resources all misalocated towards this ridiculous endevour.

This project started off simple, I wanted sort the court with a text box instead of a binary choice, but I wanted that for the agency it provided. For what I wanted, built in a way that worked effectively, I needed not only structure preventing you from just becoming god because you say so or building a full sized pyramid for 20 gold coins, I needed a solid world, and that's the core of this project now. 

First I plan on working on setting up LLM integration, building frameworks to utilize them effectively without a lot of effort. Second I plan on figuring out what types of objects I want to simulate and setting them up how I want them to run. That second part is most of this project + the only reason I'm writing that part out is to signal that the actual gameplay front end bit that the Lord-Game prototype focused on is one of the last core sections I'm going to focus on. Probably. 

## Current Development
As of now, I've stepped back from my previous prototype, Lord-Game, and decided to focus on the backend. Currently this project is focused on the underlying framework behind this project. Right now I've got the absolute basics down. I've got a working GUI, a base to the LLM module, the way I want to handle different types of games figured out, basically everything but a working prototype and the logic / scripts they use to do work. None of it is good, but it's better than what I had and what I haven now is a lot more expandable and modular.

### Development Progression
I started by taking old code from my lord-game project, and got the basic framework setup, nothing to comment on.

First major step was the "Telephone" commit. Here I took more old code from lord-game, conversation.py's class, and just put it in and changed it to use old outputs, and it kinda freaked out. Got something working, and that was a good first proper step.

Second major step was the "Better than Telephone" commit. This was like halfway through a java / processing summer school class I just finished last week, so I came back to this project with new skillz. I decided to make a new prototype where more than one bit of data was given to the LLM, and I got a list of like 12 quotes / whatever from ChatGPT. I thought I'd leave a test run of the system in the files in case it didn't run on other devices, but that's like 80 useless txt files clogging up the commit logs.

At this point, I was familiar enough with classes to know that there was no reason for what I made to be a class. I made it a series of functions, and there were some pretty significant changes to the code if I remember correctly.

Third major step's the "update" commit. Just did it like half an hour ago, and decided to dejure focus on larger named commits after I posted it. Lots of changes, first and foremost reclassified the telephone script, but this time actually utilizing classes properly, having the main functionality in one class + handling multiple turns of the first class, handled by another class in the same file. Moved both to a new doc (generation.py), having a function call the second function that handles mutliple turns of stuff to have the same aprox. functionality, but better for future development. The code was also improved in various other ways, I think substantially.

Other changes include:
- Making the save management stuff in commands handled by a class
- Messing with main.py for that change
- Fixed the last_tab_index spelling mistake in llm_interface so it'd stop giving that error
- Changed thing var to save in main.py because thing's not a good name

Update 4: not interesting to read about backend stuff

Added src folder + did some rework of stuff directly working W LLM APIs
Smaller changes
Doesn't really matter, no one's using these early dev versions.

Update 5: The one I haven't commited yet

Bigger one, worked on this for most of today.

Got rid of playground + replaced W start of domains
Played with generation.py a bit (not staying as it is for any amount of time)
Modularized a bunch
I also wrote some stuff in docs/documentation

This is a pretty substantial update, the only reason this is as short as it is, is because I don't want to go into more detail for the "modularized a bunch" point. Non-existant fans, I've made a ton of progress and I'm not slowing down, mark my words, this will be something by the end of August. School starts up again, so that's kinda the cut off point / boundry of uncertainty. I'll still work on it to be clear, but school's a thing.

## Development Plans

### Overview
Currently, this project is undergoing a full rewrite. The current plan is to build up incrimentally. If you want to help send me a message I'll help you out and get this project in a place where someone else could help meaningfully.

PLANS.md has some information about the direction I want this project to go in, but it isn't in depth, and doccumenting this project is gonna be shotty for a while longer.

### Next steps for Project

I have other stuff going on in my life and I don't know how active I'm gonna be on this project. That said, the current plan is to make a working, very very simple prototype, that forces me to develop some basic functionality and make the framework better. I have the most basic of stuff built, now I need to work on prototypes to help develop the internals that make this a useful framework.

docs/PLANS has more on the first prototype idea I think I'm gonna go with.

## Getting Started

NOTE: This isn't a game, nothing works, don't bother going through these steps if you want a working build.

### Requirements

- Access to LLM via OpenAI API (LM Studio let's you host a pseudo OpenAI server locally if you don't have money, Huggingface is not yet implemented properly)
- Basic knowledge of Python and command-line operations.

### Installation Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/neburtron/wears-the-crown.git
   ```
2. Navigate to the project directory:
   ```bash
   cd wears-the-crown
   ```
3. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the main script:
   ```bash
   python main.py
   ```
   Note: I do not have a playable version, the vast majority of this project is setup and engine code, unless you wanna make something of your own with this, there's no point in running it.

## Contribution

I am currently working on doccumenting this project better and making the code I have better and hardly anyone has seen this project. If you're interested in talking / whatever send me a message, otherwise I'm gonna work on fixing this project into something that other people can understand and work with.

## License

This project is licensed under the Unlicense, placing it in the public domain. For more details, see the [LICENSE](docs/LICENSE) file.

I do not respect copyright laws or the profit motive. I am on the side of art, copyright laws are by design opposed to artistry. This is my project, I am the lead vision behind it, but I resend my monopolistic hold on the pieces that make it up and their design. It is my vision, and that vision just so happens to include opening all the doors of the structure I intend to build. If you want to help by all means, but it is my project and I'm in charge, fork it if you want to go in another direction, more art is better than less art.

I am on the side of art is a quote I got from [CJ the X](https://www.youtube.com/@cjthex), they're responsible for my current philosophy on art, they are cool. 

## Contact

Creator, Lead Designer, and only Maintainer: MuteMaroonWorm (formerly / AKA Neburtron)
- GitHub: [neburtron](https://github.com/neburtron)
- Email: mutemaroonworm@gmail.com
- DeviantArt: [MuteMAR](https://www.deviantart.com/mutemar)

## Inspiration

This project draws significant inspiration from "Sort the Court", an indie game known for its narrative-driven gameplay. To experience it, visit [Sort the Court on Itch.io](https://graebor.itch.io/sort-the-court).

---