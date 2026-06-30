# Real-trace draft-length controller replay for speculative decoding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `87`
Project ID: `real-trace-draft-length-controller-replay-for-speculative-a24aa55bc1`
Run ID: `real-trace-draft-length-controller-replay-for-speculative-a24aa55bc1-20260629T080152328571+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `87`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 12}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- external source URL present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Learning-to-Draft throughput controller for speculative decoding: enoch://control-plane/projects/learning-to-draft-throughput-controller-20260628/runs/learning-to-draft-throughput-controller-20260628-20260629T072321937838+0000
- Exa/arXiv frontier AI scout shortlist: frontier-ai-scout-exa-arxiv-20260628
- Linear ALI-206 frontier research issue: linear-ALI-206
- Learning-to-Draft throughput controller for speculative decoding: https://arxiv.org/abs/2603.01639v1

## What looked useful

The replay method is viable and quickly exposes that controller gains are highly conditional: fixed K=4 is best at nominal draft_cost=0.12, fixed K changes with hardware cost, and EWMA gains appear only when draft tokens are expensive and remain below 1%.

## Boundaries and scale limits

Teacher-forced real model probability trace only; no measured online KV-cache serving latency, no generated-context trace, one small model pair, one public text corpus, and latency represented by a simple cost proxy.

## Claim scope

Offline replay over a 4064-observation real Pythia-70M/Pythia-410M WikiText-2 acceptance trace shows that simple AIMD/EWMA draft-length controllers do not robustly outperform hindsight-tuned fixed draft lengths under a nominal latency proxy; EWMA only wins by less than 1% when draft-token cost is high.

## Why it stopped

Useful real-trace replay result but no robust adaptive-controller advantage over tuned fixed K; evidence is bounded and proxy-based rather than publication-grade serving validation.

## Recommended next action

Stop paper pursuit for this trace-only result; run a bounded direct online speculative-decoding latency follow-up only if testing whether measured KV-cache latency changes the conclusion.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Measured online speculative decoding latency for EWMA draft-length control
- Success threshold: EWMA or another adaptive controller improves measured tokens/sec by at least 3% over the best tuned fixed K on at least two of three prompt slices without increasing wasted draft tokens by more than 10%.
- Stop condition: Stop if adaptive controllers fail to beat best fixed K by 3% on the first two measured prompt slices or if online latency rankings match the offline replay within 1%.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-draft-length-controller-replay-for-speculative-a24aa55bc1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
