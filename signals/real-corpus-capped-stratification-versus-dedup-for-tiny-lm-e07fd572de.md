# Real-corpus capped stratification versus dedup for tiny LM pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `real-corpus-capped-stratification-versus-dedup-for-tiny-lm-e07fd572de`
Run ID: `real-corpus-capped-stratification-versus-dedup-for-tiny-lm-e07fd572de-20260628T195811764460+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Data-selection curriculum for tiny pretraining: deduplication vs stratified sampling on GB10: enoch://control-plane/projects/data-selection-curriculum-for-tiny-pretraining-deduplication-vs-stratified-sampling-on-gb10-3b343ca3636d/runs/data-selection-curriculum-for-tiny-pretraining-deduplication-vs-stratified-sampling-on-gb10-3b343ca3636d-20260628T193841972255+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b7567edcb0a4

## What looked useful

Exact dedup removed only 151 of 120,000 AG News train rows. Capped stratification made the 1.2M-byte subset nearly perfectly label-balanced, but mean held-out loss was 2.6842 versus 2.6813 for random dedup and 2.6853 for source-order dedup. The practical signal is that stratification can fix balance, but balance alone did not translate into a tiny-LM validation-loss gain against a fair random-dedup control.

## Boundaries and scale limits

Single real corpus; supervised news labels used for strata; byte-level tokenizer; tiny model; 3 seeds; 2,000-document held-out set; no downstream task evaluation; no larger naturally duplicated web corpus; no long training schedule.

## Claim scope

On AG News real text with a 441,856-parameter byte-level causal Transformer, a 1.2M-byte selected training corpus, and 600 GPU training steps across three seeds, capped label x length-bin stratification corrected subset balance but did not improve held-out byte-LM loss over a random exact-dedup baseline.

## Why it stopped

Bounded direct evidence did not support the central claim that capped stratification beats dedup for tiny-LM pretraining; it only showed balance correction without validation-loss improvement over random dedup.

## Recommended next action

Stop this run as a no-paper useful signal; only pursue a bounded deepen follow-up on a more naturally skewed and duplicated real corpus with a pre-registered win margin versus random dedup.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Capped stratification on naturally skewed duplicated web-text shards
- Success threshold: Capped stratification improves mean held-out LM loss by at least 0.01 over random exact-dedup sampling across at least three seeds, with no held-out source/domain regression larger than 0.02 loss.
- Stop condition: Stop if corpus diagnostics show little duplicate/skew signal, or if capped stratification fails to beat random dedup by 0.01 mean loss after the planned three-seed matched-token run.

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-capped-stratification-versus-dedup-for-tiny-lm-e07fd572de`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
