# Function to get a random string based on the current time appended to the string "test_file"

def get_random_title():
    import time
    return "test_file_" + str(time.time()).replace(".", "") + ".txt"
