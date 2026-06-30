# Layered speculative decoding with adaptive draft depth

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `layered-speculative-decoding-with-adaptive-draft-depth-a4327fd40533`
Run ID: `layered-speculative-decoding-with-adaptive-draft-depth-a4327fd40533-20260611T181751051350+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/ecacc591180f

## What looked useful

Layered adaptive selected on easy/mixed/hard regimes achieved 0.5557 held-out shifted cost/token versus 0.5647 for adaptive-deep, a 1.58% relative reduction with bootstrap 95% CI [-0.01167, -0.00651] cost/token and 16/16 paired seed wins. It also reduced cost by 9.29% versus fixed-deep and 11.73% versus fixed-shallow.

## Boundaries and scale limits

Evidence is proxy-only: synthetic acceptance traces, modeled verifier/draft costs, no real LLM logits, no GPU latency, no KV-cache effects, and no comparison to implemented AdaEDL/SVIP/PACER baselines.

## Claim scope

In a synthetic speculative-decoding cost simulator with calibrated and held-out token-difficulty regimes, a two-layer adaptive draft-depth policy reduced held-out cost per emitted token versus tuned fixed-depth and single deep adaptive baselines.

## Why it stopped

Proxy simulator produced a useful mechanism signal but not direct model or latency evidence; this is no-paper evidence rather than full validation.

## Recommended next action

Run a bounded direct-evidence follow-up using real small-model draft/target logits and compare the layered policy against entropy-based adaptive draft-length baselines before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-logit validation of layered adaptive draft depth
- Success threshold: At least 3% cost/token or wall-clock latency reduction versus the best tuned single adaptive baseline on held-out prompts, with no output-distribution change beyond speculative decoding equivalence.
- Stop condition: Stop if the layered policy fails to beat the best single adaptive baseline by 1% on held-out real-logit traces or if its overhead eliminates modeled gains in measured latency.

## Evidence references

- Artifact root: `<local-path>/projects/layered-speculative-decoding-with-adaptive-draft-depth-a4327fd40533`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
