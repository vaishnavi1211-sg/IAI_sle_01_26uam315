# Smart Room Cleaning Agent
# PRN: 26UAM315 
# Name: Vaishnavi Ghodake
# Course: 02AML204 - Introduction to Artificial Intelligence
# SLE-1

def get_room_condition():
    """Get the current room condition from the user."""

    while True:
        condition = input(
            "Enter room condition (clean/dirty): "
        ).strip().lower()

        if condition in ["clean", "dirty"]:
            return condition

        print("Please enter clean or dirty.")


def get_dust_level():
    """Get the dust level from the user."""

    while True:
        dust = input(
            "Enter dust level (low/medium/high): "
        ).strip().lower()

        if dust in ["low", "medium", "high"]:
            return dust

        print("Please enter low, medium, or high.")


def get_person_status():
    """Check whether a person is present in the room."""

    while True:
        status = input(
            "Is anyone present in the room? (yes/no): "
        ).strip().lower()

        if status in ["yes", "no"]:
            return status

        print("Please enter yes or no.")


def cleaning_agent(condition, dust, person):
    """
    Rule-based decision-making agent.

    The agent observes the room condition, dust level,
    and person status and then recommends an action.
    """

    recommendations = []

    # Rule 1: Check room condition
    if condition == "dirty":
        recommendations.append(
            "The room needs cleaning."
        )
    else:
        recommendations.append(
            "The room is already clean."
        )

    # Rule 2: Check dust level
    if dust == "high":
        recommendations.append(
            "Perform deep cleaning because the dust level is high."
        )
    elif dust == "medium":
        recommendations.append(
            "Perform normal cleaning to reduce the dust."
        )
    else:
        recommendations.append(
            "Light cleaning or dusting is sufficient."
        )

    # Rule 3: Check whether someone is present
    if person == "yes":
        recommendations.append(
            "Clean carefully while the person is present."
        )
    else:
        recommendations.append(
            "Cleaning can be performed without disturbing anyone."
        )

    # Final decision
    if condition == "dirty" and dust == "high" and person == "no":
        decision = (
            "Start deep cleaning immediately."
        )
    elif condition == "dirty" and dust == "high":
        decision = (
            "Deep cleaning is required, but avoid disturbing the person."
        )
    elif condition == "dirty":
        decision = (
            "Start regular room cleaning."
        )
    elif dust == "high":
        decision = (
            "The room appears clean, but dusting is required."
        )
    else:
        decision = (
            "No major cleaning is required at the moment."
        )

    return decision, recommendations


def main():

    print("=" * 60)
    print("          SMART ROOM CLEANING AGENT")
    print("=" * 60)

    condition = get_room_condition()
    dust = get_dust_level()
    person = get_person_status()

    decision, recommendations = cleaning_agent(
        condition, dust, person
    )

    print("\n--- AI AGENT ANALYSIS ---")

    print("\nObservations:")
    print(f"Room Condition : {condition}")
    print(f"Dust Level     : {dust}")
    print(f"Person Present : {person}")

    print("\nRecommendations:")

    for number, recommendation in enumerate(
        recommendations, start=1
    ):
        print(f"{number}. {recommendation}")

    print("\nFinal Decision:")
    print(decision)

    print("-" * 60)


if __name__ == "__main__":
    main()
