# Real-token GPT-2-small 4 GiB blockwise AdamW validation

Status: `useful_signal`
Project ID: `real-token-gpt-2-small-4-gib-blockwise-adamw-validation-bcd8476f2b`
Run ID: `real-token-gpt-2-small-4-gib-blockwise-adamw-validation-bcd8476f2b-20260519T051434202826+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/fe090176523b

## What looked useful

Blockwise AdamW eliminated GPU-resident optimizer state for GPT-2-small on real tokens, used 0.922 GiB CPU optimizer state, kept the measured 4 GiB block run's update working set at 0.719 GiB, matched the 5-step standard AdamW loss trajectory, and exercised 162 chunks under a 0.05 GiB artificial block limit. The tradeoff was lower throughput: 254.6 tokens/s versus 1192.5 tokens/s for standard AdamW in the 5-step comparison.

## Boundaries and scale limits

Only 1 smoke step at sequence length 64, 5 controlled comparison steps at batch size 1 sequence length 128, and a 2-step chunking stress run were completed. No exact 4 GiB hard CUDA memory cap, OOM boundary search, long stability run, larger batch/context run, or publication-scale training was performed. Standard AdamW also fit comfortably at this scale.

## Claim scope

Tier 1 direct local validation: a GPT-2-small-class 123.75M parameter model trained for short real-token Wikitext-2 runs on NVIDIA GB10 using a CPU-state blockwise AdamW implementation whose per-block CUDA update working set stayed below 4 GiB and whose short-run loss trajectory matched standard AdamW.

## Why it stopped

No-paper closure: this direct Tier 1 run supports the blockwise optimizer mechanism but does not prove a practical 4 GiB advantage, because standard AdamW also fit easily and was faster at the tested GPT-2-small setting.

## Recommended next action

Run a bounded deepen test with an enforced 4 GiB CUDA memory cap and a batch/context sweep to find a real GPT-2-small configuration where standard AdamW crosses the cap while blockwise AdamW completes 100-500 real-token steps with comparable loss.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Enforced 4 GiB CUDA cap GPT-2-small AdamW boundary test
- Success threshold: Find at least one real-token GPT-2-small configuration under the enforced 4 GiB CUDA cap where standard AdamW OOMs or exceeds the cap and blockwise AdamW completes at least 100 steps, or show that no such boundary exists in the local sweep.
- Stop condition: Stop when a pass/fail boundary is found and verified with repeated runs, or after a predeclared sweep of sequence lengths 128-1024 and the largest feasible batch sizes under the 4 GiB cap shows no blockwise-only feasible region.

## Evidence references

- Artifact root: `<local-path>/projects/real-token-gpt-2-small-4-gib-blockwise-adamw-validation-bcd8476f2b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
