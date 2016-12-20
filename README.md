# exo-train
Exercise suited for a code kata

This is heavily inspired (meaning shamelessly stolen) by an exercise from
[Carlo Bottiglieri](https://github.com/inverno).

## Goal
Given a string representation of a train, print an ASCII-art representation of
this train.

* **H**: locomotive `<HHHH` or `HHHH>` (depending on which side of the traiin it is)
* **P**: passenger car `|OOOO|`
* **R**: restaurant car `|hThT|`
* **C**: cargo car `|____|` (when empty) `|^^^^|` (when full)

Cars are attached together by `::`.
