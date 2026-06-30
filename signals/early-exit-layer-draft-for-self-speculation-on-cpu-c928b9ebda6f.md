# Early-Exit Layer Draft for Self-Speculation on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `early-exit-layer-draft-for-self-speculation-on-cpu-c928b9ebda6f`
Run ID: `early-exit-layer-draft-for-self-speculation-on-cpu-c928b9ebda6f-20260629T130651986690+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c3f67e44b264

## What looked useful

Stable and moderate proxy settings achieved 2.29x and 1.52x best speedups, while the unstable low-agreement setting fell to 0.65x of baseline. Acceptance rate was the controlling boundary.

## Boundaries and scale limits

Not a pretrained transformer; no attention, KV cache, tokenizer, real text distribution, tuned early-exit head, or production CPU serving stack. Evidence is local proxy evidence over 384 generated tokens per setting.

## Claim scope

Controlled NumPy residual-stack CPU proxy: early-exit self-speculation improves throughput when early/full top-1 agreement is high enough, but becomes slower when later layers substantially change predictions.

## Why it stopped

Closed as no-paper useful signal because this run is a controlled CPU proxy, not direct pretrained-model validation.

## Recommended next action

Run a bounded direct follow-up on a small pretrained causal transformer with actual early-exit heads or exit projections, measuring top-1 agreement, exact speculative acceptance, and CPU wall-clock speed versus greedy decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained small-transformer CPU early-exit self-speculation check
- Success threshold: At least 1.2x wall-clock speedup over greedy full-model decoding on a fixed prompt set, with exact full-model output equivalence and acceptance rate high enough to explain the speedup.
- Stop condition: Stop if all tested exits have less than 50% acceptance or if best wall-clock speed is below 1.0x greedy baseline after a smoke plus one calibrated prompt batch.

## Evidence references

- Artifact root: `<local-path>/projects/early-exit-layer-draft-for-self-speculation-on-cpu-c928b9ebda6f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
