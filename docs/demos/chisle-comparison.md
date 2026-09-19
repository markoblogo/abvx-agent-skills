# Measured comparison: ABVX and Chisle

Chisle improved diff and tool-output economy without reducing acceptance scores, but increased total tokens. Two unique stopping/scope rules are promoted; the complete Chisle ruleset is not adopted.

The bounded three-arm pilot ran five coding tasks and three explanation tasks.
All raw evidence and limitations are in the
[retained benchmark](../../benchmarks/measured/2026-09-19-chisle/README.md).

| Arm | Checks | Information retained | Total tokens |
|---|---:|---:|---:|
| baseline | 8/8 | 15/15 | 464,553 |
| abvx | 8/8 | 15/15 | 465,792 |
| abvx_chisle | 8/8 | 15/15 | 486,190 |

Adding Chisle to ABVX changed total recorded tokens by **+4.4%**,
with **-36** coding diff lines (-42.4%) and
**-22.7%** tool-output bytes. The bounded port adds only the
first-sufficient-solution stopping rule and an adjacent-scope guard. Chisle
remains a benchmark competitor rather than a global dependency or default
instruction layer.
