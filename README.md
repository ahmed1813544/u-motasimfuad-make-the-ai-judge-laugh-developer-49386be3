# Make the AI Judge Laugh: Developer Excuses

[![Make.fun bounty](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![Rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/ahmed1813544/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![Reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/ahmed1813544/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)

Entry for the [make.fun bounty "Make the AI Judge Laugh: Developer Excuses"](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3).

## The entry

A single funny line a developer gives when code breaks in production, written by `main.py` to `entry.txt`:

> I tested it thoroughly — against a version of production that only exists in my head.

## How it works

`main.py` is a stdlib-only Python program. It writes the line (85 characters, one line) to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). No network, no third-party imports, fully deterministic — two runs produce byte-identical output.

Run it locally:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
