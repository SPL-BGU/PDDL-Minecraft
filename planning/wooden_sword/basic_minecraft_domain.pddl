; PolyCraft basic domain

(define (domain PolyCraft)

    (:requirements :strips :typing :negative-preconditions :fluents)

    (:predicates
        (have_wooden_sword)
    )

    (:functions
        ; Map
        (trees_in_map)

        ; Items
        (count_log_in_inventory)
        (count_planks_in_inventory)
        (count_stick_in_inventory)
    )

    ; Actions
    (:action GET_LOG
        :parameters ()
        :precondition (and
            (>= (trees_in_map) 1)
        )
        :effect (and
            (decrease (trees_in_map) 1)
            (increase (count_log_in_inventory) 1)
        )
    )

    (:action CRAFT_PLANK
        :parameters ()
        :precondition (and
            (>= (count_log_in_inventory) 1)
        )
        :effect (and
            (decrease (count_log_in_inventory) 1)
            (increase (count_planks_in_inventory) 4)
        )
    )

    (:action CRAFT_STICK
        :parameters ()
        :precondition (and
            (>= (count_planks_in_inventory) 2)
        )
        :effect (and
            (decrease (count_planks_in_inventory) 2)
            (increase (count_stick_in_inventory) 4)
        )
    )

    (:action CRAFT_WOODEN_SWORD
        :parameters ()
        :precondition (and
            (>= (count_planks_in_inventory) 2)
            (>= (count_stick_in_inventory) 1)
        )
        :effect (and
            (decrease (count_planks_in_inventory) 2)
            (decrease (count_stick_in_inventory) 1)
            (have_wooden_sword)
        )
    )

)