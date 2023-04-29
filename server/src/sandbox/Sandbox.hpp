#pragma once

// use the sandbox on supported platforms, unless disabled
#if defined(__linux__) || defined(__OpenBSD__)

# if !defined(CONFIG_NOSANDBOX)
void sandbox_start();
# else

#include <iostream>

inline void sandbox_start() {
    std::cout << "[WARN] Built without a sandbox" << std::endl;
}

# endif // CONFIG_NOSANDBOX

#else
// stub for unsupported platforms
inline void sandbox_start() {}
#endif
