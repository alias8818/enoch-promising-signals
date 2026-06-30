# Local Differential Privacy Gradient Compression for Volunteer Nodes

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `local-differential-privacy-gradient-compression-for-volunteer-nodes-a91c581d7d86`
Run ID: `local-differential-privacy-gradient-compression-for-volunteer-nodes-a91c581d7d86-20260611T161653321470+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/6237e930df94

## What looked useful

Magnitude-aware top-k compression was the only tested compressed private mechanism with useful utility: 0.8464 mean accuracy versus 0.8957 dense LDP at 0.0942x upload. Random-k LDP used similar bytes but fell to 0.7540 accuracy, and sign randomized response was near chance at 0.5107. Controls show random-k's private failure is mainly noise amplification, while top-k's loss is mostly compression bias.

## Boundaries and scale limits

Synthetic logistic task only; no formal sparse local-DP proof; no real volunteer network; no deep neural network or language-model gradients; no secure aggregation or adversarial client setting; limited to 80 rounds and five seeds.

## Claim scope

In a five-seed synthetic federated logistic volunteer-node simulation with 80 nodes, 30% dropout, 256-dimensional gradients, client clipping, and nominal Gaussian local-DP-style noise, top-k sparse updates preserved useful accuracy at about 9.4% of dense LDP upload, while random-k LDP and sign randomized response were substantially worse.

## Why it stopped

The result is a bounded synthetic/proxy mechanism test, not a full validation; it identifies a promising top-k direction and early-falsifies naive random-k/sign approaches under this setup, but lacks formal privacy accounting and real-model evidence.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded action is a formal sparse local-DP mechanism and medium-scale real-gradient validation before any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Formal sparse local-DP top-k mechanism on real model gradients
- Success threshold: Top-k-style private sparse mechanism reaches at least 90% of dense-LDP final accuracy with at most 15% of dense upload and no unaccounted privacy step.
- Stop condition: Stop if the formal privacy mechanism requires noise or sensitivity scaling that drops accuracy more than 10 percentage points below dense LDP at the target upload budget.

## Evidence references

- Artifact root: `<local-path>/projects/local-differential-privacy-gradient-compression-for-volunteer-nodes-a91c581d7d86`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
