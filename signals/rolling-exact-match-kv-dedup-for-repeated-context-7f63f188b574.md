# Rolling exact-match KV dedup for repeated context

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `rolling-exact-match-kv-dedup-for-repeated-context-7f63f188b574`
Run ID: `rolling-exact-match-kv-dedup-for-repeated-context-7f63f188b574-20260531T233120976049+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/14e8254f30b8

## What looked useful

Rolling hashes found repeated token spans in every trial, but learned-position K/V tensors were never equal for repeated spans, and the no-position control only matched at layer 0 before causal context mixing. Deeper K/V tensors diverged with median relative L2 around 0.42-0.56 in the no-position layers and around 0.68-1.01 in learned-position layers.

## Boundaries and scale limits

No pretrained LLM or serving benchmark was run. The result is a mechanistic local falsification of a necessary exact-reuse condition, not a throughput study of approximate or architecture-modified dedup schemes.

## Claim scope

Exact token-span matches do not imply exact K/V tensor equality in an unchanged standard causal transformer with positional and contextual hidden states; tested with a deterministic NumPy causal transformer over 16 trials per condition.

## Why it stopped

Early mechanistic falsification: exact repeated token spans were detected, but the necessary exact K/V tensor equality condition failed under standard causal transformer semantics.

## Recommended next action

Stop this exact-match KV dedup line for unchanged transformers; only revisit with an explicitly modified architecture or non-exact/approximate cache objective and a direct logit-equivalence test.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/rolling-exact-match-kv-dedup-for-repeated-context-7f63f188b574`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
