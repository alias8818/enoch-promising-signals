# Neural tiny-LM validation of MinHash dedup under fixed CPU budgets

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `68`
Project ID: `neural-tiny-lm-validation-of-minhash-dedup-under-fixed-cpu-7f1156ec43`
Run ID: `neural-tiny-lm-validation-of-minhash-dedup-under-fixed-cpu-7f1156ec43-20260524T012451583018+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `68`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: MinHash Deduplication for Tiny CPU Pretraining: enoch://control-plane/projects/minhash-deduplication-for-tiny-cpu-pretraining-4d412066a5fe/runs/minhash-deduplication-for-tiny-cpu-pretraining-4d412066a5fe-20260524T011756700683+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4d24ceda12ad

## What looked useful

MinHash dedup mechanically removed duplicates, including 66.67% of candidates in the strong duplicate condition, but the neural LM metrics did not meet the preregistered 0.02-nat clean-NLL and duplicate-probe thresholds. Default condition clean NLL moved against dedup by 0.00478 nats; strong duplicate condition moved in favor of dedup by only 0.00267 nats, with duplicate-source NLL increasing by only 0.00322 nats.

## Boundaries and scale limits

Not a web-scale or GPT-2-small-class validation; corpus is small and induced-contamination only, model is a tiny dependency-free character LM, and CPU budget is seconds per model rather than long pretraining.

## Claim scope

Tier 1 small direct neural character-LM test on tiny Shakespeare chunks with induced near-duplicate contamination, comparing raw contaminated training against MinHash/LSH document deduplication under matched SGD update budgets across three seeds.

## Why it stopped

The controlled small direct neural-LM test failed the stated support threshold in both default and high-removal duplicate regimes; this is an early direct falsification of the Tier 1 threshold, not a full-scale validation of MinHash dedup for large LMs.

## Recommended next action

Stop this follow-up as a no-paper useful signal; only reopen with a bounded Transformer/tokenized-corpus direct test that preserves matched CPU or wall-clock budgets and requires at least 0.02-nat clean-NLL improvement plus memorization reduction across seeds.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/neural-tiny-lm-validation-of-minhash-dedup-under-fixed-cpu-7f1156ec43`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
