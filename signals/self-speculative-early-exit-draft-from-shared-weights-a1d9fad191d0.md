# Self-speculative early-exit draft from shared weights

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `self-speculative-early-exit-draft-from-shared-weights-a1d9fad191d0`
Run ID: `self-speculative-early-exit-draft-from-shared-weights-a1d9fad191d0-20260529T083803295554+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/38987278d1af

## What looked useful

Auxiliary exit losses produced high final-layer agreement across two seeds (exit1 mean 0.960, exit2 mean 0.975) and high acceptance-probability proxies (0.962/0.979). A no-auxiliary control had comparable final NLL but much worse exit quality, especially layer 1. Measured speedup varied from positive to negative across auxiliary seeds, showing acceptance alone is insufficient without optimized verification overhead.

## Boundaries and scale limits

No natural-language corpus, no GPT-2-small-class baseline, no GPU/KV-cache optimized serving path, only two auxiliary seeds and one no-auxiliary control on a small synthetic task.

## Claim scope

Toy 4-layer causal Transformer on a synthetic variable-context next-token task: auxiliary-trained shared early exits can closely match the final layer and serve as accurate self-speculative drafts, but naive CPU wall-clock speedup is inconsistent.

## Why it stopped

Closed as no-paper useful signal: toy-scale mechanism evidence is positive/mixed, but throughput robustness and real-model validation are insufficient for a paper claim.

## Recommended next action

Run a bounded GPT-2-small-class real-text follow-up with KV-cache-aware speculative decoding and report acceptance, perplexity, and separated draft/verify/controller timings.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache GPT-2-small validation of shared early-exit self-speculative decoding
- Success threshold: At least 1.20x median wall-clock speedup over full greedy decoding with no final perplexity regression beyond 2% and exit/full top-1 agreement above 0.85 on real text.
- Stop condition: Stop if optimized verification overhead keeps median speedup below 1.05x despite acceptance above 0.85, or if exit supervision causes more than 2% final perplexity regression.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-early-exit-draft-from-shared-weights-a1d9fad191d0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
