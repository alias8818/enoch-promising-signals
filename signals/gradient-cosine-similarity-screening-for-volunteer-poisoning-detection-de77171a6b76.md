# Gradient Cosine-Similarity Screening for Volunteer Poisoning Detection

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gradient-cosine-similarity-screening-for-volunteer-poisoning-detection-de77171a6b76`
Run ID: `gradient-cosine-similarity-screening-for-volunteer-poisoning-detection-de77171a6b76-20260628T155519324316+0000`

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

- Provider-backed Research Facility batch: z-ai/glm-5.2: enoch://research-facility/provider/z-ai/glm-5.2/65bc9827b977

## What looked useful

Cosine similarity is only useful when treated as a two-sided outlier statistic; one-sided low-similarity screening ranked malicious gradients below honest gradients in the tested toy setup. Two-sided cosine screening reached AUROC 1.0 on low/moderate heterogeneity label-flip and backdoor trials, but fell to AUROC 0.746/0.682 for high-heterogeneity label-flip/random-label poisons and was defeated by a median-matched adaptive vector probe.

## Boundaries and scale limits

No real neural network, no real volunteer dataset, no multi-round training, no unknown-malicious-fraction thresholding, and only a vector-level adaptive evasion probe. Results should not be treated as full poisoning-defense validation.

## Claim scope

Synthetic logistic-regression volunteer-gradient screening with 50 volunteers, 10% malicious volunteers, 30 seeds, four non-IID heterogeneity levels, and simple label-flip/random-label/backdoor poisons. Two-sided cosine outlier scoring has useful detection signal at low/moderate heterogeneity but degrades at high heterogeneity; naive low-similarity scoring fails.

## Why it stopped

Synthetic toy evidence supports a mechanism-level signal and exposes failure modes, but it is not direct or robust enough for a paper-positive claim.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should use a small neural network with real per-client gradients and compare two-sided cosine against norm, loss, and robust aggregation baselines under non-IID clients.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small Neural Client-Gradient Validation for Two-Sided Cosine Poison Screening
- Success threshold: Two-sided cosine or a cosine-plus-baseline detector must improve recall@malicious-budget by at least 0.15 over norm-only at matched false-positive rate while reducing attack success without more than 1 percentage point clean-accuracy loss across non-IID settings.
- Stop condition: Stop as negative if cosine adds less than 0.05 AUROC over norm/loss baselines, if high non-IID false positives exceed malicious recall, or if adaptive poisons preserve attack success while evading cosine thresholds.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-cosine-similarity-screening-for-volunteer-poisoning-detection-de77171a6b76`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
