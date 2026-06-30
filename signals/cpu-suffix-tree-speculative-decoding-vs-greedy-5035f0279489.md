# CPU suffix-tree speculative decoding vs greedy

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-suffix-tree-speculative-decoding-vs-greedy-5035f0279489`
Run ID: `cpu-suffix-tree-speculative-decoding-vs-greedy-5035f0279489-20260628T121511929945+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6038a796f7be

## What looked useful

Median target-call speedup was 3.25x across 80 cases, but median wall-clock speedup was only 0.15x and no case beat greedy. Suffix-index proposals worked mechanically, but overhead dominated for a cheap CPU target model.

## Boundaries and scale limits

Not tested on real transformer targets, real tokenizers, real prompt distributions, or optimized batched verification. Results should not be generalized to LLM serving without a direct model-based follow-up.

## Claim scope

Bounded CPU proxy with synthetic token streams and a deterministic order-4 n-gram target: suffix-index speculative decoding reduced target calls but did not beat greedy wall-clock.

## Why it stopped

Proxy early falsification: the suffix-index decoder reduced target calls but failed to produce measured CPU wall-clock speedup against greedy in the bounded cheap-target benchmark.

## Recommended next action

Run a bounded direct follow-up with a small CPU transformer target and true block verification; stop this run as a proxy early falsification of the unqualified CPU speedup claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: CPU suffix-index speculation with a real small transformer verifier
- Success threshold: At least 1.2x median wall-clock speedup over greedy on a bounded prompt suite while preserving greedy-equivalent output tokens.
- Stop condition: Stop if median wall-clock speedup remains below 1.0x or if output equivalence fails under deterministic decoding.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-suffix-tree-speculative-decoding-vs-greedy-5035f0279489`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
