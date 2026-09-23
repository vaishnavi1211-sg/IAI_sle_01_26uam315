# Smart Room Cleaning Agent

## Course

02AML204 – Introduction to Artificial Intelligence

## SLE-1: Tooling & AI Contribution Log

### Project Description

The Smart Room Cleaning Agent is a simple rule-based intelligent agent that observes the condition of a room and recommends suitable cleaning actions.

The agent considers three inputs:

- Room condition
- Dust level
- Person presence

Based on these observations, predefined rules are applied to generate cleaning recommendations and a final decision.

### Working of the Agent

1. The user enters the current room condition.
2. The user enters the dust level.
3. The user specifies whether someone is present in the room.
4. The agent validates the inputs.
5. Predefined rules are applied to the observations.
6. Cleaning recommendations are generated.
7. The agent displays a final cleaning decision.

### AI Concept Used

The project demonstrates a **Rule-Based Agent**.

The agent uses predefined `IF-ELSE` rules to make decisions based on the current state of the room.

### Technologies Used

- Python
- Rule-Based Artificial Intelligence

### How to Run

Make sure Python 3 is installed.

Run the following command:

```bash
python smart_room_cleaning_agent.py
