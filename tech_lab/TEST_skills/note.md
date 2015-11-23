![TEST Debug Flow](/Users/zen1/zen/pythonstudy/tech_lab/TEST_skills/software_test_debug_flow.png)

## Write Testable Softwares

* clean code
* If not clean, refactor
* Should always be able to describe what a module does or how it interact with other code
* no extra threads
* no swamp of global variables
* modules should have unit tests
* when applicable support fault injection
* assertions, assertions, assertions

### Assertions
Notices:
1. Assertions are not used for error handling.
2. NO SIDE EFFECTS
3. NO SILLY ASSERTIONS [assert (1+1) == 2]

Why assertions?
* make code self-checking
* make code fail early, closer to the bug
* assertion lives in interface between modules can assign blame
* document assumptions, preconditions, postconditions, invariants

Statistics
GCC: 9000 assertions
LLVM: 13000 assertions (1.4M line, so 1 assertion per 110 lines)

Tips:
python -O will ignore assertions in code


Enable assertions in production?
When doing daily jobs, NASA engineer enables assertion. Only when the spacecraft trying to land Mars, they disable the assertions.

### Principles

* Interfaces that span trust boundaries are special.  
They must be tested on the full range of representable values.
