// REQUIRES: shell
// RUN: %clangxx -S -ftime-trace -mllvm --time-trace-granularity=0 -o %T/check-time-trace-blocks %s
// RUN: cat %T/check-time-trace-blocks.json | %python %s/check-time-trace-blocks.py

template <typename T>
void foo(T) {}
void bar() { foo(0); }
