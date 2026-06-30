# Cosine-audit gradient defense for volunteer CPU federated learning

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cosine-audit-gradient-defense-for-volunteer-cpu-federated-learning-b333dc69c44a`
Run ID: `cosine-audit-gradient-defense-for-volunteer-cpu-federated-learning-b333dc69c44a-20260527T180140374618+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/0b5705bd13e5

## What looked useful

Cosine audit is a cheap directional-poisoning filter in this controlled setting. It cleanly rejects directional attacks and remains effective near coordinate-median breakdown, but it adds little on benign random-noise attacks and needs real-data and adaptive-adversary validation before any paper claim.

## Boundaries and scale limits

Synthetic data only; small logistic model only; no real volunteer-device traces; no communication/dropout simulation; assumes a clean trusted server audit batch; adversaries are non-adaptive and do not optimize updates to pass the cosine audit while remaining harmful.

## Claim scope

In a bounded NumPy federated-learning simulator with synthetic non-IID 10-class data, a multinomial logistic model, 60 clients, 20 sampled clients per round, 30-45% malicious clients, and a small clean server audit batch, non-negative cosine filtering of client gradients rejects sign-flip and systematic label-flip malicious updates and preserves about 99.9% final accuracy where FedAvg, norm clipping, and coordinate median degrade under 45% malicious stress.

## Why it stopped

Proxy-only useful signal: the mechanism is supported in synthetic non-IID logistic FL but not validated on real volunteer CPU federated learning or adaptive attacks.

## Recommended next action

Run a bounded real-benchmark deepen test with an adaptive cosine-aware attacker and an ablation over audit-batch size before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cosine-audit FL on a real benchmark with adaptive cosine-aware poisoning
- Success threshold: Cosine audit or cosine audit plus clipping improves final accuracy by at least 5 percentage points over the best non-cosine baseline under adaptive attack while keeping honest rejection below 15% and adding less than 10% aggregation overhead.
- Stop condition: Stop as unsupported if adaptive positive-cosine poisoning removes the accuracy advantage or if the method requires an audit batch so large that it is impractical for the intended server setting.

## Evidence references

- Artifact root: `<local-path>/projects/cosine-audit-gradient-defense-for-volunteer-cpu-federated-learning-b333dc69c44a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
