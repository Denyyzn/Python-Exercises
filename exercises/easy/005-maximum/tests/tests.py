def tests(maximum):
  RED = "\033[91m"
  GREEN = "\033[92m"
  YELLOW = "\033[93m"
  RESET = "\033[0m"

  errors = 0

  print(f"{YELLOW}Running tests...{RESET}\n")

  if maximum(3, 7, 5) != 7:
    print(f"{RED}✗ maximum(3, 7, 5) should return 7 but returned {maximum(3, 7, 5)}{RESET}")
    errors += 1
  else:
    print(f"{GREEN}✓ maximum(3, 7, 5) returned 7{RESET}")

  if maximum(10, 2, 8) != 10:
    print(f"{RED}✗ maximum(10, 2, 8) should return 10 but returned {maximum(10, 2, 8)}{RESET}")
    errors += 1
  else:
    print(f"{GREEN}✓ maximum(10, 2, 8) returned 10{RESET}")

  if maximum(4, 4, 1) != 4:
    print(f"{RED}✗ maximum(4, 4, 1) should return 4 but returned {maximum(4, 4, 1)}{RESET}")
    errors += 1
  else:
    print(f"{GREEN}✓ maximum(4, 4, 1) returned 4{RESET}")

  if maximum(-1, -5, -3) != -1:
    print(f"{RED}✗ maximum(-1, -5, -3) should return -1 but returned {maximum(-1, -5, -3)}{RESET}")
    errors += 1
  else:
    print(f"{GREEN}✓ maximum(-1, -5, -3) returned -1{RESET}")

  if maximum(2.5, 9.1, 4.3) != 9.1:
    print(f"{RED}✗ maximum(2.5, 9.1, 4.3) should return 9.1 but returned {maximum(2.5, 9.1, 4.3)}{RESET}")
    errors += 1
  else:
    print(f"{GREEN}✓ maximum(2.5, 9.1, 4.3) returned 9.1{RESET}")

  print()

  if errors == 0:
    print(f"{GREEN}All tests passed!{RESET}")
  else:
    print(f"{RED}{errors} test(s) failed.{RESET}")