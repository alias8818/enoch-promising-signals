# KV-cache attention-pattern draft prediction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-attention-pattern-draft-prediction-d5c41d0f96b2`
Run ID: `kv-cache-attention-pattern-draft-prediction-d5c41d0f96b2-20260529T081140869585+0000`

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

Attention-copy drafting achieved 0.213 next-token accuracy on synthetic induction data versus 0.0997 for a bigram baseline and 0.1039 for shuffled attention; IID control stayed at chance around 0.008. However, last-occurrence successor reached 0.206, so most of the synthetic gain is explainable by cheap lexical recurrence.

## Boundaries and scale limits

Synthetic NumPy-only proxy using simulated induction attention, 5 seeds, 1500 train and 600 test sequences per seed/mode, length 128, vocab 128. No trained transformer, real KV-cache tensors, real text, serving-time latency, or target-model speculative acceptance was tested.

## Claim scope

On a synthetic induction-style recurrence task, simulated attention patterns that point to prior matching tokens can provide useful next-token and short-draft predictions; the effect disappears on IID controls and is only marginally better than a last-occurrence successor heuristic.

## Why it stopped

Proxy-only synthetic evidence supports the mechanism but does not validate the broader KV-cache draft-prediction claim, and the strongest simple baseline nearly matches the attention predictor.

## Recommended next action

Stop this run as no-paper useful-signal evidence; a bounded follow-up should test real small-transformer attention traces against last-occurrence and suffix-copy baselines before any scale-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real small-transformer attention-trace draft prediction versus suffix-copy baselines
- Success threshold: At least +5 absolute percentage points next-token accuracy or +0.10 accepted tokens per position over the strongest suffix-copy/last-occurrence baseline on held-out real text, with no IID or shuffled-attention artifact.
- Stop condition: Stop if real attention features fail to beat the strongest lexical recurrence baseline by the success threshold or if extraction overhead exceeds the saved target-model decoding work.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-attention-pattern-draft-prediction-d5c41d0f96b2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
