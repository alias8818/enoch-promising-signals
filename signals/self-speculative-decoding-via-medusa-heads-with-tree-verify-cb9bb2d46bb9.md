# Self-Speculative Decoding via Medusa Heads with Tree Verify

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `self-speculative-decoding-via-medusa-heads-with-tree-verify-cb9bb2d46bb9`
Run ID: `self-speculative-decoding-via-medusa-heads-with-tree-verify-cb9bb2d46bb9-20260630T181606907350+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/98573a40af07

## What looked useful

Trained heads achieved 48/48 exact greedy matches, mean acceptance 2.7927 tokens per verified step, 0.7161x baseline forward calls, and 0.9139x baseline wall time; random heads accepted 1.0 token per step and required 2.0x forward calls.

## Boundaries and scale limits

Synthetic deterministic data, tiny transformer, full-context forwards, no optimized KV cache, no production tree-attention kernel, no natural-language or GPT-2-small/7B+ validation.

## Claim scope

On a tiny synthetic causal-transformer task, trained Medusa-style future-token heads with exact path verification preserved baseline greedy output and reduced measured decoding work versus baseline and random-head control.

## Why it stopped

No-paper useful signal: the mechanism worked on a controlled toy model with a random-head control, but direct real-model evidence is still missing.

## Recommended next action

Run a bounded GPT-2-small-class real-text benchmark with KV-cache-aware greedy baseline, trained/fine-tuned Medusa heads, and an optimized or faithfully simulated tree verifier.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small-class Medusa head tree-verify benchmark on real text
- Success threshold: At least 99.9% exact greedy-token agreement or a justified exact-verification fallback, mean accepted tokens above 2.0, and at least 10% wall-clock or forward-work improvement versus KV-cache greedy decoding on the tested prompt set.
- Stop condition: Stop as negative if trained heads average at most 1.5 accepted tokens or fail to improve forward work/wall time after a bounded training sweep with a random-head control.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-decoding-via-medusa-heads-with-tree-verify-cb9bb2d46bb9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
