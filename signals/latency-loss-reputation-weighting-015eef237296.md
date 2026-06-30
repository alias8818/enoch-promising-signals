# Latency-Loss Reputation Weighting

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `latency-loss-reputation-weighting-015eef237296`
Run ID: `latency-loss-reputation-weighting-015eef237296-20260609T221401817569+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e59032affdc1

## What looked useful

Latency-loss reputation acted as a fairness/retention tradeoff rather than a dominant quality optimizer: it reduced slow_bad influence and preserved slow_good clients, but a simpler latency-only baseline achieved better clean test quality in this proxy.

## Boundaries and scale limits

CPU-only NumPy simulation; synthetic data; logistic regression; sampled latency rather than real network delay; no real async server, deep model, real dataset, adversarial clients, or large-scale deployment.

## Claim scope

In a synthetic asynchronous/federated logistic-regression proxy with fast_good, slow_good, fast_noisy, and slow_bad client groups, a smoothed latency-loss reputation rule improved clean test loss over FedAvg while retaining far more slow_good weight than latency-only weighting, but it did not beat latency-only on clean test accuracy or loss.

## Why it stopped

Proxy evidence is mixed: the rule improves over FedAvg but loses to a simpler latency-only baseline on clean test quality, so this is useful no-paper evidence rather than a full validation.

## Recommended next action

Stop paper path for this formula; run a bounded follow-up grid that tunes latency/loss/freshness weights and requires both clean-loss competitiveness with latency-only and slow_good retention above 0.75 of FedAvg.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pareto-tuned latency-loss reputation weighting
- Success threshold: On at least 30 held-out seeds, tuned reputation has mean clean loss no more than 0.002 worse than latency_only, mean accuracy no more than 0.001 worse than latency_only, and slow_good/fast_good weight ratio at least 0.75.
- Stop condition: Stop if no tuned configuration satisfies the clean-loss and slow_good-retention thresholds on held-out seeds, or if gains appear only on training/search seeds.

## Evidence references

- Artifact root: `<local-path>/projects/latency-loss-reputation-weighting-015eef237296`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
