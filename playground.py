import os
import logging
import commands
from generation import TurnedGenerate

logging.basicConfig(level=logging.INFO)


        
# Main function to set up directories and run the TurnedGenerate process.
def main(save, prompt):
    start_directory = os.path.join("saves", save, "start")  # Source path
    generate_directory = os.path.join("saves", save, "testing")  # Output path
    
    commands.create_directory(generate_directory)
    turns = 5
    logging.info(f"Starting generation process with {turns} turns.")

    try:
        generate = TurnedGenerate(run_for_turns=turns, directory=generate_directory, source=start_directory, prompt=prompt)
        generate.main()
        logging.info("Generation process completed successfully.")
    except Exception as e:
        logging.error(f"Error during generation process: {e}")