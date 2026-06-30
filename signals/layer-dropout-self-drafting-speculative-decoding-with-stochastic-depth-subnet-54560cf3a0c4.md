# Layer-Dropout Self-Drafting: Speculative Decoding with Stochastic Depth Subnet

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `layer-dropout-self-drafting-speculative-decoding-with-stochastic-depth-subnet-54560cf3a0c4`
Run ID: `layer-dropout-self-drafting-speculative-decoding-with-stochastic-depth-subnet-54560cf3a0c4-20260524T175330956378+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/1d27f25872ce

## What looked useful

Across three seeds, depth-2 stochastic-depth subnets averaged 0.672 speculative acceptance and 1.58x estimated speedup versus 0.323 acceptance and 0.98x for dense, with much lower KL to the full model. The same stochastic-depth models had worse full-depth validation perplexity, averaging 37.38 versus 17.77 dense.

## Boundaries and scale limits

Synthetic corpus only; 6-layer 128-wide model only; 900 training steps; approximate speculative cost model; no real KV-cache latency measurement; no natural-language or GPT-2-small-class validation.

## Claim scope

On a tiny 6-layer synthetic-language Transformer, stochastic-depth training made shallow prefixes substantially closer to the full model and improved local speculative-drafting acceptance versus a same-size dense baseline, but did not preserve full-model validation quality.

## Why it stopped

No-paper closure: local evidence supports the self-drafting mechanism but also shows a large quality penalty, so the current recipe is not paper-positive.

## Recommended next action

Run a bounded quality-matched follow-up that adds auxiliary shallow-head losses or reduces layerdrop rate, requiring full-depth validation perplexity within 10% of dense while preserving depth-2 acceptance above 0.60.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Quality-Matched Layerdrop Self-Drafting With Auxiliary Subnet Losses
- Success threshold: Full-depth validation perplexity within 10% of dense and depth-2 speculative acceptance at least 0.60 with estimated speedup above 1.25x over full-depth decoding.
- Stop condition: Stop if quality-matched variants cannot exceed dense depth-2 acceptance by at least 0.15 absolute or if maintaining acceptance requires more than a 10% full-depth perplexity penalty.

## Evidence references

- Artifact root: `<local-path>/projects/layer-dropout-self-drafting-speculative-decoding-with-stochastic-depth-subnet-54560cf3a0c4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
