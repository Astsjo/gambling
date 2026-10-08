def valid_int_input(prompt=""):
    while True:
        try:
            return int(input(prompt).strip().lower())
        except ValueError:
            print("Vänligen ange ett heltal/alternativ.")

def valid_float_input(prompt=""):
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Vänligen ange ett tal.")

def valid_int_string_input(prompt="", allowed_strings=[]):
    while True:
        in_put = input(prompt).strip().lower()

        if in_put in [s.lower() for s in allowed_strings]:
            return in_put
        try:
            return int(in_put)
        except ValueError:
            print("Vänligen välj ett alternativ.")