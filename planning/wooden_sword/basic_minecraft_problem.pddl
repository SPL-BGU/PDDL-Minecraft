; PolyCraft basic problem

(define (problem basic)

    (:domain PolyCraft)

    (:init
        ; Map
        (= (trees_in_map) 5)

        ; Items
        (= (count_log_in_inventory) 0)
        (= (count_planks_in_inventory) 0)
        (= (count_stick_in_inventory) 0)
    )

    (:goal
        (and
            (have_wooden_sword)
        )
    )
)