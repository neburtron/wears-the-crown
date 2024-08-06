# Core structure of project:

I am in the process of rewriting this project and making the core framework actually a framework.

This project is not ready yet for anyone to just look at, if you want to know what's going on message me. I'm going to use this doc as a way to talk about the more general structure of this project because I think that's important.

I want to make a game, that is the end goal, that is the thing that will get the most eyes, and I started this project because I wanted to play the type of game I am working towards. What I want is experemental. I don't know if people have made frameworks for LLMs like the thing I'm working on now or not, but regardless, I am focusing on making the back end as well built as I can not only to make the end product better, but also to open the doors for modding / a more community led whatever for this type of game.

there are several parts to the framework, here's how I'm structuring it:

Front end stuff (GUIs) is it's own chunk, I'm not focusing on it yet because I don't want to, but the stuff I've already built is getting reworked. Most stuff is gonna start off in the terminal, but I'm going for modularity, and I'm focusing on this project again.

Calling LLMs is what I'd consider the back end stuff. This is again, not that big of a thing. It's gonna take a while to do, but I could get it done in under a week. 

Then there's commands the LLM can issue, scripts that do things W the LLMs + commands, and domains that are in charge of how save data is structured + putting the scripts together to make a working game. This is the modular part that I want to be accessible.

Structurally that's how I want things to work. Things are going to be majorly restructured a bunch of times moving forwards, but I've decided this is probably my best bet for structuring this project

