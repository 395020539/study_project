import socket

# set up the host and port for the server
HOST = 'localhost'
PORT = 8000

# set the timeout value for the socket
TIMEOUT = 10

# create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # set the timeout for the socket
    client_socket.settimeout(TIMEOUT)

    # connect to the server
    client_socket.connect((HOST, PORT))

    # send a message to the server
    message = "Hello, server!"
    client_socket.sendall(message.encode())

    # receive a response from the server
    response = ""
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        response += data.decode()

    # print the response from the server
    print("Response from server:", response)

except socket.timeout:
    print("Connection timed out.")
except ConnectionRefusedError:
    print("Connection refused. Please check if the server is running.")
except Exception as e:
    print("An error occurred:", e)

finally:
    # close the socket
    client_socket.close()



##########################################
import socket
import time

# set up the host and port for the server
HOST = 'localhost'
PORT = 8000

# set the timeout value for the socket
TIMEOUT = 10

# set the maximum number of retries
MAX_RETRIES = 3

# create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# keep track of the number of connection attempts
num_attempts = 0

while num_attempts < MAX_RETRIES:
    try:
        # set the timeout for the socket
        client_socket.settimeout(TIMEOUT)

        # connect to the server
        client_socket.connect((HOST, PORT))

        # send a message to the server
        message = "Hello, server!"
        client_socket.sendall(message.encode())

        # receive a response from the server
        response = ""
        while True:
            data = client_socket.recv(1024)
            response += data.decode()
            if '\n' in response:
                break

        # strip any newline characters from the response
        response = response.strip()

        # print the response from the server
        print("Response from server:", response)

        # break out of the loop if the connection was successful
        break

    except socket.timeout:
        print("Connection timed out.")
    except ConnectionRefusedError:
        print("Connection refused. Please check if the server is running.")
    except Exception as e:
        print("An error occurred:", e)

    # increment the number of connection attempts
    num_attempts += 1

    # wait for a few seconds before retrying
    time.sleep(3)

if num_attempts == MAX_RETRIES:
    print("Failed to connect to the server after", MAX_RETRIES, "attempts.")

# close the socket
client_socket.close()
