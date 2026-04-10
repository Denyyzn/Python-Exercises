def tests(absolute_value):
  RED = "\033[91m"
  GREEN = "\033[92m"
  YELLOW = "\033[93m"
  RESET = "\033[0m"

  errors = 0

  print(f"{YELLOW}Running tests...{RESET}\n")

  if absolute_value(10) != 10:
    print(f"{RED}✗ absolute_value(10) should return 10 but returned {absolute_value(10)}{RESET}")
    errors += 1
  else:
    print(f"{GREEN}✓ absolute_value(10) returned 10{RESET}")

  if absolute_value(-7) != 7:
    print(f"{RED}✗ absolute_value(-7) should return 7 but returned {absolute_value(-7)}{RESET}")
    errors += 1
  else:
    print(f"{GREEN}✓ absolute_value(-7) returned 7{RESET}")

  if absolute_value(0) != 0:
    print(f"{RED}✗ absolute_value(0) should return 0 but returned {absolute_value(0)}{RESET}")
    errors += 1
  else:
    print(f"{GREEN}✓ absolute_value(0) returned 0{RESET}")

  if absolute_value(-3.5) != 3.5:
    print(f"{RED}✗ absolute_value(-3.5) should return 3.5 but returned {absolute_value(-3.5)}{RESET}")
    errors += 1
  else:
    print(f"{GREEN}✓ absolute_value(-3.5) returned 3.5{RESET}")

  if absolute_value(8.2) != 8.2:
    print(f"{RED}✗ absolute_value(8.2) should return 8.2 but returned {absolute_value(8.2)}{RESET}")
    errors += 1
  else:
    print(f"{GREEN}✓ absolute_value(8.2) returned 8.2{RESET}")

  print()

  if errors == 0:
    print(f"{GREEN}All tests passed!{RESET}")
  else:
    print(f"{RED}{errors} test(s) failed.{RESET}")