# AI Assessment 1
# Algorithm 1: Flat Rule-Based Artificial Intelligence
# Dataset: Car Evaluation Dataset
#
# This initial rule-based implementation was developed
# with AI assistance and must be reviewed and tested.
#
# The system uses ordered IF-THEN rules.
# It does not use machine learning.


def classify_car(car):

    # Extract the six vehicle attributes
    buying = car[0]
    maintenance = car[1]
    doors = car[2]
    persons = car[3]
    luggage = car[4]
    safety = car[5]

    # Rule 1: Low safety
    if safety == "low":
        return "unacc"

    # Rule 2: Insufficient passenger capacity
    if persons == "2":
        return "unacc"

    # Rule 3: Very high buying and maintenance costs
    if buying == "vhigh" and maintenance == "vhigh":
        return "unacc"

    # Rule 4: Very good vehicle
    if (
        safety == "high"
        and persons == "more"
        and buying == "low"
        and maintenance == "low"
        and luggage in ["med", "big"]
    ):
        return "vgood"

    # Rule 5: Good vehicle
    if (
        safety == "high"
        and persons != "2"
        and buying in ["low", "med"]
        and maintenance in ["low", "med"]
        and luggage == "big"
    ):
        return "good"

    # Default rule
    return "acc"


# ============================================================
# TEST ALGORITHM 1: FLAT RULE-BASED ARTIFICIAL INTELLIGENCE
# ============================================================

if __name__ == "__main__":

    print("ALGORITHM 1: FLAT RULE-BASED AI")
    print("--------------------------------")

    car1 = ["vhigh", "vhigh", "2", "2", "small", "low"]
    car2 = ["low", "low", "4", "more", "big", "high"]
    car3 = ["med", "med", "4", "4", "med", "med"]

    print("Car 1:", classify_car(car1))
    print("Car 2:", classify_car(car2))
    print("Car 3:", classify_car(car3))

    print("\nFlat Rule-Based AI executed successfully!")
