---

# Lord-Game: The Head that Wears the Crown

Welcome to "The Head that Wears the Crown", an ambitious project that aims to create a dynamic story generator game. Inspired by narrative-driven games like Dwarf Fortress, RimWorld, and Crusader Kings, this game seeks to provide the same sort of structure and player agency with gameplay more akin to that of Sort the Court.

## Project Vision

The gameplay is inspired by the simplicity and charm of the indie game "Sort the Court". Players will face a series of decisions each turn, responding to petitions brought forth by characters. Each decision will shape the simulated world, driven by an underlying logic powered by multiple instances of Language Learning Models (LLMs). 

## Gameplay Mechanics

### Core Gameplay
The gameplay is inspired by the simplicity and charm of the indie game "Sort the Court". Players will face a series of decisions each turn, responding to petitions brought forth by characters. Each decision will shape the simulated world, driven by an underlying logic powered by multiple instances of Language Learning Models (LLMs). 

### Memory
A way for information to be stored and retrieved orderly is essential for this project. The exact implementation is in the works.

### Events Independent from player
To make the world feel alive, the game will feature independent storylines with characters acting on their motivations. Initially, 5-10 characters will be richly detailed, and their actions will unfold each turn. As storylines resolve or new conditions arise, additional characters will be introduced, ensuring a dynamic and chaotic game environment. 

## Development Goals

Currently, this project is undergoing a full rewrite. The current plan is to build up incrimentally. First I'm going to setup documentation and whatever else to get things started right, then I'm going to work on either the GUI or setting up LLM implementations working towards a working build of the core gameplay. If you want to contribute send me a message and I'll formalize this section and whatever else for contribution.

## Current Status

The project is in the early stages of development. I've been working on this project for a bit over 2 months as of June 9th and decided to do a full rewrite. A full, working build isn't something to expect for some time. 

## Getting Started

### Requirements

- Access to LLM via OpenAI API (LM Studio let's you host a pseudo OpenAI server locally)
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
   Follow the prompts to configure your LLM settings and start the game.

## Contribution

We welcome contributions from developers and enthusiasts interested in this project. For more details on contributing, refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file or contact the project maintainer.

## License

This project is licensed under the Unlicense, placing it in the public domain. For more details, see the [LICENSE](LICENSE) file.

## Contact

Creator and Maintainer: MuteMaroonWorm (formerly Neburtron)
- GitHub: [neburtron](https://github.com/neburtron)
- Email: mutemaroonworm@gmail.com
- DeviantArt: [MuteMAR](https://www.deviantart.com/mutemar)


## Inspiration

This project draws significant inspiration from "Sort the Court", an indie game known for its narrative-driven gameplay. To experience it, visit [Sort the Court on Itch.io](https://graebor.itch.io/sort-the-court).


---