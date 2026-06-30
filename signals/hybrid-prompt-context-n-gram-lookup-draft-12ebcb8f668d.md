# Hybrid Prompt+Context N-gram Lookup Draft

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hybrid-prompt-context-n-gram-lookup-draft-12ebcb8f668d`
Run ID: `hybrid-prompt-context-n-gram-lookup-draft-12ebcb8f668d-20260621T042405589456+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/4ee2f99f8a58

## What looked useful

Clean probe: hybrid full-candidate accuracy 0.845 versus prompt-only 0.496 and context-only 0.504 over 5408 predictions. Conflict probe: hybrid overall 0.836, but prompt_conflict slice dropped to 0.473 versus prompt-only 1.000, exposing a source-arbitration failure.

## Boundaries and scale limits

Synthetic token data only; no real tokenizer, natural corpus, LLM verification pass, GPU throughput measurement, or end-to-end speculative decoding benchmark.

## Claim scope

A deterministic synthetic retrieval-layer probe shows that prompt+context n-gram lookup can improve exact draft-candidate coverage when relevant continuations are split across prompt and retrieved context, but naive source union can fail when prompt and context share a prefix with conflicting continuations.

## Why it stopped

No-paper closure: this is useful synthetic retrieval-layer evidence, not full validation; naive hybrid lookup also has a reproducible prompt/context conflict failure.

## Recommended next action

Run a bounded real-decoding follow-up that adds source-priority or multi-candidate arbitration to hybrid n-gram lookup and measures accepted speculative tokens plus wall-clock throughput on a small real input-grounded corpus.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hybrid n-gram lookup with source arbitration in real speculative decoding
- Success threshold: Arbitration-aware hybrid improves accepted tokens per verification step by at least 15% over prompt-only lookup and does not reduce exact/quality checks relative to prompt-only on conflict-heavy examples.
- Stop condition: Stop if hybrid accepted-token rate is within 5% of prompt-only or if conflict-heavy examples show a statistically clear rejection/quality regression.

## Evidence references

- Artifact root: `<local-path>/projects/hybrid-prompt-context-n-gram-lookup-draft-12ebcb8f668d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
