# AI Assessment 1
# Algorithm 2: Hierarchical Rule-Based Artificial Intelligence
# Dataset: Car Evaluation Dataset
# Uses manually designed IF-THEN rules (no machine learning).
# Initial implementation prepared with AI assistance.


# LEVEL 1: Evaluate vehicle price

def evaluate_price(buying, maintenance):

    costs = {
        "low": 0,
        "med": 1,
        "high": 2,
        "vhigh": 3
    }

    total = costs[buying] + costs[maintenance]

    if total <= 1:
        return "affordable"

    elif total <= 3:
        return "moderate"

    else:
        return "expensive"


# LEVEL 1: Evaluate vehicle comfort

def evaluate_comfort(doors, persons, luggage):

    if persons == "2":
        return "insufficient"

    elif luggage == "small" or (
        doors == "2" and persons == "more"
    ):
        return "limited"

    elif (
        persons == "more"
        and luggage == "big"
        and doors in ["4", "5more"]
    ):
        return "spacious"

    else:
        return "adequate"


# LEVEL 2: Evaluate technical characteristics

def evaluate_technical(safety, comfort):

    if safety == "low" or comfort == "insufficient":
        return "unsuitable"

    elif safety == "med" and comfort == "limited":
        return "restricted"

    elif safety == "high" and comfort == "spacious":
        return "excellent"

    elif safety == "high" and comfort == "adequate":
        return "strong"

    else:
        return "standard"


# LEVEL 3: Final vehicle classification

def classify_car(car):

    if len(car) != 6:
        raise ValueError("A car must contain six attributes.")

    buying, maintenance, doors, persons, luggage, safety = car

    price = evaluate_price(buying, maintenance)
    comfort = evaluate_comfort(doors, persons, luggage)
    technical = evaluate_technical(safety, comfort)

    if technical in ["unsuitable", "restricted"]:
        return "unacc"

    elif technical == "standard":

        if price == "expensive":
            return "unacc"

        return "acc"

    elif technical == "strong":

        if price == "affordable":
            return "good"

        elif price == "moderate":
            return "acc"

        return "unacc"

    else:

        if price == "affordable":
            return "vgood"

        elif price == "moderate":
            return "good"

        return "acc"


# TEST ALGORITHM 2

if __name__ == "__main__":

    print("ALGORITHM 2: HIERARCHICAL RULE-BASED AI")
    print("---------------------------------------")

    car1 = ["vhigh", "vhigh", "2", "2", "small", "low"]
    car2 = ["low", "low", "4", "more", "big", "high"]
    car3 = ["med", "med", "4", "4", "med", "med"]

    print("Car 1:", classify_car(car1))
    print("Car 2:", classify_car(car2))
    print("Car 3:", classify_car(car3))

    print("\nHierarchical Rule-Based AI executed successfully!")