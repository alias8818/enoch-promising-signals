# Local Cascade Router with Tiny Confidence Oracle

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `local-cascade-router-with-tiny-confidence-oracle-bee70431d20c`
Run ID: `local-cascade-router-with-tiny-confidence-oracle-bee70431d20c-20260524T071643017596+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2f1443c8e737

## What looked useful

The tiny oracle reduced strong-model routing slightly on average, but only 5/30 trials met the favorable route-without-accuracy-loss criterion and measured oracle overhead made average cost slightly worse than max-confidence routing.

## Boundaries and scale limits

Small built-in classification datasets only; no LLMs, no generative decoding, no batching effects, no production serving latency, and no large/overnight validation.

## Claim scope

A 30-trial sklearn proxy test of a local cascade found that a four-feature logistic confidence oracle over cheap-model probabilities did not reliably improve measured cost-accuracy tradeoffs over max-confidence thresholding.

## Why it stopped

Proxy early falsification: the tiny confidence oracle was not a reliable practical improvement over max-confidence thresholding in the bounded local cascade test.

## Recommended next action

Stop this proxy as no-paper useful signal; only revisit with a direct local LLM cascade benchmark that compares against max-confidence routing with measured end-to-end latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct Local LLM Cascade Confidence Router Benchmark
- Success threshold: Tiny oracle achieves at least 10% lower measured latency or strong-model call rate than max-confidence routing at no more than 1 percentage-point held-out accuracy loss on both tasks.
- Stop condition: Stop if the oracle fails to beat max-confidence routing by 10% on either task or if router overhead consumes the latency savings.

## Evidence references

- Artifact root: `<local-path>/projects/local-cascade-router-with-tiny-confidence-oracle-bee70431d20c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
