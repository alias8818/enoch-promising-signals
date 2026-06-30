# Activation-Reservoir Draft: Reuse Prior Hidden States as Cheap Proposals

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `activation-reservoir-draft-reuse-prior-hidden-states-as-cheap-proposals-824047fc4e1c`
Run ID: `activation-reservoir-draft-reuse-prior-hidden-states-as-cheap-proposals-824047fc4e1c-20260610T085704051278+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5157dfaf44e2

## What looked useful

Raw activation reservoirs improved mean accepted draft length to 0.2773 tokens versus 0.0273 random, 0.1055 unigram, and 0.1797 one-token suffix cache on 256 GPT-2 eval prefixes. The centered-hidden ablation fell below unigram, so the mechanism is mixed and may rely on raw activation anisotropy.

## Boundaries and scale limits

Tested only GPT-2 small, greedy decoding, one corpus split, draft length 4, reservoir size up to 512, and proposal acceptance as a proxy for speculative decoding speed. No end-to-end serving latency, stochastic decoding, larger model, or multi-corpus validation was run.

## Claim scope

On a bounded GPT-2/WikiText-2 validation trace, raw final-token hidden-state nearest-neighbor retrieval can provide cached greedy draft proposals that beat random, unigram, and same-last-token cache controls, but with low absolute accepted-token yield.

## Why it stopped

No-paper useful signal: the direct GPT-2 proxy shows a reproducible raw activation advantage, but acceptance yield is low and the centered ablation weakens the mechanism claim.

## Recommended next action

Run a bounded deepen follow-up across two additional small causal LMs with centered/whitened activation controls and an end-to-end speculative verifier cost model.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation Reservoir Robustness Across Models and Geometry Controls
- Success threshold: Activation retrieval beats the strongest cheap non-activation control by at least 0.10 mean accepted tokens with 95% paired bootstrap CI above zero in raw and centered-or-whitened settings on at least two model/corpus pairs, and projected verification speedup is positive after retrieval cost.
- Stop condition: Stop if centered-or-whitened activation retrieval fails to beat unigram or suffix controls on two model/corpus pairs, or if retrieval cost exceeds projected verification savings.

## Evidence references

- Artifact root: `<local-path>/projects/activation-reservoir-draft-reuse-prior-hidden-states-as-cheap-proposals-824047fc4e1c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
