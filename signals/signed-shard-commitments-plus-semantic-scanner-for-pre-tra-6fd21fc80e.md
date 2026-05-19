# Signed shard commitments plus semantic scanner for pre-training poison detection

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `signed-shard-commitments-plus-semantic-scanner-for-pre-tra-6fd21fc80e`
Run ID: `signed-shard-commitments-plus-semantic-scanner-for-pre-tra-6fd21fc80e-20260519T062604754773+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/f1d01a04c256

## What looked useful

Signed shard commitments detected 24/24 post-signing tamper attempts, but the tested semantic scanner was only a ranking signal for valid signed poisoned shards: mean semantic AUC 0.868 across six runs, yet only 44.4% recall at zero false positives and worse F1/AP than the lexical baseline.

## Boundaries and scale limits

Small synthetic corpus only: 24 shards, 1157 evaluated documents, 36 signed-in poison documents, 24 post-signing tamper attempts, no real web corpus, no adaptive attacker generation, and no downstream model training or backdoor persistence test.

## Claim scope

Controlled synthetic Tier 1 test of Ed25519 signed shard commitments against post-signing poison insertion, plus MiniLM semantic-prototype scanning of signed-in poison documents in otherwise valid signed shards.

## Why it stopped

No-paper closure: controlled direct evidence supports signed commitments for post-signing tamper detection, but early Tier 1 evidence shows the tested semantic scanner is insufficient as a standalone detector for signed-in pre-commit poison.

## Recommended next action

Run a bounded held-out adversarial paraphrase benchmark for a hybrid semantic plus lexical scanner before any model-training persistence experiment.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Held-out adversarial paraphrase benchmark for hybrid signed-shard poison scanning
- Success threshold: Hybrid scanner achieves recall >= 0.85 at false-positive rate <= 0.01 and AP at least 0.15 above lexical baseline across at least five seeds, with no benign rare-trigger controls flagged at the chosen threshold.
- Stop condition: Stop as negative if the hybrid scanner fails to exceed lexical baseline AP by 0.10 or cannot reach recall >= 0.70 at false-positive rate <= 0.01 on the held-out paraphrase set.

## Evidence references

- Artifact root: `<local-path>/projects/signed-shard-commitments-plus-semantic-scanner-for-pre-tra-6fd21fc80e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
