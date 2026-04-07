def tests(is_even):
  RED = "\033[91m"
  GREEN = "\033[92m"
  YELLOW = "\033[93m"
  RESET = "\033[0m"

  errors = 0

  print(f"{YELLOW}Running tests...{RESET}\n")

  if is_even(4) != True:
    print(f"{RED}✗ is_even(4) should return True but returned {is_even(4)}{RESET}")
    errors += 1
  else:
    print(f"{GREEN}✓ is_even(4) returned True{RESET}")

  if is_even(7) != False:
    print(f"{RED}✗ is_even(7) should return False but returned {is_even(7)}{RESET}")
    errors += 1
  else:
    print(f"{GREEN}✓ is_even(7) returned False{RESET}")

  if is_even(0) != True:
    print(f"{RED}✗ is_even(0) should return True but returned {is_even(0)}{RESET}")
    errors += 1
  else:
    print(f"{GREEN}✓ is_even(0) returned True{RESET}")

  if is_even(-2) != True:
    print(f"{RED}✗ is_even(-2) should return True but returned {is_even(-2)}{RESET}")
    errors += 1
  else:
    print(f"{GREEN}✓ is_even(-2) returned True{RESET}")

  if is_even(-3) != False:
    print(f"{RED}✗ is_even(-3) should return False but returned {is_even(-3)}{RESET}")
    errors += 1
  else:
    print(f"{GREEN}✓ is_even(-3) returned False{RESET}")

  print()

  if errors == 0:
    print(f"{GREEN}All tests passed!{RESET}")
  else:
    print(f"{RED}{errors} test(s) failed.{RESET}")