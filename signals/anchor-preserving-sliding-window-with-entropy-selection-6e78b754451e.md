# Anchor-Preserving Sliding Window with Entropy Selection

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-preserving-sliding-window-with-entropy-selection-6e78b754451e`
Run ID: `anchor-preserving-sliding-window-with-entropy-selection-6e78b754451e-20260529T214143314668+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/f90165f6cb55

## What looked useful

Entropy-ranked window selection improved target coverage in high-entropy factual-record contexts, but failed under high-entropy distractors and low-entropy relevant targets, making standalone entropy selection too brittle for a paper claim.

## Boundaries and scale limits

Tested only synthetic 4096-token contexts with span-retention metrics; no model inference, downstream answer accuracy, real corpus, training, or long-context deployment validation.

## Claim scope

Synthetic fixed-budget retention tests show anchor-preserving entropy selection can retain high-entropy fact spans while preserving anchors, but only when entropy is aligned with relevance.

## Why it stopped

Proxy synthetic retention evidence is mixed: the mechanism works in the favorable high-entropy-record regime but is early-falsified as a standalone heuristic by distractor and low-entropy-signal regimes.

## Recommended next action

Stop this run as a no-paper useful signal; next bounded test should combine entropy with query-aware or model-predictive relevance scoring and require improvement under both distractor and low-entropy-target regimes.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Query-Aware Entropy Window Selection Under Distractors
- Success threshold: At equal 1024-token budget, retain 100% anchors and beat the best positional/random baseline by at least 10 percentage points in full-target retention or answer accuracy in all tested regimes, with no collapse below random_windows under high-entropy noise or low-entropy signal.
- Stop condition: Stop if the query-aware variant still underperforms random_windows in either high_entropy_noise or low_entropy_signal after a smoke run and one multi-seed bounded confirmation.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-preserving-sliding-window-with-entropy-selection-6e78b754451e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
