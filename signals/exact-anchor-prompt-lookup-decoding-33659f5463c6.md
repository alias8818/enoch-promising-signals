# Exact-Anchor Prompt Lookup Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-anchor-prompt-lookup-decoding-33659f5463c6`
Run ID: `exact-anchor-prompt-lookup-decoding-33659f5463c6-20260524T184227753252+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/5dad48f191a0

## What looked useful

Exact unique-anchor lookup is fast and reliable for clean collision-free prompt protocols, and its practical value is strict abstention on absent or ambiguous anchors. Sentinel-regex framing is not robust to arbitrary unescaped payloads, so exact-anchor decoding needs collision-safe framing before model-facing claims are worth testing.

## Boundaries and scale limits

CPU-only synthetic benchmark; no pretrained LLM, no tokenizer-aware long-context testing, no natural prompt corpus, and no collision-safe serialization beyond the tested sentinel framing.

## Claim scope

On a 4,000-case synthetic benchmark, a deterministic exact-anchor prompt lookup decoder with duplicate abstention answers clean uniquely anchored key/value prompts and abstains on absent, duplicate, typo, and case-variant anchors, but fails when unescaped values contain the sentinel record delimiter sequence.

## Why it stopped

Bounded synthetic evidence supports the mechanism only under clean framing and exposes a protocol failure under delimiter injection; this is useful but not publication-grade direct evidence for LLM decoding.

## Recommended next action

Stop this run as a no-paper useful signal; next run should implement JSON Lines or length-prefixed collision-safe anchor records and rerun the duplicate, missing, typo, prefix, and delimiter adversarial families.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Collision-Safe Exact-Anchor Prompt Lookup Decoding
- Success threshold: At least 99.5% overall accuracy and 100% correct abstention on duplicate_conflict and missing_anchor families, with zero delimiter-in-value failures in the synthetic benchmark.
- Stop condition: Stop if collision-safe framing still fails delimiter or duplicate cases, or if the improvement is only due to changing the target semantics rather than fixing the protocol.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-prompt-lookup-decoding-33659f5463c6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
