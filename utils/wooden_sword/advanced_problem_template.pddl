(define (problem ${instance_name})
	(:domain PolyCraft)
	(:objects
		${cell_list} - cell
	)
	(:init ${agent_position} ${air_cells} ${tree_cells}
		(crafting_table_cell crafting_table) ${count_log_in_inventory_initial} ${count_planks_in_inventory_initial} ${count_stick_in_inventory_initial}
	)
	(:goal
		(and
			(have_wooden_sword)
		)
	)
)