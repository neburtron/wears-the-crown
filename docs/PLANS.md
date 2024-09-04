# Planning document

Right now, the plan is to work on making a simple prototype that runs for several turns and making this framework as easy to work with as possible.

## Readable

I don't think this project is all that readable. I haven't written much for comments / docstrings, and I am not 100% happy with the way things are structured. I'll fix things as I think of ways to fix them, this has been a thing I've been working on since the beginning, and I did a full rewrite near the start of this month.

## prototype

There's a handful of agents with some very basic info in json format. Lets say these are advisors.

These advisors come to the king each turn reporting back on what happened the previous turn, and asking for new orders.

There is info about the local area around the town and info like gold reserves in the treasury stored.

Each turn, the LLMs go through the conversation, update their info / memory json, and decide what to do next.

They do what they set out to do, what happens is evaluated, yeah.

This is a very basic rundown of what I want, technical implementation is gonna be something else.

That said, here's the main elements that are gonna be needed for this:
    Lord game's Conversation.py written better W bells and whistles
    LLM model tasked with determining outcomes of attempted task
    Contemplation script for agents where their info is updated, and they decide what they want to do.
    World / local region state management

Failstates and values like gold reserves are the last thing to add before promoting this
Also maybe some basic GUI or something.
