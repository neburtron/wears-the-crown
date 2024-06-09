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

1. **Interactive Decision-Making**: Players interact with LLMs to resolve issues presented by characters. Outcomes of decisions are simulated by another LLM instance, affecting the world's state.
2. **Independent Storylines**: Simulate actions of non-player characters (NPCs) independent of the player's decisions, adding depth to the game world.
3. **Resource Management**: Integrate a turn-based card game or idle game mechanics to manage resources, enhancing the gameplay experience without overwhelming computational resources.
4. **Comprehensive Memory System**: Develop a sophisticated memory system to track the world state, character motivations, and player decisions, ensuring consistent and engaging storytelling.

## Current Status

The project is in the early stages of development. I've been working on this project for a bit over 2 months as of June 9th and decided to do a full rewrite. A full, working build isn't something to expect for some time. 

## Getting Started

### Requirements

- Access to LLM via OpenAI API or a local setup (e.g., LM Studio with LLama 2 7B Q8).
- Basic knowledge of Python and command-line operations.

### Installation Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/neburtron/Lord-Game.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Lord-Game
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
- DeviantArt: Linked on GitHub profile

## Inspiration

This project draws significant inspiration from "Sort the Court", an indie game known for its narrative-driven gameplay. To experience it, visit [Sort the Court on Itch.io](https://graebor.itch.io/sort-the-court).

For detailed plans and future updates, refer to [Plans_and_Files.md](plans_and_files.md).

---

---

Please note that you are currently on a free plan which is significantly limited by the number of requests. To increase your quota, you can check available plans [here](https://c7d59216ee8ec59bda5e51ffc17a994d.auth.portal-pluginlab.ai/pricing).

Useful links: [Documentation](https://docs.askthecode.ai), [GitHub](https://github.com/askthecode/documentation), [Twitter](https://twitter.com/askthecode_ai)
