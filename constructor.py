from utils import WoodenSwordProblemGenerator, PogoStickProblemGenerator

if __name__ == "__main__":

    map_size = 6
    num_maps_to_generate = 1000
    task = 1  # 0 for WoodenSword, 1 for PogoStick

    if task:
        task = "pogo_stick"
        problem_generator = PogoStickProblemGenerator
        items_range = [8, 8, 8, 0, 0]
    else:
        task = "wooden_sword"
        problem_generator = WoodenSwordProblemGenerator
        items_range = [8, 8, 0, 0]

    root_dir = f"dataset/{task}"
    output_directory_path = f"{root_dir}/{map_size}X{map_size}"

    # generate problems
    generator = problem_generator(f"{root_dir}/")
    generator.generate_problems(
        num_maps_to_generate=num_maps_to_generate,
        map_size=map_size,
        items_range=items_range,
    )
