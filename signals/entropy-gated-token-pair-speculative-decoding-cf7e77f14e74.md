# Entropy-Gated Token-Pair Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `entropy-gated-token-pair-speculative-decoding-cf7e77f14e74`
Run ID: `entropy-gated-token-pair-speculative-decoding-cf7e77f14e74-20260525T211431116732+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/d943ecaa5e69

## What looked useful

Entropy gating tunes between single-token and always-pair speculation. It reduced target calls versus single-token speculation by up to 14.34% at low draft noise and 5.95% at high draft noise, but always-pair reduced target calls by 25.90-31.64% and dominated composite cost whenever draft-token steps were cheap to moderately cheap. When draft-token steps were expensive enough for gating to win, the gate mostly reverted to single-token behavior.

## Boundaries and scale limits

No neural model was trained or served; pair-head latency was not measured; draft/target mismatch was synthetic; results do not establish large-LM serving gains or paper-ready novelty.

## Claim scope

Controlled Markov-distribution mechanism probe of entropy-gated two-token speculative proposals versus single-token and always-pair baselines across three draft-noise settings, three seeds, and explicit target/draft composite cost ratios.

## Why it stopped

No-paper useful signal: synthetic direct mechanism evidence did not support a robust advantage for entropy-gated token-pair speculation over the stronger of single-token and always-pair baselines.

## Recommended next action

Run a bounded real-logit replay using small pretrained draft/target models and measured pair-proposal latency; stop unless entropy-gated pairs beat both single-token and always-pair policies by at least 5% composite cost.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-logit replay for entropy-gated token-pair speculation
- Success threshold: Entropy-gated pair policy beats both single-token and always-pair baselines by at least 5% composite cost in at least two datasets without increasing output distribution error.
- Stop condition: Stop as negative if gated pairs fail to beat the best baseline by 5% in the real-logit replay or only win by degenerating to single-token behavior.

## Evidence references

- Artifact root: `<local-path>/projects/entropy-gated-token-pair-speculative-decoding-cf7e77f14e74`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
