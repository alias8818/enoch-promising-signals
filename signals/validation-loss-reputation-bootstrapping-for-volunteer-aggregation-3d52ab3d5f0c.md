# Validation-Loss Reputation Bootstrapping for Volunteer Aggregation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `validation-loss-reputation-bootstrapping-for-volunteer-aggregation-3d52ab3d5f0c`
Run ID: `validation-loss-reputation-bootstrapping-for-volunteer-aggregation-3d52ab3d5f0c-20260523T174954461831+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/6bdd29b01892

## What looked useful

Validation-loss reputation produced high adversary-separation AUCs (1.000 sign-flip, 0.9998 label-flip, 0.9614 random-vector) and improved over FedAvg in all 30 main seeds. It was not uniformly superior to coordinate median: random-vector mean test loss was 0.2915 for ValRep versus 0.2818 for median.

## Boundaries and scale limits

Only synthetic binary classification was tested. No real federated benchmark, large neural model, adaptive attacker, Sybil/collusion pressure, privacy analysis, or production volunteer-system overhead was tested. Main runs used 10 seeds per attack type and completed locally in seconds.

## Claim scope

In a bounded synthetic federated logistic-regression simulation with 80 volunteer clients, 30% adversaries, noisy/skewed clients, and a clean heldout validation set, EMA validation-loss reputation can identify harmful clients and improve aggregation versus FedAvg and trimmed mean; it beats coordinate median for sign-flip and label-flip attacks but not random-vector attacks.

## Why it stopped

No-paper useful signal: the result supports the mechanism in synthetic/proxy experiments, but it is not a full validation and is mixed against coordinate median.

## Recommended next action

Run a bounded real federated benchmark follow-up with non-IID client partitions, a frozen heldout validation set, coordinate-median and trimmed-mean controls, and at least one adaptive validation-aware attacker.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Federated Benchmark Test for Validation-Loss Volunteer Reputation
- Success threshold: ValRep improves mean test loss over FedAvg by at least 10%, is no worse than coordinate median by more than 2% in every attack setting, and maintains harmful-client AUC >= 0.90 across at least 5 seeds.
- Stop condition: Stop if ValRep fails to improve over FedAvg in two attack settings or trails coordinate median by more than 5% mean test loss in any adaptive attack setting.

## Evidence references

- Artifact root: `<local-path>/projects/validation-loss-reputation-bootstrapping-for-volunteer-aggregation-3d52ab3d5f0c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
