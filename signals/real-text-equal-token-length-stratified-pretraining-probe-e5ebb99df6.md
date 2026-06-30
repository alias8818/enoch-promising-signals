# Real-text equal-token length-stratified pretraining probe

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-text-equal-token-length-stratified-pretraining-probe-e5ebb99df6`
Run ID: `real-text-equal-token-length-stratified-pretraining-probe-e5ebb99df6-20260526T182401285178+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Length-Stratified Long Context Pretraining: enoch://control-plane/projects/length-stratified-long-context-pretraining-7d650e3873b3/runs/length-stratified-long-context-pretraining-7d650e3873b3-20260525T174111937355+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9dc65dc46b70

## What looked useful

Equal token length and length stratification did not explain away the real-text pretraining advantage in this small direct probe. The reciprocal shuffled-control evaluation behaved as expected, supporting an order/structure mechanism rather than length leakage or global model quality.

## Boundaries and scale limits

Tiny 2-layer 128-dim Transformer only; Wikitext-2 only; regex tokenizer rather than BPE; 500 update steps; 2 seeds; no GPT-2-small-class baseline, bootstrap confidence intervals, larger corpus, longer training, or downstream transfer.

## Claim scope

Tier 1 controlled small direct test: on Wikitext-2 line examples with exact per-example token-count pairing and three length strata, two independent tiny causal-LM runs found that real-text pretraining beat shuffled-token pretraining on held-out real text by 8.6% to 10.1% relative NLL in every stratum, while the shuffled model won on shuffled-token controls.

## Why it stopped

No-paper closure: the Tier 1 direct test supports the mechanism, but evidence is too small and narrow for publication readiness.

## Recommended next action

Run a bounded medium confirmation with a GPT-2 tokenizer and GPT-2-small-class or parameter-matched baseline on Wikitext-103/OpenWebText subsets, requiring the same >=5% relative real-text NLL advantage in at least two strata across at least three seeds with bootstrap confidence intervals.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium BPE/tokenizer confirmation of equal-token length-stratified real-text pretraining advantage
- Success threshold: Across at least three seeds, real-text training must show >=5% relative NLL advantage over shuffled-token training on held-out real text in at least two length strata, and the shuffled-token model must retain a positive advantage on shuffled-token evals.
- Stop condition: Stop if the real-text advantage is below 5% in two or more strata across seeds, if reciprocal shuffled controls fail, or if the effect disappears under BPE tokenization.

## Evidence references

- Artifact root: `<local-path>/projects/real-text-equal-token-length-stratified-pretraining-probe-e5ebb99df6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
