# Speculative Decoding with N-gram Baseline for 2x Speedup on Local GPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `speculative-decoding-with-n-gram-baseline-for-2x-speedup-on-local-gpu-63923bf3a233`
Run ID: `speculative-decoding-with-n-gram-baseline-for-2x-speedup-on-local-gpu-63923bf3a233-20260605T080043500140+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/53456ebdc033

## What looked useful

N-gram prompt lookup reduced target forward calls and gave 3.79x speedup on repeated prompts and 2.89x on semi-varied prompts, but only 0.87x on unique-token prompts despite a 2.12x forward-call reduction. The mechanism is useful for copy-heavy contexts, not a general 2x local-GPU speedup.

## Boundaries and scale limits

Tested one small causal LM, single-prompt sequential generation, synthetic prompt modes, 8 prompts per mode, 768-token contexts, and 128 requested new tokens. Did not test 7B-class models, batched serving, real traces, or broader hyperparameter sweeps.

## Claim scope

On GB10 with distilgpt2, Transformers n-gram prompt lookup exceeded 2x throughput only when prompts contained copyable/repeated continuations; it was slower than greedy decoding on a stricter unique-token prompt contrast.

## Why it stopped

Mixed bounded evidence: favorable synthetic copy-heavy prompts support the mechanism, but the strict unique-token contrast is an early falsification of a general 2x speedup claim.

## Recommended next action

Run a bounded deepen test on realistic code/RAG traces, stratified by measured prompt-local n-gram hit rate, before any paper or broad speedup claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-stratified n-gram speculative decoding benchmark
- Success threshold: Show at least 2x tokens/sec on the high-hit-rate trace stratum and no worse than 0.95x on low-hit-rate traces, with exact or prefix parity documented under fixed token accounting.
- Stop condition: Stop if realistic high-hit-rate traces fail to reach 1.5x or low-hit-rate traces remain below 0.95x after one reasonable n-gram hyperparameter sweep.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decoding-with-n-gram-baseline-for-2x-speedup-on-local-gpu-63923bf3a233`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
