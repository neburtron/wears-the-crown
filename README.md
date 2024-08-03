---

# The Head that Wears the Crown

"The Head that Wears the Crown" is an ambitious project inspired by narrative-driven games like Dwarf Fortress, RimWorld, and Crusader Kings. It aims to create a dynamic story generator game with gameplay similar to "Sort the Court," where players make decisions each turn, influencing the simulated world powered by Language Learning Models (LLMs).

## Project Vision
The goal is to give the sort of complete freedom within a world with rules provided by the games mentioned above, but focused around talking to AI agents. Through also simulating the world through LLMs rolling dice, alongside the direct impacts of what you say, hopefully this results in a much more flexable point of contact with the world, enabling you to just invent the combustion engine in the 1300s given way way way too much resources all misalocated towards this ridiculous endevour.

This project started off simple, I wanted sort the court with a text box instead of a binary choice, but I wanted that for the agency it provided. For what I wanted, built in a way that worked effectively, I needed not only structure preventing you from just becoming god because you say so or building a full sized pyramid for 20 gold coins, I needed a solid world, and that's the core of this project now. 

First I plan on working on setting up LLM integration, building frameworks to utilize them effectively without a lot of effort. Second I plan on figuring out what types of objects I want to simulate and setting them up how I want them to run. That second part is most of this project + the only reason I'm writing that part out is to signal that the actual gameplay front end bit that the Lord-Game prototype focused on is one of the last core sections I'm going to focus on. Probably. 

## Current Development

As of now, I've stepped back from my previous prototype, Lord-Game, and decided to focus on the backend. Currently this project is focused on the underlying framework behind this project, having flexable systems that utilize LLMs, giving them input data, a prompt telling them what to do, and a set of commands, that outputs something usable. This is essential to the backend, which is the most pressing and ambitious part of this prototype.

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

## Development Plans

### Overview
Currently, this project is undergoing a full rewrite. The current plan is to build up incrimentally. If you want to help send me a message I'll help you out and get this project in a place where someone else could help meaningfully.

PLANS.md is not currently in use, I'll try and write about whatever major changes I make, but I can't see any amount of people that could be reasonably considered "masses" looking at this project for a good while. Here I'll outline short term plans because I think it's useful for both myself and the later down the road doccumentation of this project.

### Next steps for Project

I've decided to focus first on getting systems that enable LLMs to be useful for this project, second on simulating the world. The first two major commits I made were itterative generation LLM tests, and that's how things are going to continue for the time being.

Next big step forward's gonna be taking the current build and generalizing it, taking the code I wrote for the telephone test and making it so it's no longer hard coded to be the way it is.

From there, I plan on improving code, making new functions and classes, and making experements to see how well things are working and to have some experience + code to steal when I'm using the framework I've setup to make this super radical game.

Other avenues might be coming up too. I have an artist I know and she said she might be willing to make some assets, so front end stuff might be revisited, and for the summer school coding class I was in a week or so ago as of writing this, I made a prototype for an idea that would work really well as the rough 2nd half to gameplay I came up with to deal W LLMs being slow. Something to do with with GOAP peasants and rewards. Did not get close to finishing it, if I revisit it I'm not taking anything but the idea from the old draft + doing that in godot or something and figuring some way to combine A and B.

## Getting Started

NOTE: This isn't a game, nothing works, don't bother going through these steps if you want a working build.

### Requirements

- Access to LLM via OpenAI API (LM Studio let's you host a pseudo OpenAI server locally if you don't have money)
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
   Note: this is not a game yet. You can not play it. Published versions are experements + WIP builds for core, underlying systems.

## Contribution

Send me a message if you're interested in this project. I've put a lot of time into it + learning how to code, and I'd be open to talking with you about it or setting something up for you to do. 

## License

This project is licensed under the Unlicense, placing it in the public domain. For more details, see the [LICENSE](docs/LICENSE) file.

I do not respect copyright laws or the profit motive. I am on the side of art, copyright laws are inherently antithetical to the foundational ideas of artistry. This is my project though. It is my vision, and that vision just so happens to include opening all the doors, with the final end goal being making a structure for a type of game I desperately want to be able to play in a million different variations, letting far more competent individuals take the next steps forwards. This is something I am working on myself. I am open to working with others, and so long as I think your additions aren't in the wrong direction, you can help with development. If I don't like the direction your additions are going in, it's nothing personal, I'm making a framework + a basic proof of concept that utilizes it, make your thing a mod / branch off from my thing, I'd push you to make it a mod so others can use what you made with stuff other people made together to make something even better, but you do you. Yeah. 

I am on the side of art is a quote I got from [CJ the X](https://www.youtube.com/@cjthex), they're responsible for my current philosophy on art, they are cool. 

## Contact

Creator, Lead Designer, and only Maintainer: MuteMaroonWorm (formerly / AKA Neburtron)
- GitHub: [neburtron](https://github.com/neburtron)
- Email: mutemaroonworm@gmail.com
- DeviantArt: [MuteMAR](https://www.deviantart.com/mutemar)


## Inspiration

This project draws significant inspiration from "Sort the Court", an indie game known for its narrative-driven gameplay. To experience it, visit [Sort the Court on Itch.io](https://graebor.itch.io/sort-the-court).


---