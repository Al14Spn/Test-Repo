print("testul a rulat")

def main():
    message = "Hello, GitHub Actions!"
    print(message)
    return message

if __name__ == "__main__":
    assert main() == "Hello, GitHub Actions!", "Test eșuat!"
