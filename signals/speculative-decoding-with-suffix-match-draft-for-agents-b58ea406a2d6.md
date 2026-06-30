# Speculative Decoding with Suffix-Match Draft for Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `speculative-decoding-with-suffix-match-draft-for-agents-b58ea406a2d6`
Run ID: `speculative-decoding-with-suffix-match-draft-for-agents-b58ea406a2d6-20260525T170031439327+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/db0fa7a5e0de

## What looked useful

With draft length 8 and max suffix 12, the repetitive agent-shaped corpus reached 84.78% simulated target-call reduction and 77.38% draft-token acceptance, while a low-repeat agent-shaped corpus did not beat a one-token last-seen baseline. Code and markdown controls also benefited moderately, showing the mechanism is a repetition/cache effect rather than uniquely agent-specific.

## Boundaries and scale limits

CPU-only local benchmark; four corpora; strongest agent result is synthetic; no GPU serving stack, no target-model latency, no private/production traces, and no comparison to learned draft models.

## Claim scope

Online suffix-match drafting can substantially reduce simulated target verification calls on repetitive agent-shaped transcripts under exact-token speculative acceptance, but the observed benefit is conditional on repeated structural continuations and was not validated with a live model or real production agent traces.

## Why it stopped

Bounded proxy evidence supports the mechanism conditionally but is insufficient for paper-positive claims because the strongest agent evidence is synthetic and end-to-end model serving latency was not measured.

## Recommended next action

Stop this run as no-paper useful signal; next concrete test is to run the leakage-safe evaluator on real agent traces and include actual target-model verification latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Suffix-match speculative drafting on real agent traces with live verifier latency
- Success threshold: At least 20% median end-to-end latency reduction over no drafting and at least 10% over the best non-learned cache baseline on real agent traces, with no output divergence.
- Stop condition: Stop if real-trace exact-token acceptance yields less than 10% simulated target-call reduction or if lookup plus verification overhead eliminates latency gains in live serving.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decoding-with-suffix-match-draft-for-agents-b58ea406a2d6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
