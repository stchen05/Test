```markdown
# Test
test

```

## C++ setup

This workspace includes `test.cpp` (a small "Hello, World!" program).

Quick steps to get C++ working on Windows:

- Install a compiler:
  - MinGW-w64 (recommended lightweight): install via MSYS2 or the MinGW-w64 installer and add the `bin` folder to your PATH.
  - OR Visual Studio Build Tools (MSVC): install the "Desktop development with C++" workload.

- In VS Code you can build using the provided Tasks (open the Command Palette -> `Tasks: Run Build Task`):
  - "Build (g++)" — uses `g++` and produces `${fileBasenameNoExtension}.exe` next to the source file.
  - "Build (MSVC)" — uses `cl.exe` and produces the EXE similarly.

- Debugging:
  - If you have gdb (MinGW), use the "Debug (gdb)" launch configuration.
  - If you're using MSVC, use the "Debug (MSVC)" configuration.

If a compiler isn't on your PATH, install one and restart VS Code. If you'd like, I can detect installed toolchains and try to build `test.cpp` for you.
# Test
test
