# Self-Draft Early-Exit Tree Decode

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `self-draft-early-exit-tree-decode-f71824a12b41`
Run ID: `self-draft-early-exit-tree-decode-f71824a12b41-20260608T003136495934+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/7efcb0693f7e

## What looked useful

Layer-5 early-exit top-k logits often contained the final greedy path, reaching 90% full-block inclusion for branch width 8 and draft length 2, but fully materialized trees had prohibitive node counts and the best greedy self-draft result was only 0.902x sequential under the most optimistic verifier factor.

## Boundaries and scale limits

Small prompt set, distilgpt2 only, modeled serving cost rather than a fused KV-cache tree verifier, no benchmark corpus, no production latency measurement, and no 7B-class validation.

## Claim scope

On a bounded distilgpt2 CUDA trace with 20 short prompts, greedy self-drafting from early exits did not beat sequential decoding under an optimistic cost model; late-layer top-k tree inclusion was high but naive full tree materialization was uneconomical.

## Why it stopped

Bounded direct evidence found a real late-layer top-k inclusion mechanism, but both greedy self-drafting and naive full-tree materialization failed to produce a cost advantage under optimistic assumptions; this is an early bounded falsification of the naive efficiency claim, not a full validation.

## Recommended next action

Stop this run as no-paper evidence; the only worthwhile local continuation is a bounded sparse/adaptive tree verifier with a strict node budget and measured wall-clock latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Sparse adaptive early-exit tree decode with measured KV-cache latency
- Success threshold: At least 1.10x measured tokens/sec versus sequential greedy decoding with identical emitted greedy tokens over at least 1,000 decode blocks, including all draft and verifier overhead.
- Stop condition: Stop as negative if the adaptive implementation cannot keep mean draft nodes per block at or below 8, if exact greedy outputs diverge, or if measured speedup is below 1.10x.

## Evidence references

- Artifact root: `<local-path>/projects/self-draft-early-exit-tree-decode-f71824a12b41`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
