import subprocess
import sys
import os
import re
import difflib

REQUIRED_FILES = ["menuItem.h", "menuItem.cpp", "main.cpp", "makefile", "Output.txt"]
EXEC = "./menu"

def print_result(test_name, passed):
    status = "PASS" if passed else "FAIL"
    print(f"[{status}] {test_name}")


# -----------------------------
# Remove comments + clean code
# -----------------------------
def strip_comments(code):
    code = re.sub(r"//.*", "", code)
    return "\n".join([line.strip() for line in code.splitlines() if line.strip()])


# -----------------------------
# Check required files
# -----------------------------
def check_files():
    existing_files = {f.lower() for f in os.listdir(".")}
    missing = []
    for file in REQUIRED_FILES:
        if file.lower() not in existing_files:
            missing.append(file)

    if missing:
        print("Missing files:", ", ".join(missing))
        return False
    return True
  


# -----------------------------
# Check header file
# -----------------------------
def check_header():
    print("Checking menuItem.h...")
  

    with open("menuItem.h", "r") as f:
        content = strip_comments(f.read())

    # required = [
    #     "class MenuItem",
    #     "MenuItem()",
    #     "MenuItem(",
    #     "set",
    #     "get"
    # ]
    required = [
        r"class\s*MenuItem",
        r"MenuItem\s*\(\s*\)",
        r"MenuItem\s*\(",
        r"setName",
        r"setPrice",
        r"getName",
        r"getPrice",
        r"displayMenuItemData"
    ]

    for func in required:
        if not re.search(func, content):
            print(f"Missing declaration: {func}")
            return False

    return True

    

   


# -----------------------------
# Check cpp file
# -----------------------------
def check_cpp():
    print("Checking menuItem.cpp...")
   

    with open("menuItem.cpp", "r") as f:
        content = strip_comments(f.read())

    # required = [
    #     "MenuItem::MenuItem()",
    #     "MenuItem::MenuItem(",
    #     "setName",
    #     "setPrice",
    #     "getName",
    #     "getPrice"
    # ]
    
    required = [
        r"MenuItem\s*::\s*MenuItem\s*\(\s*\)",
        r"MenuItem\s*::\s*MenuItem\s*\(",
        r"setName",
        r"setPrice",
        r"getName",
        r"getPrice",
        r"displayMenuItemData"
    ]

    for func in required:
        if not re.search(func, content):
            print(f"Missing implementation: {func}")
            return False

    return True

    


# -----------------------------
# Check main file
# -----------------------------
def check_main():
    print("Checking main.cpp...")

    with open("main.cpp", "r") as f:
        content = strip_comments(f.read())

    required = [
        "MenuItem",
        "[",
        "]"
    ]

    missing = [r for r in required if r not in content]

    if missing:
        print(" main.cpp issues:")
        for m in missing:
            print(" -", m)
        return False
    return True

    # print(" main.cpp OK\n")


# -----------------------------
# Build project
# -----------------------------
def build():
    print("Building project...")

    result = subprocess.run(["make"], capture_output=True, text=True)

    if result.returncode != 0:
        print(" Build failed:\n")
        print(result.stderr)
        return False 
    return True

    print(" Build successful\n")


# -----------------------------
# Run program
# -----------------------------
def run_program():
    print("Running program...")

    if not os.path.exists(EXEC):
        print(" Executable not found")
        sys.exit(1)

    result = subprocess.run([EXEC], capture_output=True, text=True)

    if result.returncode != 0:
        print(" Program crashed")
        print(result.stderr)
        sys.exit(1)

    print("Program output captured.")
    return result.stdout.strip()


# ---------------------------
# Run make clean
# ---------------------------
def check_make_clean():
    try:
        subprocess.run(
            ["make", "clean"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=20
        )

        obj_files = [f for f in os.listdir(".") if f.endswith(".o")]
        exe_files = os.path.exists(EXEC)
        # if not os.path.exists(EXEC):
            
        #     sys.exit(1)
        print ("Checking make clean...")

        if exe_files:
            print("Executable menu is not removed.")
            return False 

        if obj_files:
            print("Not all the .o files are removed.")
            return False

        return True

    except Exception:
        return False


# -----------------------------
# Load expected output
# -----------------------------
def load_expected():
    with open("Output.txt", "r") as f:
        return f.read().strip()


# -----------------------------
# Compare outputs
# -----------------------------
def compare_output():
    print("Comparing output with Output.txt...")

    actual = run_program()
    expected = load_expected()

    if actual == expected:
        print("Output matches exactly!")
        return True
    print("Output does NOT match!\nCheck output.txt")
    
# print(" Output does NOT match!\n")

    diff = difflib.unified_diff(
    expected.splitlines(),
    actual.splitlines(),
    fromfile="Expected (Output.txt)",
    tofile="Actual (Program Output)",
    lineterm=""
    )

    print("Difference Report:")
    print("  --- : Expected output")
    print("  +++ : Your program output")
    print("  -   : Line missing or incorrect in your output")
    print("  +   : Line produced by your program that differs from expected")
    print("      : Lines without a symbol match in both outputs")
    print()

    for line in diff:
        if line.startswith("@@"):
            continue
        print(line)
    return False

     
# -----------------------------
# Main
# -----------------------------
def main():
    total = 0
    passed = 0

    

    tests = [
        ("Required Files Exist", check_files),
        ("Header Declarations", check_header),
        ("CPP Implementations", check_cpp),
        ("main.cpp Structure", check_main),
        ("Makefile Builds", build),
        ("Executable Created and Output Matching", compare_output),
        ("Make Clean Works", check_make_clean),
        
        
    ]

    for name, func in tests:
        total += 1
        result = func()
        print_result(name, result)

        if result:
            passed += 1

    if passed == total:
        print("\n======================")
        print("Project Passed")
        print("======================")
        sys.exit(0)
    else:
        print("\n======================")
        print("Project Failed")
        print("======================")
        sys.exit(1)
   


if __name__ == "__main__":
    main()