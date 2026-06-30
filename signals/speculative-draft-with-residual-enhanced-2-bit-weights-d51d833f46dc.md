# Speculative Draft with Residual-Enhanced 2-Bit Weights

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `speculative-draft-with-residual-enhanced-2-bit-weights-d51d833f46dc`
Run ID: `speculative-draft-with-residual-enhanced-2-bit-weights-d51d833f46dc-20260603T192013637936+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/5bb884061b8a

## What looked useful

Residual correction is a real mechanism for recovering dense-distribution fidelity from plain 2-bit weights, raising mean expected speculative acceptance from 0.7724 to 0.9220 across three seeds, but 4-bit remained better at 0.9544 with lower KL and higher top-1 agreement.

## Boundaries and scale limits

Small character-level MLP only; no transformer attention, tokenizer-level corpus, packed low-bit kernels, KV-cache behavior, wall-clock speculative decoding, or equal-byte residual encoding was tested.

## Claim scope

On a 150k-parameter NumPy character n-gram MLP trained on Tiny Shakespeare, a q2(W)+q2(residual) draft approximation improves exact one-token speculative acceptance versus plain per-row 2-bit quantization, but does not beat a simple per-row 4-bit control.

## Why it stopped

Bounded proxy supports the residual mechanism but early-falsifies the stronger practical claim that residual-enhanced 2-bit weights are compelling as stated, because the residual stream adds storage and a simple 4-bit control is consistently better.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should implement an equal-storage residual encoding in a small transformer draft and require it to beat a 4-bit control on acceptance and measured decode speed.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Equal-storage residual 2-bit draft in a small transformer
- Success threshold: Residual-enhanced 2-bit must beat the 4-bit control by at least 0.02 absolute expected acceptance or 5% wall-clock speculative throughput at equal or lower storage, without worse perplexity than plain 2-bit.
- Stop condition: Stop if residual encoding cannot be made equal-storage/equal-bandwidth to the 4-bit control, or if it fails to beat 4-bit on acceptance in two independent seeds.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-draft-with-residual-enhanced-2-bit-weights-d51d833f46dc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
