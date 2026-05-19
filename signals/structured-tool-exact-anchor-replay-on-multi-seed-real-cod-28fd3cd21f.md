# Structured-tool exact-anchor replay on multi-seed real Codex trace splits

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `73`
Project ID: `structured-tool-exact-anchor-replay-on-multi-seed-real-cod-28fd3cd21f`
Run ID: `structured-tool-exact-anchor-replay-on-multi-seed-real-cod-28fd3cd21f-20260516T003402488484+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `73`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 35, "followup": -5, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- strong evidence_strength
- mixed hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Structured-tool exact-anchor replay on multi-seed real Codex trace splits: internal_generated:structured-tool-exact-anchor-replay-on-multi-seed-real-cod-28fd3cd21f

## What looked useful

Exact anchor payloads are a strong sparse replay substrate for real Codex trace facts under structured output: across 720 model rows per condition, exact anchors reached 97.08% accuracy versus 97.36% for full windows, 29.86% for compressed/no-anchor, and 30.56% for hash-only controls. The remaining weakness is model-level compliance robustness, not answer recovery.

## Boundaries and scale limits

The benchmark used multiple-choice command recovery, prompt-level JSON as a tool-style interface, local cached small/medium Qwen-family models, and real trace facts rather than full autonomous downstream replay; only three of four model agents individually exceeded 95% exact-anchor valid parse+citation, so the strict four-compliant-model gate was not met.

## Claim scope

On 180 disjoint held-out command anchors from real local Codex JSONL traces across three fixed seeds and four local model agents, structured exact-anchor replay matched full-event-window answer accuracy within 0.28 percentage points and beat compressed/no-anchor and hash-only controls by 67.22 and 66.53 percentage points respectively, with 98.06% pooled exact-anchor valid parse+citation.

## Why it stopped

Bounded full validation passed the accuracy and pooled compliance thresholds but failed the stricter requirement for at least four individually compliant models; this is a useful mechanism result, not paper-positive evidence.

## Recommended next action

Stop this follow-up as no-paper useful evidence: the Tier 3 direct validation supports the mechanism but fails the strict four-compliant-model publication gate and remains prompt-level rather than a real tool runtime.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/structured-tool-exact-anchor-replay-on-multi-seed-real-cod-28fd3cd21f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
