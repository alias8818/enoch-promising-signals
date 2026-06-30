# CPU n-gram speculative drafting for small models

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-n-gram-speculative-drafting-for-small-models-a27043b68172`
Run ID: `cpu-n-gram-speculative-drafting-for-small-models-a27043b68172-20260608T013235243210+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/4dc5f69bcaa8

## What looked useful

Prompt lookup drafting is exact and can reduce verifier calls when target predictions align with local prompt copies, but acceptance collapses for a more selective target; longer prompts increased draft attempts without rescuing acceptance.

## Boundaries and scale limits

No direct neural Transformer, llama.cpp, quantized LLM, KV-cache, or production serving validation was run. The target is a controlled n-gram CPU LM, so neural batching and model-kernel costs are proxied rather than measured.

## Claim scope

Bounded CPU benchmark using a word-level n-gram target on Tiny Shakespeare: prompt n-gram drafting can reduce verifier iterations 2.0-3.1x for a repetition-friendly 3-gram target, but gives only about 1.06-1.11x ideal call reduction and slower measured runtime for a more selective 5-gram target.

## Why it stopped

No-paper useful signal: this is a controlled proxy/early mechanism test, not full validation on small neural models.

## Recommended next action

Run a bounded direct neural follow-up with a quantized CPU LM and real speculative verifier path; stop paper consideration until median tokens/s improves by at least 1.20x with exact output parity.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU neural validation of prompt n-gram speculative drafting
- Success threshold: At least 1.20x median tokens/s over greedy decoding with exact output parity and no p95 latency regression above 10% on the prompt class claimed.
- Stop condition: Stop if acceptance stays below 20% or median throughput stays below 1.05x for all draft lengths on the direct neural target.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-n-gram-speculative-drafting-for-small-models-a27043b68172`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
