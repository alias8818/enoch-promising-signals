# Dynamic Context N-Gram Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `dynamic-context-n-gram-speculative-decoding-bf6f112e05cc`
Run ID: `dynamic-context-n-gram-speculative-decoding-bf6f112e05cc-20260602T162950631529+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/e5c9324cda0f

## What looked useful

Dynamic context length selection is mechanically viable and exact-output preserving in this probe, but its best measured gain over fixed n=2 was only 0.21 to 0.45 percentage points absolute verifier-call reduction. Confidence gating raised acceptance rate but did not beat dynamic-longest on forward-call count.

## Boundaries and scale limits

Single small verifier model, one public text dataset slice, single-process Python harness, no production KV-cache serving implementation, no batching/concurrency study, and no large chat/code model validation.

## Claim scope

On distilgpt2 greedy decoding over 80 Wikitext-2 test prompts, dynamic longest context n-gram drafting preserved exact greedy output and marginally reduced target verifier forward calls versus fixed n=2 for max_draft 8 and 4.

## Why it stopped

No-paper closure: bounded direct evidence supports only a marginal mechanism signal, not a publication-grade or broadly validated result.

## Recommended next action

Run one bounded deepen follow-up with a KV-cache-aware verifier harness and GPT-2-small-class or larger models; stop unless dynamic policy improves direct verifier calls or end-to-end tokens/sec by at least 5% over fixed n=2.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache-aware dynamic n-gram speculative decoding on larger verifier models
- Success threshold: Dynamic policy achieves at least 5% lower verifier calls per generated token or at least 5% higher end-to-end tokens/sec than fixed n=2, with exact output preservation and no regression larger than 2% on non-repetitive slices.
- Stop condition: Stop if dynamic policy fails to exceed fixed n=2 by 5% on either verifier-call count or end-to-end tokens/sec after the model-size and corpus-slice controls.

## Evidence references

- Artifact root: `<local-path>/projects/dynamic-context-n-gram-speculative-decoding-bf6f112e05cc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
