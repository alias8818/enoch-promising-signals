# Real-trace anchor-linked compression replay validation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-trace-anchor-linked-compression-replay-validation-4e06ba330f`
Run ID: `real-trace-anchor-linked-compression-replay-validation-4e06ba330f-20260614T001704566874+0000`

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

- Parent run decision: Trace-Derived Semantic Compression with Anchor-Linked Retrieval: enoch://control-plane/projects/trace-derived-semantic-compression-with-anchor-linked-retrieval-e0259426ab2f/runs/trace-derived-semantic-compression-with-anchor-linked-retrieval-e0259426ab2f-20260613T212251779085+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ffda7f9aacb9

## What looked useful

Anchor-linked compression reached 11/12 exact replay accuracy at 0.75 compression ratio, 0.333 above the best non-anchor baseline. The effect was budget-sensitive and did not meet the same threshold at 0.45, 0.60, or 0.90 ratios.

## Boundaries and scale limits

Single local worker trace; deterministic artifact-derived tasks; exact structured scoring; no model-mediated replay; no independent trace population; no adversarial/noisy anchor ablation.

## Claim scope

In a Tier 1 deterministic replay test over one sanitized local Enoch worker trace, anchor-linked compression improved exact linked-fact replay at a 0.75 fact compression ratio versus no-memory, transcript-search, flat-retrieval, and layered-memory baselines.

## Why it stopped

No-paper useful signal: controlled direct local evidence supports the mechanism at one compression setting, but breadth and robustness are insufficient for publication-grade validation.

## Recommended next action

Run a bounded deepen test on at least 5 independent real worker traces with held-out task generation and noisy/adversarial anchor ablations before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-trace noisy-anchor replay validation for anchor-linked compression
- Success threshold: Mean anchor-linked exact replay accuracy >= 0.85 and >= 0.20 above the best non-anchor baseline across traces, with no single trace below 0.70 accuracy.
- Stop condition: Stop if anchor-linked mean advantage is below 0.10, if noisy anchors collapse accuracy below the best baseline, or if independent trace generation cannot be sanitized reproducibly.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-anchor-linked-compression-replay-validation-4e06ba330f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
