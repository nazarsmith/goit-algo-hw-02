from queue import Queue
import time


def generate_request(qq, data):
    request = hash(data)
    qq.put(request)


def process_request(qq):
    if qq.empty():
        print("The queue is empty. Waiting for a request to process..")
        user_input = input("Please enter your requests separated by a comma: ")
        user_input = user_input.split(",")
        return user_input
    else:
        while not qq.empty():
            time.sleep(1)
            request_to_process = qq.get()
            print(f"{request_to_process} has been processed.")
        return []


def main():
    qq = Queue()

    while True:
        user_input = process_request(qq)
        if user_input and user_input[0].lower() in [
            "exit",
            "close",
            "break",
            "stop",
            "done",
            "bye",
            "q",
        ]:
            break
        elif user_input:
            for request in user_input:
                generate_request(qq, request)


if __name__ == "__main__":
    main()
