# Real-tokenizer neural small-LM schema-aware speculative decoding

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `real-tokenizer-neural-small-lm-schema-aware-speculative-de-ddc1bae76a`
Run ID: `real-tokenizer-neural-small-lm-schema-aware-speculative-de-ddc1bae76a-20260520T001050579494+0000`

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

- Parent run decision: Grammar and Schema-Aware Speculative Decoding: enoch://control-plane/projects/grammar-and-schema-aware-speculative-decoding-cb7d3228e5bd/runs/grammar-and-schema-aware-speculative-decoding-cb7d3228e5bd-20260519T234016662262+0000
- Parent run decision: Tokenizer-level schema-aware speculative decoding with small LMs: enoch://control-plane/projects/tokenizer-level-schema-aware-speculative-decoding-with-sma-4a2f61182c/runs/tokenizer-level-schema-aware-speculative-decoding-with-sma-4a2f61182c-20260520T000222714489+0000

## What looked useful

Schema-aware draft masking preserved 100% schema validity but reduced speculative efficiency versus vanilla speculative decoding: trained draft averaged 2.00 vs 2.57 tokens per target call (-22.22%), and weak draft averaged 2.00 vs 2.36 (-14.81%). The wrong-schema control produced 0% canonical-schema validity, confirming the trie constraint was active.

## Boundaries and scale limits

Does not test pretrained transformer LLMs, real prompt-conditioned JSON workloads, stochastic speculative sampling, optimized KV-cache serving latency, or large-scale production inference.

## Claim scope

Bounded local test of schema-aware speculative decoding on synthetic fixed-order JSON using a trained ByteLevel BPE tokenizer, neural GRU target/draft language models, schema-constrained target verification, target-only and vanilla speculative baselines, wrong-schema control, and three fixed seeds.

## Why it stopped

Tier-2 fixed-seed direct metrics with real baseline and ablations did not support the claimed efficiency benefit; schema-aware draft constraints underperformed vanilla speculative decoding in both trained-draft and weak-draft settings.

## Recommended next action

Stop this follow-up as a no-paper bounded negative; only revisit with a new protocol using pretrained transformer target/draft models, prompt-conditioned real JSON tasks, full speculative sampling acceptance, and wall-clock KV-cache serving measurements.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/real-tokenizer-neural-small-lm-schema-aware-speculative-de-ddc1bae76a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
