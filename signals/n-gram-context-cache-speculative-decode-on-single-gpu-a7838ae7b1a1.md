# N-gram context cache speculative decode on single GPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-context-cache-speculative-decode-on-single-gpu-a7838ae7b1a1`
Run ID: `n-gram-context-cache-speculative-decode-on-single-gpu-a7838ae7b1a1-20260529T113103369558+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e8d22261cc54

## What looked useful

The log case exactly matched greedy output while reducing 96 greedy calls to 12 verifier iterations and measured 5.85x decode-only speedup. Longer repetitive and mixed cases showed apparent speedups but diverged from greedy output at tokens 15 and 59, so correctness is the blocking issue.

## Boundaries and scale limits

Single small model, synthetic prompts, 96-token continuations, Python/PyTorch harness, no production serving backend, no stochastic sampler equivalence test, no 7B+ model or real trace validation.

## Claim scope

On a GB10 GPU with distilgpt2 greedy decoding and synthetic prompts, n-gram context-cache drafting reduced verifier iterations and produced exact speedup on a structured-log workload, but the tested implementation failed exact greedy equivalence on 2 of 3 longer 96-token cases.

## Why it stopped

Bounded direct GPU evidence found a useful mechanism signal but falsified the tested implementation as a reliable exact speculative decoder; speedups with mismatched output are not valid positive evidence.

## Recommended next action

Stop this run as no-paper evidence; the next bounded action is an exactness-first backend follow-up that proves zero mismatches before any larger timing claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Exact n-gram draft acceptance with backend KV-cache validation
- Success threshold: 0 mismatches over 10000 generated tokens and at least 1.5x decode-only speedup on a repeated-context workload versus greedy baseline.
- Stop condition: Stop if any exactness mismatch persists after cache-position handling is fixed, or if exact replay is required and speedup falls below 1.2x.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-context-cache-speculative-decode-on-single-gpu-a7838ae7b1a1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
