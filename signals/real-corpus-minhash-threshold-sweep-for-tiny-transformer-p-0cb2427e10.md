# Real-corpus MinHash threshold sweep for tiny transformer pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-corpus-minhash-threshold-sweep-for-tiny-transformer-p-0cb2427e10`
Run ID: `real-corpus-minhash-threshold-sweep-for-tiny-transformer-p-0cb2427e10-20260619T212751788234+0000`

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

- Parent run decision: MinHash dedup threshold impact on tiny CPU pretraining: enoch://control-plane/projects/minhash-dedup-threshold-impact-on-tiny-cpu-pretraining-1b6a778e5e96/runs/minhash-dedup-threshold-impact-on-tiny-cpu-pretraining-1b6a778e5e96-20260619T205752192613+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b904a67997da

## What looked useful

Aggressive MinHash dedupe can remove 25-50% of overlapping real-text chunks without hurting this tiny transformer run, and threshold 0.30 improved validation loss slightly in both seeds. The effect is small and not enough for a paper claim.

## Boundaries and scale limits

One small literary corpus, two seeds, character-level tokenizer, one tiny 1-layer Transformer, equal optimizer steps rather than equal token budget, local 192-kept-chunk deduplication window, and no GPT-2-small-class or web-corpus baseline.

## Claim scope

On a bounded Tiny Shakespeare character-level pretraining test with 640 overlapping real-text chunks, MinHash thresholds 0.30 and 0.50 changed the training set and produced small mean validation-loss improvements over no dedupe after 120 optimizer steps; thresholds 0.70 and 0.90 removed no chunks and were no-ops.

## Why it stopped

Tier 1 direct evidence found a small useful mechanism signal, but the effect size and scope are insufficient for publication readiness.

## Recommended next action

Run a deeper bounded confirmation with fixed-token-budget training, at least five seeds, tokenized corpus chunks, and a GPT-2-small-class or parameter-matched baseline before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fixed-token-budget MinHash threshold confirmation on tokenized real corpus
- Success threshold: Across at least five seeds, threshold 0.30 or 0.50 must improve mean held-out validation loss by at least 0.01 or preserve loss within 0.005 while reducing repeated chunks by at least 20%, with no degradation in a no-op threshold sanity check.
- Stop condition: Stop if dedupe thresholds no longer remove meaningful chunks, if fixed-token-budget validation loss is worse than no dedupe by more than 0.005, or if seed variance dominates the observed threshold effect.

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-minhash-threshold-sweep-for-tiny-transformer-p-0cb2427e10`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
