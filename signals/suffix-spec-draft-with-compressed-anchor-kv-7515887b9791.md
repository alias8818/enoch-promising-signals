# Suffix-Spec Draft with Compressed Anchor KV

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-spec-draft-with-compressed-anchor-kv-7515887b9791`
Run ID: `suffix-spec-draft-with-compressed-anchor-kv-7515887b9791-20260609T052400540023+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/df7ee48e93fd

## What looked useful

Sparse/stride anchors at 3.15%, 12.60%, and 25.20% of old-prefix KV tokens achieved teacher top-1-in-compressed-top-5 rates of 0.7222, 0.7702, and 0.8838 versus 0.2525 for no-prefix control. Segment-mean KV compression was worse than no-prefix at 4-32 anchors and only recovered near-full NLL at 64 anchors, about 50% KV retention.

## Boundaries and scale limits

No separate draft model was trained; no full speculative decoding verifier loop was implemented; contexts were short, corpus was small, and the result is not a production or paper-scale validation.

## Claim scope

On a small GPT-2 inference proxy with 128-token anchors and 32-token suffixes, sparse retained anchor KV preserves substantially more full-KV teacher ranking information than a no-prefix control, but naive segment-mean compressed KV fails at aggressive compression.

## Why it stopped

Closed as no-paper useful signal because this was a bounded inference proxy, not a full suffix-spec draft validation; it supports sparse anchor retention but early-falsifies naive mean-compressed KV at aggressive compression.

## Recommended next action

Run a bounded deepen follow-up with an actual speculative decoding loop measuring verifier acceptance rate, exactness, and tokens/s for sparse anchors versus full-KV and trained-draft controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Speculative Decode Acceptance with Sparse Anchor KV
- Success threshold: At 12.5% or lower old-prefix KV retention, sparse-anchor drafting should improve accepted tokens/s by at least 15% over the no-prefix draft control while matching verifier outputs exactly and keeping acceptance within 10% relative of full-KV draft behavior.
- Stop condition: Stop if sparse anchors fail to improve accepted tokens/s over no-prefix control or if exact verifier output equivalence cannot be maintained.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-spec-draft-with-compressed-anchor-kv-7515887b9791`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
