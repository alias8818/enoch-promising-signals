# GPU Candidate Buffer Verification With Independent Suffix-Array Cross-Check

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `gpu-candidate-buffer-verification-with-independent-suffix-1956faed0c`
Run ID: `gpu-candidate-buffer-verification-with-independent-suffix-1956faed0c-20260609T021442066517+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: CPU Suffix-Tree Draft for GPU Verification: enoch://control-plane/projects/cpu-suffix-tree-draft-for-gpu-verification-15fc2652ce5c/runs/cpu-suffix-tree-draft-for-gpu-verification-15fc2652ce5c-20260609T001642921234+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/48099f486882

## What looked useful

Tier 1 direct test passed: clean GPU candidate buffers matched suffix-array oracle results exactly on random and repeated-prefix/adversarial 64 KiB inputs; deliberate corruption controls produced mismatches as expected.

## Boundaries and scale limits

Tested only fixed-length exact substring matching on 4 KiB and 64 KiB synthetic texts with one GPU kernel and a simple CPU suffix-array oracle; not validated for large corpora, variable-length queries, approximate matching, concurrent producers, or production transfer costs.

## Claim scope

A CUDA exact-match candidate buffer can be independently cross-checked against a CPU suffix-array oracle with zero discrepancies on controlled 64 KiB random and adversarial texts, and injected buffer corruption is detected.

## Why it stopped

No-paper closure: the Tier 1 controlled direct mechanism test is useful and supported, but it is too small and synthetic for publication-grade validation.

## Recommended next action

Run a medium confirmation with 1-16 MiB texts, variable pattern lengths, optimized suffix-array construction, and an end-to-end comparison against CPU brute-force verification cost.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium-scale GPU candidate-buffer verification with variable-length suffix-array oracle
- Success threshold: All clean cases have zero mismatched queries, all corruption controls are detected, and suffix-array verification is faster than or diagnostically preferable to CPU brute-force verification for at least one non-toy workload.
- Stop condition: Stop if any clean case shows unexplained mismatches, if suffix-array verification is consistently slower than brute-force at all tested sizes, or if memory/runtime exceeds the local medium-run budget.

## Evidence references

- Artifact root: `<local-path>/projects/gpu-candidate-buffer-verification-with-independent-suffix-1956faed0c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
