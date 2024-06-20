(define (problem ${instance_name})
	(:domain PolyCraft)

	(:init ${trees_in_map_initial} ${count_log_in_inventory_initial} ${count_planks_in_inventory_initial} ${count_stick_in_inventory_initial}
	)
	(:goal
		(and
			(have_wooden_sword)
		)
	)
)