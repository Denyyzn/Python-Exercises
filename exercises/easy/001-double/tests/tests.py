def tests(double):
  RED = "\033[91m"
  GREEN = "\033[92m"
  YELLOW = "\033[93m"
  RESET = "\033[0m"

  errors = 0

  print(f"{YELLOW}Running tests...{RESET}\n")

  if double(2) != 4:
    print(f"{RED}✗ double(2) should return 4 but returned {double(2)}{RESET}")
    errors += 1
  else:
    print(f"{GREEN}✓ double(2) returned 4{RESET}")

  if double(7) != 14:
    print(f"{RED}✗ double(7) should return 14 but returned {double(7)}{RESET}")
    errors += 1
  else:
    print(f"{GREEN}✓ double(7) returned 14{RESET}")

  if double(0) != 0:
    print(f"{RED}✗ double(0) should return 0 but returned {double(0)}{RESET}")
    errors += 1
  else:
    print(f"{GREEN}✓ double(0) returned 0{RESET}")

  if double(-3) != -6:
    print(f"{RED}✗ double(-3) should return -6 but returned {double(-3)}{RESET}")
    errors += 1
  else:
    print(f"{GREEN}✓ double(-3) returned -6{RESET}")

  if double(1.5) != 3.0:
    print(f"{RED}✗ double(1.5) should return 3.0 but returned {double(1.5)}{RESET}")
    errors += 1
  else:
    print(f"{GREEN}✓ double(1.5) returned 3.0{RESET}")

  print()

  if errors == 0:
    print(f"{GREEN}All tests passed!{RESET}")
  else:
    print(f"{RED}{errors} test(s) failed.{RESET}")