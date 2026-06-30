# Learning-to-Draft throughput controller for speculative decoding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `87`
Project ID: `learning-to-draft-throughput-controller-20260628`
Run ID: `learning-to-draft-throughput-controller-20260628-20260629T072321937838+0000`

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

- Exa/arXiv frontier AI scout shortlist: frontier-ai-scout-exa-arxiv-20260628
- Linear ALI-206 frontier research issue: linear-ALI-206
- Learning-to-Draft throughput controller for speculative decoding: https://arxiv.org/abs/2603.01639v1

## What looked useful

Linear UCB underperformed badly on the nonlinear draft-length reward surface, while binned contextual UCB recovered most oracle value. The best fixed k remained a very strong baseline, so learning-to-draft needs real traces or workloads with stronger per-context optimal-k variation before paper claims are warranted.

## Boundaries and scale limits

No real draft or target model was run; acceptance distributions, latency curves, and request contexts were synthetic. The tuned run used 8 seeds x 50000 simulated cycles and completed in 88 seconds CPU-only.

## Claim scope

In a synthetic speculative-decoding throughput simulator with four acceptance/latency regimes, a context-binned UCB draft-length controller can match the best fixed draft length on aggregate and beat a naive EWMA heuristic, but it does not robustly outperform the best fixed-k baseline across seeds.

## Why it stopped

Proxy useful-signal result only: the controller did not robustly beat the strongest fixed-k synthetic baseline, and no real-model speculative decoding evidence was produced.

## Recommended next action

Run a bounded real-trace or small live-model follow-up that replays measured acceptance and latency, with success defined as at least 3% paired throughput improvement over the best fixed-k baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace draft-length controller replay for speculative decoding
- Success threshold: At least 3% paired mean tokens/sec improvement over the best fixed-k baseline across at least 20 seeds or trace shards, with the controller within 5% of oracle and no correctness regressions.
- Stop condition: Stop if the controller fails to beat best fixed-k by 1% on paired mean throughput or if EWMA matches the learned controller within 1 percentage point on real traces.

## Evidence references

- Artifact root: `<local-path>/projects/learning-to-draft-throughput-controller-20260628`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
