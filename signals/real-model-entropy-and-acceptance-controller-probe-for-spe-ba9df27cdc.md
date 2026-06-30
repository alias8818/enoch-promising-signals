# Real-model entropy and acceptance controller probe for speculative decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-model-entropy-and-acceptance-controller-probe-for-spe-ba9df27cdc`
Run ID: `real-model-entropy-and-acceptance-controller-probe-for-spe-ba9df27cdc-20260520T023107177553+0000`

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

- Parent run decision: Unified Entropy and Acceptance Controller for Speculative Decoding: enoch://control-plane/projects/unified-entropy-and-acceptance-controller-for-speculative-decoding-ae0e751c63ff/runs/unified-entropy-and-acceptance-controller-for-speculative-decoding-ae0e751c63ff-20260519T232009327995+0000
- ChatGPT Pro speculative decoding research map 2026-05-19: file://new-chatgpt-pro-ideas-05-19.md
- Spec-Decoding Oracle Trace Ranker: Instrumented DFlash Trace Analysis to Rank 12 Branch Proposals: file://new-chatgpt-pro-ideas-05-19.md

## What looked useful

Entropy is a real acceptance diagnostic: in the 512-token replicate, draft entropy correlated negatively with binary acceptance (Pearson -0.205) and accept probability (Pearson -0.268), with accepted tokens lower entropy than rejected tokens. However, fixed gamma 6 achieved 3.436 generated tokens per target pass, while the entropy+acceptance controller achieved 2.393, 30.4% worse than the best fixed policy.

## Boundaries and scale limits

Small pretrained GPT-2-family models only; hand-written prompts only; logical target-pass metric from exact speculative acceptance simulation; no production batched verification latency, larger model pairs, tuned policies, or broad dataset validation.

## Claim scope

Tier 1 real-model speculative sampling probe with gpt2 target, distilgpt2 draft, eight prompts, and fixed gamma 1/2/4/6 versus acceptance-only and entropy+acceptance controllers. Draft entropy predicts lower acceptance, but the tested entropy+acceptance controller does not beat the best fixed gamma.

## Why it stopped

Direct Tier 1 real-model evidence falsified the success threshold: the entropy+acceptance controller was more than 30% worse than the best fixed draft length on generated tokens per logical target verification pass, although entropy remained predictive of acceptance.

## Recommended next action

Stop this controller design as no-paper evidence; a bounded follow-up should test an entropy-aware controller that only backs off from high gamma after calibrated evidence of rejection cost, using batched verification and at least two target/draft pairs.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated high-gamma entropy backoff for speculative decoding
- Success threshold: Entropy-aware calibrated high-gamma backoff beats the best fixed gamma by at least 5% on generated tokens or wall-clock throughput per target verification pass on both model pairs without reducing exact speculative sampling validity.
- Stop condition: Stop if the calibrated controller fails to beat the best fixed gamma on either model pair, or if entropy/backoff decisions do not explain any throughput gain beyond acceptance-only control.

## Evidence references

- Artifact root: `<local-path>/projects/real-model-entropy-and-acceptance-controller-probe-for-spe-ba9df27cdc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
