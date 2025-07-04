# simple.py
def generate_file():
    with open("build_output/result.txt", "w") as f:
        f.write("This is a generated file from Jenkins build process.\n")

if __name__ == "__main__":
    print("Starting build process...")
    generate_file()
    print("Build process completed.")
