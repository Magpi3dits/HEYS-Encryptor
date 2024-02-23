# Function to convert a string to its binary representation
def string_to_binary(string):
    return ''.join(bin(ord(char))[2:].zfill(8) for char in string)

def errorHandling():
    print("End of program has been reached.")
    input("Press any button to end.")
    exit()

# Function to convert a binary string to its corresponding hexadecimal representation
def binary_to_hex(binary_str):
    return hex(int(binary_str, 2))[2:].upper()

Complete_Cipher = ""
hex_value = ""
round_count = 1
Ciphers = []


def final_round():

    K = k4

    BIN = hex_to_binary(Complete_Cipher)
    print(Complete_Cipher)
    K_BIN = ''.join(format(int(c, 16), '04b') for c in K)
    print("Binary key:", K_BIN)

    # Key (constant value) - converted to binary
    K_BIN = ''.join(format(int(c, 16), '04b') for c in K)
    print("Binary key:", K_BIN)

    # Perform XOR operation between input binary and key binary
    INPUT = xor_binary(BIN, K_BIN)
    print("XOR result (binary):", INPUT)

    # Convert XOR result from binary to hexadecimal
    hex_output = binary_to_hex(INPUT)
    print("Hex output:", hex_output)

    # Replace characters in hexadecimal output using the conversion table
    print()
    OUTPUT = ''.join(conversion_table.get(char, char) for char in hex_output)
    print("Output:", OUTPUT)

    # Print OUTPUT in binary
    OUTPUT_BINARY = hex_to_binary(OUTPUT)
    print("OUTPUT (binary):", OUTPUT_BINARY)

    K = k5

    # Key (constant value) - converted to binary
    K_BIN = ''.join(format(int(c, 16), '04b') for c in K)
    print("Binary key:", K_BIN)

    # Perform XOR operation between input binary and key binary
    INPUT = xor_binary(OUTPUT_BINARY, K_BIN)
    print("XOR result (binary):", INPUT)

    print("\n\nYour Final Cipher is: ", binary_to_hex(INPUT))

    Ciphers.append(binary_to_hex(INPUT))

    print("\n\n**FINAL RESULTS**\n\n")
    print("Heys Cipher - 1 Round: ", Ciphers[0])
    print("\nHeys Cipher - 2 Round: ", Ciphers[1])
    print("\nHeys Cipher - 3 Round: ", Ciphers[2])
    print("\nHeys Cipher - 4 Round: ", Ciphers[3])

    Ciphers.clear()


# Function to perform XOR operation between two binary strings
def xor_binary(bin_str1, bin_str2):
    return bin(int(bin_str1, 2) ^ int(bin_str2, 2))[2:].zfill(max(len(bin_str1), len(bin_str2)))

def hex_to_binary(hex_string):
    binary_string = ""
    for char in hex_string:
        binary_string += bin(int(char, 16))[2:].zfill(4)
    return binary_string

def hex_to_text(hex_string, encoding='ascii'):
    hex_copy = hex_string
    # Convert hexadecimal string to bytes
    byte_string = bytes.fromhex(hex_string)

    try:
        # Decode bytes to text string using the specified encoding
        text_string = byte_string.decode(encoding)
        return text_string
    except UnicodeDecodeError:
        print("Error: Unable to decode hexadecimal string using the specified encoding.")
        hex_value = 1
        Complete_Cipher = hex_string
        print(hex_value)
        return None


round_count = 1
first_round_done = 0

print(r"""\

 __    __   ___________    ____  _______.     ______  __  .______    __    __   _______ .______
|  |  |  | |   ____\   \  /   / /       |    /      ||  | |   _  \  |  |  |  | |   ____||   _  \
|  |__|  | |  |__   \   \/   / |   (----`   |  ,----'|  | |  |_)  | |  |__|  | |  |__   |  |_)  |
|   __   | |   __|   \_    _/   \   \       |  |     |  | |   ___/  |   __   | |   __|  |      /
|  |  |  | |  |____    |  | .----)   |      |  `----.|  | |  |      |  |  |  | |  |____ |  |\  \----.
|__|  |__| |_______|   |__| |_______/        \______||__| | _|      |__|  |__| |_______|| _| `._____|


   ___               _           _   _              __                       _
  / __\ __ ___  __ _| |_ ___  __| | | |__  _   _    \ \  ___  ___  ___ _ __ | |__
 / / | '__/ _ \/ _` | __/ _ \/ _` | | '_ \| | | |    \ \/ _ \/ __|/ _ \ '_ \| '_ \
/ /__| | |  __/ (_| | ||  __/ (_| | | |_) | |_| | /\_/ / (_) \__ \  __/ |_) | | | |
\____/_|  \___|\__,_|\__\___|\__,_| |_.__/ \__, | \___/ \___/|___/\___| .__/|_| |_|
                                           |___/                      |_|
         ___ ____   ___ ____   ___   ___ _________
 /\ /\  / _ \___ \ / _ \___ \ / _ \ / _ \___ / ___|
/ / \ \/ /_)/ __) | | | |__) | | | | (_) ||_ \___ \
\ \_/ / ___/ / __/| |_| / __/| |_| |\__, |__) |__) |
 \___/\/    |_____|\___/_____|\___/   /_/____/____/


WARNING: This script is janky asf, should still work
IMPORTANT: Any ciphers with 0 may return as non-existent or not print properly. e.g. 00F3 printing to F3.

""")

K = input("Input Key: ")
key = [K[0:4], K[4:8], K[8:12], K[12:16], K[16:20]]

k1 = K[0:4]
k2 = K[4:8]
k3 = K[8:12]
k4 = K[12:16]
k5 = K[16:20]

for i in range(round_count):
    K = ''.join(key[i])

while True:
    split_count = 0
    divide_same_round = 0
    # Input string
    print("\n\n*MAIN MENU*\n\n")

    if Complete_Cipher != None:
        BIN = hex_to_binary(Complete_Cipher)
        K_BIN = ''.join(format(int(c, 16), '04b') for c in K)

    if Complete_Cipher == "":

        print("ONLY INPUT 2 BYTES IF 'NINE', THEN  JUST 'NI!'")
        input_string = input("(type 'quit' to exit) Enter 2 byte string: ")

        # Convert input string to binary
        BIN = string_to_binary(input_string)

        if input_string == "quit":
            break

    if round_count == 1:
        K = k1
    if round_count == 2:
        K = k2
    if round_count == 3:
        K = k3
    if round_count == 4:
        K = k4


    # Key (constant value) - converted to binary
    K_BIN = ''.join(format(int(c, 16), '04b') for c in K)

    # Perform XOR operation between input binary and key binary
    INPUT = xor_binary(BIN, K_BIN)


    conversion_table = {
        '0': 'E', '1': '4', '2': 'D', '3': '1',
        '4': '2', '5': 'F', '6': 'B', '7': '8',
        '8': '3', '9': 'A', 'A': '6', 'B': 'C',
        'C': '5', 'D': '9', 'E': '0', 'F': '7'
    }

    # Convert XOR result from binary to hexadecimal
    hex_output = binary_to_hex(INPUT)

    # Replace characters in hexadecimal output using the conversion table
    OUTPUT = ''.join(conversion_table.get(char, char) for char in hex_output)

    # Print OUTPUT in binary
    OUTPUT_BINARY = hex_to_binary(OUTPUT)

    # Function to split binary string into 4-character chunks
    def split_binary(binary_str):
        return [binary_str[i:i+4] for i in range(0, len(binary_str), 4)]

    # Split OUTPUT_BINARY into 4-character chunks
    output_chunks = split_binary(OUTPUT_BINARY)

    # Print the chunks
    for i, chunk in enumerate(output_chunks):
        print(f"Chunk {i+1}: {chunk}")

    # Extract the first character from each chunk
    first_chars = [chunk[0] for chunk in output_chunks]

    # Print the first characters
    for i, char in enumerate(first_chars):
        print(f"First character {i+1}: {char}")

    print("\n**DEBUGGING STUFF ABOVE, IGNORE IF NOT BROKE**\n")

    # Extract the second character from each chunk
    second_chars = [chunk[1] for chunk in output_chunks]

    BLOCK1 = ''.join(first_chars)
    print("BLOCK1 (binary):", BLOCK1)
    BLOCK1_HEX = binary_to_hex(BLOCK1)
    print("BLOCK1 (hex):", BLOCK1_HEX)

    # Concatenate the second characters into a single variable
    BLOCK2 = ''.join(second_chars)
    print("BLOCK2 (binary):", BLOCK2)
    BLOCK2_HEX = binary_to_hex(BLOCK2)
    print("BLOCK2 (hex):", BLOCK2_HEX)

    # Extract the third character from each chunk
    third_chars = [chunk[2] for chunk in output_chunks]

    # Concatenate the third characters into a single variable
    BLOCK3 = ''.join(third_chars)
    print("BLOCK3 (binary):", BLOCK3)
    BLOCK3_HEX = binary_to_hex(BLOCK3)
    print("BLOCK3 (hex):", BLOCK3_HEX)

    # Extract the fourth character from each chunk
    fourth_chars = [chunk[3] for chunk in output_chunks]

    # Concatenate the fourth characters into a single variable
    BLOCK4 = ''.join(fourth_chars)
    print("BLOCK4 (binary):", BLOCK4)
    BLOCK4_HEX = binary_to_hex(BLOCK4)
    print("BLOCK4 (hex):", BLOCK4_HEX)

    Complete_Cipher = BLOCK1_HEX+BLOCK2_HEX+BLOCK3_HEX+BLOCK4_HEX
    print("Complete Cipher: ", Complete_Cipher)

    Next_Round = hex_to_text(Complete_Cipher)
    print("Text string:", Next_Round)

    Ciphers.append(Complete_Cipher)

    print("\n\nYour Cipher after ", round_count, " round(s) is ", Complete_Cipher + "\n\n")

    round_count = round_count + 1

    input("Press any Enter/Return to continue ...")


    if k2 == '':
        errorHandling()

    if k3 == '':
        errorHandling()

    if k4 == '':
        errorHandling()

    if k5 == '':
        errorHandling()

    if round_count == 4:
        print("FINAL ROUND")
        final_round()
        round_count = 1
        Complete_Cipher = ""
