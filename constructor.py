import sys
import json
import argparse
from utils import WoodenSwordProblemGenerator, PogoStickProblemGenerator


def main(map_size, num_maps_to_generate, task):

    with open('config.json', 'r') as file:
        data = json.load(file)

    if task:
        task = "pogo_stick"
        problem_generator = PogoStickProblemGenerator

        items_range_dict = data["craft_pogo_stick_task"]
        order = ["minecraft:log", "minecraft:planks", "minecraft:stick", "polycraft:sack_polyisoprene_pellets", "polycraft:tree_tap"]
    else:
        task = "wooden_sword"
        problem_generator = WoodenSwordProblemGenerator

        items_range_dict = data["craft_wooden_sword_task"]
        order = ["minecraft:log", "minecraft:planks", "minecraft:stick", "minecraft:wooden_sword"]

    items_range = [items_range_dict[key] for key in order]
    root_dir = f"dataset/{task}"

    # generate problems
    generator = problem_generator(f"{root_dir}/")
    generator.generate_problems(
        num_maps_to_generate=num_maps_to_generate,
        map_size=map_size,
        items_range=items_range,
    )


def validate_map_size(value):
    ivalue = int(value)
    if ivalue < 6:
        raise argparse.ArgumentTypeError(f"Invalid value for --map_size: {value}. Must be >= 6.")
    return ivalue


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate maps based on given parameters.")
    parser.add_argument("--map_size", type=validate_map_size, required=True, metavar='int', help="Size of the map (must be >= 6)")
    parser.add_argument("--num_maps", type=int, required=True, metavar='int', help="Number of maps to generate")
    parser.add_argument("--task", type=int, required=True, choices=[0, 1], help="Task type: 0 for WoodenSword, 1 for PogoStick")

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    main(args.map_size, args.num_maps, args.task)
