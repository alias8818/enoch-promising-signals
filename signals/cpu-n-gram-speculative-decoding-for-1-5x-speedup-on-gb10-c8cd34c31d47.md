# CPU n-gram speculative decoding for 1.5x speedup on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-n-gram-speculative-decoding-for-1-5x-speedup-on-gb10-c8cd34c31d47`
Run ID: `cpu-n-gram-speculative-decoding-for-1-5x-speedup-on-gb10-c8cd34c31d47-20260528T215959080130+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/0390c3e9c4a0

## What looked useful

Acceptance rate controls viability: repeat-heavy prompts with 69-100% accepted proposal tokens reduced verifier calls and produced 1.84x-4.12x speedups, while natural-prompt acceptance of 0-4.2% produced 0.86x-0.96x speedups.

## Boundaries and scale limits

Only GPT-2 small, three hand-authored prompt classes, 64-128 generated tokens, no real traffic trace, no batching, no server integration, no asynchronous CPU/GPU overlap, and no 7B+ model validation.

## Claim scope

On GB10 with GPT-2 small, batch size 1, fp16 cached greedy decoding, a serial CPU n-gram proposer preserved exact greedy output and exceeded 1.5x only on structured or deliberately repetitive hand-authored prompts; it did not exceed 1.5x on the natural prompt.

## Why it stopped

Direct small-model GB10 evidence is mixed: the mechanism works on repeat-heavy prompts but the tested natural prompt fails the 1.5x target, so this is not publication-grade support for the broad hypothesis.

## Recommended next action

Stop this run as a no-paper useful signal; deepen with a bounded real repeated-prefix workload before making any broader 1.5x claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evaluate CPU n-gram speculative decoding on real repeated-prefix workloads
- Success threshold: Median speedup at least 1.5x with exact greedy output and at least 60% median accepted proposal tokens on the repeated-prefix corpus, while reporting the natural-control result separately.
- Stop condition: Stop if median accepted proposal tokens stay below 40% or median speedup stays below 1.2x on the repeated-prefix corpus after tuning n-gram length and draft length.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-n-gram-speculative-decoding-for-1-5x-speedup-on-gb10-c8cd34c31d47`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
