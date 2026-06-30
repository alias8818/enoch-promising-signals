# Attention-Pattern Lookahead: Predicting Next-Token via KV-Cache Reuse

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `attention-pattern-lookahead-predicting-next-token-via-kv-cache-reuse-25d6866a590d`
Run ID: `attention-pattern-lookahead-predicting-next-token-via-kv-cache-reuse-25d6866a590d-20260529T194603405764+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ec37227404fd

## What looked useful

Adjacent GPT-2 attention maps can have high cosine similarity, but direct reuse does not preserve the value context: held-out mean relative context error was 0.6375 at 128-token blocks and 0.6553 at 256-token blocks; a calibrated self-mass control still had mean errors of 0.5824 and 0.6029. Previous-position logits were also a poor next-token proxy, adding 5.34 to 5.68 NLL.

## Boundaries and scale limits

Single GPT-2-small model, Wikitext-2 validation text, no custom end-to-end speculative decoder, no larger model families, and no learned attention-pattern predictor. Evidence is direct for attention/context reuse metrics and proxy-only for full next-token decoding.

## Claim scope

Bounded early falsification of naive adjacent attention-pattern reuse on GPT-2-small using Wikitext-2 validation blocks of 128 and 256 tokens. The tested reuse method copies the previous token's attention distribution over the KV cache, plus a calibrated self-mass control.

## Why it stopped

Proxy/direct prerequisite test falsified naive adjacent attention-pattern reuse for GPT-2-small; this is an early falsification, not a full validation of all KV-cache reuse variants.

## Recommended next action

Stop this naive-reuse line as no-paper evidence; a bounded follow-up should implement a learned per-head attention/context predictor and require direct next-token NLL preservation before any scale-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned Attention-Context Predictor for KV-Cache Lookahead
- Success threshold: Mean held-out value-context relative error below 0.20 and next-token NLL delta no worse than +0.10 versus original GPT-2-small, with positive estimated compute savings for replaced attention heads/layers.
- Stop condition: Stop if learned prediction cannot beat 0.40 mean held-out value-context relative error or worsens next-token NLL by more than +0.25 after a bounded GPT-2-small evaluation.

## Evidence references

- Artifact root: `<local-path>/projects/attention-pattern-lookahead-predicting-next-token-via-kv-cache-reuse-25d6866a590d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
