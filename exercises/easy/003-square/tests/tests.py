def tests(square):
  RED = "\033[91m"
  GREEN = "\033[92m"
  YELLOW = "\033[93m"
  RESET = "\033[0m"

  errors = 0

  print(f"{YELLOW}Running tests...{RESET}\n")

  if square(2) != 4:
    print(f"{RED}✗ square(2) should return 4 but returned {square(2)}{RESET}")
    errors += 1
  else:
    print(f"{GREEN}✓ square(2) returned 4{RESET}")

  if square(5) != 25:
    print(f"{RED}✗ square(5) should return 25 but returned {square(5)}{RESET}")
    errors += 1
  else:
    print(f"{GREEN}✓ square(5) returned 25{RESET}")

  if square(0) != 0:
    print(f"{RED}✗ square(0) should return 0 but returned {square(0)}{RESET}")
    errors += 1
  else:
    print(f"{GREEN}✓ square(0) returned 0{RESET}")

  if square(-3) != 9:
    print(f"{RED}✗ square(-3) should return 9 but returned {square(-3)}{RESET}")
    errors += 1
  else:
    print(f"{GREEN}✓ square(-3) returned 9{RESET}")

  if square(1.5) != 2.25:
    print(f"{RED}✗ square(1.5) should return 2.25 but returned {square(1.5)}{RESET}")
    errors += 1
  else:
    print(f"{GREEN}✓ square(1.5) returned 2.25{RESET}")

  print()

  if errors == 0:
    print(f"{GREEN}All tests passed!{RESET}")
  else:
    print(f"{RED}{errors} test(s) failed.{RESET}")