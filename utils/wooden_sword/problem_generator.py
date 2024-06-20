import os
import json

from typing import List, Dict, Tuple
from pathlib import Path

from pddl_plus_parser.problem_generators import get_problem_template

import random

SEED = 63
random.seed(SEED)


class ProblemGenerator:
    def __init__(self, output_dir="dataset/"):
        self.example_map_path = "utils/wooden_sword/wooden_sword.json"
        self.output_directory_path = Path(output_dir)

        self.domain = "planning/wooden_sword/basic_minecraft_domain.pddl"

    def basic_pddl_minecraft_generate(
        self,
        instance_name: str,
        trees_in_map: int,
        count_log_in_inventory: int,
        count_planks_in_inventory: int,
        count_stick_in_inventory: int,
    ) -> str:
        """
        Generate a single basic planning problem instance.

        :instance_name: the name of the problem instance.
        :trees_in_map: the number of trees in the map.
        :count_log_in_inventory: the number of logs in the inventory.
        :count_planks_in_inventory: the number of planks in the inventory.
        :count_stick_in_inventory: the number of sticks in the inventory.
        """
        template = get_problem_template(
            Path("utils/wooden_sword/basic_problem_template.pddl")
        )
        template_mapping = {
            "instance_name": instance_name,
            "trees_in_map_initial": f"(= (trees_in_map) {trees_in_map})",
            "count_log_in_inventory_initial": f"(= (count_log_in_inventory) {count_log_in_inventory})",
            "count_planks_in_inventory_initial": f"(= (count_planks_in_inventory) {count_planks_in_inventory})",
            "count_stick_in_inventory_initial": f"(= (count_stick_in_inventory) {count_stick_in_inventory})",
        }
        return template.substitute(template_mapping)

    def advanced_pddl_minecraft_generate(
        self,
        instance_name: str,
        map_size: int,
        crafting_table_cell: int,
        agent_position: int,
        tree_positions: List[int],
        count_log_in_inventory: int,
        count_planks_in_inventory: int,
        count_stick_in_inventory: int,
    ) -> str:
        """
        Generate a single advanced planning problem instance.

        :instance_name: the name of the problem instance.
        :map_size: the size of the map.
        :crafting_table_cell: the cell of the crafting table.
        :agent_position: the cell of the agent.
        :tree_positions: the cells of the trees.
        :count_log_in_inventory: the number of logs in the inventory.
        :count_planks_in_inventory: the number of planks in the inventory.
        :count_stick_in_inventory: the number of sticks in the inventory.
        """
        template = get_problem_template(
            Path("utils/wooden_sword/advanced_problem_template.pddl")
        )
        template_mapping = {
            "instance_name": instance_name,
            "cell_list": " ".join(
                [f"cell{i}" for i in range(map_size) if i != crafting_table_cell]
            ),
            "agent_position": f"(position cell{agent_position})",
            "air_cells": " ".join(
                [
                    f"(air_cell cell{i})"
                    for i in range(map_size)
                    if i not in tree_positions and i != crafting_table_cell
                ]
            ),
            "tree_cells": " ".join([f"(tree_cell cell{i})" for i in tree_positions]),
            "count_log_in_inventory_initial": f"(= (count_log_in_inventory) {count_log_in_inventory})",
            "count_planks_in_inventory_initial": f"(= (count_planks_in_inventory) {count_planks_in_inventory})",
            "count_stick_in_inventory_initial": f"(= (count_stick_in_inventory) {count_stick_in_inventory})",
        }
        return template.substitute(template_mapping)

    def generate_maps(
        self, map_json: Dict, map_size: int, max_num_trees: int, items_range: List[int]
    ) -> Tuple[List, List, List, List, Dict]:
        """
        Generate a single planning problem instance into the given map.
        Returns a objects in the map, agent starting location, initial inventory and inventory counting.
        """
        generator = lambda: [
            random.randint(2, map_size - 1),
            4,
            random.randint(2, map_size - 2),
        ]

        forbidden_locations = set()
        one_space = lambda x: [x[0], x[1], x[2] + 1]
        two_space = lambda x: [x[0], x[1], x[2] + 2]

        num_trees = random.randint(0, max_num_trees)
        tree_locations_in_map = []

        # crafting table location
        crafting_table_location_in_map = generator()
        forbidden_locations.add(str(crafting_table_location_in_map))
        forbidden_locations.add(str(one_space(crafting_table_location_in_map)))
        objects_in_map = [
            {
                "blockPos": crafting_table_location_in_map,
                "blockName": "minecraft:crafting_table",
            }
        ]

        # agent location
        while (
            agent_starting_location := generator()
        ) == crafting_table_location_in_map:
            pass
        forbidden_locations.add(str(agent_starting_location))

        # trees in map
        for _ in range(num_trees):
            # find a new location, save two spaces for place tree tap
            found = True
            tries = 0
            while found and tries < 100:
                new_point = generator()
                new_point_1 = one_space(new_point)
                new_point_2 = two_space(new_point)
                new_lst = [str(new_point), str(new_point_1), str(new_point_2)]
                found = str(new_point) in forbidden_locations
                found = any(item in forbidden_locations for item in new_lst)
                tries += 1

            if tries == 100:
                break

            forbidden_locations.add(str(new_point))
            forbidden_locations.add(str(one_space(new_point)))
            forbidden_locations.add(str(two_space(new_point)))

            tree_locations_in_map.append(new_point)
            objects_in_map.append(
                {
                    "blockPos": new_point,
                    "blockName": "tree",
                }
            )

        # initial inventory
        initial_inventory = {
            "pos": [3, 4, 6],
            "name": "Add Items 1",
            "color": -256,
            "type": "ADD_ITEMS",
            "canProceed": False,
            "isDone": False,
            "completionTime": 0,
            "uuid": "b6ae0b79-e683-4c8a-b33c-39659562c617",
            "itemList": [],
        }

        items = [
            "minecraft:log",
            "minecraft:planks",
            "minecraft:stick",
            "minecraft:wooden_sword",
        ]

        items_count = {}

        for j, (item, item_range) in enumerate(zip(items, items_range)):
            num_items = random.randint(0, item_range)
            items_count[item] = num_items
            if num_items == 0:
                continue
            initial_inventory["itemList"].append(
                {
                    "slot": j,
                    "itemDef": {
                        "itemName": item,
                        "itemMeta": 0,
                        "count": num_items,
                    },
                }
            )

        # update json
        map_json["features"][0]["pos"] = agent_starting_location
        map_json["features"][1]["pos2"] = [map_size + 1, 6, map_size + 1]
        map_json["features"][2]["blockList"] = objects_in_map
        map_json["features"][3]["pos2"] = [map_size + 1, 4, map_size + 1]
        map_json["features"].insert(5, initial_inventory)

        return (
            tree_locations_in_map,
            crafting_table_location_in_map,
            agent_starting_location,
            initial_inventory["itemList"],
            items_count,
        )

    def generate_problems(
        self,
        num_maps_to_generate: int = 100,
        map_size: int = 30,
        basic_only: bool = False,
        items_range: list = [8, 8, 0, 0],
    ) -> None:
        """
        Generate problems using the example map.
        :param num_maps_to_generate: number of maps to generate
        """

        generated_maps = {}

        if basic_only:
            output_directory_path = self.output_directory_path / "basic"
        else:
            output_directory_path = (
                self.output_directory_path / f"{map_size}X{map_size}"
            )
        if not os.path.exists(output_directory_path):
            os.makedirs(output_directory_path)
        else:
            raise Exception(f"Directory {output_directory_path} already exists")

        i = -1
        while (i := i + 1) < num_maps_to_generate:
            with open(self.example_map_path, "r") as map_file:
                map_json = json.load(map_file)
            (
                tree_locations_in_map,
                crafting_table_location_in_map,
                agent_starting_location,
                initial_inventory,
                items_count,
            ) = self.generate_maps(
                map_json, map_size, map_size * int(map_size / 3), items_range
            )

            # check if duplicte
            tree_count = len(tree_locations_in_map)
            if basic_only:
                generated_map = str([tree_count] + initial_inventory)
            else:
                generated_map = str(
                    tree_locations_in_map
                    + crafting_table_location_in_map
                    + agent_starting_location
                    + initial_inventory
                )
            if generated_map in generated_maps:
                i -= 1
                continue

            # generate basic minecraft pddl
            problem = output_directory_path / f"basic_map_instance_{i}.pddl"
            with open(problem, "wt") as problem_file:
                problem_file.write(
                    self.basic_pddl_minecraft_generate(
                        instance_name=f"instance_{i}",
                        trees_in_map=tree_count,
                        count_log_in_inventory=items_count["minecraft:log"],
                        count_planks_in_inventory=items_count["minecraft:planks"],
                        count_stick_in_inventory=items_count["minecraft:stick"],
                    )
                )

            generated_maps[generated_map] = True

            # generate advanced minecraft pddl
            if not basic_only:
                transform_to_cell = lambda x: (x[0] - 1) + ((x[2] - 1) * map_size)
                tree_positions = []
                for tree_location in tree_locations_in_map:
                    tree_positions.append(transform_to_cell(tree_location))
                crafting_table_cell = transform_to_cell(crafting_table_location_in_map)
                agent_position = transform_to_cell(agent_starting_location)

                with open(
                    output_directory_path / f"advanced_map_instance_{i}.pddl", "wt"
                ) as problem_file:
                    problem_file.write(
                        self.advanced_pddl_minecraft_generate(
                            instance_name=f"instance_{i}",
                            map_size=map_size**2,
                            crafting_table_cell=crafting_table_cell,
                            agent_position=agent_position,
                            tree_positions=tree_positions,
                            count_log_in_inventory=items_count["minecraft:log"],
                            count_planks_in_inventory=items_count["minecraft:planks"],
                            count_stick_in_inventory=items_count["minecraft:stick"],
                        )
                    )
